# pygame-exercise-jewelthief.py

# A Jewel Thief Clone

import random

import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)

NUM_COINS = 100
NUM_ENEMIES = 5

GOOMBA_IMAGE = pg.image.load("./Images/goomba.png")

GOOMBA_IMAGE_SMALL = pg.transform.scale(
    GOOMBA_IMAGE, (GOOMBA_IMAGE.get_width() // 2, GOOMBA_IMAGE.get_height() // 2)
)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.images = [
            pg.image.load("./Images/mario.webp"),
            pg.transform.flip(pg.image.load("./Images/mario.webp"), True, False),
        ]

        self.facing = 0  # 0 is right
        self.image = self.images[self.facing]

        self.rect = self.image.get_rect()

        self.lives = 10

    def update(self):
        """Update the location of Mario with the mouse"""
        next_pos = pg.mouse.get_pos()

        if self.rect.centerx > next_pos[0]:
            self.facing = 1
        elif self.rect.centerx < next_pos[0]:
            self.facing = 0

        self.image = self.images[self.facing]

        self.rect.center = next_pos


class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load("./Images/coin.png")
        self.rect = self.image.get_rect()

        # Randomize initial location
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)


class Goomba(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # set the image to a scaled version
        self.image = GOOMBA_IMAGE_SMALL

        self.rect = self.image.get_rect()

        # Spawn in a random location
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

        self.vel_x = random.choice([-6, -5, -4, 4, 5, 6])
        self.vel_y = random.choice([-6, -5, -4, 4, 5, 6])

        self.max_speed = 9

    def update(self):
        """Make the goomba move and bounce"""
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Bounce off the edge of the screen
        if self.rect.top < 0:
            self.rect.top = 0  # keep it inside the screen
            self.vel_y *= -1
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y *= -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel_x *= -1
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.vel_x *= -1

    def increase_speed(self):
        """Increase speed to a limit"""

        if abs(self.vel_x) < self.max_speed:
            if self.vel_x > 0:
                self.vel_x += 0.25
            else:
                self.vel_x -= 0.25
        if abs(self.vel_y) < self.max_speed:
            if self.vel_y > 0:
                self.vel_y += 0.25
            else:
                self.vel_y -= 0.25


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # Hide the mouse
    pg.mouse.set_visible(False)

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    score = 0

    font = pg.font.SysFont("Futura", 24)

    # Sprite Groups
    all_sprites = pg.sprite.Group()
    coin_sprites = pg.sprite.Group()
    enemy_sprites = pg.sprite.Group()

    # Create Player object
    player = Player()
    all_sprites.add(player)

    # Create Coin objects
    for _ in range(NUM_COINS):
        coin = Coin()

        all_sprites.add(coin)
        coin_sprites.add(coin)

    # Create enemies
    for _ in range(NUM_ENEMIES):
        enemy = Goomba()

        all_sprites.add(enemy)
        enemy_sprites.add(enemy)

    pg.display.set_caption("Jewel Thief Clone (Nintendo Don't Sue Us)")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        all_sprites.update()

        # Get a list of ALL COINS Mario has collided with
        coins_collided = pg.sprite.spritecollide(player, coin_sprites, True)

        for coin in coins_collided:
            # Increase the score by 10
            score += 10

            print(f"Score: {score}")

        # If the coin_sprites group is empty, respawn all coins and increase enemy speed
        if len(coin_sprites) <= 0:
            for _ in range(NUM_COINS):
                coin = Coin()

                all_sprites.add(coin)
                coin_sprites.add(coin)

            for sprite in enemy_sprites:
                sprite.increase_speed()

        # Check for collision between the enemies and the player
        enemies_collided = pg.sprite.spritecollide(player, enemy_sprites, False)

        # If collided with enemy, decrease the player's life
        for enemy in enemies_collided:
            player.lives -= 0.1

            print(int(player.lives))

        # --- Draw items
        screen.fill(WHITE)

        # Create a surface for the score
        score_image = font.render(f"Score: {score}", True, BLACK)

        all_sprites.draw(screen)

        # "Blit" the surface on the screen
        screen.blit(score_image, (5, 5))

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()

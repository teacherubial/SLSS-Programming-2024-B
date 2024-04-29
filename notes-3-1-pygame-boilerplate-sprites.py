# Intro to Pygame
#    - boilerplate
#    - Sprite class

import random
import pygame

WIDTH = 1280  # Pixels
HEIGHT = 760
SCREEN_SIZE = (WIDTH, HEIGHT)

LOGO_IMAGES = [
    pygame.image.load("./Images/dvd-logo.png"),
    pygame.image.load("./Images/dvd-logo-2.svg"),
    pygame.image.load("./Images/dvd-logo-3.gif"),
]


class Dvdlogo(pygame.sprite.Sprite):
    """Represents the DVD Logo"""

    def __init__(self):
        super().__init__()

        self.image = random.choice(LOGO_IMAGES)
        # sets the x and y to 0
        #    first position of the image is in the top right
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(0, HEIGHT - self.rect.height)

        # How much position changes over time
        #    - pixels per tick
        self.vel_x = random.choice([-6, -5, -4, -3, 3, 4, 5, 6])
        self.vel_y = random.choice([-6, -5, -4, -3, 3, 4, 5, 6])

    def update(self):
        # Update position of Dvdlogo
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Keep the Dvdlogo in the screen
        # Right side of the screen
        #     - if the right edge of dvdlogo > WIDTH
        #          - switch the direction (+vel-x -> -vel-x)
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.vel_x = -self.vel_x
        if self.rect.left < 0:
            self.rect.left = 0
            self.vel_x = -self.vel_x
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.vel_y = -self.vel_y
        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = -self.vel_y

    def incr_velocity(self):
        """Increases the velocity in the proper direction"""
        if self.vel_x < 0:
            self.vel_x -= 1
        elif self.vel_x > 0:
            self.vel_x += 1
        else:
            self.vel_x = random.choice([-1, 1])

        if self.vel_y < 0:
            self.vel_y -= 1
        elif self.vel_y > 0:
            self.vel_y += 1
        else:
            self.vel_y = random.choice([-1, 1])

    def decr_velocity(self):
        """Decreases the velocity in the proper direction"""
        if self.vel_x < 0:
            self.vel_x += 1
        elif self.vel_x > 0:
            self.vel_x -= 1
        else:
            self.vel_x = random.choice([-1, 1])

        if self.vel_y < 0:
            self.vel_y += 1
        elif self.vel_y > 0:
            self.vel_y -= 1
        else:
            self.vel_y = random.choice([-1, 1])


def start():
    """Environment Setup and Game Loop"""

    pygame.init()

    # --CONSTANTS--
    # COLOURS
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    EMERALD = (21, 219, 147)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GRAY = (128, 128, 128)

    # --VARIABLES--
    screen = pygame.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    all_sprites.add(Dvdlogo())

    pygame.display.set_caption("DVD Screen Saver")

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # Listen for the keyboard space bar to be pressed
            # spawn a new dvdlogo object
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    all_sprites.add(Dvdlogo())
                if pygame.key.get_pressed()[pygame.K_1]:
                    for sprite in all_sprites:
                        sprite.incr_velocity()
                if pygame.key.get_pressed()[pygame.K_2]:
                    for sprite in all_sprites:
                        sprite.decr_velocity()
                if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                    if len(all_sprites) > 0:
                        all_sprites.spritedict.popitem()

        # --- Update the world state
        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)

        all_sprites.draw(screen)

        # Update the screen with anything new
        pygame.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()

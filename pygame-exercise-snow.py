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


class Snowflake(pg.sprite.Sprite):
    def __init__(self, size: int):
        """
        Params:
            size: diameter of snowflake in pixels
        """
        # Super class constructor
        super().__init__()

        # Create a blank surface
        self.image = pg.Surface((size, size))

        # Draw a circle inside of it
        pg.draw.circle(self.image, WHITE, (size // 2, size // 2), size // 2)

        self.rect = self.image.get_rect()

        # Spawn it in the middle of the screen
        # Chooses a random x-coordinate
        self.rect.centerx = random.randrange(0, WIDTH + 1)
        self.rect.centery = HEIGHT // 2

    def update(self):
        """Make the snow fall from top to bottom"""


def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    # Add 100 snowflakes to the all_sprites Group
    for _ in range(100):
        all_sprites.add(Snowflake(10))

    pg.display.set_caption("Snowfall Landscape")

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # --- Update the world state
        # Update the state of all sprites
        all_sprites.update()

        # --- Draw items
        screen.fill(BLACK)

        # Draw all the sprites
        all_sprites.draw(screen)

        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps


def main():
    start()


if __name__ == "__main__":
    main()

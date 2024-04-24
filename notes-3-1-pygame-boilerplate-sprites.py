# Intro to Pygame
#    - boilerplate
#    - Sprite class

import pygame


class Dvdlogo(pygame.sprite.Sprite):
    """Represents the DVD Logo"""

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./Images/dvd-logo.png")

        # sets the x and y to 0
        #    first position of the image is in the top right
        self.rect = self.image.get_rect()

        # How much position changes over time
        #    - pixels per tick
        self.vel_x = 3
        self.vel_y = 0

    def update(self):
        # Update position of Dvdlogo
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Keep the Dvdlogo in the screen
        # Right side of the screen
        #     - if the right edge of dvdlogo > WIDTH
        #          - switch the direction (+vel-x -> -vel-x)
        if self.rect.right >= 1280:
            self.vel_x = -self.vel_x
        # Left side

        # Top side
        # Bottom side

        print(self.rect.x, self.rect.y)


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

    WIDTH = 1280  # Pixels
    HEIGHT = 760
    SCREEN_SIZE = (WIDTH, HEIGHT)

    # --VARIABLES--
    screen = pygame.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pygame.time.Clock()

    dvdlogo = Dvdlogo()
    # Move the DVD logo to the middle-ish
    dvdlogo.rect.centerx = WIDTH // 2
    dvdlogo.rect.centery = HEIGHT // 2

    all_sprites = pygame.sprite.Group()
    all_sprites.add(dvdlogo)

    pygame.display.set_caption("DVD Screen Saver")

    # --MAIN LOOP--
    while not done:
        # --- Event Listener
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

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

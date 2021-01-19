# shmup.py
# Top-down shoot-m-up game
# Goals:
#    - get more comfortable with sprites and mouse
#    - create new sprites IN the main loop (bullets)
#    - using pygame.mouse a little more comfortably

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 720
HEIGHT = 1280
TITLE = "SHMUP"

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/galaga_ship.png")
        # Scaling the image down by 0.5x
        self.image = pygame.transform.scale(self.image, (64, 64))

        self.rect = self.image.get_rect()

    def update(self):
        """Move the player with the mouse"""
        self.rect.center = pygame.mouse.get_pos()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, y_coord):
        """
        Arguments:
            y_coord - initial y-coordinate
        """
        super().__init__()

        self.image = pygame.image.load("./images/mario.png")

        self.rect = self.image.get_rect()

        # initial location middle of the screen at y_coord
        self.rect.centerx = WIDTH / 2
        self.rect.centery = y_coord

        self.x_vel = 3

class Bullet(pygame.sprite.Sprite):
    def __init__(self, coords):
        super().__init__()

        self.image = pygame.image.load("./images/bullet.png")
        # Scale to 22x36px
        self.image = pygame.transform.scale(self.image, (22, 36))

        self.rect = self.image.get_rect()
        # Start the bullet at coords
        self.rect.centerx, self.rect.bottom = coords

        self.y_vel = -3




    def update(self):
        """Move the enemy side-to-side"""
        self.rect.x += self.x_vel

        # Keep enemy in the screen
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.x_vel *= -1


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Sprite Groups
    all_sprites = pygame.sprite.RenderUpdates()
    enemy_sprites = pygame.sprite.Group()

    #  --- enemies
    enemy = Enemy(100)
    all_sprites.add(enemy)
    enemy_sprites.add(enemy)

    #  --- player
    player = Player()
    all_sprites.add(player)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites.update()

        # ----- DRAW
        screen.fill(BLACK)
        dirty_rectangles = all_sprites.draw(screen)

        # ----- UPDATE
        pygame.display.update(dirty_rectangles)
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
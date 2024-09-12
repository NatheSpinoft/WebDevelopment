import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Zelda-like Game')

# Set up clock for framerate
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 128, 0))  # Green square as placeholder
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5
    
    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((128, 128, 128))  # Gray square as placeholder
        self.rect = self.image.get_rect(topleft=(x, y))

# Create the player and tilemap
player = Player(WIDTH//2, HEIGHT//2)
player_group = pygame.sprite.Group(player)

tiles = pygame.sprite.Group()
for i in range(25):  # Grid size example
    for j in range(19):
        tile = Tile(i * 32, j * 32)
        tiles.add(tile)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_group.update(keys)
    
    # Clear screen
    screen.fill((0, 0, 0))

    # Draw tiles and player
    tiles.draw(screen)
    player_group.draw(screen)

    # Update display
    pygame.display.flip()

    # Frame rate control
    clock.tick(60)

pygame.quit()
sys.exit()
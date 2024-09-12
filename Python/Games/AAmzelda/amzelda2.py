import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Zelda-like Game with Boundaries')

# Set up clock for framerate
clock = pygame.time.Clock()

# Colors
GREEN = (0, 128, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(GREEN)  # Green square as placeholder
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5
    
    def update(self, keys, boundaries):
        # Create a copy of the player's current position
        old_position = self.rect.topleft
        
        # Move the player based on input
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        
        # Check for collision with boundaries
        if pygame.sprite.spritecollide(self, boundaries, False):
            # If collision happens, revert to old position
            self.rect.topleft = old_position

class Boundary(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLUE)  # Blue for the building boundary
        self.rect = self.image.get_rect(topleft=(x, y))

# Create the player
player = Player(WIDTH//2, HEIGHT//2)
player_group = pygame.sprite.Group(player)

# Create the tile map (background)
tiles = pygame.sprite.Group()
for i in range(25):  # Grid size example
    for j in range(19):
        tile = pygame.Surface((32, 32))
        tile_rect = tile.get_rect(topleft=(i * 32, j * 32))
        pygame.draw.rect(screen, GRAY, tile_rect)

# Create boundaries (buildings or walls)
boundaries = pygame.sprite.Group()
building1 = Boundary(100, 500, 100, 100)  # Example of a 128x128 pixel building
building2 = Boundary(500, 200, 64, 192)   # Example of a tall building
boundaries.add(building1, building2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    
    # Update player position based on input and handle boundary collisions
    player_group.update(keys, boundaries)

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw tiles (background)
    tiles.draw(screen)

    # Draw boundaries (buildings)
    boundaries.draw(screen)

    # Draw the player
    player_group.draw(screen)

    # Update display
    pygame.display.flip()

    # Frame rate control
    clock.tick(60)

pygame.quit()
sys.exit()
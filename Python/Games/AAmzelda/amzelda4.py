import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Zelda-like Game with Tiled Background and Buildings')

# Set up clock for framerate
clock = pygame.time.Clock()

# Load the tile image (assuming 20x20 px)
tile_image = pygame.image.load('tile1.png').convert()
tile_image = pygame.transform.scale(tile_image, (20, 20))

# Load the building image
building_image = pygame.image.load('building.png').convert_alpha()

# Load the player images
player_image_vert = pygame.image.load('sprite.png').convert_alpha()  # For up/down
player_image_horiz = pygame.image.load('spriteside.png').convert_alpha()  # For left/right

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = player_image_vert  # Initial image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5
        self.direction = 'vertical'  # Initial direction
    
    def update(self, keys, boundaries):
        old_position = self.rect.topleft

        # Check movement direction and update the image
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            self.image = player_image_horiz  # Horizontal image for left/right
        elif keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            self.image = player_image_vert  # Vertical image for up/down
        
        # Move the player
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Handle collisions with boundaries
        if pygame.sprite.spritecollide(self, boundaries, False):
            self.rect.topleft = old_position

class Boundary(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.image = pygame.transform.scale(image, (width, height))  # Scale the building image
        self.rect = self.image.get_rect(topleft=(x, y))

# Create the player
player = Player(WIDTH // 2, HEIGHT // 2)
player_group = pygame.sprite.Group(player)

# Create boundaries (buildings) using the building image
boundaries = pygame.sprite.Group()
building1 = Boundary(100, 100, 128, 128, building_image)  # Small building
building2 = Boundary(300, 0, 128, 228, building_image)   # Tall building on the right
building3 = Boundary(500, 100, 128, 128, building_image)   # Tall building on the right
wall1 = Boundary(0,0,600, 20)
boundaries.add(building1, building2, building3, wall1)

# Function to tile the background with the tile image
def draw_tiled_background(screen, tile_image):
    for x in range(0, WIDTH, 20):  # 20px is the size of the tile
        for y in range(0, HEIGHT, 20):
            screen.blit(tile_image, (x, y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    player_group.update(keys, boundaries)

    # Draw tiled background
    draw_tiled_background(screen, tile_image)

    # Draw boundaries (buildings)
    boundaries.draw(screen)

    # Draw the player
    player_group.draw(screen)

    # Update display
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
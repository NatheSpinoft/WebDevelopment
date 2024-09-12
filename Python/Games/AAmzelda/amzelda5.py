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
tile_image = pygame.image.load('tile.png').convert()
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

# Add specific buildings as boundaries
building1 = Boundary(100, 100, 128, 128, building_image)  # Small building
building2 = Boundary(500, 200, 64, 192, building_image)   # Tall building on the right
boundaries.add(building1, building2)

# Function to create walls
def create_walls(boundaries, wall_image):
    # Top wall (stack horizontally)
    for x in range(0, WIDTH, wall_image.get_width()):
        boundary = Boundary(x, 0, wall_image.get_width(), wall_image.get_height(), wall_image)
        boundaries.add(boundary)
    
    # Left wall (stack vertically)
    for y in range(0, HEIGHT, wall_image.get_height()):
        boundary = Boundary(0, y, wall_image.get_width(), wall_image.get_height(), wall_image)
        boundaries.add(boundary)

# Load the wall image (you can use the same building image or another image)
wall_image = pygame.image.load('wall.png').convert_alpha()

# Create walls on the top and left side using the wall image
create_walls(boundaries, wall_image)

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

    # Draw boundaries (buildings and walls)
    boundaries.draw(screen)

    # Draw the player
    player_group.draw(screen)

    # Update display
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
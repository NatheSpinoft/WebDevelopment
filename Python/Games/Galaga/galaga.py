import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Galaga")

# FPS (frames per second) clock
clock = pygame.time.Clock()

# Load player sprite
player_image = pygame.image.load("Ghost2.png")  # Add a path to your player image
player_rect = player_image.get_rect()
player_rect.centerx = SCREEN_WIDTH // 2
player_rect.bottom = SCREEN_HEIGHT - 20

# Player speed
player_speed = 5

# Enemy setup
enemy_image = pygame.image.load("bubble.png")  # Add a path to your enemy image
enemy_speed = 3
enemy_list = []

# Function to spawn an enemy
def spawn_enemy():
    enemy_rect = enemy_image.get_rect()
    enemy_rect.x = random.randint(0, SCREEN_WIDTH - enemy_rect.width)
    enemy_rect.y = random.randint(-150, -enemy_rect.height)
    enemy_list.append(enemy_rect)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses for player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < SCREEN_WIDTH:
        player_rect.x += player_speed

    # Spawn enemies periodically
    if len(enemy_list) < 5:
        spawn_enemy()

    # Move enemies
    for enemy_rect in enemy_list:
        enemy_rect.y += enemy_speed
        if enemy_rect.top > SCREEN_HEIGHT:
            enemy_list.remove(enemy_rect)

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the player
    screen.blit(player_image, player_rect)

    # Draw enemies
    for enemy_rect in enemy_list:
        screen.blit(enemy_image, enemy_rect)

    # Update the display
    pygame.display.flip()

    # Frame rate control
    clock.tick(60)

# Quit Pygame
pygame.quit()
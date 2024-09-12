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
RED = (255, 0, 0)

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Galaga")

# FPS (frames per second) clock
clock = pygame.time.Clock()

# Load assets
player_image = pygame.image.load("player.png")
enemy_image = pygame.image.load("enemy.png")
bullet_image = pygame.image.load("bullet.png")

# Font for score and game over text
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

# Player setup
player_rect = player_image.get_rect()
player_rect.centerx = SCREEN_WIDTH // 2
player_rect.bottom = SCREEN_HEIGHT - 20
player_speed = 5

# Bullet setup
bullet_speed = -10
bullet_list = []

# Enemy setup
enemy_speed = 3
enemy_list = []
spawn_enemy_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_enemy_event, 1000)  # Spawn an enemy every second

# Score and lives setup
score = 0
lives = 5

# Function to spawn an enemy
def spawn_enemy():
    enemy_rect = enemy_image.get_rect()
    enemy_rect.x = random.randint(0, SCREEN_WIDTH - enemy_rect.width)
    enemy_rect.y = random.randint(-150, -enemy_rect.height)
    enemy_list.append(enemy_rect)

# Function to draw the score and lives
def draw_score_and_lives():
    score_surface = font.render(f"Score: {score}", True, WHITE)
    lives_surface = font.render(f"Lives: {lives}", True, RED)
    screen.blit(score_surface, (10, 10))
    screen.blit(lives_surface, (SCREEN_WIDTH - 120, 10))

# Function to show Game Over screen
def show_game_over():
    screen.fill(BLACK)
    game_over_text = big_font.render("GAME OVER", True, RED)
    final_score_text = font.render(f"Final Score: {score}", True, WHITE)
    retry_text = font.render("Press R to Try Again", True, WHITE)
    
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2))
    screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
    
    pygame.display.flip()

# Function to reset the game
def reset_game():
    global score, lives, bullet_list, enemy_list, player_rect
    score = 0
    lives = 5
    bullet_list = []
    enemy_list = []
    player_rect.centerx = SCREEN_WIDTH // 2
    player_rect.bottom = SCREEN_HEIGHT - 20

# Game loop
running = True
game_over = False

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_enemy_event and not game_over:
            spawn_enemy()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                # Create a bullet when space is pressed
                bullet_rect = bullet_image.get_rect()
                bullet_rect.centerx = player_rect.centerx
                bullet_rect.top = player_rect.top
                bullet_list.append(bullet_rect)
            if event.key == pygame.K_r and game_over:
                reset_game()
                game_over = False

    if not game_over:
        # Key presses for player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.right < SCREEN_WIDTH:
            player_rect.x += player_speed

        # Move bullets
        for bullet_rect in bullet_list[:]:
            bullet_rect.y += bullet_speed
            if bullet_rect.bottom < 0:
                bullet_list.remove(bullet_rect)

        # Move enemies
        for enemy_rect in enemy_list[:]:
            enemy_rect.y += enemy_speed
            if enemy_rect.top > SCREEN_HEIGHT:
                enemy_list.remove(enemy_rect)
                lives -= 1  # Lose a life if an enemy passes

        # Collision detection between bullets and enemies
        for bullet_rect in bullet_list[:]:
            for enemy_rect in enemy_list[:]:
                if bullet_rect.colliderect(enemy_rect):
                    bullet_list.remove(bullet_rect)
                    enemy_list.remove(enemy_rect)
                    score += 10  # Increase score when an enemy is hit

        # Collision detection between player and enemies
        for enemy_rect in enemy_list[:]:
            if player_rect.colliderect(enemy_rect):
                enemy_list.remove(enemy_rect)
                lives -= 1  # Lose a life if hit by an enemy

        # Check for game over
        if lives <= 0:
            game_over = True

        # Fill the screen with black
        screen.fill(BLACK)

        # Draw the player
        screen.blit(player_image, player_rect)

        # Draw bullets
        for bullet_rect in bullet_list:
            screen.blit(bullet_image, bullet_rect)

        # Draw enemies
        for enemy_rect in enemy_list:
            screen.blit(enemy_image, enemy_rect)

        # Draw the score and lives
        draw_score_and_lives()

        # Update the display
        pygame.display.flip()

    else:
        # Show Game Over screen
        show_game_over()

    # Frame rate control
    clock.tick(60)

# Quit Pygame
pygame.quit()
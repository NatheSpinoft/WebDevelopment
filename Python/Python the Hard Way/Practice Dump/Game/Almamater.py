import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BEIGE = (222, 198, 162)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player_speed = 5

# Create the screen with the window border
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Function to draw the map
def draw_map():
    # Fill the background
    screen.fill(BEIGE)

    # Draw walls
    pygame.draw.rect(screen, BROWN, (0, 0, SCREEN_WIDTH, 20))  # Top wall
    pygame.draw.rect(screen, BROWN, (0, 0, 20, SCREEN_HEIGHT))  # Left wall
    pygame.draw.rect(screen, BROWN, (SCREEN_WIDTH - 20, 0, 20, SCREEN_HEIGHT))  # Right wall
    pygame.draw.rect(screen, BROWN, (0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20))  # Bottom wall

    # Draw the player
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

# Game loop
def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check for key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Quit the game with Esc key
                    pygame.quit()
                    sys.exit()

        # Get keys pressed
        keys = pygame.key.get_pressed()

        # Move the player
        if keys[pygame.K_LEFT] and player_pos[0] > 20:  # Left
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size - 20:  # Right
            player_pos[0] += player_speed
        if keys[pygame.K_UP] and player_pos[1] > 20:  # Up
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN] and player_pos[1] < SCREEN_HEIGHT - player_size - 20:  # Down
            player_pos[1] += player_speed

        draw_map()
        pygame.display.flip()

# Run the game
if __name__ == "__main__":
    game_loop()

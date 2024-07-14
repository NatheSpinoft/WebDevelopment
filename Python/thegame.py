import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Game clock
clock = pygame.time.Clock()

# Player settings
player_width = 50
player_height = 50
player_x = (screen_width // 2) - (player_width // 2)
player_y = screen_height - player_height - 10
player_speed = 10

# Object settings
object_width = 30
object_height = 30
object_speed = 5
object_list = []

# Score
score = 0

# Font
font = pygame.font.SysFont(None, 35)

def draw_player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_width, player_height])

def draw_object(obj):
    pygame.draw.rect(screen, white, [obj[0], obj[1], object_width, object_height])

def display_score(score):
    text = font.render("Score: " + str(score), True, white)
    screen.blit(text, [10, 10])

def game_loop():
    global player_x, score

    game_over = False

    # Main game loop
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        # Add new objects
        if random.randint(1, 20) == 1:
            object_list.append([random.randint(0, screen_width - object_width), -object_height])

        # Move objects and check for collision
        for obj in object_list[:]:
            obj[1] += object_speed
            if obj[1] > screen_height:
                object_list.remove(obj)
            elif player_y < obj[1] + object_height and player_y + player_height > obj[1] and player_x < obj[0] + object_width and player_x + player_width > obj[0]:
                object_list.remove(obj)
                score += 1

        # Clear screen
        screen.fill(black)

        # Draw player
        draw_player(player_x, player_y)

        # Draw objects
        for obj in object_list:
            draw_object(obj)

        # Display score
        display_score(score)

        # Update display
        pygame.display.flip()

        # Frame rate
        clock.tick(60)

    pygame.quit()

# Start the game
game_loop()

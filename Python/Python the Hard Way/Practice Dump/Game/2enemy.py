import pygame
import tkinter as tk
from tkinter import messagebox
import math

# Initialize Pygame
pygame.init()

# Create the Tkinter window
root = tk.Tk()
root.title("Pygame with Tkinter")

# Set up Pygame window dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Enemy properties
ENEMY_RADIUS = 20
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
RADIUS = 150  # Radius for the enemies' circular path
angle1, angle2 = 0, 180  # Initial angles for the two enemies
angle_speed = 0.01  # Speed of rotation

# Game loop flag
running = True

# Game loop
def game_loop():
    global angle1, angle2, running
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Fill the background
        screen.fill(WHITE)

        # Calculate enemy positions
        enemy1_x = CENTER_X + RADIUS * math.cos(angle1)
        enemy1_y = CENTER_Y + RADIUS * math.sin(angle1)

        enemy2_x = CENTER_X + RADIUS * math.cos(angle2)
        enemy2_y = CENTER_Y + RADIUS * math.sin(angle2)

        # Draw enemies
        pygame.draw.circle(screen, RED, (int(enemy1_x), int(enemy1_y)), ENEMY_RADIUS)
        pygame.draw.circle(screen, GREEN, (int(enemy2_x), int(enemy2_y)), ENEMY_RADIUS)

        # Update angles
        angle1 += angle_speed
        angle2 += angle_speed

        # Refresh the display
        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Limit to 60 FPS

# Start the game loop in a separate thread
import threading
game_thread = threading.Thread(target=game_loop)
game_thread.start()

# Run the Tkinter main loop
try:
    root.mainloop()
except KeyboardInterrupt:
    running = False

# Clean up
pygame.quit()

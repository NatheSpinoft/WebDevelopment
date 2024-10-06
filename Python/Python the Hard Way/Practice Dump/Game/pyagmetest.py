import pygame

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame Test")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()

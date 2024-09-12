import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Move the Image and Shoot Bubbles")

# Define colors
white = (255, 255, 255)

# Load the images and set their size
images = [
    pygame.transform.scale(pygame.image.load("/Users/stefanpinto/Documents/Programming/WebDevelopment/Python/Games/Visual-game/Ghost.png"), (50, 50)),
    pygame.transform.scale(pygame.image.load("/Users/stefanpinto/Documents/Programming/WebDevelopment/Python/Games/Visual-game/Ghost2.png"), (50, 50)),
    # Add more images if you want
]

# Load the bubble image and set its size
bubble_image = pygame.transform.scale(pygame.image.load("/Users/stefanpinto/Documents/Programming/WebDevelopment/Python/Games/Visual-game/bubble.png"), (20, 20))

# Set up variables for switching images
current_image = 0
last_switch_time = time.time()
switch_interval = 1  # Switch every 1 second

# Set up the square position
square_x = width // 2 - 50 // 2
square_y = height // 2 - 50 // 2
square_speed = 5

# Class to handle the bubble's behavior
class Bubble:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        self.y -= 10  # Move bubble upward

    def draw(self, surface):
        surface.blit(bubble_image, (self.x, self.y))

# Set up a list to hold bubbles
bubbles = []

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the current keys pressed
    keys = pygame.key.get_pressed()

    # Move the square
    if keys[pygame.K_LEFT]:
        square_x -= square_speed
    if keys[pygame.K_RIGHT]:
        square_x += square_speed
    if keys[pygame.K_UP]:
        square_y -= square_speed
    if keys[pygame.K_DOWN]:
        square_y += square_speed

    # Prevent the square from moving off the screen
    square_x = max(0, min(square_x, width - 50))
    square_y = max(0, min(square_y, height - 50))

    # Shoot a bubble when the spacebar is pressed
    if keys[pygame.K_SPACE]:
        bubble_x = square_x + 50 // 2 - 10  # Start bubble in the center of the square
        bubble_y = square_y
        bubbles.append(Bubble(bubble_x, bubble_y))

    # Move and draw each bubble
    for bubble in bubbles:
        bubble.move()
        bubble.draw(window)

    # Remove bubbles that have moved off the screen
    bubbles = [bubble for bubble in bubbles if bubble.y > -20]

    # Switch images based on time
    current_time = time.time()
    if current_time - last_switch_time >= switch_interval:
        current_image = (current_image + 1) % len(images)  # Cycle through images
        last_switch_time = current_time

    # Fill the background
    window.fill(white)

    # Draw the current image (the square)
    window.blit(images[current_image], (square_x, square_y))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)
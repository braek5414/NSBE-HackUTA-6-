# main.py
import pygame
from player import Player  # Import the Player class
from platforms import Platform  # Import the Platform class

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Create a Player instance
player = Player(x=640, y=360, size=50, speed=5)  # Initialize the player at a safe height

# Create platforms
platforms = [
    Platform(x=300, y=600, width=200, height=20),
    Platform(x=600, y=450, width=200, height=20),
    Platform(x=100, y=300, width=200, height=20)
]

# Infinite scroll variables
scroll_speed = 2  # How fast the background scrolls up

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # Get key states and update player movement
    keys = pygame.key.get_pressed()
    player.move(keys, platforms)  # Move the player based on key presses

    # Render the platforms
    for platform in platforms:
        platform.draw(screen)  # Draw each platform

    # Render the player
    player.draw(screen)  # Draw the player on the screen

    # Scroll the world upwards (optional)
    # You can adjust the scroll behavior based on player position

    # Flip the display to put your work on the screen
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()

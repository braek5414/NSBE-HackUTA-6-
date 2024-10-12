import streamlit as st
from pyvirtualdisplay import Display
import pygame
import cv2
import numpy as np

# Set up the virtual display
display = Display(visible=0, size=(800, 600))
display.start()

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Pygame loop
def run_pygame():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen and update Pygame
        screen.fill((0, 128, 255))  # Example background color
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

        # Capture the screen as an image
        img_data = pygame.surfarray.array3d(pygame.display.get_surface())
        img_data = np.rot90(img_data)  # Rotate for correct orientation
        img_data = cv2.cvtColor(img_data, cv2.COLOR_RGB2BGR)  # Convert to BGR for OpenCV

        yield img_data

# Streamlit app to display Pygame
st.title("Embedded Pygame in Streamlit")

# Placeholder for video
video_placeholder = st.empty()

# Run the Pygame game loop and display it
game_generator = run_pygame()
for frame in game_generator:
    video_placeholder.image(frame, channels="BGR", use_column_width=True)

# Stop the virtual display when done
pygame.quit()
display.stop()
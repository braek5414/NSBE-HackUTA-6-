# player.py
import pygame

class Player:
    def __init__(self, x, y, size, speed):
        self.position = [x, y]
        self.size = size
        self.speed = speed
        self.color = (0, 0, 255)  # Blue color
        self.velocity_y = 0  # Vertical velocity
        self.gravity = 0.5
        self.jump_power = 10
        self.on_ground = False  # Check if the player is on the ground

    def move(self, keys):
        if keys[pygame.K_a]:
            self.position[0] -= self.speed  # Move left
        if keys[pygame.K_d]:
            self.position[0] += self.speed  # Move right

        # Jumping
        if keys[pygame.K_w] and self.on_ground:  # Space for jumping
            self.velocity_y = -self.jump_power  # Set upward velocity
            self.on_ground = False  # Player is now in the air

        # Apply gravity
        self.velocity_y += self.gravity
        self.position[1] += self.velocity_y

        # Reset if the player falls below the screen
        if self.position[1] > 720:
            self.position[1] = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.size, self.size))

    def reset(self):
        self.position = [640, 360]  # Reset position
        self.velocity_y = 0
        self.on_ground = True  # Reset ground state

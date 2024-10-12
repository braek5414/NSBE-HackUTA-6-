# player.py
import pygame

class Player:
    def __init__(self, x, y, size, speed):
        self.rect = pygame.Rect(x, y, size, size)  # Change to use a Rect for collision
        self.speed = speed
        self.color = (0, 0, 255)  # Blue color
        self.velocity_y = 0  # Vertical velocity
        self.gravity = 0.5
        self.jump_power = 10
        self.on_ground = True  # Initially, the player is on the ground

    def move(self, keys, platforms):
        # Horizontal movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed  # Move left
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed  # Move right

        # Jumping
        if keys[pygame.K_SPACE] and self.on_ground:  # Space for jumping
            self.velocity_y = -self.jump_power  # Set upward velocity
            self.on_ground = False  # Player is now in the air

        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Check for ground collision with platforms
        self.on_ground = False  # Reset on ground status
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                self.rect.y = platform.rect.top - self.rect.height  # Place the player on top of the platform
                self.velocity_y = 0  # Stop downward movement
                self.on_ground = True  # Player is on the ground

        # Reset if the player falls below the screen
        if self.rect.y > 720:
            self.reset()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def reset(self):
        self.rect.topleft = (640, 360)  # Reset position
        self.velocity_y = 0
        self.on_ground = True  # Reset ground state

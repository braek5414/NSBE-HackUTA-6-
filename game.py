import pygame, sys
import random
from button import Button

# Initialize Pygame
pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Black.jpeg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Create the screen (for both game and menu)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Platformer")

# Game loop function
def game_loop():
    running = True
    clock = pygame.time.Clock()
    score = 0
    high_score = 0
    lives = 3
    game_over = False
    platform_count = INITIAL_PLATFORM_COUNT  # Start with more platforms
    camera_movement = 0  # For upward camera movement
    lava_y = SCREEN_HEIGHT  # Starting position of the lava

    player = Player()
    player_group = pygame.sprite.Group()
    player_group.add(player)

    platforms = create_platforms(platform_count)

    while running:
        clock.tick(FPS)
        SCREEN.fill(BLACK)  # Use SCREEN instead of screen

        if not game_over:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    player.jump()

            # Update player and platforms
            player_group.update()
            platforms.update(camera_movement)

            # lava
            pygame.draw.rect(SCREEN, RED, (0, lava_y, SCREEN_WIDTH, SCREEN_HEIGHT))  # Use SCREEN
            
            # Check if the player falls into the lava
            if player.rect.top > lava_y:
                lives -= 1

            # Game Over
            if lives < 0:
                game_over = True

            # Check for collision between player and platforms
            if pygame.sprite.spritecollide(player, platforms, False):
                player.velocity_y = PLAYER_JUMP
                score += 1

                # Increase platform count initially, then gradually reduce it as time goes on
                if score % 5 == 0 and platform_count < 12:
                    platform = Platform(random.randint(0, SCREEN_WIDTH - PLATFORM_WIDTH), random.randint(-100, 0))
                    platforms.add(platform)
                    platform_count += 1

                # After a certain score, start reducing platforms
                if score % 10 == 0 and platform_count > 5:
                    platform_to_remove = platforms.sprites()[0]
                    platforms.remove(platform_to_remove)
                    platform_count -= 1

            # Camera movement (slowly moving upwards)
            camera_movement += 0.01
            player.rect.y += camera_movement

            # Draw everything
            player_group.draw(SCREEN)
            platforms.draw(SCREEN)

            # Display score, high score, lives
            score_text = font.render(f"Score: {score}", True, WHITE)
            SCREEN.blit(score_text, (10, 10))  # Use SCREEN
            
            high_score = max(high_score, score)
            high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
            SCREEN.blit(high_score_text, (10, 40))  # Use SCREEN

            lives_text = font.render(f"Lives: {lives}", True, WHITE)
            SCREEN.blit(lives_text, (10, 50))  # Use SCREEN


        else:
            # Game Over screen with Retry option
            game_over_text = font.render("Game Over", True, RED)
            final_score_text = font.render(f"Final Score: {score}", True, WHITE)
            high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
            retry_text = font.render("Press SPACE to Retry", True, WHITE)
            BackMenu = front.render("Press B to go back to the main menu", True, WHITE)

            SCREEN.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
            SCREEN.blit(final_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
            SCREEN.blit(high_score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 40))
            SCREEN.blit(retry_text, (SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 + 80))

            # Event handling for retrying after game over
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Restart game
                    score = 0
                    player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
                    player.velocity_y = 0
                    platform_count = INITIAL_PLATFORM_COUNT
                    platforms.empty()
                    platforms = create_platforms(platform_count)
                    lava_y = SCREEN_HEIGHT  # Reset lava
                    camera_movement = 0  # Reset camera movement
                    game_over = False

        # Update the display
        pygame.display.flip()

    pygame.quit()

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# Game constants
FPS = 60
GRAVITY = 0.4
PLAYER_JUMP = -11
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLATFORM_SPEED = 3
INITIAL_PLATFORM_COUNT = 8  # Starting number of platforms
LAVA_SPEED = 1  # Speed at which the lava rises

# Load ninja image
ninja_image = pygame.image.load("ninja.gif")  # Use the uploaded ninja image

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Platformer")

# Font for displaying score and game over
font = pygame.font.Font(None, 36)

# Class for the player character
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ninja_image, (40, 50))  # Resize ninja image to fit player size
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
        self.velocity_y = 0

    def update(self):
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        # Horizontal movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Wrap around the screen horizontally
        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH

    def jump(self):
        self.velocity_y = PLAYER_JUMP

# Class for the platforms
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, camera_movement):
        self.rect.y += PLATFORM_SPEED + camera_movement
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, SCREEN_WIDTH - PLATFORM_WIDTH)

# Create player and platform groups
def create_platforms(num_platforms):
    platforms = pygame.sprite.Group()
    for i in range(num_platforms):
        platform = Platform(random.randint(0, SCREEN_WIDTH - PLATFORM_WIDTH), random.randint(50, SCREEN_HEIGHT - 50))
        platforms.add(platform)
    return platforms




def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("LAVA NINJA", True, "#F7342B")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play_Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options_Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit_Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_loop()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()




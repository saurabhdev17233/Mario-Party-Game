import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Mario Party")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Board spaces (positions)
board_positions = [(100, 500), (200, 500), (300, 500), (400, 500), (500, 500), 
                   (600, 500), (700, 500), (700, 400), (700, 300), (600, 300), 
                   (500, 300), (400, 300), (300, 300), (200, 300), (100, 300)]

# Player setup
player_pos = 0  # Start position
player_radius = 20
player_color = RED

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Draw board spaces
    for pos in board_positions:
        pygame.draw.circle(screen, BLUE, pos, 30)

    # Draw player
    pygame.draw.circle(screen, player_color, board_positions[player_pos], player_radius)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Roll dice on SPACE key
                dice_roll = random.randint(1, 6)
                player_pos = min(player_pos + dice_roll, len(board_positions) - 1)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

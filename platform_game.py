import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_SPACE, KEYDOWN, KEYUP, QUIT

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_width, player_height = 40, 60
player_x = WIDTH // 2
player_y = HEIGHT - player_height - 50
player_speed = 5
jump_speed = 10

# Physics
gravity = 0.5
player_y_vel = 0
on_ground = False

# Platforms
platforms = [
    pygame.Rect(0, HEIGHT - 20, WIDTH, 20),  # ground
    pygame.Rect(200, HEIGHT - 150, 200, 20),
    pygame.Rect(450, HEIGHT - 300, 150, 20),
]

# Input state
move_left = False
move_right = False
jump = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_left = True
            elif event.key == K_RIGHT:
                move_right = True
            elif event.key == K_SPACE and on_ground:
                player_y_vel = -jump_speed
                on_ground = False
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_left = False
            elif event.key == K_RIGHT:
                move_right = False

    # Horizontal movement
    if move_left:
        player_x -= player_speed
    if move_right:
        player_x += player_speed

    # Apply gravity
    player_y_vel += gravity
    player_y += player_y_vel

    # Simple collision detection
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    on_ground = False
    for plat in platforms:
        if player_rect.colliderect(plat) and player_y_vel >= 0:
            player_y = plat.top - player_height
            player_y_vel = 0
            on_ground = True

    # Keep player in bounds
    if player_x < 0:
        player_x = 0
    elif player_x + player_width > WIDTH:
        player_x = WIDTH - player_width

    screen.fill(WHITE)

    # Draw platforms
    for plat in platforms:
        pygame.draw.rect(screen, BLACK, plat)

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

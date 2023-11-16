import pygame, sys

# ===== General Setup ===== #
pygame.init()
clock = pygame.time.Clock()

# ===== Setup The Main Window ===== #
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 960
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

while True:
    # ===== Handling Input ===== #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    # ===== Update The Window ===== #
    pygame.display.flip()
    clock.tick(60)
        

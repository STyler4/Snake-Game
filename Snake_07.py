import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1000, 750))
game_icon = pygame.image.load('images/snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake game - by Sam Tyler")

# Tuple containing the colours to be used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (188, 227, 199)

# Fonts for the game
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)


quit_game = False

# Snake will be 20 x 20 pixels
snake_x = 490  # Centre point horizontally is (1000-20 snake width)/2 = 490
snake_y = 350  # Centre point vertically is (720-20 snake height)/2 = 350

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    # Create rectangle for snake
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()
            
pygame.quit()
quit()

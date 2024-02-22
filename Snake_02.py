import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1000, 750))
game_icon = pygame.image.load('images/snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake game - by Sam Tyler")

time.sleep(5)
pygame.quit()
quit()

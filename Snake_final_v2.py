import pygame
import time
import random

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
yellow = (255, 255, 0)ra

# Fonts for the game
score_font = pygame.font.SysFont("snake chan.ttf", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arial black", 20)

clock = pygame.time.Clock()  # sets the speed at which the snake moves


def load_high_score():
    try:
        hi_score_file = open("HI_score.txt", 'r')
    except IOError:
        hi_score_file = open("HI_score.txt", 'w')
        hi_score_file.write("0")
    hi_score_file = open("HI_score.txt", 'r')
    value = hi_score_file.read()
    hi_score_file.close()
    return value


# Function to update record of the highest score
def update_high_score(score, high_score):
    if int(score) > int(high_score):
        return score
    else:
        return high_score


def save_high_score(high_score):
    high_score_file = open("HI_score.txt", 'w')
    high_score_file.write(str(high_score))
    high_score_file.close()


def player_score(score, score_colour, hi_score, elapsed_time):
    display_score = score_font.render(f"Score: {score}", True, score_colour)
    screen.blit(display_score, (10, 10))  # Coordinates for top left

    # High score
    display_hi_score = score_font.render(f"High Score: {hi_score}", True, score_colour)
    screen.blit(display_hi_score, (10, 30))  # Coordinates for top left

    # Timer
    display_time = score_font.render(f"Time: {elapsed_time}", True, score_colour)
    screen.blit(display_time, (800, 10))  # Coordinates for top right


# Create snake - replaces the previous snake drawing section in the loop
def draw_snake(snake_list):
    for i in snake_list:
        pygame.draw.rect(screen, red, [i[0], i[1], 20, 20])


def message(msg, txt_colour, bkgd_colour):
    txt = msg_font.render(msg, True, txt_colour, bkgd_colour)

    # Centre rectangle: 1000/2 = 500 and 720/2 = 360
    text_box = txt.get_rect(center=(500, 360))
    screen.blit(txt, text_box)


# Function to run the main loop
def game_loop():
    start_time = time.time()  # To record time
    quit_game = False
    game_over = False

    # Initialize snake position
    snake_x = 480  # Centre point horizontally is (1000-20 snake width)/2 = 490
    snake_y = 340  # Centre point vertically is (720-20 snake height)/2 = 350

    snake_x_change = 0  # holds the value of changes in the x-coordinate
    snake_y_change = 0  # holds the value of changes in the y-coordinate
    snake_list = []
    snake_length = 1

    # Setting a random position for the food - to start
    food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(20, 720 - 20) / 20) * 20

    # Load the high score
    high_score = int(load_high_score())

    # Score
    score = 0

    # Give user the option to quit or play again when they die
    while not quit_game:
        elapsed_time = round(time.time() - start_time)  # Calculate elapsed time

        while game_over:
            save_high_score(high_score)
            screen.fill(white)
            message("You died! press 'Q' to Quit or 'A' to play Again", black, white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()  # Restart the main game loop
                if event.type == pygame.QUIT:
                    quit_game = True
                    game_over = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True

            # Handling snake movement
            if not game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        snake_x_change = -20
                        snake_y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        snake_x_change = 20
                        snake_y_change = 0
                    elif event.key == pygame.K_UP:
                        snake_x_change = 0
                        snake_y_change = -20
                    elif event.key == pygame.K_DOWN:
                        snake_x_change = 0
                        snake_y_change = 20

        if snake_x >= 1000 or snake_x < 0 or snake_y >= 720 or snake_y < 0:
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)  # Changes screen (surface) from default black to green

        # Create snake (replaces simple rectangle in previous version)
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        draw_snake(snake_list)

        player_score(score, black, high_score, elapsed_time)

        # Link speed of snake to player score to increase difficulty
        if score > 3:
            speed = score
        else:
            speed = 3

        # Create circle for food
        food = pygame.Rect(food_x, food_y, 20, 20)
        apple = pygame.image.load('images/apple_3.png').convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple, [20, 20])
        screen.blit(resized_apple, food)

        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            # Set new random position for the food if snake touches it
            food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
            food_y = round(random.randrange(20, 720 - 20) / 20) * 20

            # Increase length of snake (by original size)
            snake_length += 1

            # Increment score
            score += 1

            # Update high score
            high_score = update_high_score(score, high_score)

        # Limit frame rate to 5 fps
        clock.tick(5)

    pygame.quit()
    quit()


# Main routine
game_loop()


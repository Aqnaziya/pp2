import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def generate_food():
    foods = []
    for _ in range(3):  # Generate 3 red foods
        x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        foods.append({"x": x, "y": y, "color": RED, "points": 1, "duration": 150})
    # Generate 1 blue food
    x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    foods.append({"x": x, "y": y, "color": BLUE, "points": 3, "duration": 150})
    return foods

def regenerate_food():
    global foods
    foods = generate_food()

def Your_score(score, level):
    value = score_font.render("Ur score: " + str(score) + " and Ur level: " + str(level), True, WHITE)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    global snake_speed, foods
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    level = 0  # Set initial level
    foods = generate_food()

    while not game_over:
        while game_close == True:
            dis.fill(BLACK)
            message("You lose! Press Q for exit or press C to play again!", RED)
            Your_score(Length_of_snake - 1, level)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLACK)

        for food in foods:
            if food['duration'] > 0:
                pygame.draw.rect(dis, food['color'], [food['x'], food['y'], snake_block, snake_block])
                food['duration'] -= 1
            else:
                foods.remove(food)

        if not foods:
            regenerate_food()

        for food in foods:
            if x1 == food['x'] and y1 == food['y']:
                Length_of_snake += food['points']
                foods.remove(food)
            if (Length_of_snake - 1) % 10 == 0 and Length_of_snake - 1 != 0:
                level += 1

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1, level)
        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
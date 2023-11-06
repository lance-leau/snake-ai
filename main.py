import hamiltonian_cycle
import snake_game

import pygame
import random
import time

GRID_WIDTH = snake_game.GRID_WIDTH
GRID_HEIGHT = snake_game.GRID_HEIGHT
SQUARE_SIZE = snake_game.SQUARE_SIZE


def player():
    snake = snake_game.Snake()
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * SQUARE_SIZE, GRID_HEIGHT * SQUARE_SIZE))
    
    # Main loop
    quit = False
    while not quit:
        # check for events
        for event in pygame.event.get():
            # if red cross is pressed
            if event.type == pygame.QUIT:
                quit = True
            # if key is pressed
            if event.type == pygame.KEYDOWN:
                snake.checkKey(event.key)
        
        if (snake.inputQueue != []):
            snake.direction = snake.inputQueue.pop(0)
        
        # update grid state
        if not snake.step():
            snake.printSnake(screen, (255, 0, 0))
            pygame.display.flip()
            time.sleep(1)
            quit = True
        snake.printSnake(screen)
        pygame.display.flip()
        time.sleep(0.2)
    
    # Quit pygame
    pygame.quit()
    
def ai():
    snake = snake_game.Snake()
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * SQUARE_SIZE, GRID_HEIGHT * SQUARE_SIZE))

    # generate cycle:
    cycle = hamiltonian_cycle.generate_hamiltonian_cycle(GRID_WIDTH, GRID_HEIGHT)

    # Main loop
    quit = False
    while not quit:
        # check for events
        for event in pygame.event.get():
            # if red cross is pressed
            if event.type == pygame.QUIT:
                quit = True
        
        dir = snake.getDirectionFromPath(cycle, cycle[snake.apple[1]][snake.apple[0]])
        snake.inputQueue.append(dir)

        if (snake.inputQueue != []):
            snake.direction = snake.inputQueue.pop(0)
        
        # update grid state
        if not snake.step():
            snake.printSnake(screen, (255, 0, 0))
            pygame.display.flip()
            time.sleep(1)
            quit = True
        snake.printSnake(screen)
        pygame.display.flip()
        if snake.size > 390:
            time.sleep(1)
        else:
            time.sleep(0.02)
    # Quit pygame
    pygame.quit()

def start():
    inp = int(input("player(1)/ai(2)\n"))
    if inp == 1:
        player()
    elif inp == 2:
        ai()
    else:
        start()

start()
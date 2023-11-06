import pygame
import random

# constants
GRID_WIDTH = 25
GRID_HEIGHT = 8
SQUARE_SIZE = 30

class Direction:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Snake:
    def __init__(self):
        '''
        a snake is an array of 2D coords with a direction
        the head of the snake is at index 0
        '''
        self.body = [(2, 0), (1, 0), (0, 0)]
        self.direction = Direction.RIGHT
        self.size = 3
        self.inputQueue = []
        self.apple = (GRID_WIDTH//2, GRID_HEIGHT//2)
        self.addBody = False # set to True if just eaten apple 

    def step(self):
        '''
        makes the snake move one step in the direction it is going
        return - True if step is valid
               - False if step is not valid
        '''
        if self.addBody:
            self.size += 1
            self.addBody = False
            if not self.resetApple():
                return False
        else:
            self.body.pop()
        
        (new_x, new_y) = (self.body[0][0], self.body[0][1])
        
        match self.direction:
            case Direction.UP:
                new_y = new_y - 1 if new_y - 1 >= 0 else GRID_HEIGHT - 1
            case Direction.RIGHT:
                new_x = new_x + 1 if new_x + 1 < GRID_WIDTH else 0
            case Direction.DOWN:
                new_y = new_y + 1 if new_y + 1 < GRID_HEIGHT else 0
            case Direction.LEFT:
                new_x = new_x - 1 if new_x - 1 >= 0 else GRID_WIDTH - 1
        
        if (new_x, new_y) == self.apple:
            self.addBody = True
        
        if (new_x, new_y) in self.body:
            self.body.insert(0, (new_x, new_y))
            return False
        
        self.body.insert(0, (new_x, new_y))
        
        return True
    
    def resetApple(self):
        freeCells = []
        for i in range(GRID_HEIGHT):
            for j in range(GRID_WIDTH):
                if (j, i) not in self.body:
                    freeCells.append((j, i))
        if freeCells == []:
            return False
        else:
            self.apple = freeCells[random.randint(0, len(freeCells)-1)]
            return True

    
    def printSnake(self, screen, color = (0, 255, 0)):

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1000, 500))

        apple = pygame.Rect(self.apple[0] * SQUARE_SIZE, self.apple[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(screen, (255, 0, 0), apple)

        for bod in self.body:
            borderSize = SQUARE_SIZE//10
            square = pygame.Rect((bod[0]*SQUARE_SIZE) + borderSize, (bod[1]*SQUARE_SIZE) + borderSize, SQUARE_SIZE - 2 * borderSize, SQUARE_SIZE - 2 * borderSize)
            pygame.draw.rect(screen, color, square)

        square = pygame.Rect((self.body[0][0]*SQUARE_SIZE), (self.body[0][1]*SQUARE_SIZE), SQUARE_SIZE, SQUARE_SIZE)
        pygame.draw.rect(screen, color, square)


    def checkKey(self, key):
        match key:
            case pygame.K_UP:
                if (self.inputQueue == []):
                    if self.direction != Direction.DOWN:
                        self.inputQueue.append(Direction.UP)
                elif (self.inputQueue[-1] != Direction.DOWN):
                    self.inputQueue.append(Direction.UP)
            case pygame.K_RIGHT:
                if (self.inputQueue == []):
                    if self.direction != Direction.LEFT:
                        self.inputQueue.append(Direction.RIGHT)
                elif (self.inputQueue[-1] != Direction.LEFT):
                    self.inputQueue.append(Direction.RIGHT)
            case pygame.K_DOWN:
                if (self.inputQueue == []):
                    if self.direction != Direction.UP:
                        self.inputQueue.append(Direction.DOWN)
                elif (self.inputQueue[-1] != Direction.UP):
                    self.inputQueue.append(Direction.DOWN)
            case pygame.K_LEFT:
                if (self.inputQueue == []):
                    if self.direction != Direction.RIGHT:
                        self.inputQueue.append(Direction.LEFT)
                elif (self.inputQueue[-1] != Direction.RIGHT):
                    self.inputQueue.append(Direction.LEFT)

    def getDirectionFromPath(self, cycle, apple):
        (x, y) = (self.body[0][0], self.body[0][1])
        currPathPos = cycle[y][x]
        max = GRID_HEIGHT * GRID_WIDTH
        if x+1 < GRID_WIDTH and cycle[y][x+1] == (currPathPos+1)%max:
            ret = (Direction.RIGHT, cycle[y][x+1])
        elif y+1 < GRID_HEIGHT and cycle[y+1][x] == (currPathPos+1)%max:
            ret = (Direction.DOWN, cycle[y+1][x])
        elif x-1 >= 0 and cycle[y][x-1] == (currPathPos+1)%max:
            ret = (Direction.LEFT, cycle[y][x-1])
        elif y-1 >= 0 and cycle[y-1][x] == (currPathPos+1)%max:
            ret = (Direction.UP, cycle[y-1][x])
        
        if (currPathPos < apple):    
            if x+1 < GRID_WIDTH and apple - cycle[y][x+1] >= self.size and cycle[y][x+1] > ret[1]:
                ret = (Direction.RIGHT, cycle[y][x+1])
            if x-1 >= 0 and apple - cycle[y][x-1] >= self.size and cycle[y][x-1] > ret[1]:
                ret = (Direction.LEFT, cycle[y][x-1])
            if y+1 < GRID_HEIGHT and apple - cycle[y+1][x] >= self.size and cycle[y+1][x] > ret[1]:
                ret = (Direction.DOWN, cycle[y+1][x])
            if y-1 >= 0 and apple - cycle[y-1][x] >= self.size and cycle[y-1][x] > ret[1]:
                ret = (Direction.UP, cycle[y-1][x])
            
        return ret[0]
    
    
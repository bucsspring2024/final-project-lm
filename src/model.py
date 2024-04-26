import random
import pygame

cell_size = 28

class Snake():
    def __init__(self, x, y):
        """
        Contains the snake head and body as well as direction variables
        args: (Int) Snake x-pos and Snake y-pos
        return: None
        """
        self.x = x
        self.y = y
        self.snake_head = pygame.Rect((self.x*cell_size)+cell_size, self.y*cell_size, cell_size, cell_size)
        self.snake_body = [pygame.Rect(self.x*cell_size, self.y*cell_size, cell_size, cell_size)]
        self.x_change = 0
        self.y_change = 0
        self.direction = ""

    def move(self):
        """
        Determines x and y changes based on direction
        args: None
        return: None
        """
        if self.direction == "up":
            self.x_change = 0
            self.y_change = -cell_size
        elif self.direction == "right":
            self.x_change = cell_size
            self.y_change = 0
        elif self.direction == "down":
            self.x_change = 0
            self.y_change = cell_size
        elif self.direction == "left":
            self.x_change = -cell_size
            self.y_change = 0

    def update_snake(self):
        """
        Changes x and y positons of snake to make it move
        args: None
        return: None
        """
        self.snake_body.append(self.snake_head)
        for i in range(len(self.snake_body)-1):
            self.snake_body[i].x, self.snake_body[i].y = self.snake_body[i+1].x, self.snake_body[i+1].y
        self.snake_head.x += self.x_change
        self.snake_head.y += self.y_change
        self.snake_body = self.snake_body[:-1]


class Apple():
    def __init__(self):
        """
        Contains apple object's x and y position variables
        args: None
        return: None
        """
        self.x = (random.randint(0, cell_size-1))*cell_size
        self.y = (random.randint(0, cell_size-1))*cell_size

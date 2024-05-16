import pygame, random
from src.model import Snake, Apple
from src.score import Score

class Controller:
  
  def __init__(self):
    """
    Sets up pygame data, score class, and fonts that will
    be used
    args: None
    return: None
    """
    #setup pygame data
    pygame.init()
    self.cell_size = 28
    self.screen_size = self.cell_size * self.cell_size
    self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
    self.running = True
    self.state = "menu"
    self.score = Score()
    self.clock = pygame.time.Clock()
    self.score_font = pygame.font.Font("assets/font.ttf", 100)
    self.menu_font = pygame.font.Font("assets/menu.ttf", 50)
    self.title_font = pygame.font.Font("assets/title.ttf", 150)
    self.over_font = pygame.font.Font("assets/game.ttf", 65)
    self.final_font = pygame.font.Font("assets/game.ttf", 35)
    self.return_font = pygame.font.Font("assets/title.ttf", 80)

  def mainloop(self):
    """
    Cycles through loops/screens based on self.state
    args: None
    return: None
    """
    #select state loop
    while True:
        if self.state == "menu":
           self.menuloop()
        elif self.state == "score":
           self.scoreloop()
        elif self.state == "game":
           self.gameloop()
        elif self.state =="end":
           self.endloop()
    
  def menuloop(self):
    """
    Creates main menu with three buttons
    args: None
    return: None
    """
      #event loop
    while self.state == "menu":
      for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
              pos = pygame.mouse.get_pos()
              if start_button.collidepoint(pos):
                self.state = "game"
                self.snake = Snake(random.randint(2, self.cell_size-2),10)
                self.apple = Apple()
              if quit_button.collidepoint(pos):
                pygame.quit()
                exit()
              if score_button.collidepoint(pos):
                 self.state = "score"
      #update data
      self.screen.fill("black")
      buttons = [(pygame.Rect(70,self.screen_size-300,200,150)),
                 (pygame.Rect(300,self.screen_size-300,200,150)),
                 (pygame.Rect(530,self.screen_size-300,200,150))]
      start_button = buttons[0]
      score_button = buttons[1]
      quit_button = buttons[2]
      text = [(self.menu_font.render("Start", True, "green")),
              (self.menu_font.render("Game", True, "green")),
              (self.menu_font.render("High", True, "green")),
              (self.menu_font.render("Quit", True, "green")),
              (self.menu_font.render("Score", True, "green")),
              (self.title_font.render("Snake", True, "green"))]
      for button in buttons:
         pygame.draw.rect(self.screen, "green", button, 5)
      self.screen.blit(text[0], (start_button.x+30,start_button.y+10))
      self.screen.blit(text[1], (start_button.x+30,start_button.y+70))
      self.screen.blit(text[1], (quit_button.x+30,quit_button.y+70))
      self.screen.blit(text[2], (score_button.x+30,score_button.y+10))
      self.screen.blit(text[3], (quit_button.x+30,quit_button.y+10))
      self.screen.blit(text[4], (score_button.x+30,score_button.y+70))
      self.screen.blit(text[5], (150,220))
      #redraw
      pygame.display.update()

  def scoreloop(self):
     """
    Draws high score screen with a menu button below
    args: None
    return: None
    """
     # event loop
     while self.state == "score":
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              pygame.quit()
              exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
              pos = pygame.mouse.get_pos()
              if menu_button.collidepoint(pos):
                 self.state = "menu"
         #update data
        menu = pygame.Rect((self.screen_size/2)-150,500,300,100)
        high_score = self.score.read_score()
        menu_text = self.return_font.render("Menu", True, "green")
        score_text = self.final_font.render("The High Score is: ", True, "green")
        high_score_text = self.title_font.render(high_score, True, "green")
        self.screen.fill("black")
        menu_button = pygame.draw.rect(self.screen, "green", menu, 5)
        self.screen.blit(high_score_text, (300, 200))
        self.screen.blit(score_text, (100, 150))
        self.screen.blit(menu_text, (menu.x+48,menu.y))
        #redraw
        pygame.display.update()

  def gameloop(self):
     """
    Handles game events/logic and game ending situations
    args: None
    return: None
    """
      #event loop
     while self.state == "game":
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              pygame.quit()
              exit()
           if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != "down":
                    self.snake.direction = "up"
                if event.key == pygame.K_RIGHT and self.snake.direction != "left":
                    self.snake.direction = "right"
                if event.key == pygame.K_DOWN and self.snake.direction != "up":
                    self.snake.direction = "down"
                if event.key == pygame.K_LEFT and self.snake.direction != "right":
                    self.snake.direction = "left"
      #update data
        self.snake_score = len(self.snake.snake_body)-1
        self.snake.move()
        self.screen.fill("black")
        scoring = self.score_font.render("Score: " + str(self.snake_score), True, "green")
        self.screen.blit(scoring, (0, 0))
        pygame.draw.rect(self.screen, "green", self.snake.snake_head)
        for segment in self.snake.snake_body:
            pygame.draw.rect(self.screen, "green", segment)
            pygame.draw.rect(self.screen, "black", segment, 1)
        apple = pygame.Rect(self.apple.x, self.apple.y, self.cell_size, self.cell_size)
        pygame.draw.rect(self.screen, "red", apple, 0, 12)
        self.snake.update_snake()
        if self.snake.snake_head.x > (self.screen_size-self.cell_size) or self.snake.snake_head.y > (self.screen_size-self.cell_size):
            self.state = "end"
            self.score.update_score(self.snake_score)
        if self.snake.snake_head.x < 0 or self.snake.snake_head.y < 0:
            self.state = "end"
            self.score.update_score(self.snake_score)
        snake_copy = self.snake.snake_body[:-1]
        for segment in snake_copy:
            if self.snake.snake_head.x == segment.x and self.snake.snake_head.y == segment.y:
                self.state = "end"
                self.score.update_score(self.snake_score)
        if self.snake.snake_head.x == self.apple.x and self.snake.snake_head.y == self.apple.y:
               self.snake.snake_body.append(pygame.Rect(self.snake.snake_body[-1].x, self.snake.snake_body[-1].y, self.cell_size, self.cell_size))
               self.snake.snake_body.append(pygame.Rect(self.snake.snake_body[-1].x, self.snake.snake_body[-1].y, self.cell_size, self.cell_size))
               self.apple.x = (random.randint(0, self.cell_size-1))*self.cell_size
               self.apple.y = (random.randint(0, self.cell_size-1))*self.cell_size
               for segment in self.snake.snake_body:
                  if self.apple.x == segment.x and self.apple.y == segment.y:
                     self.apple.x = (random.randint(0, self.cell_size-1))*self.cell_size
                     self.apple.y = (random.randint(0, self.cell_size-1))*self.cell_size
        self.clock.tick(20)
      #redraw
        pygame.display.update()

  def endloop(self):
     """
    Displays game over screen with score and a menu return button
    args: None
    return: None
    """
     #event loop
     while self.state == "end":
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
              pygame.quit()
              exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
              pos = pygame.mouse.get_pos()
              if menu_button.collidepoint(pos):
                 self.state = "menu"
                 self.snake_score = 0
     #update data
        self.screen.fill("black")
        final_score = self.final_font.render("Final Score: " + str(self.snake_score), True, "green")
        game_over = self.over_font.render("Game Over", True, "green")
        menu_text = self.return_font.render("Menu", True, "green")
        menu = pygame.Rect((self.screen_size/2)-150,500,300,100)
        menu_button = pygame.draw.rect(self.screen, "green", menu, 5)
        self.screen.blit(final_score, (140, 300))
        self.screen.blit(game_over, (40,200))
        self.screen.blit(menu_text, (menu.x+48,menu.y))
     #redraw
        pygame.display.update()
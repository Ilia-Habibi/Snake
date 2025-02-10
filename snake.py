import pygame,random
from sys import exit

class FOOD:
    def __init__(self):
        self.randomize()

    def draw_food(self):
        food_rect =pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),food_rect)

    def randomize(self):
        self.x = random.randint(0,x_cells-1)
        self.y = random.randint(0,y_cells-1)
        self.pos = pygame.math.Vector2(self.x,self.y)

class SNAKE:
    def __init__(self):
        self.body = [pygame.math.Vector2(5,10),pygame.math.Vector2(6,10)]
        self.direction = pygame.math.Vector2(1,0)
        self.eating = False
    
    def draw_snake(self):
        for bead in self.body:
            bead_rect = pygame.Rect(bead.x*cell_size,bead.y*cell_size,cell_size,cell_size)
            pygame.draw.rect(screen,(183,191,122),bead_rect)

    def move_snake(self):
        if self.eating == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]
            self.eating = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]

    def add_bead(self):
        self.eating = True

class LOGIC:
    def __init__(self):
        self.snake = SNAKE()
        self.food = FOOD()

    def update(self):
        self.snake.move_snake()
        self.check_eating()

    def draw_stuff(self):
        self.food.draw_food()
        self.snake.draw_snake()

    def check_eating(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_bead()


pygame.init()
cell_size=40
x_cells=20
y_cells=15
screen = pygame.display.set_mode((cell_size*x_cells,cell_size*y_cells))
pygame.display.set_caption("Snake")
clock =pygame.time.Clock()
main_game = LOGIC()
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update,150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == screen_update:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = pygame.math.Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = pygame.math.Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = pygame.math.Vector2(1,0)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = pygame.math.Vector2(-1,0)

    screen.fill((175,215,70))
    main_game.draw_stuff()
    pygame.display.update()
    clock.tick(60)
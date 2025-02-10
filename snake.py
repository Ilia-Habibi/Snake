import pygame,random
from sys import exit

class FOOD:
    def __init__(self):
        self.randomize()

    def draw_food(self):
        food_rect =pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        rotated_image = pygame.transform.rotate(load_circle, angle)
        rotated_rect = rotated_image.get_rect(center=food_rect.center)
        screen.blit(rotated_image,rotated_rect)

    def randomize(self):
        self.x = random.randint(0,x_cells-1)
        self.y = random.randint(0,y_cells-1)
        self.pos = pygame.math.Vector2(self.x,self.y)

class SNAKE:
    def __init__(self):
        self.body = [pygame.math.Vector2(5,10),pygame.math.Vector2(4,10),pygame.math.Vector2(3,10)]
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
        self.check_death()

    def draw_stuff(self):
        self.food.draw_food()
        self.snake.draw_snake()

    def check_eating(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_bead()

    def check_death(self):
        if not 0 <= self.snake.body[0].x < x_cells:
            self.game_over()
        if not 0<= self.snake.body[0].y < y_cells:
            self.game_over()

        for bead in self.snake.body[1:]:
            if  bead == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        exit()

pygame.init()
cell_size=40
x_cells=20
y_cells=15
screen = pygame.display.set_mode((cell_size*x_cells,cell_size*y_cells))
pygame.display.set_caption("Snake")
clock =pygame.time.Clock()
main_game = LOGIC()
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update,200)
load_circle = pygame.image.load('spinning circle.png').convert_alpha()
angle = 0 
rotation_speed = 6

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == screen_update:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                main_game.snake.direction = pygame.math.Vector2(0,-1)
            if event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
                main_game.snake.direction = pygame.math.Vector2(0,1)
            if event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
                main_game.snake.direction = pygame.math.Vector2(1,0)
            if event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
                main_game.snake.direction = pygame.math.Vector2(-1,0)

    angle = (angle + rotation_speed)

    screen.fill((175,50,70))
    main_game.draw_stuff()
    pygame.display.update()
    clock.tick(60)
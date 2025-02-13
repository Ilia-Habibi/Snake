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

        self.head_up = pygame.image.load('graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('graphics/head_left.png').convert_alpha()
		
        self.tail_up = pygame.image.load('graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('graphics/body_bl.png').convert_alpha()
    
    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index == 0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == pygame.math.Vector2(1,0): self.head = self.head_left
        elif head_relation == pygame.math.Vector2(-1,0): self.head = self.head_right
        elif head_relation == pygame.math.Vector2(0,1): self.head = self.head_up
        elif head_relation == pygame.math.Vector2(0,-1): self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == pygame.math.Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == pygame.math.Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == pygame.math.Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == pygame.math.Vector2(0,-1): self.tail = self.tail_down


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
        self.draw_grass()
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

    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(y_cells):
            if row % 2 == 0: 
                for col in range(x_cells):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(x_cells):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)			
        
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
load_circle = pygame.image.load('graphics/spinning circle.png').convert_alpha()
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

    screen.fill((175,215,70))
    main_game.draw_stuff()
    pygame.display.update()
    clock.tick(60)
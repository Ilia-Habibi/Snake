import pygame
from sys import exit

class Food:
    def __init__(self):
        self.x = 5
        self.y = 4
        self.pos = pygame.math.Vector2(self.x,self.y)

    def draw_food(self):
        food_rect =pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),food_rect)

pygame.init()
cell_size=40
x_cells=20
y_cells=15
screen = pygame.display.set_mode((cell_size*x_cells,cell_size*y_cells))
pygame.display.set_caption("Snake")
clock =pygame.time.Clock()
food = Food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((175,215,70))
    food.draw_food()

    pygame.display.update()
    clock.tick(60)
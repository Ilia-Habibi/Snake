import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake")
clock =pygame.time.Clock()
def draw_gradient_background(surface, top_color, bottom_color):
    for y in range(600):
        # Interpolate between the top and bottom colors
        r = top_color[0] + (bottom_color[0] - top_color[0]) * y // 600
        g = top_color[1] + (bottom_color[1] - top_color[1]) * y // 600
        b = top_color[2] + (bottom_color[2] - top_color[2]) * y // 600
        pygame.draw.line(surface, (r, g, b), (0, y), (800, y))

top_color = (50, 150, 50)  
bottom_color = (0, 50, 0) 


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    draw_gradient_background(screen, top_color, bottom_color)


    pygame.display.update()
    clock.tick(60)
import pygame
import os

WIDTH, HEIGHT = 1000, 600 

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pyracing') 

BACKGROUND_COLOR = (3, 252, 132)

FPS = 60




def draw_window():
    WIN.fill((BACKGROUND_COLOR))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()

import pygame

pygame.init()


HEIGHT, WIDTH = 700, 500

WIN = pygame.display.set_mode((700, 500))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

FPS = 60


def main():

    run = True

    clock = pygame.time.Clock()

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                break

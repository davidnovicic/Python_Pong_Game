import pygame

pygame.init()


WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGTH = 20, 100


class Paddle:
    COLOLR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):

        pygame.draw.rect(win, self.COLOLR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL


def draw(win, paddles):

    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    pygame.display.update()


def handle_paddle_movement(keys, left_paddle, right_paddle):

    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(
        10, HEIGHT // 2 - PADDLE_HEIGTH // 2, PADDLE_WIDTH, PADDLE_HEIGTH
    )
    right_paddle = Paddle(
        WIDTH - 30, HEIGHT // 2 - PADDLE_HEIGTH // 2, PADDLE_WIDTH, PADDLE_HEIGTH
    )

    while run:

        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)


if __name__ == "__main__":
    main()

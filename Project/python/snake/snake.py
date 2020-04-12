
import os
import pygame
from pygame.locals import *
import random
from collections import deque


class Block(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Screen(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.points = [[None] * self.height for _ in range(self.width)]

    def new_block(self, x, y):
        self.points[x][y] = Block(x, y)
        return self.points[x][y]

    def del_block(self, x, y):
        self.points[x][y] = None

    def desplay(self):
        pass


class SnakeGame(object):
    def __init__(self, width, height, draw_block):
        self.width = width
        self.height = height
        self.snake = None
        self._init_snake()
        self.food = self._new_food()
        self.draw_block = draw_block
        self.direction = (1, 0)
        self._init_draw()

    def _new_food(self):
        x = random.randint(0, self.width-1)
        y = random.randint(0, self.height-1)
        while (x, y) in self.snake:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
        return (x, y)

    def _init_snake(self):
        self.snake = deque()
        self.snake.append((0, self.height//2))
        self.snake.append((1, self.height//2))
        self.snake.append((2, self.height//2))

    def _init_draw(self):
        for body in self.snake:
            self.draw_block(*body, (255, 0, 0))
        self.draw_block(*self.food, color=(255, 255, 0))
        pygame.display.update()

    DIRECTIONS = {"up": (0, -1), "down": (0, 1),
                  "left": (-1, 0), "right": (1, 0)}

    def move(self, direction=None):
        if direction in self.DIRECTIONS.keys():
            x = self.direction[0] + self.DIRECTIONS[direction][0]
            y = self.direction[1] + self.DIRECTIONS[direction][1]
            if x or y:
                self.direction = (self.DIRECTIONS[direction])

        x = self.snake[-1][0] + self.direction[0]
        y = self.snake[-1][1] + self.direction[1]
        next = (x, y)

        if x < 0 or y < 0 or x >= self.width or y >= self.height or next in self.snake:
            self.process_failed()
            return

        self.snake.append(next)
        self.draw_block(*next, color=(255, 0, 0))

        if next == self.food:
            self.food = self._new_food()
            self.draw_block(*self.food, color=(255, 255, 0))
        else:
            tail = self.snake.popleft()
            self.draw_block(*tail)

        pygame.display.update()

    def process_failed(self):
        print("Game over!")


class PyBlock(Block):
    def __init__(self, x, y):
        super(PyBlock, self).__init(x, y)
        self.color =


def main():

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # 初始化pygame，为使用硬件做准备
    pygame.init()

    # 创建一个窗口
    screen = pygame.display.set_mode((900, 700), 0, 32)

    # 设置窗口标题
    pygame.display.set_caption("Snake")

    # 提示语
    text = "欢迎进入贪食蛇游戏，请按任意键开始"
    # font = pygame.font.Font(None, 60)
    screen.fill(WHITE)
    font = pygame.font.SysFont('SimHei', 32)
    font_img = font.render(text, True, RED, None)
    screen.blit(font_img, (20, 9))

    # 画出贪食蛇主界面
    pygame.draw.rect(screen, BLACK, Rect(50, 50, 800, 600))

    def draw_block(x, y, color=BLACK):
        # print("draw:", x, y)
        # pygame.draw.rect(screen, Black, Rect(50+x*20, 50+y*20, 20, 20))
        pygame.draw.rect(screen, color, Rect(50+x*20+1, 50+y*20+1, 20-2, 20-2))
    snake = SnakeGame(800//20, 600//20, draw_block)
    pygame.display.update()

    # 游戏主循环
    while True:
        event = pygame.event.wait()
        # if event.type == pygame.QUIT:
        #             exit(0)
        if event.type == QUIT:
            exit(0)
        elif event.type == KEYDOWN:
            if event.key in [K_w, K_UP]:
                snake.move("up")
            elif event.key in [K_s, K_DOWN]:
                snake.move("down")
            elif event.key in [K_a, K_LEFT]:
                snake.move("left")
            elif event.key in [K_d, K_RIGHT]:
                snake.move("right")


if __name__ == "__main__":
    main()

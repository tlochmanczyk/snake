import random


class Snake:
    def __init__(self, size):
        self.size = size
        self.reset()

    def reset(self):
        self.length = 3
        self.direction = 'u'       # u,d,l,r - directions
        self.position = [[int(self.size/2) + pos, int(self.size/2)] for pos in range(self.length)]

    def growing(self):
        self.length += 1
        self.position.append([None, None])

    def moving(self, direction=None):
        if direction is None:
            direction = self.direction

        x = self.position[0][0]
        y = self.position[0][1]

        if direction == 'u':
            x -= 1
            self.direction = 'u'
        elif direction == 'd':
            x += 1
            self.direction = 'd'
        elif direction == 'l':
            y -= 1
            self.direction = 'l'
        elif direction == 'r':
            y += 1
            self.direction = 'r'

        if x >= self.size:
            x = x - self.size
        if x <= -1:
            x = x + self.size
        if y >= self.size:
            y = y - self.size
        if y <= -1:
            y = y + self.size

        self.position = [[x, y], *(self.position[:-1])]

    def get_position(self):
        return self.position


class Board:
    def __init__(self, size=10):
        self.size = size
        self.board = self.clear()

    def fill(self, x, y, var):
        self.board[y][x] = var

    def check(self, x, y):
        return self.board[y][x]

    def clear(self):
        return [self.size * ['-'] for _ in range(self.size)]

    def print_game(self):
        for row in self.board:
            print(''.join(row))


class Loot:
    def __init__(self, size):
        self.value = 1
        self.set_coordinates(size)

    def set_coordinates(self, size):
        self.x = random.randint(0, size - 1)
        self.y = random.randint(0, size - 1)

    def get_coordinates(self):
        return [self.x, self.y]


class Game:
    def __init__(self, size=10):
        self.size = size
        self.reward = 0
        self.snake = Snake(self.size)
        self.loot = Loot(self.size)
        self.board = Board(self.size)

    def draw(self):
        self.board.board = self.board.clear()

        self.board.fill(*(self.loot.get_coordinates()), '|')

        position = self.snake.get_position()
        for pos in position:
            self.board.fill(*pos, '#')

    def rule_check(self):
        if self.loot.get_coordinates() == self.snake.get_position()[0]:
            self.reward += 1
            self.snake.growing()
            self.loot.set_coordinates(self.size)

        for pos in self.snake.position[1:]:
            if pos == self.snake.position[0]:
                return False
        return True

    def reset(self):
        self.reward = 0
        self.snake.reset()
        self.board.clear()

    def engine(self, key):
        self.snake.moving(key)
        self.draw()
        return self.board.board, self.reward, self.rule_check(), {}

import gym
from .snake_game import Game
#import snake_game
import numpy as np


from gym import error, spaces, utils
from gym.utils import seeding

import copy

class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.board_size = 10
        self.action_space = spaces.Discrete(5)  # up,down.left,right,nothing
        self.observation_space = spaces.Box(low=0, high=2, shape=((self.board_size)**2,))   # empty, snake, reward
        self.game = Game(self.board_size)

    def step(self, action):
        key = 'n'

        if action == 0:
            key = 'u'
        elif action == 1:
            key = 'd'
        elif action == 2:
            key = 'l'
        elif action == 3:
            key = 'r'
        elif action == 4:
            key = 'n'

        observation, reward, done, info = self.game.engine(key)

        observation = self.observation_transform(observation)

        return observation, reward, done, info

    def reset(self):
        self.game.reset()
        return self.observation_transform(self.game.board.board)

    def render(self, mode='human'):
        self.game.board.print_game()

    def close(self):
        del self.game

    def observation_transform(self, observation):
        observation = copy.deepcopy(observation)
        for row in range(len(observation)):
            for col in range(len(observation[row])):
                if observation[row][col] == '-': observation[row][col] = 0
                elif observation[row][col] == '#': observation[row][col] = 1
                elif observation[row][col] == '|': observation[row][col] = 2

        observation = np.array(observation)
        return np.reshape(observation, (self.board_size)**2)









# import random
#
#
# class Snake:
#     def __init__(self, size):
#         self.size = size
#         self.reset()
#
#     def reset(self):
#         self.length = 3
#         self.direction = 'u'       # u,d,l,r - directions
#         self.position = [[int(self.size/2) + pos, int(self.size/2)] for pos in range(self.length)]
#
#     def growing(self):
#         self.length += 1
#         self.position.append([None, None])
#
#     def moving(self, direction=None):
#         if direction is None:
#             direction = self.direction
#
#         x = self.position[0][0]
#         y = self.position[0][1]
#
#         if direction == 'u':
#             x -= 1
#             self.direction = 'u'
#         elif direction == 'd':
#             x += 1
#             self.direction = 'd'
#         elif direction == 'l':
#             y -= 1
#             self.direction = 'l'
#         elif direction == 'r':
#             y += 1
#             self.direction = 'r'
#
#         if x >= self.size:
#             x = x - self.size
#         if x <= -1:
#             x = x + self.size
#         if y >= self.size:
#             y = y - self.size
#         if y <= -1:
#             y = y + self.size
#
#         self.position = [[x, y], *(self.position[:-1])]
#
#     def get_position(self):
#         return self.position
#
#
# class Board:
#     def __init__(self, size=10):
#         self.size = size
#         self.board = self.clear()    # (e)mpty, envs (t)ail,  envs (h)ead, (r)eward
#
#     def fill(self, x, y, var):
#         self.board[y][x] = var
#
#     def check(self, x, y):
#         return self.board[y][x]
#
#     def clear(self):
#         return [self.size * ['-'] for _ in range(self.size)]
#
#     def print_game(self):
#         for row in self.board:
#             print(''.join(row))
#
#
# class Loot:
#     def __init__(self, size):
#         self.value = 1
#         self.set_coordinates(size - 1)
#
#     def set_coordinates(self, size):
#         self.x = random.randint(0, size)
#         self.y = random.randint(0, size)
#
#     def get_coordinates(self):
#         return [self.x, self.y]
#
#
# class Game:
#     def __init__(self, size=10):
#         self.size = size
#         self.reward = 0
#         self.snake = Snake(self.size)
#         self.loot = Loot(self.size)
#         self.board = Board(self.size)
#
#     def draw(self):
#         self.board.board = self.board.clear()
#         #self.board.cls()
#
#         self.board.fill(*(self.loot.get_coordinates()), '|')
#
#         position = self.snake.get_position()
#         for pos in position:
#             self.board.fill(*pos, '#')
#
#         # self.board.print_game()
#
#     def rule_check(self):
#         if self.loot.get_coordinates() == self.snake.get_position()[0]:
#             self.reward += 1
#             self.snake.growing()
#             self.loot.set_coordinates(self.size)
#
#         for pos in self.snake.position[1:]:
#             if pos == self.snake.position[0]:
#                 return False
#         return True
#
#     def reset(self):
#         self.reward = 0
#         self.snake.reset()
#         self.board.clear()
#
#     def engine(self, key):
#         self.snake.moving(key)
#         self.draw()
#         return self.board.board, self.reward, self.rule_check(), {}


# if __name__ == '__main__':
#     g = Game()
#     cond = True
#     i = 0
#     while cond or i > 100:
#         key = input()
#         if key == 'n':
#             key = None
#
#         cond = g.engine(key)
#         i += 1


import gym
from .snake_game import Game
import numpy as np
from gym import spaces
import copy


class SnakeEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.board_size = 10
        self.action_space = spaces.Discrete(5)  # up,down.left,right,nothing
        self.observation_space = spaces.Box(low=0, high=2, shape=(self.board_size**2,))   # empty, snake, reward
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
                if observation[row][col] == '-':
                    observation[row][col] = 0
                elif observation[row][col] == '#':
                    observation[row][col] = 1
                elif observation[row][col] == '|':
                    observation[row][col] = 2

        observation = np.array(observation)
        return np.reshape(observation, self.board_size**2)

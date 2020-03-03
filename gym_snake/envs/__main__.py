#from .snake_env import SnakeEnv
import gym_snake
# import gym
#
# env = gym.make('snake-v0')
# print(env.reset())

from tkinter import *

from gym_snake.envs import snake_gui

import pyperclip


def ClickedPlay():
    snake_gui.main()


def ClickedTrain():
    txt = "hmmmmm"
    pyperclip.copy(txt)


def ClickedTest():
    pass

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    window = Tk()

    window.title("Welcome to snake environment app")

    window.geometry('150x200')

    btn_play = Button(window, text="Play!", width = 10, height = 2, command=ClickedPlay)
    btn_play.grid(row=1)
    window.grid_rowconfigure(0, minsize = 15)
    window.grid_columnconfigure(0, weight = 1)

    btn_train = Button(window, text="Train", width = 10, height = 2, command=ClickedTrain)
    btn_train.grid(row=3)
    window.grid_rowconfigure(2, minsize = 20)
    window.grid_columnconfigure(0, weight = 1)

    btn_test = Button(window, text="Test", width = 10, height = 2)
    btn_test.grid(row=5)
    window.grid_rowconfigure(4, minsize = 20)
    window.grid_columnconfigure(0, weight = 1)

    window.mainloop()

if __name__ == '__main__':
    main()
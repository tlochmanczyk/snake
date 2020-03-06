# TODO: join menu in tkinter with snake_gui
# TODO: make comments
# TODO: make requirements.txt
# TODO: make README.md (with installation)
# TODO: make train&test funcionality
# TODO: make display in menu
# TODO: add tests
# TODO: add new ideas to game


from tkinter import *
from gym_snake.envs import snake_gui
import pyperclip


def clicked_play():
    snake_gui.main()


def clicked_train():
    txt = "train template + new file soon"
    pyperclip.copy(txt)


def clicked_test():
    txt = "test template soon"
    pyperclip.copy(txt)


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    window = Tk()

    window.title("Welcome to snake environment app")

    window.geometry('150x200')

    btn_play = Button(window, text="Play!", width=10, height=2, command=clicked_play)
    btn_play.grid(row=1)
    window.grid_rowconfigure(0, minsize=15)
    window.grid_columnconfigure(0, weight=1)

    btn_train = Button(window, text="Train", width=10, height=2, command=clicked_train)
    btn_train.grid(row=3)
    window.grid_rowconfigure(2, minsize=20)
    window.grid_columnconfigure(0, weight=1)

    btn_test = Button(window, text="Test", width=10, height=2, command=clicked_test())
    btn_test.grid(row=5)
    window.grid_rowconfigure(4, minsize=20)
    window.grid_columnconfigure(0, weight=1)

    window.mainloop()


if __name__ == '__main__':
    main()

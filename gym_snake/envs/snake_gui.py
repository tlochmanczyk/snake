import arcade
import random
print('dupa')
#import snake_game
from .snake_game import Game

SQUARE_SIZE = 25
MARGIN = 5
ROWS = 10
COLUMNS = 10

SCREEN_WIDTH = (SQUARE_SIZE + MARGIN) * COLUMNS + MARGIN
SCREEN_HEIGHT = (SQUARE_SIZE + MARGIN) * ROWS + MARGIN

SCREEN_TITLE = "SNAKE"

SNAKE_COLOR = arcade.color.ANDROID_GREEN
REWARD_COLOR = arcade.color.AMBER
EMPTY_COLOR = arcade.color.ANTIQUE_WHITE


#class Display(arcade.Window, snake_game.Game):
class Display(arcade.Window, Game):

    """Main welcome window
    """
    def __init__(self, game):
        """Initialize the window
        """
        self.game = game
        self.board = game.board.board #= self.board_mock() #
        self.key = None

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.ARSENIC)



    def on_draw(self):

        arcade.start_render()

        for row in range(ROWS):
            for col in range(COLUMNS):
                if self.board[row][col] == '-':
                    color = EMPTY_COLOR
                elif self.board[row][col] == '|':
                    color = REWARD_COLOR
                else:
                    color = SNAKE_COLOR

                x = (MARGIN + SQUARE_SIZE) * col + MARGIN + SQUARE_SIZE // 2
                y = (MARGIN + SQUARE_SIZE) * row + MARGIN + SQUARE_SIZE // 2

                arcade.draw_rectangle_filled(x, y, SQUARE_SIZE, SQUARE_SIZE, color)

    def board_mock(self):
        elems = ['-', '|', '#']
        tmp = []
        for _ in range(COLUMNS):
            x = [random.choice(elems) for _ in range(ROWS)]
            tmp.append(x)
        return tmp

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.key = 'r'
        elif symbol == arcade.key.DOWN:
            self.key = 'l'
        elif symbol == arcade.key.RIGHT:
            self.key = 'd'
        elif symbol == arcade.key.LEFT:
            self.key = 'u'


    def on_update(self, delta_time):
        self.board, _, rules, _ = self.game.engine(self.key)
        if not rules:
            arcade.close_window()


def main():
    x = Game()
    app = Display(x)
    arcade.run()

# Main code entry point
if __name__ == "__main__":
    #x = snake_game.Game()
    # x = Game()
    # app = Display(x)
    # arcade.run()
    main()
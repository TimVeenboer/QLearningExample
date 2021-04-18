import numpy as np

WIDTH, HEIGHT = 4, 6

class Game:
    def __init__(self):
        self.board = np.array([
            [-1, -1, -100, -1],
            [-100, -1, -100, -1],
            [-100, -1, -1, -1],
            [-100, -100, -1, -100],
            [-100, -1, -1, -100],
            [+100, -1, -100, -100]
        ])

        self.done = False
        self.player_position = [0, 0]

    def move(self, action):
        if action == 0:
            # move right
            if self.player_position[1] < WIDTH-1:
                self.player_position[1] += 1
        if action == 1:
            # move left
            if self.player_position[1] > 0:
                self.player_position[1] -= 1
        if action == 2:
            # move down
            if self.player_position[0] < HEIGHT-1:
                self.player_position[0] += 1
        if action == 3:
            # move up
            if self.player_position[0] > 0:
                self.player_position[0] -= 1

        reward = self.board[self.player_position[0]][self.player_position[1]]

        if reward == 100 or reward == -100:
            self.done = True

        return reward

    def __str__(self):
        """Print the board"""
        board_str = ''
        b = self.board.copy()
        b[self.player_position[0]][self.player_position[1]] = 0
        for row in b:
            for space in row:
                symbol = 'X'
                if space == -1:
                    symbol = 'G'
                elif space == 100:
                    symbol = 'F'
                elif space == 0:
                    symbol = 'P'

                board_str += '|{}'.format(symbol)
            board_str += '|\n'

        return '-'*9 + '\n' + board_str + '-'*9
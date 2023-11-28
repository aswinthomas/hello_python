from player import Player
from grid import GridState


class Game:
    def __init__(self, grid, connectN, targetScore):
        self._grid = grid
        self._connectN = connectN
        self._targetScore = targetScore

        self._players = [
            Player('Player 1', GridState.YELLOW),
            Player('Player 2', GridState.RED)
        ]

        self._score = {}
        for player in self._players:
            self._score[player.get_name()] = 0

    def print_board(self):
        print('Board:\n')
        grid = self._grid.get_grid()
        for i in range(len(grid)):
            row = ''
            for piece in grid[i]:
                if piece == GridState.EMPTY:
                    row += '0 '
                elif piece == GridState.YELLOW:
                    row += 'Y '
                elif piece == GridState.RED:
                    row += 'R '
            print(row)
        print('')

    def play_move(self, player):
        self.print_board()
        print(f"{player.get_name()}'s turn")
        col_cnt = self._grid.get_column_count()
        move_column = int(input(f"Enter column between {0} and {col_cnt - 1} to add piece: "))
        move_row = self._grid.place_piece(move_column, player.get_piece_color())
        return move_row, move_column

    def play_round(self):
        while True:
            for player in self._players:
                row, col = self.play_move(player)
                piece_color = player.get_piece_color()
                if self._grid.check_win(self._connectN, row, col, piece_color):
                    self._score[player.get_name()] += 1
                    return player

    def play(self):
        max_score = 0
        winner = None
        while max_score < self._targetScore:
            winner = self.play_round()
            print(f"{winner.get_name()} won the round")
            max_score = max(self._score[winner.get_name()], max_score)

            self._grid.initGrid()  # reset grid
        print(f"{winner.get_name()} won the game")

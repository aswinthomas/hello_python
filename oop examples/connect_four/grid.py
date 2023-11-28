from enum import Enum


class GridState(Enum):
    EMPTY = 0,
    YELLOW = 1,
    RED = 2


class Grid:
    def __init__(self, rows, columns):
        self._m = rows
        self._n = columns
        self._grid = None
        self.init_grid()

    def init_grid(self):
        self._grid = [[GridState.EMPTY for _ in range(self._n)] for _ in range(self._m)]

    def get_grid(self):
        return self._grid

    def get_column_count(self):
        return self._n

    def place_piece(self, column, piece):
        if column < 0 or column >= self._n:
            raise ValueError("Invalid Column input")
        if piece == GridState.EMPTY:
            raise ValueError("Piece cannot be empty")
        for r in range(self._m - 1, -1, -1):
            if self._grid[r][column] == GridState.EMPTY:
                self._grid[r][column] = piece
                return r

    def check_win(self, connectN, row, col, piece):
        count = 0
        # Check horizontal
        for c in range(self._n):
            if self._grid[row][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check vertical
        count = 0
        for r in range(self._m):
            if self._grid[r][col] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check diagonal
        count = 0
        for r in range(self._m):
            c = row + col - r
            if 0 <= c < self._n and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        # Check anti-diagonal
        count = 0
        for r in range(self._m):
            c = col - row + r
            if 0 <= c < self._n and self._grid[r][c] == piece:
                count += 1
            else:
                count = 0
            if count == connectN:
                return True

        return False

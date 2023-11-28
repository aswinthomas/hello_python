class Player:
    def __init__(self, name, piece_color):
        self._name = name
        self._color = piece_color

    def get_name(self):
        return self._name

    def get_piece_color(self):
        return self._color

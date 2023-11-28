## Connect four

Design a Connect Four game played on a mxn grid. Two players take turns dropping colored discs into the
grid. The first player to get four discs in a row (vertically, horizontally or diagonally) wins.

### High level details

- Grid represent state of the board, each cell having a state of empty, red or yellow. This could be a GridState enum.
- Player with a color assigned and playing multiple rounds, each playing with their turn say place_piece()
- Score of each player after multiple game rounds
- Game containing everything including Player and Grid, keeping track of Score
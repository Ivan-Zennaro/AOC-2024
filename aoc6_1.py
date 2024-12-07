from enum import Enum

class Direction(Enum):
    UP = 1 
    RIGHT = 2
    DOWN = 3
    LEFT = 4

move = {
    Direction.UP: (-1, 0),
    Direction.RIGHT: (0, 1),
    Direction.DOWN: (1, 0),
    Direction.LEFT: (0, -1)
}

matrix = []

def find_start_position(mat):
    return next(((x, y) for x, row in enumerate(mat) for y, value in enumerate(row) if value == '^'), None)

def nextDirection(dir):
    directions = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]
    return directions[(directions.index(dir) + 1) % len(directions)]

def walk(dir, x, y, mat):
    mat[x][y] = "X"
    while(True):
        dx, dy = move[dir]
        newPos = (x + dx, y + dy)

        if not(0 <= newPos[0] < len(matrix) and 0 <= newPos[1] < len(matrix[0])):
            return mat

        if mat[newPos[0]][newPos[1]] == "#":
            dir = nextDirection(dir)
        else:
            x, y = newPos
            mat[x][y] = "X"

with open("input.txt", "r") as file:
    for line in file:
        row = list(line.strip())
        matrix.append(row)

position = find_start_position(matrix)
res = walk(Direction.UP, position[0], position[1], matrix)
print(sum(row.count('X') for row in res))
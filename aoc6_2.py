from enum import Enum
from aoc6_1 import walk, find_start_position, Direction, move, nextDirection

space = []

def isLoop(dir, x, y, mat, dirMat, initial) -> bool:
    mat[x][y] = 'X'
    dirMat[x][y].add(dir)
    while(True):  
        dx, dy = move[dir]
        newPos = (x + dx, y + dy)
        if not(0 <= newPos[0] < len(space) and 0 <= newPos[1] < len(space[0])):
            return 0
        if dir in dirMat[newPos[0]][newPos[1]]: #loop
            return 1
        if mat[newPos[0]][newPos[1]] == "#":
            dir = nextDirection(dir)
        else:
            x, y = newPos
            mat[x][y] = "X"
            dirMat[x][y].add(dir)

with open("input.txt", "r") as file:
    for line in file:
        row = list(line.strip())
        space.append(row)

tot = 0
start_position = find_start_position(space)
space_copy = [row[:] for row in space]
visitedSpace = walk(Direction.UP, start_position[0], start_position[1], space_copy)
visitedCoordinates = {(x, y) for x, row in enumerate(visitedSpace) for y, value in enumerate(row) if value == 'X'}
visitedCoordinates.remove(start_position)

for coordinates in visitedCoordinates:
    space_copy = [row[:] for row in space]
    space_copy[coordinates[0]][coordinates[1]] = "#"
    visitedDirections = [[set() for _ in range(len(space[0]))] for _ in range(len(space))] # to keep track of the visit direction
    if isLoop(Direction.UP, start_position[0], start_position[1], space_copy, visitedDirections, coordinates):
        tot += 1

print(tot)
print("end")



matrix = []

with open("input.txt", "r") as file:
    for line in file:
        row = list(line.strip())
        matrix.append(row)

    tot = 0
    for i in range(len(matrix)-2):
        for j in range(len(matrix[0])-2):
            if matrix[i][j] == 'S' and matrix[i][j +2] == 'S' and matrix[i+1][j+1] == 'A' and matrix[i+2][j] == 'M' and matrix[i+2][j+2] == 'M':
                tot += 1
            if matrix[i][j] == 'M' and matrix[i][j +2] == 'S' and matrix[i+1][j+1] == 'A' and matrix[i+2][j] == 'M' and matrix[i+2][j+2] == 'S':
                tot += 1
            if matrix[i][j] == 'M' and matrix[i][j +2] == 'M' and matrix[i+1][j+1] == 'A' and matrix[i+2][j] == 'S' and matrix[i+2][j+2] == 'S':
                tot += 1
            if matrix[i][j] == 'S' and matrix[i][j +2] == 'M' and matrix[i+1][j+1] == 'A' and matrix[i+2][j] == 'S' and matrix[i+2][j+2] == 'M':
                tot += 1
print(tot)
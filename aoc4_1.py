matrix = []

with open("input.txt", "r") as file:
    for line in file:
        row = list(line.strip())
        matrix.append(row)

    tot = 0

    # scan horizontal
    for i in range(len(matrix)):
        for j in range(len(matrix[0]) - 3):
            substr = ''.join(matrix[i][j:j+4])
            if substr == "XMAS" or substr == "SAMX":
                tot += 1

    # scan vertical
    for j in range(len(matrix[0])):
        for i in range(len(matrix)-3):
            substr = ''.join(matrix[i + k][j] for k in range(4))
            if substr == "XMAS" or substr == "SAMX":
                tot += 1

    # scan diagonal 1
    for i in range(len(matrix)-3):
        for j in range(len(matrix[0])-3):
            substr = matrix[i][j] + matrix[i + 1][j+1] + matrix[i+2][j+2] + matrix[i+3][j+3]
            if substr == "XMAS" or substr == "SAMX":
                tot += 1

    # scan diagonal 2
    for i in range(len(matrix)-3):
        for j in range(3, len(matrix[0])):
            substr = matrix[i][j] + matrix[i+1][j-1] + matrix[i+2][j-2] + matrix[i+3][j-3]
            if substr == "XMAS" or substr == "SAMX":
                tot += 1

print(tot)
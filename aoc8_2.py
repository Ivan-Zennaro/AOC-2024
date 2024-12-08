from collections import defaultdict

space = []

with open("input.txt", "r") as file:
    for line in file:
        row = list(line.strip())
        space.append(row)

stations = defaultdict(list)
antinodes = set()

for i, line in enumerate(space):
    for j, elem in enumerate(line):
        if elem != '.':
            stations[elem].append((i,j))
            antinodes.add((i,j))

for s in stations:

    for i1, c1 in enumerate(stations[s]):
        for i2, c2 in enumerate(stations[s]):

            if i1 == i2: continue

            dx = c2[1] - c1[1]
            dy = c2[0] - c1[0]

            antiX = c2[1] + dx
            antiY = c2[0] + dy 
           
            while 0 <= antiX < len(space[0]) and 0 <= antiY < len(space):
                antinodes.add((antiY, antiX))
                antiY = antiY + dy 
                antiX = antiX + dx            

print(len(antinodes))
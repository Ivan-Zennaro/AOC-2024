from aoc2_1 import isSafe

with open('input.txt', 'r') as file:
    tot = 0
    for line in file:
        rep = list(map(int,line.split()))
        if any(isSafe(rep[:i] + rep[i+1:]) for i in range(len(rep))):
            tot += 1
    print(tot)

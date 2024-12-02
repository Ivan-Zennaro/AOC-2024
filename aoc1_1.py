with open('input.txt', 'r') as file:
    data = [list(map(int, line.split())) for line in file]

    l1, l2 = zip(*data)
    tot = sum(abs(a - b) for a, b in zip(sorted(l1), sorted(l2)))

    print(tot)

from collections import Counter

with open('input.txt', 'r') as file:
    l1, l2 = zip(*(map(int, line.split()) for line in file))

dict2 = Counter(l2)
tot = sum(x * dict2[x] for x in l1)

print(tot)

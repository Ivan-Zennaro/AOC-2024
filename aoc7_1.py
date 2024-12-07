matrix = []

def compute(l, bin):
    tot = l[0]
    for i, b in enumerate(bin):
        tot = tot + l[i + 1] if b == 0 else tot * l[i + 1]
    return tot

tot = 0

with open("input.txt", "r") as file:
    for line in file:
        key, values = line.strip().split(": ")
        key = int(key)
        values_list = list(map(int, values.split()))
        total_combinations = 2 ** (len(values_list) - 1)

        for i in range(total_combinations):
            binary_representation = list(map(int,format(i, f'0{len(values_list)-1}b')))
            if compute(values_list, binary_representation) == key:
                tot += key
                break

print(tot)

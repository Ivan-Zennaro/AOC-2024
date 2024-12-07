def compute(l, bin):
    tot = l[0]
    operations = {0: lambda x: x + l[i + 1], 1: lambda x: x * l[i + 1], 2: lambda x: int(str(x) + str(l[i + 1]))}
    
    for i, b in enumerate(bin):
        tot = operations[b](tot)
    
    return tot

def convert_to_ternary(number, length):
    ternary = ""
    while number > 0:
        ternary = str(number % 3) + ternary
        number //= 3
    return ternary.zfill(length)

def precompute_combinations(num_values):
    total_combinations = 3 ** (num_values - 1)
    return [list(map(int, convert_to_ternary(i, num_values - 1))) for i in range(total_combinations)]
    
with open("input.txt", "r") as file:
    nLines = sum(1 for _ in file)

res = 0
with open("input.txt", "r") as file:
    counter = 0
    for line in file:
        counter += 1
        print(f"Computing line {counter} of {nLines}")
        
        key, values = line.strip().split(": ")
        key = int(key)
        values_list = list(map(int, values.split()))

        ternary_combinations = precompute_combinations(len(values_list))

        # Try all ternary combinations and check if computed value matches the key
        for ternary_rep in ternary_combinations:
            computed = compute(values_list.copy(), ternary_rep)
            if computed == key:
                res += key
                break

print(res)

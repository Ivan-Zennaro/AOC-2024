from collections import defaultdict

rule = defaultdict(set)
update = []

with open('input.txt', 'r') as file:
    for line in file.read().splitlines():
        if '|' in line:
            key, value = map(int, line.split('|'))
            rule[key].add(value)
        elif ',' in line:
            update.append(list(map(int, line.split(','))))

tot = 0  

for line in update:
    valid = True

    for i in range(1, len(line)):
        if not valid:
            break
        # Check if any previous element is in rule of the current element
        if any(line[j] in rule[line[i]] for j in range(i)):
            valid = False

    # If valid, add the middle element to the total
    if valid:
        tot += line[len(line) // 2]
        
print(tot)
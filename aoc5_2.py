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
        for j in range(0, i):
            if line[j] in rule[line[i]]: 
                line[i], line[j] = line[j], line[i]
                valid = False

    # If not valid, add the middle element to the total
    if not valid:
       tot += line[len(line) // 2]
        
print(tot)
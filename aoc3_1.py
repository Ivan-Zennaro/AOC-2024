import re

with open('input.txt', 'r') as file:

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, file.read())

    tot = 0
    for match in matches:
        num1, num2 = map(int, match)
        tot += num1 * num2
    
    print(tot)
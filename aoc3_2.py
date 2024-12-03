import re

with open('input.txt', 'r') as file:

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"
    matches = re.findall(pattern, file.read())

    tot = 0
    do = True

    for match in matches:
        if "do()" in match:  
            do = True
        elif "don't()" in match:  
            do = False
        elif do:  
            num1, num2, _, _ = match
            tot += int(num1) * int(num2)

    print(tot)
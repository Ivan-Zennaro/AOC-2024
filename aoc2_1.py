def isIncreasing(arr) -> bool:
    return len(arr) < 2 or arr[-1] > arr[0]

def isSafe(arr) -> bool:
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] > 0 and not isIncreasing(arr):
            return False
        if arr[i + 1] - arr[i] < 0 and isIncreasing(arr):
            return False
        if abs(arr[i + 1] - arr[i]) > 3 or arr[i + 1] == arr[i]:
            return False
    return True

with open('input.txt', 'r') as file:
    tot = sum(1 for line in file if isSafe(list(map(int, line.split()))))
    print(tot)

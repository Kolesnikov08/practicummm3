import math
n = int(input())
for i in range(2, n + 1):
    prostoe = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            prostoe = False
            break
    if prostoe:
        print(i)
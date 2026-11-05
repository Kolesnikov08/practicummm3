n = int(input())
c = 0
for i in range(1, n):
    for j in range(i, n):
        if i**2 + j**2 == n:
            c = c + 1
print(c)
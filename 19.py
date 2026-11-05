n = int(input())
c = 0
for i in range(0, n+1):
    for j in range(i, n+1):
            c = c + i + j
print(c)
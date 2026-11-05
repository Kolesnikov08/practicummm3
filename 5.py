n = int(input())
for i in range(1, n):
    n1 = i**3
    if n1<n:
        print(n1, end=' ')
    else:
        break

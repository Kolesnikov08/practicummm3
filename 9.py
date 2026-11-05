n, k, r = map(int, input().split())
s = n
d = 1
while s < r:
    s = s + s*k/100
    d = d + 1
print(d)
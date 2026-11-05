a = float(input())
b = float(input())
c = 0
while a != 0:
    if a < b:
        c = c + 1
    a = b
    b = float(input())
print(c)
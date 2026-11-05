import math
n = int(input('введите число: '))
while math.sqrt(n) != int(math.sqrt(n)):
    print('нет')
    n = int(input('введите еще раз '))
print('нормас')
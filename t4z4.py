a = int(input("Введите целое число:\n"))
b = 0
while a > 0:
    c = a % 10
    a = a // 10
    b = b * 10
    b = b + c
print('"Обратное" ему число:', b)
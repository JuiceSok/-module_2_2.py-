while True:

    first = int(input('Введите число:'))
    second = int(input('Введите число:'))
    third = int(input('Введите число:'))
    x = first
    y = second
    z = third

    print(x, y, z, sep="\n")
    if x == y and y == z:
        print('ответ:', '3')
    elif x != y and y != z:
        print('ответ:', '0')
    elif x == y or y == z or z == x:
        print('ответ:', '2')

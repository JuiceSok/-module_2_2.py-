first = int(input('Введите число:'))
second = int(input('Введите число:'))
third = int(input('Введите число:'))
if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third:
    print('Вывод: 2')
else:
    print('Вывод: 0')

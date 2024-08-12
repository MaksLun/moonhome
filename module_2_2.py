first = int(input("Введите числo 1 из 3: "))
second = int(input("Введите числo 2 из 3: "))
third = int(input("Введите числo 3 из 3: "))
if first == second and first == third and second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
elif first != second and first != third and second != third:
    print('0')



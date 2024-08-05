#словари
my_dict = {'Maksim': 1999, 'Dima': 1998, 'Lexus': 1999}
print(my_dict)
print(my_dict['Maksim'])
my_dict['Artem'] = 1999
print(my_dict)
print(my_dict.get('Ivan'))
my_dict.update({'Masha': 1995, 'Alina':2001})
print(my_dict)
a = my_dict.pop('Masha')
print(a)
print(my_dict)
#множества
my_set = {1, 2, 2, 3, 4, 1, 2, 3, 'max', (1, 2, 3)}
print(my_set)
my_set.add(7)
my_set.add('new')
my_set.remove('max')
print(my_set)

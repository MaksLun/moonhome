immutable_var = (1, 2, 'H', 'R')#неизменяемый тип, но мы можем в кортеж добавить изменяемые элементы
print(immutable_var)
immutable_var = ([1, 2], ['H', 'R'])
immutable_var[0][0] = 200
print(immutable_var)
mutable_list = [1, 2, 'H', 'R']
mutable_list.remove(2)
print(mutable_list)
mutable_list [1] = 'p'
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
mutable_list.extend(['peach'])
print(mutable_list)


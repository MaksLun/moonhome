my_string = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_string):
    if my_string[index] > 0:
        print(my_string[index])
    elif my_string[index] == 0:
        continue
    else:
        break
    index += 1

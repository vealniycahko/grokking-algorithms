# Бинарный поиск, используя рекурсию. [O(log n)]


def binary_search(search_list, low, high, element):
    upper_bound_error_list = []
    try:
        for i in range(low, high+1):
            upper_bound_error_list.append(search_list[i])
    except IndexError:
        return print("The specified upper bound is greater than the actual upper bound of the list "
                     "or the specified lower bound is less than the actual lower bound of the list \n"
                     "----------")
    if high >= low >= 0:
        mid = low + (high - low) // 2
        if search_list[mid] == element:
            return print("The element we are looking for is at index %d \n"
                         "----------" % mid)
        elif search_list[mid] > element:
            return binary_search(search_list, low, mid - 1, element)
        else:
            return binary_search(search_list, mid + 1, high, element)
    else:
        return print("The element we are looking for is not in the list or "
                     "the specified upper bound is greater than the actual upper bound of the list "
                     "or the specified lower bound is less than the actual lower bound of the list \n"
                     "----------")
    

my_list = [0, 2, 6, 7, 7, 9]

# Создаем переменную "x", хранящую число, которое находится в списке "my_list".
x = 6
# Создаем переменную "y", хранящую число, которое не находится в списке "my_list".
y = 4

# Все параметры указаны верно.
binary_search(my_list, 0, len(my_list) - 1, x)

# Нижняя граница указана неверно.
binary_search(my_list, -1, len(my_list) - 1, x)

# Нижняя граница указана неверно.
binary_search(my_list, -7, len(my_list) - 1, x)

# Верхняя граница указана неверно.
binary_search(my_list, 0, 6, x)

# Верхняя граница указана неверно.
binary_search(my_list, 0, -1, x)

# Верхняя граница указана неверно.
binary_search(my_list, 0, -8, x)

# Указанная нижняя граница больше указанной верхней границы.
binary_search(my_list, 3, 2, x)

# Число, которое нужно найти, указано неверно.
binary_search(my_list, 0, len(my_list) - 1, y)

# Указанные границы образуют список,
# который входит в список "search_list", но является меньше списка "search_list".
binary_search(my_list, 1, 4, x)

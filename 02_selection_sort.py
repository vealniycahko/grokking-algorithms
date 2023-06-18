# Сортировка выбором. [O(n*n)]


def find_smallest(list_to_sort):
    smallest = list_to_sort[0]
    smallest_index = 0
    for i in range(1, len(list_to_sort)):
        if list_to_sort[i] < smallest:
            smallest_index = i
            smallest = list_to_sort[i]
    return smallest_index

def selection_sort(list_to_sort):
    new_list = []
    for i in range(len(list_to_sort)):
        smallest = find_smallest(list_to_sort)
        new_list.append(list_to_sort.pop(smallest))
    return new_list


print(selection_sort([5, 3, 6, 2, 10]))

# Быстрая сортировка, используя рекурсию. [O(n*log n)]


def quick_sort(list_to_sort):
    if len(list_to_sort) < 2:
        return list_to_sort
    else:
        pivot = list_to_sort[0]
        less = [i for i in list_to_sort[1:] if i <= pivot]
        greater = [i for i in list_to_sort[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([2, 0, 6, 9, 7, 7]))

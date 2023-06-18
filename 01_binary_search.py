# Бинарный поиск. [O(log n)]


def binary_search(search_list, number):
    low = 0
    high = len(search_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = search_list[mid]
        if guess == number:
            return mid
        if guess > number:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 7))
print(binary_search(my_list, 8))

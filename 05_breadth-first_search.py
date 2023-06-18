# Поиск в ширину, используя хеш-таблицы (словари) и двусторонние очереди.
# [O(V+E); V - количество вершин графа, E - количество ребер графа]


from collections import deque


def person_is_seller(char_name):
    return char_name[-1] == 'r'


char_graph = {"Shepard": ["Garrus", "Liara", "Wrex"],
              "Garrus": ["Grunt"],
              "Liara": ["Grunt", "Shadow Broker"],
              "Wrex": ["Mordin", "Tali"],
              "Shadow Broker": [],
              "Grunt": [],
              "Mordin": [],
              "Tali": []}


def search_seller(char_name):
    search_queue = deque()
    search_queue += char_graph[char_name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                return print(person + " is a mango seller!")
            else:
                search_queue += char_graph[person]
                searched.append(person)
    return print("There is no mango seller among the characters")


search_seller("Shepard")

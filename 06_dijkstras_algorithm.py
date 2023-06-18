# Алгоритм Дейкстры, используя хеш-таблицы (словари).
# [O(E*log V); V - количество вершин графа, E - количество ребер графа]
# Здесь нам нужно найти все кратчайшие пути от начального узла до всех остальных узлов
# в направленном ациклическом взвешенном графе.


graph = {"start": {"a": 6,
                   "b": 2},
         "a": {"fin": 1},
         "b": {"a": 3,
               "fin": 5},
         "fin": {}}

infinity = float("inf")

costs = {"a": 6,            
         "b": 2,            
         "fin": infinity}   

parents = {"a": "start",    
           "b": "start",    
           "fin": None}     

processed = []


def find_lowest_cost_node(table_of_costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for key_node in table_of_costs:
        value_cost = table_of_costs[key_node]
        if value_cost < lowest_cost and key_node not in processed:
            lowest_cost = value_cost
            lowest_cost_node = key_node
    return lowest_cost_node

node = find_lowest_cost_node(costs)  # "a" - "fin" - None

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for neighbor_name in neighbors.keys():
        new_cost = cost + neighbors[neighbor_name]
        if costs[neighbor_name] > new_cost:
            costs[neighbor_name] = new_cost
            parents[neighbor_name] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


print(costs)
print(parents)

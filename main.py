from makerGraph import Graph
#from makerOrGraph import Graph

# Пример использования

k = int(input("Введите количесвто первых простых минимальных пути: "))

# Пример использования
graph = Graph()
graph.add_edge('a', 'b', 1)
graph.add_edge('a', 'c', 3)
graph.add_edge('b', 'c', 1)
graph.add_edge('b', 'd', 6)
graph.add_edge('c', 'e', 2)
graph.add_edge('d', 'e', 1)

k_paths = graph.yen_k_shortest_paths('a', 'e', k)
for idx, path in enumerate(k_paths):
    print(f"Path {idx + 1}: {' -> '.join(path)}")
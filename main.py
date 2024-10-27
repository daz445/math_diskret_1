from makerGraph import Graph
#from makerOrGraph import Graph

# Пример использования

#k = int(input("Введите количесвто первых простых минимальных пути: "))

# Пример использования
graph = Graph()
graph.add_edge('a', 'c', 4)
graph.add_edge('a', 'e', 1)
graph.add_edge('a', 'h', 6)
graph.add_edge('b', 'a', 2)
graph.add_edge('c', 'a', 5)
graph.add_edge('c', 'e', 9)
graph.add_edge('c', 'h', 2)
graph.add_edge('d', 'c', 5)
graph.add_edge('d', 'g', 6)
graph.add_edge('e', 'b', 8)
graph.add_edge('e', 'c', 1)
graph.add_edge('g', 'a', 4)
graph.add_edge('g', 'e', 7)
graph.add_edge('g', 'h', 1)
graph.add_edge('h', 'b', 3)
graph.add_edge('h', 'f', 5)

k_paths = graph.yen_k_shortest_paths('a', 'f', 3)#k)
for idx, path in enumerate(k_paths):
    print(f"Path {idx + 1}: {' -> '.join(path)}")
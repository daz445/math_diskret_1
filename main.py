from makerGraph import Graph,Yen

#k = int(input("Введите количесвто первых простых минимальных пути: "))

# Пример использования
graph = Graph()

"""Вариант 1 <a,f>:
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

Вариант 2 <a,g>:
graph.add_edge('a', 'b', 2)
graph.add_edge('a', 'e', 1)
graph.add_edge('a', 'g', 9)
graph.add_edge('a', 'h', 6)
graph.add_edge('b', 'a', 2)
graph.add_edge('b', 'g', 1)
graph.add_edge('d', 'c', 5)
graph.add_edge('d', 'f', 1)
graph.add_edge('e', 'a', 1)
graph.add_edge('g', 'a', 4)
graph.add_edge('g', 'e', 3)
graph.add_edge('g', 'h', 1)
graph.add_edge('h', 'c', 2)
graph.add_edge('h', 'f', 5)
graph.add_edge('h', 'g', 1)

Вариант 3 <a,h>
graph.add_edge('a', 'c', 4)
graph.add_edge('a', 'e', 9)
graph.add_edge('a', 'g', 1)
graph.add_edge('b', 'a', 2)
graph.add_edge('b', 'e', 3)
graph.add_edge('c', 'a', 5)
graph.add_edge('c', 'e', 4)
graph.add_edge('c', 'h', 5)
graph.add_edge('d', 'c', 5)
graph.add_edge('d', 'e', 1)
graph.add_edge('d', 'h', 3)
graph.add_edge('e', 'a', 2)
graph.add_edge('e', 'c', 1)
graph.add_edge('f', 'b', 4)
graph.add_edge('g', 'a', 4)
graph.add_edge('g', 'e', 7)
graph.add_edge('g', 'h', 1)
graph.add_edge('h', 'b', 3)

Вариант 4 <a,e>
graph.add_edge('a', 'b', 2)
graph.add_edge('a', 'c', 1)
graph.add_edge('a', 'e', 1)
graph.add_edge('a', 'g', 7)
graph.add_edge('b', 'a', 1)
graph.add_edge('c', 'd', 4)
graph.add_edge('c', 'f', 4)
graph.add_edge('c', 'h', 2)
graph.add_edge('d', 'c', 5)
graph.add_edge('d', 'g', 2)
graph.add_edge('e', 'b', 8)
graph.add_edge('e', 'c', 1)
graph.add_edge('e', 'f', 3)
graph.add_edge('g', 'b', 2)
graph.add_edge('g', 'e', 1)
graph.add_edge('g', 'h', 1)
graph.add_edge('h', 'c', 2)
graph.add_edge('h', 'f', 5)
"""

#Вариант 4 как пример 
graph.add_edge('a', 'b', 2)
graph.add_edge('a', 'c', 1)
graph.add_edge('a', 'e', 1)
graph.add_edge('a', 'g', 7)
graph.add_edge('b', 'a', 1)
graph.add_edge('c', 'd', 4)
graph.add_edge('c', 'f', 4)
graph.add_edge('c', 'h', 2)
graph.add_edge('d', 'c', 5)
graph.add_edge('d', 'g', 2)
graph.add_edge('e', 'b', 8)
graph.add_edge('e', 'c', 1)
graph.add_edge('e', 'f', 3)
graph.add_edge('g', 'b', 2)
graph.add_edge('g', 'e', 1)
graph.add_edge('g', 'h', 1)
graph.add_edge('h', 'c', 2)
graph.add_edge('h', 'f', 5)

start = 'a'
end = 'e'

print("Все пути:")
all_paths = graph.find_all_paths(start, end)
all_paths.sort(key=lambda x:x[1])
for path, weight in all_paths:
    print(f"Путь: {' -> '.join(path)}, Сумма весов: {weight}")


print("Пути по алгоритму:")
yen = Yen(graph)
k_paths = yen.yen_k_shortest_paths(start, end, 3)

# Вывод результатов
for weight, path in k_paths:
    print(f"Путь: {' -> '.join(path)}, Сумма весов: {weight}")
    

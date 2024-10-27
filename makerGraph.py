import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))  # Если граф неориентированный


class Yen:
    def __init__(self, graph):
        self.graph = graph

    def dijkstra(self, start, end):
        """Использует алгоритм Дейкстры для нахождения кратчайшего пути."""
        queue = [(0, start, [])]  # (дистанция, текущая вершина, путь)
        visited = set()
        
        while queue:
            (cost, u, path) = heapq.heappop(queue)
            if u in visited:
                continue
            visited.add(u)
            path = path + [u]

            if u == end:
                return (cost, path)

            for (v, weight) in self.graph.edges[u]:
                if v not in visited:
                    heapq.heappush(queue, (cost + weight, v, path))

        return float("inf"), []  # В случае, если нет пути

    def yen_k_shortest_paths(self, start, end, k):
        """Находит K кратчайших путей от start до end."""
        # 1. Находим первый кратчайший путь
        cost, path = self.dijkstra(start, end)

        if cost == float("inf"):
            return []  # Если нет доступного пути

        k_shortest_paths = [(cost, path)]  # Начальный кратчайший путь

        # 2. Основной цикл поиска k кратчайших путей
        for i in range(1, k):
            found_new_path = False
            
            # Проверяем все предыдущие пути
            for j in range(len(k_shortest_paths[i - 1][1]) - 1):
                spur_node = k_shortest_paths[i - 1][1][j]
                removed_edges = []  # Список для восстановления рёбер

                # Убираем все рёбра, которые были в предыдущих маршрутах
                for route in k_shortest_paths:
                    if j + 1 < len(route[1]):  # Проверка длины
                        u = route[1][j]
                        v = route[1][j + 1]
                        # Удаляем ребро u -> v
                        self.graph.edges[u] = [(n, w) for n, w in self.graph.edges[u] if n != v]
                        removed_edges.append((u, v))

                # Находим путь от spur_node до end
                spur_cost, spur_path = self.dijkstra(spur_node, end)

                if spur_cost != float("inf"):
                    total_path = k_shortest_paths[i - 1][1][:j + 1] + spur_path
                    
                    # Проверка на уникальность узлов
                    if len(set(total_path)) == len(total_path):  # Убедимся, что все узлы уникальны
                        total_cost = k_shortest_paths[i - 1][0] + spur_cost

                        # Проверка на уникальность пути и добавление в список
                        if (total_cost, total_path) not in k_shortest_paths:
                            k_shortest_paths.append((total_cost, total_path))
                            found_new_path = True  # Новый путь найден

                # Восстанавливаем граф
                for (u, v) in removed_edges:
                    self.graph.add_edge(u, v, self.get_weight(u, v))  # Восстановление ребра

            # Если не нашли новых путей, выходим из цикла
            if not found_new_path:
                break

            # Сортировка и ограничение списка до k
            k_shortest_paths = sorted(k_shortest_paths, key=lambda x: x[0])[:k]

        return k_shortest_paths

    def get_weight(self, u, v):
        """Возвращает вес ребра между узлами u и v."""
        for neighbor, weight in self.graph.edges[u]:
            if neighbor == v:
                return weight
        return float("inf")




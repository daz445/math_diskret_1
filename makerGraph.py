import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))  # Если граф неориентированный

    def dijkstra(self, start, end):
        queue = []
        heapq.heappush(queue, (0, start))
        distances = {start: 0}
        previous_nodes = {start: None}

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == end:
                break

            for neighbor, weight in self.edges[current_node]:
                distance = current_distance + weight

                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

        # Проверяем, найден ли путь
        if end not in previous_nodes:
            return [], float('inf')  # Возвращаем пустой путь и бесконечную дистанцию

        path = []
        while end is not None:
            path.append(end)
            end = previous_nodes[end]
        path.reverse()
        return path, distances.get(path[-1], float('inf'))


    def yen_k_shortest_paths(self, start, end, k):
        # Находим первый кратчайший путь
        first_path, _ = self.dijkstra(start, end)
        paths = [first_path]
        potential_paths = []

        for k_index in range(1, k):
            for i in range(len(paths[k_index - 1]) - 1):
                spur_node = paths[k_index - 1][i]
                root_path = paths[k_index - 1][:i + 1]

                # Удаляем все ребра, которые были использованы в предыдущих путях
                removed_edges = []
                for p in paths:
                    if p[:i + 1] == root_path:
                        u = p[i]
                        v = p[i + 1]
                        self.edges[u].remove((v, self.get_weight(u, v)))
                        removed_edges.append((u, v))

                spur_path, spur_distance = self.dijkstra(spur_node, end)
                if spur_distance == float('inf'):
                    continue  # Пропускаем итерацию, если путь не найден
                if spur_distance < float('inf'):
                    total_path = root_path + spur_path[1:]
                    total_distance = sum(self.get_weight(total_path[j], total_path[j + 1]) for j in range(len(total_path) - 1))
                    potential_paths.append((total_path, total_distance))

                # Восстанавливаем удаленные ребра
                for u, v in removed_edges:
                    self.edges[u].append((v, self.get_weight(u, v)))

            # Сортируем потенциальные пути по длине
            potential_paths.sort(key=lambda x: x[1])
            if not potential_paths:
                break

            # Добавляем самый короткий путь в список
            paths.append(potential_paths[0][0])
            potential_paths.pop(0)

        return paths

    def get_weight(self, u, v):
        for neighbor, weight in self.edges[u]:
            if neighbor == v:
                return weight
        return float('inf')




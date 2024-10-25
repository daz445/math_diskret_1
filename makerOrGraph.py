import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

    def dijkstra(self, start, end):
        queue = []
        heapq.heappush(queue, (0, start))
        distances = {start: 0}
        previous_nodes = {start: None}

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == end:
                break

            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_distance + weight

                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

        # Проверяем, найден ли путь
        if end not in previous_nodes:
            return [], float('inf')

        path = []
        while end is not None:
            path.append(end)
            end = previous_nodes[end]
        path.reverse()
        return path, distances.get(path[-1], float('inf'))

    def yen_k_shortest_paths(self, start, end, k):
        # Находим первый кратчайший путь
        first_path, _ = self.dijkstra(start, end)
        if not first_path:
            return []

        paths = [first_path]
        path_costs = []

        for i in range(1, k):
            potential_paths = []

            for j in range(len(paths[i - 1]) - 1):
                spur_node = paths[i - 1][j]
                root_path = paths[i - 1][:j + 1]

                # Удаляем ребра из графа
                removed_edges = []
                for path in paths:
                    if len(path) > j and root_path == path[:j + 1]:
                        next_node = path[j + 1]
                        if next_node in self.edges[spur_node]:
                            self.edges[spur_node] = [(node, weight) for node, weight in self.edges[spur_node] if node != next_node]
                            removed_edges.append((spur_node, next_node))

                # Находим спурный путь
                spur_path, spur_cost = self.dijkstra(spur_node, end)
                if spur_path:
                    total_path = root_path + spur_path[1:]
                    total_cost = sum(weight for _, weight in zip(total_path[:-1], [self.get_edge_weight(total_path[i], total_path[i + 1]) for i in range(len(total_path) - 1)]))
                    potential_paths.append((total_path, total_cost))

                # Восстанавливаем удаленные рёбра
                for from_node, to_node in removed_edges:
                    self.add_edge(from_node, to_node, self.get_edge_weight(from_node, to_node))

            # Если есть потенциальные пути, выбираем минимальный
            if potential_paths:
                potential_paths.sort(key=lambda x: x[1])
                paths.append(potential_paths[0][0])
                path_costs.append(potential_paths[0][1])
            else:
                break

        return paths

    def get_edge_weight(self, from_node, to_node):
        for neighbor, weight in self.edges.get(from_node, []):
            if neighbor == to_node:
                return weight
        return float('inf')



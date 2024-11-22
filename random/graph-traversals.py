from collections import deque


class Graph:
    def __init__(self) -> None:
        adj_list_no_cycle = {
            "a": ["b", "c"],
            "b": ["d"],
            "c": ["e"],
            "d": ["f"],
            "e": [],
            "f": [],
        }

        self.dfs_traversal_with_stack(adj_list_no_cycle, "a")
        self.dfs_traversal_recursive(adj_list_no_cycle, "a")
        self.bfs_traversal_with_queue(adj_list_no_cycle, "a")
        self.bfs_traversal_recursive(adj_list_no_cycle, "a")

        adj_list_has_cycle = {
            "i": ["j", "k"],
            "j": ["k", "i"],
            "k": ["i", "j", "l", "m"],
            "m": [],
            "l": ["k"],
        }

        print()
        print("#" * 10)
        self.dfs_traversal_with_stack(adj_list_has_cycle, "i")
        self.dfs_traversal_recursive(adj_list_has_cycle, "i")
        self.bfs_traversal_with_queue(adj_list_has_cycle, "i")
        self.bfs_traversal_recursive(adj_list_has_cycle, "i")

    def dfs_traversal_with_stack(self, graph: dict, source: str) -> None:
        stack = [source]

        visited = set()
        visited.add(source)
        print(source, end=" ")

        while len(stack) > 0:
            curr_node = stack.pop()

            for neigh in graph[curr_node]:
                if neigh not in visited:
                    print(neigh, end=" ")
                    visited.add(neigh)
                    stack.append(neigh)

        print()

    def dfs_traversal_recursive(self, graph: dict, source: str) -> None:
        visited = set()

        def dfs(node: str) -> None:
            for neigh in graph[node]:
                if neigh not in visited:
                    print(neigh, end=" ")
                    visited.add(neigh)
                    dfs(neigh)

        dfs(source)

    def bfs_traversal_with_queue(self, graph: dict, source: str) -> None:
        print()

        queue = deque([source])

        visited = set()
        visited.add(source)
        print(source, end=" ")

        while len(queue) > 0:
            curr_node = queue.pop()

            for neigh in graph[curr_node]:
                if neigh not in visited:
                    print(neigh, end=" ")
                    visited.add(neigh)
                    queue.appendleft(neigh)

        print()

    def bfs_traversal_recursive(self, graph: dict, source: str) -> None:
        visited = set()

        def bfs(nodes: list[str]) -> None:
            if not nodes:
                return

            next_level_nodes = []
            for neigh in nodes:
                for next_level_node in graph[neigh]:
                    if next_level_node not in visited:
                        print(next_level_node, end=" ")
                        visited.add(next_level_node)
                        next_level_nodes.append(next_level_node)

            bfs(next_level_nodes)

        bfs([source])


graph = Graph()

"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.



Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1


Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""

# Time Complexity:  O(V*E) -> for dfs, O(E*logV) -> for dijkstra
# Space Complexity: O(V+E) -> for dfs, O(V + E) -> for dijkstra
import collections
import heapq


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2

        result = self.network_delay_time_dfs(times, n, k)
        assert result == 2, err_msg_invalid_result
        print(result)

        result = self.network_delay_time_dijkstra(times, n, k)
        assert result == 2, err_msg_invalid_result
        print(result)

        times = [[1, 2, 1]]
        n = 2
        k = 1

        result = self.network_delay_time_dfs(times, n, k)
        assert result == 1, err_msg_invalid_result
        print(result)

        result = self.network_delay_time_dijkstra(times, n, k)
        assert result == 1, err_msg_invalid_result
        print(result)

        times = [[1, 2, 1]]
        n = 2
        k = 2

        result = self.network_delay_time_dfs(times, n, k)
        assert result == -1, err_msg_invalid_result
        print(result)

        result = self.network_delay_time_dijkstra(times, n, k)
        assert result == -1, err_msg_invalid_result
        print(result)

    # Time limit exceeds for larger inputs
    def network_delay_time_dfs(self, times: list[list[int]], n: int, k: int) -> int:
        if not times or not times[0] or n == 0 or k < 1:
            return -1

        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist_map = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node: int, time: int) -> None:
            if time >= dist_map[node]:
                return

            dist_map[node] = time

            for neigh, dist in graph[node]:
                dfs(neigh, dist + time)

        dfs(k, 0)
        result = max(dist_map.values())

        return int(result) if result < float("inf") else -1

    # Dijkstra -> BFS + Min Heap
    def network_delay_time_dijkstra(
        self, times: list[list[int]], n: int, k: int
    ) -> int:
        if not times or not times[0] or n == 0 or k < 1:
            return -1

        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = [(0, k)]
        visited = set()
        min_time = 0

        while min_heap:
            curr_weight, curr_node = heapq.heappop(min_heap)

            if curr_node in visited:
                continue

            visited.add(curr_node)
            min_time = max(min_time, curr_weight)

            for node, weight in graph[curr_node]:
                heapq.heappush(min_heap, (weight + curr_weight, node))

        return min_time if len(visited) == n else -1


# Create an instance of the class
solution = Solution()

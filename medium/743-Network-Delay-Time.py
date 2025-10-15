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

# Time Complexity:  O(E*logV)
# Space Complexity: O(V+E)
import collections
import heapq


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n = 4
        k = 2

        result = self.network_delay_time_dijkstra(times, n, k)
        assert result == 2, err_msg_invalid_result
        print(result)

        times = [[1, 2, 1]]
        n = 2
        k = 1

        result = self.network_delay_time_dijkstra(times, n, k)
        assert result == 1, err_msg_invalid_result
        print(result)

        times = [[1, 2, 1]]
        n = 2
        k = 2

        result = self.network_delay_time_dijkstra(times, n, k)
        assert result == -1, err_msg_invalid_result

    # Dijkstra -> BFS + Min Heap
    def network_delay_time_dijkstra(
        self, times: list[list[int]], n: int, k: int
    ) -> int:
        if not times or not times[0] or k < 1 or n < k:
            return -1

        adj_list = collections.defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))

        visited_set = set()
        min_heap = [(0, k)]
        min_time = 0

        while min_heap:
            curr_weight, curr_node = heapq.heappop(min_heap)

            if curr_node in visited_set:
                continue

            visited_set.add(curr_node)
            min_time = max(min_time, curr_weight)

            for next_node, next_weight in adj_list[curr_node]:
                heapq.heappush(min_heap, (curr_weight + next_weight, next_node))

        return min_time if len(visited_set) == n else -1


# Create an instance of the class
solution = Solution()

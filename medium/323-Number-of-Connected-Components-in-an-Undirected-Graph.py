"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.



Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1


Constraints:
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""

# Time Complexity:  O(N)
# Space Complexity: O(N)

import collections


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        n, edges = 5, [[0, 1], [1, 2], [3, 4]]

        result = self.count_components(n, edges)
        assert result == 2, err_msg_invalid_result
        print(result)

        n, edges = 5, [[0, 1], [1, 2], [2, 3], [3, 4]]

        result = self.count_components(n, edges)
        assert result == 1, err_msg_invalid_result
        print(result)

    def count_components(self, n: int, edges: list[list[int]]) -> int:
        if n == 0:
            return 0

        adj_list = collections.defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        result = 0
        visited_set = set()

        def helper(node: int) -> None:
            if node in visited_set:
                return

            visited_set.add(node)

            for neigh in adj_list[node]:
                helper(neigh)

            return

        for node in range(n):
            if node not in visited_set:
                result += 1
                helper(node)

        return result


# Create an instance of the class
solution = Solution()

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


# Time Complexity:  O(V+E)
# Space Complexity: O(V+E)

import collections
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        n, edges = 5, [[0,1],[1,2],[3,4]]

        result = self.count_components(n, edges)
        assert result == 2, err_msg_invalid_result
        print(result)

        n, edges = 5, [[0,1],[1,2],[2,3],[3,4]]

        result = self.count_components(n, edges)
        assert result == 1, err_msg_invalid_result
        print(result)


    def count_components(self, n: int, edges: list[list[int]]) -> int:
        graph_map = collections.defaultdict(list)

        for node, edge in edges:
            graph_map[node].append(edge)
            graph_map[edge].append(node)

        result = 0
        visited_set = set()

        def dfs(node: int) -> None:
            visited_set.add(node)

            for neighbor in graph_map[node]:
                if neighbor not in visited_set:
                    dfs(neighbor)


        for node in range(n):
            if node not in visited_set:
                dfs(node)
                result += 1

        return result


# Create an instance of the class
solution = Solution()
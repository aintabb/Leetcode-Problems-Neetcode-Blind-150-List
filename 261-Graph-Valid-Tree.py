"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.



Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false


Constraints:
1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no self-loops or repeated edges.
"""


# Time Complexity:  O(N)
# Space Complexity: O(N)

import collections
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        n, edges = 5, [[0,1],[0,2],[0,3],[1,4]]

        result = self.valid_tree(n, edges)
        assert result == True, err_msg_invalid_result
        print(result)

        n, edges = 5, [[0,1],[1,2],[2,3],[1,3],[1,4]]

        result = self.valid_tree(n, edges)
        assert result == False, err_msg_invalid_result
        print(result)


    """
        in a tree there should be n - 1 edges
        there should not be loops,
        all nodes should be reachable
    """
    def valid_tree(self, n: int, edges: list[list[int]]) -> bool:
        if (len(edges) != n - 1):
            return False

        graph_map = collections.defaultdict(list)
        for node, edge in edges:
            graph_map[node].append(edge)
            graph_map[edge].append(node)

        visited_set = set()

        def dfs(node: int) -> None:
            visited_set.add(node)

            for neighbor in graph_map[node]:
                if neighbor not in visited_set:
                    dfs(neighbor)

        dfs(0)
        return len(visited_set) == n


# Create an instance of the class
solution = Solution()
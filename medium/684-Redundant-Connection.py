"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.



Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]


Constraints:
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""


# Time Complexity:  O(N)
# Space Complexity: O(N)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        edges = [[1, 2], [1, 3], [2, 3]]

        result = self.find_redundant_connection(edges)
        assert result == [2, 3], err_msg_invalid_result
        print(result)

        edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]

        result = self.find_redundant_connection(edges)
        assert result == [1, 4], err_msg_invalid_result
        print(result)

        edges = [
            [7, 8],
            [2, 6],
            [2, 8],
            [1, 4],
            [9, 10],
            [1, 7],
            [3, 9],
            [6, 9],
            [3, 5],
            [3, 10],
        ]

        result = self.find_redundant_connection(edges)
        assert result == [3, 10], err_msg_invalid_result
        print(result)

    def find_redundant_connection(self, edges: list[list[int]]) -> list[int]:
        if not edges or not edges[0]:
            return []

        len_edges = len(edges)
        parents = list(range(len_edges + 1))
        ranks = [1] * (len_edges + 1)

        def find_parent(node: int) -> int:
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]

            return node

        def union(node_one: int, node_two: int) -> bool:
            p_one = find_parent(node_one)
            p_two = find_parent(node_two)

            if p_one == p_two:
                return False

            if ranks[p_one] > ranks[p_two]:
                ranks[p_one] += ranks[p_two]
                parents[p_two] = p_one
            else:
                ranks[p_two] += ranks[p_one]
                parents[p_one] = p_two

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []


# Create an instance of the class
solution = Solution()

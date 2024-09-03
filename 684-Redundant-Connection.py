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

        edges = [[1,2],[1,3],[2,3]]

        result = self.find_redundant_connection(edges)
        assert result == [2,3], err_msg_invalid_result
        print(result)

        edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]

        result = self.find_redundant_connection(edges)
        assert result == [1,4], err_msg_invalid_result
        print(result)


    def find_redundant_connection(self, edges: list[list[int]]) -> list[int]:
        if not edges:
            return []

        # Union-Find
        len_edges = len(edges)
        parents = [i for i in range(len_edges + 1)]
        ranks = [1] * (len_edges + 1)

        def find(node: int) -> int:
            curr_parent = parents[node]

            while (curr_parent != parents[curr_parent]):
                parents[curr_parent] = parents[parents[curr_parent]]
                curr_parent = parents[curr_parent]

            return curr_parent

        def union(node_one: int, node_two: int) -> bool:
            parent_one, parent_two = find(node_one), find(node_two)

            if (parent_one == parent_two):
                return False

            if (ranks[parent_one] > ranks[parent_two]):
                ranks[parent_one] += ranks[parent_two]
                parents[parent_two] = parent_one
            else:
                ranks[parent_two] += ranks[parent_one]
                parents[parent_one] = parent_two

            return True

        for node, edge in edges:
            if not union(node, edge):
                return [node, edge]

        return []


# Create an instance of the class
solution = Solution()
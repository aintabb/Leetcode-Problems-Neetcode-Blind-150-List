"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.



Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Explanation:
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18


Constraints:
1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
"""


# Time Complexity:  O(n**2*log(n))
# Space Complexity: O(n**2)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]

        result = self.min_cost_connect_points(points)
        assert result == 20, err_msg_invalid_result
        print(result)

        points = [[3, 12], [-2, 5], [-4, 1]]

        result = self.min_cost_connect_points(points)
        assert result == 18, err_msg_invalid_result
        print(result)

    def min_cost_connect_points(self, points: list[list[int]]) -> int:
        if not points or not points[0]:
            return 0

        # Union-Find part
        len_points = len(points)
        parents = [i for i in range(len_points + 1)]
        ranks = [1] * (len_points + 1)

        def find(node: int) -> int:
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]

            return node

        def union(node_one: int, node_two: int) -> bool:
            parent_one, parent_two = find(node_one), find(node_two)
            if parent_one == parent_two:
                return False

            if ranks[parent_one] > ranks[parent_two]:
                ranks[parent_one] += ranks[parent_two]
                parents[parent_two] = parent_one
            else:
                ranks[parent_two] += ranks[parent_one]
                parents[parent_one] = parent_two

            return True

        edges = []
        for i in range(len_points):
            xi_one, yi_one = points[i]
            for j in range(i + 1, len_points):
                xi_two, yi_two = points[j]
                dist = abs(xi_one - xi_two) + abs(yi_one - yi_two)
                edges.append([dist, i, j])

        edges.sort()

        min_cost = 0
        for dist, u, v in edges:
            if union(u, v):
                min_cost += dist

        return min_cost


# Create an instance of the class
solution = Solution()

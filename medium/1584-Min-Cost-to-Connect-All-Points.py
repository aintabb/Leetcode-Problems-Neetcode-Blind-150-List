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

# Time Complexity:  O(N^2*logN) -> same for both
# Space Complexity: O(N^2) -> same for both
import heapq


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]

        result = self.min_cost_connect_points_kruskals_algo(points)
        assert result == 20, err_msg_invalid_result
        print(result)

        result = self.min_cost_connect_points_prims_algo(points)
        assert result == 20, err_msg_invalid_result
        print(result)

        points = [[3, 12], [-2, 5], [-4, 1]]

        result = self.min_cost_connect_points_kruskals_algo(points)
        assert result == 18, err_msg_invalid_result
        print(result)

        result = self.min_cost_connect_points_prims_algo(points)
        assert result == 18, err_msg_invalid_result
        print(result)

    def min_cost_connect_points_kruskals_algo(self, points: list[list[int]]) -> int:
        if not points or not points[0]:
            return 0

        len_points = len(points)
        parents = list(range(len_points + 1))
        ranks = [1] * (len_points + 1)

        def find(node: int) -> int:
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]

            return node

        def union(node_one: int, node_two: int) -> bool:
            parent_one = find(node_one)
            parent_two = find(node_two)

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
            x1, y1 = points[i]
            for j in range(i + 1, len_points):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append([dist, i, j])

        edges.sort()

        result = 0
        for dist, i, j in edges:
            if union(i, j):
                result += dist

        return result

    def min_cost_connect_points_prims_algo(self, points: list[list[int]]) -> int:
        if not points or not points[0]:
            return 0

        len_points = len(points)
        adj_list = {idx: [] for idx in range(len_points)}  # i : list of [cost, node]

        for i in range(len_points):
            x1, y1 = points[i]
            for j in range(i + 1, len_points):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj_list[i].append([dist, j])
                adj_list[j].append([dist, i])

        # Prim's algo
        result = 0
        visited_set = set()
        min_heap = [[0, 0]]  # [cost, point]

        while len(visited_set) < len_points:
            curr_cost, curr_node = heapq.heappop(min_heap)

            if curr_node in visited_set:
                continue

            visited_set.add(curr_node)
            result += curr_cost

            for neigh_cost, neigh in adj_list[curr_node]:
                if neigh not in visited_set:
                    heapq.heappush(min_heap, [neigh_cost, neigh])

        return result


# Create an instance of the class
solution = Solution()

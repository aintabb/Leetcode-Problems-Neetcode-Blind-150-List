"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).



Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.


Constraints:
1 <= k <= points.length <= 104
-104 <= xi, yi <= 104
"""

# Time Complexity:  O(N*log(N))
# Space Complexity: O(N)
from math import sqrt
import heapq


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        points, k = [[1, 3], [-2, 2]], 1

        result = self.k_closest(points, k)
        assert result == [[-2, 2]], err_msg_invalid_result
        print(result)

        points, k = [[3, 3], [5, -1], [-2, 4]], 2

        result = self.k_closest(points, k)
        assert result == [[3, 3], [-2, 4]], err_msg_invalid_result
        print(result)

    def k_closest(self, points: list[list[int]], k: int) -> list[list[int]]:
        if not points or k == 0:
            return []

        min_heap = []
        for x, y in points:
            dist_to_orgn = sqrt(x**2 + y**2)
            heapq.heappush(min_heap, (dist_to_orgn, x, y))

        result = []
        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            result.append([x, y])

        return result


# Create an instance of the class
solution = Solution()

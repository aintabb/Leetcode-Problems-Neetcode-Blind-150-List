"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

It starts raining, and water gradually rises over time. At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.

You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).



Example 1:
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.


Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n2
Each value grid[i][j] is unique.
"""

# Time Complexity:  O(N^2*logN)
# Space Complexity: O(N^2)
import heapq


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        grid = [[0, 2], [1, 3]]

        result = self.swim_in_water_dijkstra(grid)
        assert result == 3, err_msg_invalid_result
        print(result)

        grid = [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]

        result = self.swim_in_water_dijkstra(grid)
        assert result == 16, err_msg_invalid_result
        print(result)

    def swim_in_water_dijkstra(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        min_heap = [(grid[0][0], 0, 0)]
        visited_set = set()
        len_grid = len(grid)

        visited_set.add((0, 0))

        while min_heap:
            curr_time, curr_row, curr_col = heapq.heappop(min_heap)

            if curr_row == len_grid - 1 and curr_col == len_grid - 1:
                return curr_time

            for dx, dy in dirs:
                new_row = curr_row + dx
                new_col = curr_col + dy

                if not (
                    0 <= new_row < len_grid
                    and 0 <= new_col < len_grid
                    and (new_row, new_col) not in visited_set
                ):
                    continue

                visited_set.add((new_row, new_col))
                # Increase or maintain the time when moving to a cell with a higher elevation
                heapq.heappush(
                    min_heap, (max(curr_time, grid[new_row][new_col]), new_row, new_col)
                )

        return -1


# Create an instance of the class
solution = Solution()

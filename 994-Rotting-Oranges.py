"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""


# Time Complexity:  O(m*n)
# Space Complexity: O(m*n)
from collections import deque
from re import L

class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        grid = [[2,1,1],[1,1,0],[0,1,1]]

        result = self.oranges_rotting(grid)
        assert result == 4, err_msg_invalid_result
        print(result)

        grid = [[2,1,1],[0,1,1],[1,0,1]]

        result = self.oranges_rotting(grid)
        assert result == -1, err_msg_invalid_result
        print(result)

        grid = [[0,2]]

        result = self.oranges_rotting(grid)
        assert result == 0, err_msg_invalid_result
        print(result)


    def oranges_rotting(self, grid: list[list[int]]) -> int:
        FRESH, ROTTEN = 1, 2
        rows, cols = len(grid), len(grid[0])
        fresh_count, time = 0, 0

        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if (grid[row][col] == ROTTEN):
                    queue.append((row, col))

                if (grid[row][col] == FRESH):
                    fresh_count += 1

        if (fresh_count == 0):
            return time

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue and fresh_count > 0:
            q_len = len(queue)

            for _ in range(q_len):
                row, col = queue.pop()

                for r_offset, c_offset in dirs:
                    new_r, new_c = row + r_offset, col + c_offset

                    if (
                        0 <= new_r < rows and
                        0 <= new_c < cols and
                        grid[new_r][new_c] == FRESH
                    ):
                        grid[new_r][new_c] = ROTTEN
                        queue.append((new_r, new_c))
                        fresh_count -= 1

            time += 1

        return time if fresh_count == 0 else -1


# Create an instance of the class
solution = Solution()
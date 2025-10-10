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
import collections


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

        result = self.oranges_rotting(grid)
        assert result == 4, err_msg_invalid_result
        print(result)

        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]

        result = self.oranges_rotting(grid)
        assert result == -1, err_msg_invalid_result
        print(result)

        grid = [[0, 2]]

        result = self.oranges_rotting(grid)
        assert result == 0, err_msg_invalid_result
        print(result)

    def oranges_rotting(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        FRESH, ROTTEN = 1, 2
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        fresh_count = 0

        cell_q = collections.deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == ROTTEN:
                    cell_q.appendleft([row, col, 0])
                elif grid[row][col] == FRESH:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        min_minutes_spent = 0
        while cell_q and fresh_count > 0:
            row, col, minutes_spent = cell_q.pop()

            for dx, dy in dirs:
                new_row = row + dx
                new_col = col + dy

                if (
                    0 <= new_row < ROWS
                    and 0 <= new_col < COLS
                    and grid[new_row][new_col] == FRESH
                ):
                    grid[new_row][new_col] = ROTTEN
                    fresh_count -= 1
                    min_minutes_spent = minutes_spent + 1

                    cell_q.appendleft([new_row, new_col, minutes_spent + 1])

        return min_minutes_spent if fresh_count == 0 else -1


# Create an instance of the class
solution = Solution()

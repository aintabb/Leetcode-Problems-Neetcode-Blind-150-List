"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""


# Time Complexity:  O(m*n)
# Space Complexity: O(m*n)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]

        result = self.max_area_of_island_with_set(grid)
        assert result == 6, err_msg_invalid_result
        print(result)

        result = self.max_area_of_island_without_set(grid)
        assert result == 6, err_msg_invalid_result
        print(result)

        grid = [[0, 0, 0, 0, 0, 0, 0, 0]]

        result = self.max_area_of_island_with_set(grid)
        assert result == 0, err_msg_invalid_result
        print(result)

        result = self.max_area_of_island_without_set(grid)
        assert result == 0, err_msg_invalid_result
        print(result)

    def max_area_of_island_without_set(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def traverse(row: int, col: int) -> int:
            if not (0 <= row < rows and 0 <= col < cols and grid[row][col] == 1):
                return 0

            grid[row][col] = 0

            max_area = 1

            for r_offset, c_offset in (0, 1), (1, 0), (0, -1), (-1, 0):
                next_r, next_c = row + r_offset, col + c_offset
                max_area += traverse(next_r, next_c)

            return max_area

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, traverse(row, col))

        return max_area

    def max_area_of_island_with_set(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited_set = set()

        def helper(row: int, col: int) -> int:
            if not (
                0 <= row < ROWS
                and 0 <= col < COLS
                and grid[row][col] == 1
                and (row, col) not in visited_set
            ):
                return 0

            visited_set.add((row, col))

            max_area = 1
            for dx, dy in dirs:
                new_row = row + dx
                new_col = col + dy
                max_area += helper(new_row, new_col)

            return max_area

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    max_area = max(max_area, helper(row, col))

        return max_area


# Create an instance of the class
solution = Solution()

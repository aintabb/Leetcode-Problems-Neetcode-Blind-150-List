"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.



Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

Example 2:
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.


Constraints:
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""


# Time Complexity:  O(m*n)
# Space Complexity: O(m*n)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]

        result = self.pacific_atlantic(heights)
        assert result == [
            [0, 4],
            [1, 3],
            [1, 4],
            [2, 2],
            [3, 0],
            [3, 1],
            [4, 0],
        ], err_msg_invalid_result
        print(result)

        heights = [[1]]

        result = self.pacific_atlantic(heights)
        assert result == [[0, 0]], err_msg_invalid_result
        print(result)

    # top, left -> pacific
    # bottom, right -> atlantic
    def pacific_atlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return [[]]

        ROWS, COLS = len(heights), len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        pacific_set = set()
        atlantic_set = set()
        result = []

        def helper(row: int, col: int, flow_set: set, prev_height: int) -> None:
            if not (
                0 <= row < ROWS
                and 0 <= col < COLS
                and (row, col) not in flow_set
                and prev_height <= heights[row][col]
            ):
                return

            flow_set.add((row, col))
            prev_height = heights[row][col]

            for dx, dy in dirs:
                new_row = row + dx
                new_col = col + dy

                helper(new_row, new_col, flow_set, prev_height)

        for row in range(ROWS):
            helper(row, 0, pacific_set, heights[row][0])
            helper(row, COLS - 1, atlantic_set, heights[row][COLS - 1])

        for col in range(COLS):
            helper(0, col, pacific_set, heights[0][col])
            helper(ROWS - 1, col, atlantic_set, heights[ROWS - 1][col])

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific_set and (row, col) in atlantic_set:
                    result.append([row, col])

        return result


# Create an instance of the class
solution = Solution()

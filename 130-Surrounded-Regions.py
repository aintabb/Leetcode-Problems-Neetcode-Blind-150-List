"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.



Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:
Input: board = [["X"]]
Output: [["X"]]



Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""


# Time Complexity:  O(m*n)
# Space Complexity: O(m*n)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]

        self.solve(board)
        assert board == [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ], err_msg_invalid_result
        print(board)

        board = [["X"]]

        self.solve(board)
        assert board == [["X"]], err_msg_invalid_result
        print(board)

        board = [["O"]]

        self.solve(board)
        assert board == [["O"]], err_msg_invalid_result
        print(board)

    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row: int, col: int) -> None:
            if (
                row < 0
                or row == rows
                or col < 0
                or col == cols
                or board[row][col] != "O"
            ):
                return

            board[row][col] = "T"

            for dy, dx in dirs:
                new_row, new_col = row + dy, col + dx
                dfs(new_row, new_col)

        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)

        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"


# Create an instance of the class
solution = Solution()

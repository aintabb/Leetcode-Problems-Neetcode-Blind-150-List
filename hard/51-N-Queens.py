"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.



Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]


Constraints:
1 <= n <= 9
"""


# Time Complexity:  O(N!)
# Space Complexity: O(N^2)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        n = 4

        result = self.solve_N_queens(n)
        assert result == [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."],
        ], err_msg_invalid_result
        print(result)

        n = 1

        result = self.solve_N_queens(n)
        assert result == [["Q"]], err_msg_invalid_result
        print(result)

    def solve_N_queens(self, n: int) -> list[list[str]]:
        if not n:
            return [[]]

        col_set = set()
        pos_diag_set = set()
        neg_diag_set = set()
        result = []

        board = [["."] * n for _ in range(n)]

        def backtrack(row: int) -> None:
            if row == n:
                copy_board = ["".join(row) for row in board]
                result.append(copy_board)
                return

            for col in range(n):
                pos_diag_val = row + col
                neg_diag_val = row - col

                if (
                    col in col_set
                    or pos_diag_val in pos_diag_set
                    or neg_diag_val in neg_diag_set
                ):
                    continue

                col_set.add(col)
                pos_diag_set.add(pos_diag_val)
                neg_diag_set.add(neg_diag_val)
                board[row][col] = "Q"

                backtrack(row + 1)

                col_set.discard(col)
                pos_diag_set.discard(pos_diag_val)
                neg_diag_set.discard(neg_diag_val)
                board[row][col] = "."

        backtrack(0)
        return result


# Create an instance of the class
solution = Solution()

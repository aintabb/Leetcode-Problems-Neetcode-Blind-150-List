'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:

Input: board =
     00  01  02
00 [["5","3",".",".","7",".",".",".","."]
10,["6",".",".","1","9","5",".",".","."]
20,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

'''

# Time Complexity: O(9^2) -->> O(N)
# Space Complexity: O(9) -->> O(N)
import collections

class ValidSudoku:
  def __init__(self) -> None:
        err_msg_invalid_valid_sudoku = "Provided sudoku is not valid. Something is wrong!"
        board = [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]

        result = self.is_valid_sudoku(board)
        assert result == True, err_msg_invalid_valid_sudoku
        print(result)

        board = [["8","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]

        result = self.is_valid_sudoku(board)
        assert result == False, err_msg_invalid_valid_sudoku
        print(result)


  def is_valid_sudoku(self, board: list[list[str]]) -> bool:
    rows  = collections.defaultdict(set)
    cols  = collections.defaultdict(set)
    grids = collections.defaultdict(set)

    for row in range(9):
      for col in range(9):
        if (board[row][col] == "."):
          continue

        if (board[row][col] in rows[row] or
            board[row][col] in cols[col] or
            board[row][col] in grids[(row // 3, col // 3)]):
            return False

        rows[row].add(board[row][col])
        cols[col].add(board[row][col])
        grids[(row // 3, col // 3)].add(board[row][col])

    return True

valid_sudoku = ValidSudoku()
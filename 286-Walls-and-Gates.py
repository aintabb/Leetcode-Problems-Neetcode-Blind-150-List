"""
You are given an m x n grid rooms initialized with these three possible values.

- -1 A wall or an obstacle.
- 0 A gate.
- INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.



Example 1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Example 2:
Input: rooms = [[-1]]
Output: [[-1]]


Constraints:
m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 2**31 - 1.
"""


# Time Complexity:  O(m*n)
# Space Complexity: O(m*n)
from collections import deque

class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        rooms = [
            [2147483647,-1,0,2147483647],
            [2147483647,2147483647,2147483647,-1],
            [2147483647,-1,2147483647,-1],
            [0,-1,2147483647,2147483647]
        ]

        self.walls_and_gates(rooms)
        assert rooms == [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]], err_msg_invalid_result
        print(rooms)

        rooms = [[-1]]

        self.walls_and_gates(rooms)
        assert rooms == [[-1]], err_msg_invalid_result
        print(rooms)


    # 0 -> gate, -1 -> A wall or an obstacle, INF -> empty room
    def walls_and_gates(self, rooms: list[list[int]]) -> None:
        GATE, EMPTY = 0, 2**31 - 1
        rows, cols = len(rooms), len(rooms[0])

        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if (rooms[row][col] == GATE):
                    queue.append((row, col, 0))

        while queue:
            row, col, dist = queue.popleft()

            for r_offset, c_offset in [(0,1), (1,0), (0,-1), (-1, 0)]:
                new_r, new_c = row + r_offset, col + c_offset

                if (
                    0 <= new_r < rows and
                    0 <= new_c < cols and
                    rooms[new_r][new_c] == EMPTY
                ):
                    rooms[new_r][new_c] = dist + 1
                    queue.append((new_r, new_c, dist + 1))


# Create an instance of the class
solution = Solution()
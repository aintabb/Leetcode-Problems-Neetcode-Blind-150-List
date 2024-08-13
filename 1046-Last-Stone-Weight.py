"""
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.



Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1


Constraints:
1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""


# Time Complexity:  O(n*log(n))
# Space Complexity: O(n)
import heapq

class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        stones = [2, 7, 4, 1, 8, 1]

        result = self.last_stone_weight(stones)
        assert result == 1, err_msg_invalid_result
        print(result)

        stones = [1]

        result = self.last_stone_weight(stones)
        assert result == 1, err_msg_invalid_result
        print(result)


    def last_stone_weight(self, stones: list[int]) -> int:
        if (len(stones) == 1):
            return stones[0]

        # Construct a max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while (len(stones) != 1):
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if (x >= y):
                # We try to keep max heap feature. That's why we do (y - x) to have a negative value
                heapq.heappush(stones, y - x)

        return -stones[0]


# Create an instance of the class
solution = Solution()
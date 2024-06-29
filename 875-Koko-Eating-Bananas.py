"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.



Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23


Constraints:
1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""


# Time Complexity:  O(M log N) -> M is the number of piles, N is the range of possible speeds k during binary search
# Space Complexity: O(1)
from math import ceil

class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        piles, h = [3, 6, 7, 11], 8

        result = self.min_eating_speed(piles, h)
        assert result == 4, err_msg_invalid_result
        print(result)

        piles, h = [30, 11, 23, 4, 20], 5

        result = self.min_eating_speed(piles, h)
        assert result == 30, err_msg_invalid_result
        print(result)

        piles, h = [30, 11, 23, 4, 20], 6

        result = self.min_eating_speed(piles, h)
        assert result == 23, err_msg_invalid_result
        print(result)


    def min_eating_speed(self, piles: list[int], h: int) -> int:
        left, right = ceil(sum(piles) / h), max(piles)
        result = right

        while (left <= right):
            k = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += ceil(pile / k)

            if (hours <= h):
                right = k - 1
                result = k
            else:
                left = k + 1

        return result


# Create an instance of the class
solution = Solution()
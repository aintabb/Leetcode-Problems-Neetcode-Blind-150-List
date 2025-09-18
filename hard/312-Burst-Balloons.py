"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.



Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:
Input: nums = [1,5]
Output: 10


Constraints:
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""


# Time Complexity:  O(N^3) -> for both
# Space Complexity: O(N^2) -> for both
## Where "N" is the length of the input
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [3, 1, 5, 8]

        result = self.max_coins_top_down_memo(nums)
        assert result == 167, err_msg_invalid_result
        print(result)

        nums = [3, 1, 5, 8]

        result = self.max_coins_bottom_up_tabulation(nums)
        assert result == 167, err_msg_invalid_result
        print(result)

        nums = [1, 5]

        result = self.max_coins_top_down_memo(nums)
        assert result == 10, err_msg_invalid_result
        print(result)

        nums = [1, 5]

        result = self.max_coins_bottom_up_tabulation(nums)
        assert result == 10, err_msg_invalid_result
        print(result)

    def max_coins_top_down_memo(self, nums: list[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        nums = [1] + nums + [1]
        coin_cache = {}

        def helper(left: int, right: int) -> int:
            if left > right:
                return 0

            if (left, right) in coin_cache:
                return coin_cache[(left, right)]

            result = 0
            for idx in range(left, right + 1):
                coins = nums[left - 1] * nums[idx] * nums[right + 1]
                coins += helper(left, idx - 1) + helper(idx + 1, right)
                result = max(result, coins)

            coin_cache[(left, right)] = result
            return result

        return helper(1, len(nums) - 2)

    def max_coins_bottom_up_tabulation(self, nums: list[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        nums = [1] + nums + [1]
        len_nums = len(nums)
        dp = [[0 for _ in range(len_nums)] for _ in range(len_nums)]

        for i in range(len_nums - 2, -1, -1):
            for j in range(len_nums):
                if i + 1 == j:
                    dp[i][j] = 0
                    continue

                for k in range(i + 1, j):
                    coins = nums[i] * nums[j] * nums[k]
                    coins += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], coins)

        return dp[0][len_nums - 1]


# Create an instance of the class
solution = Solution()

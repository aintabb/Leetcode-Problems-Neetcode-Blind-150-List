"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
"""


# Time Complexity:  O(N) -> for both method
# Space Complexity: O(N) -> for tabulation, O(1) -> for regular dude
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [1, 2, 3, 1]

        result = self.rob_space_optimized(nums)
        assert result == 4, err_msg_invalid_result
        print(result)

        result = self.rob_tabulation_bottom_up(nums)
        assert result == 4, err_msg_invalid_result
        print(result)

        nums = [2, 7, 9, 3, 1]

        result = self.rob_space_optimized(nums)
        assert result == 12, err_msg_invalid_result
        print(result)

        result = self.rob_tabulation_bottom_up(nums)
        assert result == 12, err_msg_invalid_result
        print(result)

    def rob_space_optimized(self, nums: list[int]) -> int:
        if not nums:
            return 0

        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]

        if len_nums == 2:
            return max(nums[0], nums[1])

        first_rob = 0
        second_rob = 0
        max_rob = 0

        for num in nums:
            max_rob = max(num + first_rob, second_rob)
            first_rob = second_rob
            second_rob = max_rob

        return max_rob

    def rob_tabulation_bottom_up(self, nums: list[int]) -> int:
        if not nums:
            return 0

        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]

        dp = [0] * len_nums
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for house in range(2, len_nums):
            dp[house] = max(nums[house] + dp[house - 2], dp[house - 1])

        return dp[len_nums - 1]


# Create an instance of the class
solution = Solution()

"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.



Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1


Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""


# Time Complexity:  O(target * len(nums)) -> for both
# Space Complexity: O(target) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums, target = [1, 1, 1, 1, 1], 3

        result = self.find_target_sum_ways_memo_top_down(nums, target)
        assert result == 5, err_msg_invalid_result
        print(result)

        result = self.find_target_sum_ways_tabulation(nums, target)
        assert result == 5, err_msg_invalid_result
        print(result)

        nums, target = [1], 1

        result = self.find_target_sum_ways_memo_top_down(nums, target)
        assert result == 1, err_msg_invalid_result
        print(result)

        result = self.find_target_sum_ways_tabulation(nums, target)
        assert result == 1, err_msg_invalid_result
        print(result)

    def find_target_sum_ways_memo_top_down(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0

        total_sum = sum(nums)
        if total_sum < abs(target) or (total_sum + target) % 2 != 0:
            return 0

        sum_cache = {}

        def helper(idx: int, total_so_far: int) -> int:
            if idx == len(nums):
                return 1 if total_so_far == 0 else 0

            if (idx, total_so_far) in sum_cache:
                return sum_cache[(idx, total_so_far)]

            add = helper(idx + 1, total_so_far + nums[idx])
            subtract = helper(idx + 1, total_so_far - nums[idx])

            sum_cache[(idx, total_so_far)] = add + subtract
            return sum_cache[(idx, total_so_far)]

        return helper(0, target)

    def find_target_sum_ways_tabulation(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0

        total_sum = sum(nums)
        if total_sum < abs(target) or (total_sum + target) % 2 != 0:
            return 0

        target = (total_sum + target) // 2
        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for curr_sum in range(target, num - 1, -1):
                dp[curr_sum] += dp[curr_sum - num]

        return dp[target]


# Create an instance of the class
solution = Solution()

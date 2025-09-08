"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.



Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

# Time Complexity:  O(N*target)
# Space Complexity: O(target)


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [1, 5, 11, 5]

        result = self.can_partition(nums)
        assert result == True, err_msg_invalid_result
        print(result)

        nums = [1, 2, 3, 5]

        result = self.can_partition(nums)
        assert result == False, err_msg_invalid_result
        print(result)

        nums = [1, 2, 5]

        result = self.can_partition(nums)
        assert result == False, err_msg_invalid_result
        print(result)

    def can_partition(self, nums: list[int]) -> bool:
        if not nums:
            return False

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        dp = [False] * (target_sum + 1)
        dp[0] = True

        for num in nums:
            for curr_sum in range(target_sum, num - 1, -1):
                dp[curr_sum] = dp[curr_sum] or dp[curr_sum - num]

        return dp[target_sum]


# Create an instance of the class
solution = Solution()

"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.


Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""


# Time Complexity:  O(N^2) -> for both
# Space Complexity: O(N) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [10, 9, 2, 5, 3, 7, 101, 18]

        result = self.length_of_LIS_tabulation_bottom_up(nums)
        assert result == 4, err_msg_invalid_result
        print(result)

        result = self.length_of_LIS_memo_top_down(nums)
        assert result == 4, err_msg_invalid_result
        print(result)

        nums = [0, 1, 0, 3, 2, 3]

        result = self.length_of_LIS_tabulation_bottom_up(nums)
        assert result == 4, err_msg_invalid_result
        print(result)

        result = self.length_of_LIS_memo_top_down(nums)
        assert result == 4, err_msg_invalid_result
        print(result)

        nums = [7, 7, 7, 7, 7, 7, 7]

        result = self.length_of_LIS_tabulation_bottom_up(nums)
        assert result == 1, err_msg_invalid_result
        print(result)

        result = self.length_of_LIS_memo_top_down(nums)
        assert result == 1, err_msg_invalid_result
        print(result)

    def length_of_LIS_memo_top_down(self, nums: list[int]) -> int:
        if not nums:
            return 0

        len_nums = len(nums)
        num_cache = {}

        def helper(idx: int) -> int:
            if idx in num_cache:
                return num_cache[idx]

            max_len = 1
            for prev_idx in range(idx):
                if nums[prev_idx] < nums[idx]:
                    max_len = max(max_len, 1 + helper(prev_idx))

            num_cache[idx] = max_len
            return max_len

        max_len_lis = 0
        for idx in range(len_nums):
            max_len_lis = max(max_len_lis, helper(idx))

        return max_len_lis

    def length_of_LIS_tabulation_bottom_up(self, nums: list[int]) -> int:
        if not nums:
            return 0

        len_nums = len(nums)
        dp = [1] * len_nums

        for next_idx in range(1, len_nums):
            for prev_idx in range(next_idx):
                if nums[next_idx] > nums[prev_idx]:
                    dp[next_idx] = max(dp[next_idx], 1 + dp[prev_idx])

        return max(dp)


# Create an instance of the class
solution = Solution()

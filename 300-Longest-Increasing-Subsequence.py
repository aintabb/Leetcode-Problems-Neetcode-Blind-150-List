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


# Time Complexity:  O(N**2) -> for both
# Space Complexity: O(N) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [10,9,2,5,3,7,101,18]

        result = self.length_of_LIS_tabulation(nums)
        assert result == 4, err_msg_invalid_result
        print(result)

        result = self.length_of_LIS_memo(nums)
        assert result == 4, err_msg_invalid_result
        print(result)

        nums = [0,1,0,3,2,3]

        result = self.length_of_LIS_tabulation(nums)
        assert result == 4, err_msg_invalid_result
        print(result)

        result = self.length_of_LIS_memo(nums)
        assert result == 4, err_msg_invalid_result
        print(result)

        nums = [7,7,7,7,7,7,7]

        result = self.length_of_LIS_tabulation(nums)
        assert result == 1, err_msg_invalid_result
        print(result)

        result = self.length_of_LIS_memo(nums)
        assert result == 1, err_msg_invalid_result
        print(result)


    def length_of_LIS_tabulation(self, nums: list[int]) -> int:
        if not nums:
            return 0

        len_nums = len(nums)
        dp = [1] * len_nums

        for prev in range(len_nums - 1, -1, -1):
            for next in range(prev + 1, len_nums):
                if (nums[prev] < nums[next]):
                    dp[prev] = max(dp[prev], 1 + dp[next])

        return max(dp)

    def length_of_LIS_memo(self, nums: list[int]) -> int:
        if not nums:
            return 0

        memo = {}
        len_nums = len(nums)

        def lis_ending_at(idx: int) -> int:
            if (idx in memo):
                return memo[idx]

            max_length = 1
            for prev_idx in range(idx):
                if (nums[prev_idx] < nums[idx]):
                    max_length = max(max_length, 1 + lis_ending_at(prev_idx))

            memo[idx] = max_length

            return max_length

        max_lis = 0
        for i in range(len_nums):
            max_lis = max(max_lis, lis_ending_at(i))

        return max_lis


# Create an instance of the class
solution = Solution()

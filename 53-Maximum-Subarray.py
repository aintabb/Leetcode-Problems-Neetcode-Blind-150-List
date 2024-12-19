"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.



Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

# Time Complexity:  O(N**2) -> for the brute force, O(N) -> for the kadane
# Space Complexity: O(1) -> for both


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

        result = self.max_sub_array_brute_force(nums)
        assert result == 6, err_msg_invalid_result
        print(result)

        result = self.max_sub_array_kadane(nums)
        assert result == 6, err_msg_invalid_result
        print(result)

        nums = [1]

        result = self.max_sub_array_brute_force(nums)
        assert result == 1, err_msg_invalid_result
        print(result)

        result = self.max_sub_array_kadane(nums)
        assert result == 1, err_msg_invalid_result
        print(result)

        nums = [5, 4, -1, 7, 8]

        result = self.max_sub_array_brute_force(nums)
        assert result == 23, err_msg_invalid_result
        print(result)

        result = self.max_sub_array_kadane(nums)
        assert result == 23, err_msg_invalid_result
        print(result)

    # Time limit exceeds for larger inputs
    def max_sub_array_brute_force(self, nums: list[int]) -> int:
        if not nums:
            return 0

        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]

        max_sum = float("-inf")
        for i in range(len_nums):
            curr_sum = 0
            for j in range(i, len_nums):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)

        return int(max_sum)

    def max_sub_array_kadane(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        max_sub = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += num
            max_sub = max(max_sub, curr_sum)

        return max_sub


# Create an instance of the class
solution = Solution()

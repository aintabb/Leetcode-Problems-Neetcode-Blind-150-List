"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1


Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""


# Time Complexity:  O(N)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [2, 2, 1]
        result = self.single_number(nums)
        assert result == 1, err_msg_invalid_result
        print(result)

        nums = [4, 1, 2, 1, 2]
        result = self.single_number(nums)
        assert result == 4, err_msg_invalid_result
        print(result)

        nums = [1]
        result = self.single_number(nums)
        assert result == 1, err_msg_invalid_result
        print(result)


    def single_number(self, nums: list[int]) -> int:
        n = len(nums)
        result = nums[0]

        for i in range(1, n):
            result ^= nums[i]

        return result


# Create an instance of the class
solution = Solution()
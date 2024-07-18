"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3


Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""


# Time Complexity:  O(N)
# Space Complexity: O(N)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [1, 3, 4, 2, 2]

        result = self.find_duplicate(nums)
        assert result == 2, err_msg_invalid_result
        print(result)

        nums = [3, 1, 3, 4, 2]

        result = self.find_duplicate(nums)
        assert result == 3, err_msg_invalid_result
        print(result)

        nums = [3, 3, 3, 3, 3]

        result = self.find_duplicate(nums)
        assert result == 3, err_msg_invalid_result
        print(result)


    def find_duplicate(self, nums: list[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        # Finding the cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Finding the duplicate
        fast = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]

        return slow

# Create an instance of the class
solution = Solution()
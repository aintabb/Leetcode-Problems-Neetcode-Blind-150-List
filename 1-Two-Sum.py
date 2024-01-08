'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



# Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

# Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

class TwoSum:
    def __init__(self) -> None:
        err_msg_invalid_indices = "Provided indices do not add up to the target value. Something is wrong!"
        nums, target = [2, 7, 11, 15], 9

        result = self.find_indices(nums, target)
        assert result == [0, 1] or [1, 0], err_msg_invalid_indices
        print(result)

        nums, target = [3, 2, 4], 6

        result = self.find_indices(nums, target)
        assert result == [1, 2] or [2, 1], err_msg_invalid_indices
        print(result)

        nums, target = [3, 3], 6

        result = self.find_indices(nums, target)
        assert result == [0, 1] or [1, 0], err_msg_invalid_indices
        print(result)

    def find_indices(self, nums: list[int], target: int) -> list[int]:
        if (len(nums) < 2):
          return []

        if (len(nums) == 2):
          return [0, 1]

        remaining_map = {}
        for index, num in enumerate(nums):
          complement = target - num
          if complement in remaining_map:
            return [index, remaining_map[complement]]
          remaining_map[num] = index

        return []

# Create an instance of the class
two_sum = TwoSum()
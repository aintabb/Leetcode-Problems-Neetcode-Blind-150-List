"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""

# Time Complexity:  O(logN)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums, target = [-1,0,3,5,9,12], 9

        result = self.search_with_recursion(nums, target)
        assert result == 4, err_msg_invalid_result
        print(result)

        nums, target = [-1,0,3,5,9,12], 2

        result = self.search_with_recursion(nums, target)
        assert result == -1, err_msg_invalid_result
        print(result)


    def search_with_recursion(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        def binary_search(left, right):
            if (right >= left):
                # To prevent integer overflow. It usually don't happen in Python
                middle = left + (right - left) // 2

                if (nums[middle] > target):
                    return binary_search(left, middle - 1)
                elif (nums[middle] < target):
                    return binary_search(middle + 1, right)
                else:
                    return middle
            else:
                return -1

        return binary_search(left, right)

    def search_with_iteration(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while (right >= left):
            middle = left + (right - left) // 2

            if (nums[middle] > target):
                right = middle - 1
            elif (nums[middle] < target):
                left = middle + 1
            else:
                return middle

        return -1

# Create an instance of the class
solution = Solution()
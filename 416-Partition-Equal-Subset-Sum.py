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
from tarfile import tar_filter


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [1,5,11,5]

        result = self.can_partition(nums)
        assert result == True, err_msg_invalid_result
        print(result)

        nums = [1,2,3,5]

        result = self.can_partition(nums)
        assert result == False, err_msg_invalid_result
        print(result)


    def can_partition(self, nums: list[int]) -> bool:
        if not nums:
            return False

        sum_nums = sum(nums)
        if (sum_nums % 2 != 0):
            return False

        len_nums = len(nums)
        target = sum_nums // 2
        dp = set([0])

        for i in range(len_nums - 1, -1, -1):
            dp_temp = set()

            for t in dp:
                if (t + nums[i] == target):
                    return True

                dp_temp.add(t)
                dp_temp.add(t + nums[i])

            dp = dp_temp

        return True if target in dp else False


# Create an instance of the class
solution = Solution()

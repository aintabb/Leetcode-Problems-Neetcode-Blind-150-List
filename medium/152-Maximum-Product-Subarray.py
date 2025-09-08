"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:
1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""


# Time Complexity:  O(N)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [2, 3, -2, 4]

        result = self.max_product(nums)
        assert result == 6, err_msg_invalid_result
        print(result)

        nums = [-2, 0, -1]

        result = self.max_product(nums)
        assert result == 0, err_msg_invalid_result
        print(result)

    def max_product(self, nums: list[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        result = max_prod = min_prod = nums[0]

        for idx in range(1, len(nums)):
            if nums[idx] < 0:
                min_prod, max_prod = max_prod, min_prod

            min_prod = min(nums[idx], min_prod * nums[idx])
            max_prod = max(nums[idx], max_prod * nums[idx])
            result = max(result, max_prod)

        return result


# Create an instance of the class
solution = Solution()

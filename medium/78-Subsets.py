"""
Given an integer array nums of unique elements, return all possible
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]


Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


# Time Complexity:  O(2^N)
# Space Complexity: O(N*(2^N))
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [1, 2, 3]

        result = self.subsets(nums)
        assert result == [
            [1, 2, 3],
            [1, 2],
            [1, 3],
            [1],
            [2, 3],
            [2],
            [3],
            [],
        ], err_msg_invalid_result
        print(result)

        nums = [0]

        result = self.subsets(nums)
        assert result == [[0], []], err_msg_invalid_result
        print(result)

    def subsets(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return [[]]

        result = []
        subset = []

        def backtrack(idx: int) -> None:
            if idx == len(nums):
                result.append(subset[:])
                return

            subset.append(nums[idx])
            backtrack(idx + 1)

            subset.pop()
            backtrack(idx + 1)

        backtrack(0)
        return result


# Create an instance of the class
solution = Solution()

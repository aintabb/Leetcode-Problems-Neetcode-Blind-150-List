"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]


Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""


# Time Complexity:  O(N*(2^N))
# Space Complexity: O(N*(2^N))
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [1, 2, 2]

        result = self.subsets_with_dup(nums)
        assert result == [[1, 2, 2], [1, 2], [1], [2, 2], [2], []], err_msg_invalid_result
        print(result)

        nums = [0]

        result = self.subsets_with_dup(nums)
        assert result == [[0], []], err_msg_invalid_result
        print(result)


    def subsets_with_dup(self, nums: list[int]) -> list[list[int]]:
        result, subset = [], []
        n = len(nums)

        nums.sort()

        def backtrack(idx: int) -> None:
            if (idx == n):
                result.append(subset[:])
                return

            subset.append(nums[idx])
            backtrack(idx + 1)
            subset.pop()

            while (idx + 1 < n and nums[idx] == nums[idx + 1]):
                idx += 1

            backtrack(idx + 1)

        backtrack(0)
        return result


# Create an instance of the class
solution = Solution()
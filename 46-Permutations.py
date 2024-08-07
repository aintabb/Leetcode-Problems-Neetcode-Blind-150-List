"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""


# Time Complexity:  O(N! * N)
# Space Complexity: O(N! * N)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [1, 2, 3]

        result = self.permute(nums)
        assert result == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], err_msg_invalid_result
        print(result)

        nums = [0, 1]

        result = self.permute(nums)
        assert result == [[0, 1], [1, 0]], err_msg_invalid_result
        print(result)

        nums = [1]

        result = self.permute(nums)
        assert result == [[1]], err_msg_invalid_result
        print(result)


    def permute(self, nums: list[int]) -> list[list[int]]:
        result, perm = [], []
        n = len(nums)

        def backtrack() -> None:
            if (len(perm) == n):
                result.append(perm[:])
                return

            for num in nums:
                if num not in perm:
                    perm.append(num)
                    backtrack()
                    perm.pop()

        backtrack()
        return result

# Create an instance of the class
solution = Solution()
"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""


# Time Complexity:  O(N*(2^N))
# Space Complexity: O(N*(2^N))
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        candidates, target = [10,1,2,7,6,1,5], 8

        result = self.combination_sum_two(candidates, target)
        assert result == [[1,1,6], [1,2,5], [1,7], [2,6]], err_msg_invalid_result
        print(result)

        candidates, target = [2,5,2,1,2], 5

        result = self.combination_sum_two(candidates, target)
        assert result == [[1,2,2], [5]], err_msg_invalid_result
        print(result)


    def combination_sum_two(self, candidates: list[int], target: int) -> list[list[int]]:
        result, candidate = [], []
        n = len(candidates)

        candidates.sort()

        def backtrack(idx: int, total: int) -> None:
            if (total == target):
                result.append(candidate[:])
                return

            if (idx >= n or total > target):
                return

            candidate.append(candidates[idx])
            backtrack(idx + 1, total + candidates[idx])
            candidate.pop()

            while (idx + 1 < n and candidates[idx] == candidates[idx + 1]):
                idx += 1

            backtrack(idx + 1, total)

        backtrack(0, 0)
        return result


# Create an instance of the class
solution = Solution()
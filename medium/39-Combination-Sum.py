"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []


Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""


# Time Complexity:  O((2^N)*T) -> T: Target value
# Space Complexity: O(T)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        candidates, target = [2, 3, 6, 7], 7

        result = self.combination_sum(candidates, target)
        assert result == [[2, 2, 3], [7]]
        print(result)

        candidates, target = [2, 3, 5], 8

        result = self.combination_sum(candidates, target)
        assert result == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        print(result)

        candidates, target = [2], 1

        result = self.combination_sum(candidates, target)
        assert result == [], err_msg_invalid_result
        print(result)

    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        if not candidates or target < 1:
            return [[]]

        result = []
        candidate = []

        def backtrack(idx: int, total: int) -> None:
            if total == target:
                result.append(candidate[:])
                return

            if idx == len(candidates) or total > target:
                return

            candidate.append(candidates[idx])
            # We don't increase the index to allow using the same number multiple times
            backtrack(idx, total + candidates[idx])

            candidate.pop()
            backtrack(idx + 1, total)

        backtrack(0, 0)
        return result


# Create an instance of the class
solution = Solution()

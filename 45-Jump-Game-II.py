"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2


Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

# Time Complexity:  O(N**2) -> for both memo and dp, O(N) -> for the greedy
# Space Complexity: O(N) -> for both memo and dp, O(1) -> for the greedy


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [2, 3, 1, 1, 4]

        result = self.jump_memo(nums)
        assert result == 2, err_msg_invalid_result
        print(result)

        result = self.jump_dp(nums)
        assert result == 2, err_msg_invalid_result
        print(result)

        result = self.jump_greedy(nums)
        assert result == 2, err_msg_invalid_result
        print(result)

        nums = [2, 3, 0, 1, 4]

        result = self.jump_memo(nums)
        assert result == 2, err_msg_invalid_result
        print(result)

        result = self.jump_dp(nums)
        assert result == 2, err_msg_invalid_result
        print(result)

        result = self.jump_greedy(nums)
        assert result == 2, err_msg_invalid_result
        print(result)

    def jump_memo(self, nums: list[int]) -> int:
        if not nums:
            return 0

        len_nums = len(nums)
        memo = {}

        def dfs(idx: int) -> int:
            if idx in memo:
                return memo[idx]
            if idx == len_nums - 1:
                return 0
            if nums[idx] == 0:
                return 1000000

            min_steps = 1000000
            end = min(len_nums - 1, idx + nums[idx])

            for j in range(idx + 1, end + 1):
                min_steps = min(min_steps, 1 + dfs(j))

            memo[idx] = min_steps
            return min_steps

        return dfs(0)

    def jump_dp(self, nums: list[int]) -> int:
        if not nums:
            return 0

        len_nums = len(nums)
        dp = [1000000] * len_nums
        dp[-1] = 0

        for i in range(len_nums - 2, -1, -1):
            end = min(len_nums - 1, i + nums[i])
            for j in range(i + 1, end + 1):
                dp[i] = min(dp[i], 1 + dp[j])

        return dp[0]

    def jump_greedy(self, nums: list[int]) -> int:
        if not nums:
            return 0

        len_nums = len(nums)
        min_steps = 0
        left = right = 0

        while right < len_nums - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left = right + 1
            right = farthest
            min_steps += 1

        return min_steps


# Create an instance of the class
solution = Solution()

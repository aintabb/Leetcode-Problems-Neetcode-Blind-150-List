"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

# Time Complexity:  O(N**2) -> for both memo and dp, O(N) -> for the greedy
# Space Complexity: O(N) -> for both memo and dp, O(1) -> for the greedy


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums = [2, 3, 1, 1, 4]

        result = self.can_jump_memo(nums)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.can_jump_dp(nums)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.can_jump_greedy(nums)
        assert result == True, err_msg_invalid_result
        print(result)

        nums = [3, 2, 1, 0, 4]

        result = self.can_jump_memo(nums)
        assert result == False, err_msg_invalid_result
        print(result)

        result = self.can_jump_dp(nums)
        assert result == False, err_msg_invalid_result
        print(result)

        result = self.can_jump_greedy(nums)
        assert result == False, err_msg_invalid_result
        print(result)

    # Time limit exceeds for larger inputs
    def can_jump_memo(self, nums: list[int]) -> bool:
        if not nums:
            return True

        memo = {}

        def dfs(idx: int) -> bool:
            if idx in memo:
                return memo[idx]
            if idx == len(nums) - 1:
                return True

            if nums[idx] == 0:
                return False

            end = min(len(nums) - 1, idx + nums[idx])
            for j in range(idx + 1, end + 1):
                if dfs(j):
                    memo[idx] = True
                    return True

            memo[idx] = False
            return False

        return dfs(0)

    def can_jump_dp(self, nums: list[int]) -> bool:
        if not nums:
            return True

        len_nums = len(nums)
        dp = [False] * len_nums
        dp[-1] = True

        for i in range(len_nums - 2, -1, -1):
            end = min(len_nums - 1, i + nums[i])
            for j in range(i + 1, end + 1):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]

    def can_jump_greedy(self, nums: list[int]) -> bool:
        if not nums or len(nums) < 2:
            return True

        len_nums = len(nums)
        last_pos = len_nums - 1

        for idx in range(len_nums - 1, -1, -1):
            if idx + nums[idx] >= last_pos:
                last_pos = idx

        return last_pos == 0


# Create an instance of the class
solution = Solution()

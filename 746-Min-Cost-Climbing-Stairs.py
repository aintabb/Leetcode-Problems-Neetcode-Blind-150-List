"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.


Constraints:
2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""


# Time Complexity:  O(2^N) -> R - O(N) -> M, T, T no space
# Space Complexity: O(N) -> R, M, T -  O(1) - T no space
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        cost = [10, 15, 20]

        result = self.min_cost_climbing_stairs_recursive(cost)
        assert result == 15, err_msg_invalid_result
        print(result)

        result = self.min_cost_climbing_stairs_memoization(cost)
        assert result == 15, err_msg_invalid_result
        print(result)

        result = self.min_cost_climbing_stairs_tabulation_with_memory(cost)
        assert result == 15, err_msg_invalid_result
        print(result)

        result = self.min_cost_climbing_stairs_tabulation_no_memory(cost)
        assert result == 15, err_msg_invalid_result
        print(result)

        cost = [1,100,1,1,1,100,1,1,100,1]

        result = self.min_cost_climbing_stairs_recursive(cost)
        assert result == 6, err_msg_invalid_result
        print(result)

        result = self.min_cost_climbing_stairs_memoization(cost)
        assert result == 6, err_msg_invalid_result
        print(result)

        result = self.min_cost_climbing_stairs_tabulation_with_memory(cost)
        assert result == 6, err_msg_invalid_result
        print(result)

        result = self.min_cost_climbing_stairs_tabulation_no_memory(cost)
        assert result == 6, err_msg_invalid_result
        print(result)


    def min_cost_climbing_stairs_recursive(self, cost: list[int]) -> int:
        def min_cost_helper(curr_step: int) -> int:
            # Base Cases: if we're at the first or second step, return it's cost
            if curr_step <= 1:
                return cost[curr_step]

            return cost[curr_step] + min(
                min_cost_helper(curr_step - 1), min_cost_helper(curr_step - 2)
            )

        n = len(cost)

        # Minimum of the two possibilities
        return min(min_cost_helper(n - 1), min_cost_helper(n - 2))

    def min_cost_climbing_stairs_memoization(self, cost: list[int]) -> int:
        def min_cost_helper_memo(curr_step: int) -> int:
            if curr_step <= 1:
                return cost[curr_step]

            cache[curr_step] = cost[curr_step] + min(
                min_cost_helper_memo(curr_step - 1), min_cost_helper_memo(curr_step - 2)
            )

            return cache[curr_step]

        n = len(cost)
        cache = {}

        return min(min_cost_helper_memo(n - 1), min_cost_helper_memo(n - 2))

    def min_cost_climbing_stairs_tabulation_with_memory(self, cost: list[int]) -> int:
        n = len(cost)

        dp = [0] * (n + 1)

        # Base cases: the cost of reaching the first two steps is their respective costs
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        # The final step is the top of the floor, which can be reached either
        # from the last step or the second to last step
        dp[n] = min(dp[n - 1], dp[n - 2])

        return dp[n]

    def min_cost_climbing_stairs_tabulation_no_memory(self, cost: list[int]) -> int:
        n = len(cost)

        # Base cases: the cost of reaching the first two steps is their respective costs
        prev = cost[0]
        curr = cost[1]

        for i in range(2, n):
            temp = min(prev, curr) + cost[i]
            prev = curr
            curr = temp

        return min(prev, curr)


# Create an instance of the class
solution = Solution()
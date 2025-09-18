"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.



Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1


Constraints:
1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
"""


# Time Complexity:  O(amount * len(coins)) -> for both
# Space Complexity: O(amount) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        amount, coins = 5, [1, 2, 5]

        result = self.coin_change_two_memo_top_down(amount, coins)
        assert result == 4, err_msg_invalid_result
        print(result)

        result = self.coin_change_two_tabulation_bottom_up(amount, coins)
        assert result == 4, err_msg_invalid_result
        print(result)

        amount, coins = 3, [2]

        result = self.coin_change_two_memo_top_down(amount, coins)
        assert result == 0, err_msg_invalid_result
        print(result)

        result = self.coin_change_two_memo_top_down(amount, coins)
        assert result == 0, err_msg_invalid_result
        print(result)

        amount, coins = 10, [10]

        result = self.coin_change_two_memo_top_down(amount, coins)
        assert result == 1, err_msg_invalid_result
        print(result)

        result = self.coin_change_two_memo_top_down(amount, coins)
        assert result == 1, err_msg_invalid_result
        print(result)

    def coin_change_two_memo_top_down(self, amount: int, coins: list[int]) -> int:
        if not coins or amount < 0:
            return 0

        cache = {}

        def helper(idx: int, rem: int) -> int:
            if rem == 0:
                return 1

            if idx == len(coins) or rem < 0:
                return 0

            if (idx, rem) in cache:
                return cache[(idx, rem)]

            include = helper(idx, rem - coins[idx])
            exclude = helper(idx + 1, rem)

            cache[(idx, rem)] = include + exclude
            return cache[(idx, rem)]

        return helper(0, amount)

    def coin_change_two_tabulation_bottom_up(
        self, amount: int, coins: list[int]
    ) -> int:
        if not coins or amount < 0:
            return 0

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for curr_amount in range(coin, amount + 1):
                dp[curr_amount] += dp[curr_amount - coin]

        return dp[amount]


# Create an instance of the class
solution = Solution()

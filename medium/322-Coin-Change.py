"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0


Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2**31 - 1
0 <= amount <= 104
"""


# Time Complexity:  O(amount * len(coins)) -> for both
# Space Complexity: O(amount) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        coins = [1, 2, 5]
        amount = 11

        result = self.coin_change_tabulation_bottom_up(coins, amount)
        assert result == 3, err_msg_invalid_result
        print(result)

        result = self.coin_change_memoization_top_down(coins, amount)
        assert result == 3, err_msg_invalid_result
        print(result)

        coins = [2]
        amount = 3

        result = self.coin_change_tabulation_bottom_up(coins, amount)
        assert result == -1, err_msg_invalid_result
        print(result)

        result = self.coin_change_memoization_top_down(coins, amount)
        assert result == -1, err_msg_invalid_result
        print(result)

        coins = [1]
        amount = 0

        result = self.coin_change_tabulation_bottom_up(coins, amount)
        assert result == 0, err_msg_invalid_result
        print(result)

        result = self.coin_change_memoization_top_down(coins, amount)
        assert result == 0, err_msg_invalid_result
        print(result)

    def coin_change_memoization_top_down(self, coins: list[int], amount: int) -> int:
        if not coins or not amount:
            return 0

        # Define a cache to store the results of sub-problems
        coin_cache = {}

        def helper(rem: int) -> int:
            # If the remaining amount is 0, return 0 (no coins needed)
            if rem == 0:
                return 0

            # If the remaining amount is less than 0, return -1 (invalid case)
            if rem < 0:
                return -1

            # If the result is already in the cache, return it
            if rem in coin_cache:
                return coin_cache[rem]

            # Initialize the minimum number of coins to a large value
            min_coins = float("inf")
            for coin in coins:
                result = helper(rem - coin)
                if result >= 0:  # If result is valid
                    min_coins = min(min_coins, result + 1)

            # Cache the result
            coin_cache[rem] = min_coins if min_coins != float("inf") else -1
            return coin_cache[rem]

        return helper(amount)

    def coin_change_tabulation_bottom_up(self, coins: list[int], amount: int) -> int:
        if not coins or not amount:
            return 0

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for rem in range(coin, amount + 1):
                dp[rem] = min(dp[rem], 1 + dp[rem - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1


# Create an instance of the class
solution = Solution()

"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0


Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""


# Time Complexity:  O(n) -> for both
# Space Complexity: O(n) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        prices = [1,2,3,0,2]

        result = self.max_profit_memo(prices)
        assert result == 3, err_msg_invalid_result
        print(result)

        result = self.max_profit_tabulation(prices)
        assert result == 3, err_msg_invalid_result
        print(result)

        prices = [1]

        result = self.max_profit_memo(prices)
        assert result == 0, err_msg_invalid_result
        print(result)

        result = self.max_profit_tabulation(prices)
        assert result == 0, err_msg_invalid_result
        print(result)


    def max_profit_memo(self, prices: list[int]) -> int:
        len_prices = len(prices)
        if (len_prices <= 1):
            return 0

        memo = {}

        def dfs(idx, buying):
            # Base case: if we've gone through all prices, return 0
            if (idx >= len_prices):
                return 0

            # Calculate the profit if we do nothing (cooldown)
            cool_down = dfs(idx + 1, buying)

            if buying:
                # If we're buying, we can either buy or cooldown
                # If we buy, we spend the current price and switch to selling state
                buy = dfs(idx + 1, not buying) - prices[idx]
                memo[(idx, buying)] = max(buy, cool_down)
            else:
                # If we're selling, we can either sell or cooldown
                # If we sell, we gain the current price and switch to buying state
                # Note the i + 2 to account for the mandatory cooldown day
                sell = dfs(idx + 2, not buying) + prices[idx]
                memo[(idx, buying)] = max(sell, cool_down)

            return memo[(idx, buying)]

        # Start the recursion in the buying state
        return dfs(0, True)


    def max_profit_tabulation(self, prices: list[int]) -> int:
        if len(prices) <= 1:
            return 0

        len_prices = len(prices)

        # Initialize our DP arrays
        buy = [0] * len_prices  # Maximum profit if we buy on this day or take no action
        sell = [0] * len_prices  # Maximum profit if we sell on this day or take no action

        # Base cases
        buy[0] = -prices[0]  # If we buy on day 0, our profit is negative the price
        buy[1] = max(-prices[0], -prices[1])  # We can either buy on day 0 or day 1
        sell[1] = max(0, prices[1] - prices[0])  # We can either do nothing or buy on day 0 and sell on day 1

        # Fill the DP arrays
        for i in range(2, len_prices):
            # If we buy on day i, we either take no action (buy[i-1]) or we sell two days ago and buy today
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])

            # If we sell on day i, we either take no action (sell[i-1]) or we buy yesterday and sell today
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])

        # The maximum profit is the maximum value in the sell array
        return max(sell)


# Create an instance of the class
solution = Solution()
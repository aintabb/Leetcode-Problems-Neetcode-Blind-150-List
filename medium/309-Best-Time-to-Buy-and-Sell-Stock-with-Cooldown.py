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
# Space Complexity: O(n) -> for top-down, O(1) -> for bottom-up\tabulation
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        prices = [1, 2, 3, 0, 2]

        result = self.max_profit_memo_top_down(prices)
        assert result == 3, err_msg_invalid_result
        print(result)

        result = self.max_profit_tabulation_bottom_up(prices)
        assert result == 3, err_msg_invalid_result
        print(result)

        prices = [1]

        result = self.max_profit_memo_top_down(prices)
        assert result == 0, err_msg_invalid_result
        print(result)

        result = self.max_profit_tabulation_bottom_up(prices)
        assert result == 0, err_msg_invalid_result
        print(result)

    def max_profit_memo_top_down(self, prices: list[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        profit_cache = {}
        len_prices = len(prices)

        def helper(idx: int, buying_state: bool) -> int:
            # Base case: if we've gone through all prices, return 0
            if idx >= len_prices:
                return 0

            if (idx, buying_state) in profit_cache:
                return profit_cache[(idx, buying_state)]

            # Calculate the profit if we do nothing (cooldown)
            cool_down = helper(idx + 1, buying_state)

            # If we're buying, we can either buy or cooldown
            if buying_state:
                # If we buy, we spend the current price and switch to selling state
                buy = helper(idx + 1, not buying_state) - prices[idx]
                profit_cache[(idx, buying_state)] = max(buy, cool_down)
            else:
                # If we're selling, we can either sell or cooldown
                # If we sell, we gain the current price and switch to buying state
                # Note the i + 2 to account for the mandatory cooldown day
                sell = helper(idx + 2, not buying_state) + prices[idx]
                profit_cache[(idx, buying_state)] = max(sell, cool_down)

            return profit_cache[(idx, buying_state)]

        # Start the recursion in the buying state
        return helper(0, True)

    def max_profit_tabulation_bottom_up(self, prices: list[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        buy, sell, cooldown = -prices[0], 0, 0

        for price in prices[1:]:
            # We can either stay in the buying state or transition from the cooldown state
            # to the buying state by buying the stock
            new_buy = max(buy, cooldown - price)
            # We can either stay in the selling state or transition from the buying state
            # to the selling state by selling the stock
            new_sell = max(sell, buy + price)
            # We can either stay in the cooldown state or transition from the selling state
            # to the cooldown state by cooling down
            new_cooldown = max(sell, cooldown)

            buy, sell, cooldown = new_buy, new_sell, new_cooldown

        return max(sell, cooldown)


# Create an instance of the class
solution = Solution()

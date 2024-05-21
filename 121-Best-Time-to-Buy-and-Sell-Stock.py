"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

# Time Complexity:  O(1)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        prices = [7,1,5,3,6,4]

        result = self.max_profit(prices)
        assert result == 5, err_msg_invalid_result
        print(result)

        prices = [7,6,4,3,1]

        result = self.max_profit(prices)
        assert result == 0, err_msg_invalid_result
        print(result)

        prices = [6]

        result = self.max_profit(prices)
        assert result == 0, err_msg_invalid_result
        print(result)


    def max_profit(self, prices: list[int]) -> int:
        max_profit = 0
        len_of_p  = len(prices)

        if (len_of_p == 1):
            return max_profit

        left, right = 0, 1
        while (right < len_of_p):
            if (prices[left] < prices[right]):
                curr_profit = prices[right] - prices[left]
                max_profit  = max(max_profit, curr_profit)
            else:
                left = right
            right += 1

        return max_profit

# Create an instance of the class
solution = Solution()
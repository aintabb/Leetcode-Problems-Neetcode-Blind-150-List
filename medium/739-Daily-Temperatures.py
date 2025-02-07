"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


# Time Complexity:  O(N)
# Space Complexity: O(N)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

        result = self.daily_temperatures(temperatures)
        assert result == [1, 1, 4, 2, 1, 1, 0, 0], err_msg_invalid_result
        print(result)

        temperatures = [30, 40, 50, 60]

        result = self.daily_temperatures(temperatures)
        assert result == [1, 1, 1, 0], err_msg_invalid_result
        print(result)

        temperatures = [30, 60, 90]

        result = self.daily_temperatures(temperatures)
        assert result == [1, 1, 0], err_msg_invalid_result
        print(result)

    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        len_temp = len(temperatures)

        if len_temp == 1:
            return [0]

        temp_stack = []
        result = [0] * len_temp

        for idx in range(len_temp):
            # Navigate back temps in the stack
            while temp_stack and temperatures[idx] > temperatures[temp_stack[-1]]:
                prev_index = temp_stack.pop()
                result[prev_index] = idx - prev_index
            # If the stack is empty or given temp is lower than what we have in the stack,
            # add it to the stack
            temp_stack.append(idx)

        return result


# Create an instance of the class
solution = Solution()

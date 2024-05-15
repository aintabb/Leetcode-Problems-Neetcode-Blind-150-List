"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10

Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

######################
heights = [3, 5, 12]
Output: 4

# Edge Cases:
- if len of heights is 1, return heights[0]

# Approach:
- use a variable to keep the max area ~ max_area
- loop through the array
- check i and i + 1
- get either max(height[i], height[i + 1]) or min(....) * 2. Whichever is the greatest

######################

Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
"""

# Time Complexity:
# Space Complexity:

class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        heights = [2,1,5,6,2,3]

        result = self.largest_rectangle_area(heights)
        assert result == 10, err_msg_invalid_result
        print(result)

        heights = [2,4]

        result = self.largest_rectangle_area(heights)
        assert result == 4, err_msg_invalid_result
        print(result)

        heights = [2,1,2]

        result = self.largest_rectangle_area(heights)
        assert result == 3, err_msg_invalid_result
        print(result)


    def largest_rectangle_area(self, heights: list[int]) -> int:
        max_area   = 0
        pair_stack = [] # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while (pair_stack and pair_stack[-1][1] > h):
                index, height = pair_stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index

            pair_stack.append((start, h))

        for i, h in pair_stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area

# Create an instance of the class
solution = Solution()
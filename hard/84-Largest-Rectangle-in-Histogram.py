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


Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
"""

# Time Complexity:  O(N)
# Space Complexity: O(N)


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        heights = [2, 1, 5, 6, 2, 3]

        result = self.largest_rectangle_area(heights)
        assert result == 10, err_msg_invalid_result
        print(result)

        heights = [2, 4]

        result = self.largest_rectangle_area(heights)
        assert result == 4, err_msg_invalid_result
        print(result)

        heights = [2, 1, 2]

        result = self.largest_rectangle_area(heights)
        assert result == 3, err_msg_invalid_result
        print(result)

    def largest_rectangle_area(self, heights: list[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        # To keep indices of bars in increasing order
        bar_idx_stack = []
        max_area = 0

        # Append "0" to handle the last bar
        heights.append(0)

        for idx, h in enumerate(heights):
            while bar_idx_stack and heights[bar_idx_stack[-1]] > h:
                last_bar_idx = bar_idx_stack.pop()
                last_height = heights[last_bar_idx]
                width = idx if not bar_idx_stack else idx - bar_idx_stack[-1] - 1

                max_area = max(max_area, last_height * width)

            bar_idx_stack.append(idx)

        return max_area


# Create an instance of the class
solution = Solution()

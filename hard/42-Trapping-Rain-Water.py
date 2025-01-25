"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""


# Time Complexity:  O(N)
# Space Complexity: O(1)
class TrappingRainWater:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

        result = self.trapping_rain_water_no_memory(height)
        assert result == 6, err_msg_invalid_result
        print(result)

        height = [4, 2, 0, 3, 2, 5]

        result = self.trapping_rain_water_no_memory(height)
        assert result == 9, err_msg_invalid_result
        print(result)

        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

        result = self.trapping_rain_water_with_memory(height)
        assert result == 6, err_msg_invalid_result
        print(result)

        height = [4, 2, 0, 3, 2, 5]

        result = self.trapping_rain_water_with_memory(height)
        assert result == 9, err_msg_invalid_result
        print(result)

    """
    Given a list of non-negative integers representing an elevation map where the width of each bar is 1,
    this function calculates the amount of water it is able to trap after raining.

    Args:
        height (list[int]): A list of non-negative integers representing the height of each bar.

    Returns:
        int: The total amount of water that can be trapped.
    """

    def trapping_rain_water_no_memory(self, height: list[int]) -> int:
        if not height or len(height) < 3:
            return 0

        total_area = 0
        left_idx, right_idx = 0, len(height) - 1
        left_max, right_max = height[left_idx], height[right_idx]

        while left_idx < right_idx:
            # If the max height on the left side is smaller than the right side
            if left_max < right_max:
                left_idx += 1
                # Update the max height on the left side
                left_max = max(left_max, height[left_idx])
                # Calculate the water that can be trapped
                total_area += left_max - height[left_idx]
            else:
                # Same goes for the right side
                right_idx -= 1
                right_max = max(right_max, height[right_idx])
                total_area += right_max - height[right_idx]

        return total_area

    def trapping_rain_water_with_memory(self, height: list[int]) -> int:
        if not height or len(height) < 3:
            return 0

        len_height = len(height)
        max_left = [0] * len_height
        max_value = 0

        for idx in range(1, len_height):
            max_value = max(max_value, height[idx - 1])
            max_left[idx] = max_value

        max_right = [0] * len_height
        max_value = height[len_height - 1]

        for idx in range(len_height - 2, -1, -1):
            max_value = max(max_value, height[idx + 1])
            max_right[idx] = max_value

        total_area = 0

        for idx in range(len_height):
            min_height = min(max_left[idx], max_right[idx])
            area_to_fill = min_height - height[idx]
            total_area += area_to_fill if area_to_fill > 0 else 0

        return total_area


# Create an instance of the class
trapping_rain_water = TrappingRainWater()

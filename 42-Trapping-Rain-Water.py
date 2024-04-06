'''
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
'''

# Time Complexity:  O(N)
# Space Complexity: O(1)
class TrappingRainWater:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        height = [0,1,0,2,1,0,1,3,2,1,2,1]

        result = self.trapping_rain_water_no_memory(height)
        assert result == 6, err_msg_invalid_result
        print(result)

        height = [4,2,0,3,2,5]

        result = self.trapping_rain_water_no_memory(height)
        assert result == 9, err_msg_invalid_result
        print(result)

        height = [0,1,0,2,1,0,1,3,2,1,2,1]

        result = self.trapping_rain_water_with_memory(height)
        assert result == 6, err_msg_invalid_result
        print(result)

        height = [4,2,0,3,2,5]

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
      result = 0
      if (len(height) < 3):
        return result

      l, r = 0, len(height) - 1
      left_max, right_max = height[l], height[r]

      while (l < r):
        # If the max height on the left side is smaller than the right side
        if (left_max < right_max):
          l += 1
          # Update the max height on the left side
          left_max = max(left_max, height[l])
          # Calculate the water that can be trapped
          result += left_max - height[l]
        else:
          # Same goes for the right side
          r -= 1
          right_max = max(right_max, height[r])
          result += right_max - height[r]

      return result


    def trapping_rain_water_with_memory(self, height: list[int]) -> int:
      result, len_of_height = 0, len(height)
      if (len_of_height < 3):
        return result

      max_left  = [0] * len_of_height
      max_value = max_left[0] = height[0]

      for i in range(1, len_of_height, 1):
        max_value = max(max_value, height[i - 1])
        max_left[i] = max_value

      max_right = [0] * len_of_height
      max_value = height[len_of_height - 1]

      for i in range(len_of_height - 2, -1, -1):
        max_value = max(max_value, height[i + 1])
        max_right[i] = max_value

      for i, num in enumerate(height):
        min_height = min(max_left[i], max_right[i])
        result += min_height - height[i] if min_height - height[i] > 0 else 0

      return result

# Create an instance of the class
trapping_rain_water = TrappingRainWater()
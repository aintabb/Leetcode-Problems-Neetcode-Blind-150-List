'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1


Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

# Time Complexity:  O(N)
# Space Complexity: O(1)
class ContainerWithMostWater:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        height = [1,8,6,2,5,4,8,3,7]

        result = self.container_with_most_water(height)
        assert result == 49, err_msg_invalid_result
        print(result)

        height = [1,1]

        result = self.container_with_most_water(height)
        assert result == 1, err_msg_invalid_result
        print(result)

        height = [9, 1, 5, 7, 9]

        result = self.container_with_most_water(height)
        assert result == 36, err_msg_invalid_result
        print(result)


    def container_with_most_water(self, height: list[int]) -> int:
      max_area, l, r = 0, 0, len(height) - 1

      while (l < r):
        curr_area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, curr_area)

        if (height[l] < height[r]):
          l += 1
        else:
          r -= 1

      return max_area


# Create an instance of the class
container_with_most_water = ContainerWithMostWater()
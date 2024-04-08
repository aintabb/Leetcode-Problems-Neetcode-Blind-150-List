'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []

Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

# Time Complexity:  O(N^2)
# Space Complexity: O(1)


class ThreeSum:
    def __init__(self) -> None:
        err_msg_invalid_numbers = "Provided numbers does not add up to the sum. Something is wrong!"

        numbers = [-1,0,1,2,-1,-4]

        result = self.three_sum(numbers)
        assert result == [[-1,-1,2],[-1,0,1]], err_msg_invalid_numbers
        print(result)

        numbers = [0,1,1]

        result = self.three_sum(numbers)
        assert result == [], err_msg_invalid_numbers
        print(result)

        numbers = [0,0,0]

        result = self.three_sum(numbers)
        assert result == [[0, 0, 0]], err_msg_invalid_numbers
        print(result)

        numbers = [0,0,0,0]

        result = self.three_sum(numbers)
        assert result == [[0, 0, 0]], err_msg_invalid_numbers
        print(result)


    def three_sum(self, nums: list[int]) -> list[list[int]]:
      result = []
      nums.sort()

      for i, val in enumerate(nums):
        # To prevent duplicates, skip the current value if it is the same as the previous one
        # See, [-3, 3, 4, -3, 1, 2] for an example
        if (i > 0 and val == nums[i - 1]):
          continue

        # Use two pointers to search for the other two values that adds up to 0
        l, r = i + 1, len(nums) - 1

        while (l < r):
          three_sum = val + nums[l] + nums[r]
          # Adjust pointers if the sum is too large or too small
          if (three_sum > 0):
            r -= 1
          elif (three_sum < 0):
            l += 1
          else:
            result.append([val, nums[l], nums[r]])

            # Increment left pointer until it is unique (not equal to the previous value)
            # See, [-2, -2, 0, 0, 2, 2] for an example
            l += 1
            while (nums[l] == nums[l - 1] and l < r):
              l += 1

      return result


# Create an instance of the class
three_sum = ThreeSum()
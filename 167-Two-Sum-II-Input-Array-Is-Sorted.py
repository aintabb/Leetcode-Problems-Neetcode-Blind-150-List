'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.



Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''

# Time Complexity:  O(N)
# Space Complexity: O(1)
class TwoSumTwo:
    def __init__(self) -> None:
        err_msg_invalid_number_pair = "Provided numbers does not add up to the sum. Something is wrong!"

        numbers, target = [2,7,11,15], 9

        result = self.two_sum(numbers, target)
        assert result == [1, 2], err_msg_invalid_number_pair
        print(result)

        numbers, target = [2,3,4], 6

        result = self.two_sum(numbers, target)
        assert result == [1, 3], err_msg_invalid_number_pair
        print(result)

        numbers, target = [-1, 0], -1

        result = self.two_sum(numbers, target)
        assert result == [1, 2], err_msg_invalid_number_pair
        print(result)


    def two_sum(self, numbers: list[int], target: int) -> list[int]:
      len_of_numbers = len(numbers)

      if (len_of_numbers == 2):
        return [1, 2]

      l, r = 0, len_of_numbers - 1
      while (l < r):
        curr_sum = numbers[l] + numbers[r]
        if (curr_sum > target):
          r -= 1
        elif (curr_sum < target):
          l += 1
        else:
          return [l + 1, r + 1]

      return []


# Create an instance of the class
two_sum_two = TwoSumTwo()
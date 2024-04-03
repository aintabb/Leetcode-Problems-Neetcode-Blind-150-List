'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

'''

# Time Complexity:
# Space Complexity:
class TwoSum:
    def __init__(self) -> None:
        err_msg_invalid_indices = "Provided indices do not add up to the target value. Something is wrong!"
        nums, target = [2, 7, 11, 15], 9

        result = self.find_indices(nums, target)
        assert result == [0, 1] or [1, 0], err_msg_invalid_indices
        print(result)

        nums, target = [3, 2, 4], 6

        result = self.find_indices(nums, target)
        assert result == [1, 2] or [2, 1], err_msg_invalid_indices
        print(result)

        nums, target = [3, 3], 6

        result = self.find_indices(nums, target)
        assert result == [0, 1] or [1, 0], err_msg_invalid_indices
        print(result)

    def find_indices(self, nums: list[int], target: int) -> list[int]:
        if (len(nums) < 2):
          return []

        if (len(nums) == 2):
          return [0, 1]

        remaining_map = {}
        for index, num in enumerate(nums):
          complement = target - num
          if complement in remaining_map:
            return [index, remaining_map[complement]]
          remaining_map[num] = index

        return []

# Create an instance of the class
two_sum = TwoSum()
'''
  Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

  Example 1:

  Input: nums = [1,2,3,1]
  Output: true
  Example 2:

  Input: nums = [1,2,3,4]
  Output: false
  Example 3:

  Input: nums = [1,1,1,3,3,4,3,2,4,2]
  Output: true

  Constraints:

  1 <= nums.length <= 105
  -109 <= nums[i] <= 109
'''

class ContainsDuplicate:
  def __init__(self) -> None:
    err_msg_duplicates = "There should be duplicates. Something is wrong!"
    nums = [1, 2, 3, 1]

    result = self.find_duplcates_with_map(nums)
    assert result == True, err_msg_duplicates
    print(result)

    result = self.find_duplcates_with_set(nums)
    assert result == True, err_msg_duplicates
    print(result)

    err_msg_no_duplicates = "There should be duplicates. Something is wrong!"
    nums = [1,2,3,4]

    result = self.find_duplcates_with_map(nums)
    assert result == False, err_msg_no_duplicates
    print(result)

    result = self.find_duplcates_with_set(nums)
    assert result == False, err_msg_no_duplicates
    print(result)

    nums = [1,1,1,3,3,4,3,2,4,2]

    result = self.find_duplcates_with_map(nums)
    assert result == True, err_msg_duplicates
    print(result)

    result = self.find_duplcates_with_set(nums)
    assert result == True, err_msg_duplicates
    print(result)

  def find_duplcates_with_map(self, nums: list) -> bool:
    if not isinstance(nums, list) or len(nums) <= 1:
      return False

    duplicates_map = {}
    for num in nums:
        if num in duplicates_map:
            return True
        duplicates_map[num] = 1

    return False

  def find_duplcates_with_set(self, nums: list) -> bool:
    if not isinstance(nums, list) or len(nums) <= 1:
      return False

    duplicates_set = set()
    for num in nums:
        if num in duplicates_set:
            return True
        else:
          duplicates_set.add(num)

    return False

# Create an instance of the class
duplicate_checker = ContainsDuplicate()

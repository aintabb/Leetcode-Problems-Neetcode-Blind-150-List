'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

# Time Complexity:
# Space Complexity:
class LongestConsecutiveSequence:
    def __init__(self) -> None:
        err_msg_invalid_length = "Provided length is not correct. Something is wrong!"

        nums = [100,4,200,1,3,2]

        result = self.longest_consecutive(nums)
        assert result == 4, err_msg_invalid_length
        print(result)

        nums = [0,3,7,2,5,8,4,6,0,1]

        result = self.longest_consecutive(nums)
        assert result == 9, err_msg_invalid_length
        print(result)

        nums = []

        result = self.longest_consecutive(nums)
        assert result == 0, err_msg_invalid_length
        print(result)


    def longest_consecutive(self, nums: list[int]) -> int:
      len_of_nums = len(nums)
      if len_of_nums == 0:
        return 0

      # Convert input array to a set
      num_set = set(nums)

      longest_seq_len = 0
      for num in nums:
        # If there is no previous number, meaning it is the start of a sequence
        if num - 1 not in num_set:
          # Reset the sequence length
          curr_seq_length = 0
          # Get the next number in the sequence
          while num + curr_seq_length in num_set:
            curr_seq_length += 1
          # Update the longest sequence length
          longest_seq_len = max(curr_seq_length, longest_seq_len)

      return longest_seq_len

# Create an instance of the class
longest_consecutive_sequence = LongestConsecutiveSequence()
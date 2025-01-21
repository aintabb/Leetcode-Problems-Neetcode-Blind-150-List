"""
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
"""


# Time Complexity:  O(N)
# Space Complexity: O(N)
class LongestConsecutiveSequence:
    def __init__(self) -> None:
        err_msg_invalid_length = "Provided length is not correct. Something is wrong!"

        nums = [100, 4, 200, 1, 3, 2]

        result = self.longest_consecutive(nums)
        assert result == 4, err_msg_invalid_length
        print(result)

        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

        result = self.longest_consecutive(nums)
        assert result == 9, err_msg_invalid_length
        print(result)

        nums = []

        result = self.longest_consecutive(nums)
        assert result == 0, err_msg_invalid_length
        print(result)

    def longest_consecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            curr_num = num

            # If there is no previous number, meaning it is the start of a sequence
            if curr_num - 1 not in nums_set:
                curr_streak = 1

                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_streak += 1

                # Update the longest sequence length
                longest = max(longest, curr_streak)

        return longest


# Create an instance of the class
longest_consecutive_sequence = LongestConsecutiveSequence()

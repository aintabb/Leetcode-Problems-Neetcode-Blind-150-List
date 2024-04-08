'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''

# Time Complexity:  O(N)
# Space Complexity: O(N+k)
from collections import defaultdict

class TopKFrequentElements:
  def __init__(self) -> None:
        err_msg_invalid_frequent_elements = "Provided frequent elements are not valid. Something is wrong!"
        nums, k = [1,1,1,2,2,3], 2

        result = self.top_k_frequent(nums, k)
        assert result == [1, 2], err_msg_invalid_frequent_elements
        print(result)

        nums, k = [1], 1
        result = self.top_k_frequent(nums, k)
        assert result == [1], err_msg_invalid_frequent_elements
        print(result)


  def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
    # Step 1: Count the frequency of each number
    count_map = {}
    freq_bucket = [[] for i in range(len(nums) + 1)]

    # Step 2: Group numbers by frequency
    for n in nums:
      count_map[n] = 1 + count_map.get(n, 0)
    for n, c in count_map.items():
      freq_bucket[c].append(n)

    # Step 3: Extract the top k frequent numbers
    top_k_elements = []
    for i in range(len(freq_bucket) - 1, 0, -1):
      for n in freq_bucket[i]:
        top_k_elements.append(n)
        if len(top_k_elements) == k:
          return top_k_elements

    return top_k_elements

top_k_frequent = TopKFrequentElements()
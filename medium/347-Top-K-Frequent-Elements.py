"""
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

"""

# Time Complexity:  O(N) -> with array, O(N*logK) -> with min heap
# Space Complexity: O(N) -> for both
import heapq


class TopKFrequentElements:
    def __init__(self) -> None:
        err_msg_invalid_frequent_elements = (
            "Provided frequent elements are not valid. Something is wrong!"
        )
        nums, k = [1, 1, 1, 2, 2, 3], 2

        result = self.top_k_frequent_with_array(nums, k)
        assert result == [1, 2], err_msg_invalid_frequent_elements
        print(result)

        result = self.top_k_frequent_with_min_heap(nums, k)
        assert result == [1, 2] or [2, 1], err_msg_invalid_frequent_elements
        print(result)

        nums, k = [1], 1

        result = self.top_k_frequent_with_array(nums, k)
        assert result == [1], err_msg_invalid_frequent_elements
        print(result)

        result = self.top_k_frequent_with_min_heap(nums, k)
        assert result == [1], err_msg_invalid_frequent_elements
        print(result)

    def top_k_frequent_with_array(self, nums: list[int], k: int) -> list[int]:
        if not nums or k > len(nums):
            return []

        if len(nums) == 1:
            return [nums[0]]

        # Step 1: Count the frequency of each number
        freq_map = {}
        freq_bucket = [[] for _ in range(len(nums) + 1)]

        # Step 2: Group numbers by frequency
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)
        for num, count in freq_map.items():
            freq_bucket[count].append(num)

        # Step 3: Extract the top k frequent numbers
        top_k_elements = []
        for i in range(len(freq_bucket) - 1, -1, -1):
            for num in freq_bucket[i]:
                top_k_elements.append(num)
                if len(top_k_elements) == k:
                    return top_k_elements

        return top_k_elements

    def top_k_frequent_with_min_heap(self, nums: list[int], k: int) -> list[int]:
        if not nums or k > len(nums):
            return []

        if len(nums) == 1:
            return [nums[0]]

        freq_map = dict()
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)

        min_heap = []
        for num, count in freq_map.items():
            heapq.heappush(min_heap, (count, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        top_k = [num for _, num in min_heap]

        return top_k


top_k_frequent = TopKFrequentElements()

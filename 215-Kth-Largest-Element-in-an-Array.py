"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""


# Time Complexity:  O(N + k*log(N)) -> Max heap, O(N*log(k)) -> Min heap
# Space Complexity: O(1) -> Max heap, O(k) -> Min heap
import heapq

class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums, k = [3,2,1,5,6,4], 2

        result = self.find_kth_largest_max_heap(nums, k)
        assert result == 5, err_msg_invalid_result
        print(result)

        result = self.find_kth_largest_min_heap(nums, k)
        assert result == 5, err_msg_invalid_result
        print(result)

        nums, k = [3,2,3,1,2,4,5,5,6], 4

        result = self.find_kth_largest_max_heap(nums, k)
        assert result == 4, err_msg_invalid_result
        print(result)

        result = self.find_kth_largest_min_heap(nums, k)
        assert result == 4, err_msg_invalid_result
        print(result)


    def find_kth_largest_max_heap(self, nums: list[int], k: int) -> int:
        nums = [-num for num in nums]

        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)

    def find_kth_largest_min_heap(self, nums: list[int], k: int) -> int:
        min_heap = []

        for num in nums:
            if (len(min_heap) < k):
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]

# Create an instance of the class
solution = Solution()
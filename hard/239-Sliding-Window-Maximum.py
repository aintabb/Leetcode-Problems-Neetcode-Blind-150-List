"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

# Time Complexity:  O(n*k) -> for the brute-force where n is the len(nums)
# Space Complexity: O(n - k + 1) -> for the brute-force
from collections import deque
import collections


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3

        result = self.max_sliding_window_brute_force(nums, k)
        assert result == [3, 3, 5, 5, 6, 7], err_msg_invalid_result
        print(result)

        result = self.max_sliding_window_optimal(nums, k)
        assert result == [3, 3, 5, 5, 6, 7], err_msg_invalid_result
        print(result)

        nums, k = [1], 1

        result = self.max_sliding_window_brute_force(nums, k)
        assert result == [1], err_msg_invalid_result
        print(result)

        result = self.max_sliding_window_optimal(nums, k)
        assert result == [1], err_msg_invalid_result
        print(result)

        nums, k = [1, 2, 1, 0, 4, 2, 6], 3

        result = self.max_sliding_window_brute_force(nums, k)
        assert result == [2, 2, 4, 4, 6], err_msg_invalid_result
        print(result)

        result = self.max_sliding_window_optimal(nums, k)
        assert result == [2, 2, 4, 4, 6], err_msg_invalid_result
        print(result)

        nums, k = [9, 11], 2

        result = self.max_sliding_window_brute_force(nums, k)
        assert result == [11], err_msg_invalid_result
        print(result)

        result = self.max_sliding_window_optimal(nums, k)
        assert result == [11], err_msg_invalid_result
        print(result)

    def max_sliding_window_brute_force(self, nums: list[int], k: int) -> list[int]:
        if not nums or k > len(nums):
            return []

        if k <= 1:
            return nums

        len_nums = len(nums)
        max_window = []
        for idx in range(len_nums - k + 1):
            max_val = nums[idx]
            for j in range(idx, idx + k):
                max_val = max(max_val, nums[j])

            max_window.append(max_val)

        return max_window

    def max_sliding_window_optimal(self, nums: list[int], k: int) -> list[int]:
        if not nums or len(nums) <= 1:
            return nums

        len_nums = len(nums)

        max_window = []
        q = (
            collections.deque()
        )  # Deque to store indices of elements in the current window
        left = right = 0

        while right < len_nums:
            # Keep monotonically decreasing queue status
            # Remove indices from the deque's back if they point to smaller elements
            # than the current element, as they cannot be the maximum for any current or future window
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)

            # If the left pointer is out of the range of the deque’s current window, remove it
            # This ensures the deque only contains indices within the current window
            if left > q[0]:
                q.popleft()

            # Once the window reaches the required size, append the maximum to the result
            if (right + 1) >= k:
                # The maximum value for the current window is at the index q[0]
                max_window.append(nums[q[0]])
                left += 1

            right += 1

        return max_window


# Create an instance of the class
solution = Solution()

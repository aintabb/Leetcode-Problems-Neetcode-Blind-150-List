"""
Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:
input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2
output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Constraints:
- [time limit] 5000ms

- [input] array.integer arr
  1 ≤ arr.length ≤ 100

- [input] integer k
  0 ≤ k ≤ 20

[output] array.integer
"""

# Time Complexity:
# Space Complexity:
import heapq

class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        arr, k = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2
        result = self.sort_k_messed_array(arr, k)
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], err_msg_invalid_result
        print(result)

        arr, k = [1, 0], 1
        result = self.sort_k_messed_array(arr, k)
        assert result == [0, 1], err_msg_invalid_result
        print(result)

        arr, k = [1, 0, 3, 2], 1
        result = self.sort_k_messed_array(arr, k)
        assert result == [0, 1, 2, 3], err_msg_invalid_result
        print(result)

        arr, k = [1,0,3,2,4,5,7,6,8], 1
        result = self.sort_k_messed_array(arr, k)
        assert result == [0,1,2,3,4,5,6,7,8], err_msg_invalid_result
        print(result)

        arr, k = [1,4,5,2,3,7,8,6,10,9], 2
        result = self.sort_k_messed_array(arr, k)
        assert result == [1,2,3,4,5,6,7,8,9,10], err_msg_invalid_result
        print(result)


    def sort_k_messed_array(self, arr: list[int], k: int) -> list[int]:
        len_of_arr = len(arr)
        if (len_of_arr == 1 or k == 0):
            return arr

        min_heap = arr[:k+1]
        heapq.heapify(min_heap)

        for i in range(k + 1, len_of_arr):
            arr[i-(k + 1)] = heapq.heappop(min_heap)

            heapq.heappush(min_heap, arr[i])

        for i in range(k + 1):
            arr[len_of_arr - k - 1 + i] = heapq.heappop(min_heap)

        return arr


# Create an instance of the class
solution = Solution()
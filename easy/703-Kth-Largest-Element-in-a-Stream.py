"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


Constraints:

1 <= k <= 104
0 <= nums.length <= 104
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""

# Time Complexity:  O(n) -> for the constructor, O(log(k)) -> for the add method
# Space Complexity: O(k)
import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.min_heap, self.k = nums, k
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

# Test Case
ops = ["KthLargest", "add", "add", "add", "add", "add"]
vals = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
expected_results = [None, 4, 5, 5, 8, 8]

for op, val, expected_result in zip(ops, vals, expected_results):
    if op == "KthLargest":
        kth_largest = KthLargest(val[0], val[1])
    elif op == "add":
        result = kth_largest.add(val[0])

        assert result == expected_result, err_msg_invalid_result
        print(result)

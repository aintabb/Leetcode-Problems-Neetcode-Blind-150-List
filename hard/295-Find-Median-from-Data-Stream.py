"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:
-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.


Follow up:
If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""

# Time Complexity:  O(m*log(N)) for addNum(), O(m) for findMedian()
# Space Complexity: O(N)
## Where m is the number of function calls and N is the length of the array
import heapq


class MedianFinder:

    def __init__(self):
        # max heap keeps the smaller values whereas the min heaps bigger ones
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


ops_dict = {
    "MedianFinder": MedianFinder,
    "addNum": MedianFinder.addNum,
    "findMedian": MedianFinder.findMedian,
}

err_msg_invalid_result = (
    "Provided result is not correct for the given function. Something is wrong!"
)

test_cases = []

# Test Case - 1
ops_one = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
vals_one = [[], [1], [2], [], [3], []]
expected_results_one = [None, None, None, 1.5, None, 2.0]

test_cases.append(list(zip(ops_one, vals_one, expected_results_one)))

# Test Case - 2
ops_two = [
    "MedianFinder",
    "addNum",
    "addNum",
    "addNum",
    "addNum",
    "addNum",
    "addNum",
    "addNum",
    "findMedian",
]
vals_two = [[], [10], [20], [15], [30], [25], [5], [18], []]
expected_results_two = [None, None, None, None, None, None, None, None, 18]

test_cases.append(list(zip(ops_two, vals_two, expected_results_two)))

for test_case in test_cases:
    for op, val, expected_result in test_case:
        if op == "MedianFinder":
            median_finder = MedianFinder()
            # Update the "MedianFinder" instance
            ops_dict[op] = median_finder
            continue

        if op == "addNum":
            ops_dict[op](median_finder, val[0])
            result = None
        else:
            result = ops_dict[op](median_finder)

        assert result == expected_result, err_msg_invalid_result
        print(result)

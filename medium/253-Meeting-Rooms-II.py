"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.



Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:
1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""

import heapq


# Time Complexity:  O(N*logN)
# Space Complexity: O(N)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        intervals = [[0, 30], [5, 10], [15, 20]]

        result = self.min_meeting_rooms(intervals)
        assert result == 2, err_msg_invalid_result
        print(result)

        intervals = [[7, 10], [2, 4]]

        result = self.min_meeting_rooms(intervals)
        assert result == 1, err_msg_invalid_result
        print(result)

        intervals = [[2, 11], [6, 16], [11, 16]]

        result = self.min_meeting_rooms(intervals)
        assert result == 2, err_msg_invalid_result
        print(result)

    def min_meeting_rooms(self, intervals: list[list[int]]) -> int:
        if not intervals or len(intervals) < 1:
            return 0

        if len(intervals) == 1:
            return 1

        intervals.sort(key=lambda x: x[0])

        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, interval[1])

        return len(min_heap)


# Create an instance of the class
solution = Solution()

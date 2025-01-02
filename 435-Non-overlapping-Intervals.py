"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.



Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""


# Time Complexity:  O(N*logN)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]

        result = self.erase_overlap_intervals_sort_by_end(intervals)
        assert result == 1, err_msg_invalid_result
        print(result)

        result = self.erase_overlap_intervals_sort_by_start(intervals)
        assert result == 1, err_msg_invalid_result
        print(result)

        intervals = [[1, 2], [1, 2], [1, 2]]

        result = self.erase_overlap_intervals_sort_by_end(intervals)
        assert result == 2, err_msg_invalid_result
        print(result)

        result = self.erase_overlap_intervals_sort_by_start(intervals)
        assert result == 2, err_msg_invalid_result
        print(result)

        intervals = [[1, 2], [2, 3]]

        result = self.erase_overlap_intervals_sort_by_end(intervals)
        assert result == 0, err_msg_invalid_result
        print(result)

        result = self.erase_overlap_intervals_sort_by_start(intervals)
        assert result == 0, err_msg_invalid_result
        print(result)

    def erase_overlap_intervals_sort_by_end(self, intervals: list[list[int]]) -> int:
        if not intervals or len(intervals) == 1:
            return 0

        intervals.sort(key=lambda i: i[1])
        end = intervals[0][1]
        count = 0

        for idx in range(1, len(intervals)):
            if end > intervals[idx][0]:
                count += 1
            else:
                end = intervals[idx][1]

        return count

    def erase_overlap_intervals_sort_by_start(self, intervals: list[list[int]]) -> int:
        if not intervals or len(intervals) == 1:
            return 0

        # intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
        # intervals = [[1, 2], [1, 3], [2, 3], [3, 4]]
        intervals.sort(key=lambda i: i[0])

        end = intervals[0][1]
        count = 0

        for idx in range(1, len(intervals)):
            if intervals[idx][0] >= end:
                end = intervals[idx][1]
            else:
                count += 1
                end = min(end, intervals[idx][1])

        return count


# Create an instance of the class
solution = Solution()

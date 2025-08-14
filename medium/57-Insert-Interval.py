"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.



Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""


# Time Complexity:  O(N) -> same for both
# Space Complexity: O(1) -> same for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        intervals, new_interval = [[1, 3], [6, 9]], [2, 5]

        result = self.insert_greedy(intervals, new_interval)
        assert result == [[1, 5], [6, 9]], err_msg_invalid_result
        print(result)

        result = self.insert_linear(intervals, new_interval)
        assert result == [[1, 5], [6, 9]], err_msg_invalid_result
        print(result)

        intervals, new_interval = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]

        result = self.insert_greedy(intervals, new_interval)
        assert result == [[1, 2], [3, 10], [12, 16]], err_msg_invalid_result
        print(result)

        result = self.insert_linear(intervals, new_interval)
        assert result == [[1, 2], [3, 10], [12, 16]], err_msg_invalid_result
        print(result)

        intervals = [[1, 5]]
        new_interval = [2, 3]

        result = self.insert_greedy(intervals, new_interval)
        assert result == [[1, 5]], err_msg_invalid_result
        print(result)

        result = self.insert_linear(intervals, new_interval)
        assert result == [[1, 5]], err_msg_invalid_result
        print(result)

    def insert_greedy(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        if not new_interval:
            return intervals

        if not intervals:
            return [new_interval]

        result = []
        for idx, interval in enumerate(intervals):
            if new_interval[1] < interval[0]:
                result.append(new_interval)
                return result + intervals[idx:]
            elif new_interval[0] > interval[1]:
                result.append(interval)
            else:
                new_interval = [
                    min(interval[0], new_interval[0]),
                    max(interval[1], new_interval[1]),
                ]

        result.append(new_interval)
        return result

    def insert_linear(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        if not intervals:
            return [new_interval]

        result = []
        idx = 0
        len_intervals = len(intervals)

        # Add all intervals that come before the newInterval
        while idx < len_intervals and new_interval[0] > intervals[idx][1]:
            result.append(intervals[idx])
            idx += 1

        # Merge all overlapping intervals with new_interval
        while idx < len_intervals and new_interval[1] >= intervals[idx][0]:
            new_interval = [
                min(intervals[idx][0], new_interval[0]),
                max(intervals[idx][1], new_interval[1]),
            ]
            idx += 1

        # Add the newInterval
        result.append(new_interval)

        # Add all remaining intervals
        while idx < len_intervals:
            result.append(intervals[idx])
            idx += 1

        return result


# Create an instance of the class
solution = Solution()

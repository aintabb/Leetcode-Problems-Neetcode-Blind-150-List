"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false

Explanation:
(0,30),(5,10) and (0,30),(15,20) will conflict

Example 2:
Input: intervals = [(5,8),(9,15)]
Output: true
Note:

(0,8),(8,10) is not considered a conflict at 8

Constraints:
0 <= intervals.length <= 100
0 <= intervals[i].start < intervals[i].end <= 1000
"""


# Time Complexity:  O(NlogN)
# Space Complexity: O(1)
class Solution:

    class Interval:
        def __init__(self, start: int, end: int) -> None:
            self.start = start
            self.end = end

    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        intervals = [self.Interval(0, 30), self.Interval(5, 10), self.Interval(15, 20)]
        result = self.can_attend_meetings(intervals)
        assert result == False, err_msg_invalid_result
        print(result)

        intervals = [self.Interval(5, 8), self.Interval(9, 15)]
        result = self.can_attend_meetings(intervals)
        assert result == True, err_msg_invalid_result
        print(result)


    def can_attend_meetings(self, intervals: list[Interval]) -> bool:
        intervals.sort(key = lambda i : i.start)

        for i in range(1, len(intervals)):
            first = intervals[i - 1]
            second = intervals[i]

            if first.end > second.start:
                return False

        return True


# Create an instance of the class
solution = Solution()
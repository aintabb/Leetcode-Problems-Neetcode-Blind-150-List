"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

# Time Complexity:  O(N*logN)
# Space Complexity: O(N)


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

        result = self.merge(intervals)
        assert result == [[1, 6], [8, 10], [15, 18]], err_msg_invalid_result
        print(result)

        intervals = [[1, 4], [4, 5]]

        result = self.merge(intervals)
        assert result == [[1, 5]], err_msg_invalid_result
        print(result)

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        # Sort the intervals by start time
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for idx in range(1, len(intervals)):
            # If the current interval overlaps with the last interval in the result,
            # merge them
            if result[-1][1] >= intervals[idx][0]:
                result[-1][1] = max(result[-1][1], intervals[idx][1])
            else:
                # Otherwise, add the current interval to the result
                result.append(intervals[idx])

        return result


# Create an instance of the class
solution = Solution()

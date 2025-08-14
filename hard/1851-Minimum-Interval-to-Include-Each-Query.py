"""
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.



Example 1:
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.

Example 2:
Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.


Constraints:
1 <= intervals.length <= 105
1 <= queries.length <= 105
intervals[i].length == 2
1 <= lefti <= righti <= 107
1 <= queries[j] <= 107
"""

import heapq
from re import A
from unittest import result


# Time Complexity:  O(N*logN + M*logM)
# Space Complexity: O(N + M)
## N is the number of intervals and M is the number of queries
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        intervals, queries = [[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]

        result = self.minInterval(intervals, queries)
        assert result == [3, 3, 1, 4], err_msg_invalid_result
        print(result)

        intervals, queries = [[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]

        result = self.minInterval(intervals, queries)
        assert result == [2, -1, 4, 6], err_msg_invalid_result
        print(result)

    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        # Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
        if not intervals and not queries:
            return []

        if not intervals:
            return [-1] * len(queries)

        if not queries:
            return [-1] * len(intervals)

        intervals.sort()

        min_heap = []
        size_map = {}
        idx = 0

        for q in sorted(queries):
            while idx < len(intervals) and intervals[idx][0] <= q:
                left, right = intervals[idx]
                heapq.heappush(min_heap, (right - left + 1, right))
                idx += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            size_map[q] = min_heap[0][0] if min_heap else -1

        return [size_map[q] for q in queries]


# Create an instance of the class
solution = Solution()

"""
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

Return the minimum number of intervals required to complete all tasks.


Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.



Constraints:
1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""


# Time Complexity:  O(T*log(T)) -> "T" is the task count
# Space Complexity: O(T)
from collections import deque
import heapq
from typing import Counter


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        tasks, n = ["A","A","A","B","B","B"], 2

        result = self.least_interval(tasks, n)
        assert result == 8, err_msg_invalid_result
        print(result)

        tasks, n = ["A","C","A","B","D","B"], 1

        result = self.least_interval(tasks, n)
        assert result == 6, err_msg_invalid_result
        print(result)

        tasks, n = ["A","A","A", "B","B","B"], 3

        result = self.least_interval(tasks, n)
        assert result == 10, err_msg_invalid_result
        print(result)



    def least_interval(self, tasks: list[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-count for count in counter.values()]
        heapq.heapify(max_heap)

        q = deque() # pair of (freq, idle_time)
        time_spent = 0

        while q or max_heap:
            time_spent += 1

            if max_heap:
                freq = 1 + heapq.heappop(max_heap)

                if freq:
                    q.append([freq, n + time_spent])

            if q and q[0][1] == time_spent:
                heapq.heappush(max_heap, q.popleft()[0])

        return time_spent



# Create an instance of the class
solution = Solution()
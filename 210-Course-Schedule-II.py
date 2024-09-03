"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]


Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""


# Time Complexity:  O(V+E)
# Space Complexity: O(V)

import collections
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        num_courses, prerequisites = 2, [[1,0]]

        result = self.find_order(num_courses, prerequisites)
        assert result == [0,1], err_msg_invalid_result
        print(result)

        num_courses, prerequisites = 4, [[1,0],[2,0],[3,1],[3,2]]

        result = self.find_order(num_courses, prerequisites)
        assert result == [0, 1, 2, 3], err_msg_invalid_result
        print(result)

    def find_order(self, num_courses: int, prerequisites: list[list[int]]) -> list[int]:
        orders = []

        if not num_courses:
            return orders

        graph_map = collections.defaultdict(list)
        for node, edge in prerequisites:
            graph_map[node].append(edge)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * num_courses

        def dfs(node: int) -> bool:
            state = states[node]

            if (state == VISITED):
                return True
            if (state == VISITING):
                return False

            states[node] = VISITING

            for neighbor in graph_map[node]:
                if not dfs(neighbor):
                    return False

            states[node] = VISITED
            orders.append(node)

            return True


        for i in range(num_courses):
            if not dfs(i):
                return []

        return orders


# Create an instance of the class
solution = Solution()
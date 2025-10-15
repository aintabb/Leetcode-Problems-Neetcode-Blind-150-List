"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.



Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.


Constraints:
1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
"""

# Time Complexity:  O(E*logE)
# Space Complexity: O(E)
## Where E is the number of tickets (edges).
import collections


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

        result = self.find_itinerary_hierholzers_algo(tickets)
        assert result == ["JFK", "MUC", "LHR", "SFO", "SJC"], err_msg_invalid_result
        print(result)

        tickets = [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]

        result = self.find_itinerary_hierholzers_algo(tickets)
        assert result == [
            "JFK",
            "ATL",
            "JFK",
            "SFO",
            "ATL",
            "SFO",
        ], err_msg_invalid_result
        print(result)

    def find_itinerary_hierholzers_algo(self, tickets: list[list[str]]) -> list[str]:
        if not tickets:
            return []

        adj_list = collections.defaultdict(list)
        tickets.sort()

        for src, dst in tickets[::-1]:
            adj_list[src].append(dst)

        result = []

        def dfs(src: str) -> None:
            while adj_list[src]:
                dst = adj_list[src].pop()
                dfs(dst)

            result.append(src)

        dfs("JFK")
        return result[::-1]


# Create an instance of the class
solution = Solution()

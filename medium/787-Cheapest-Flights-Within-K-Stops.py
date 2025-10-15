"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.



Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.


Constraints:
1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
"""

# Time Complexity:  O((V+E)*logV) -> for the regular, O(n*k) -> for the modified
# Space Complexity: O(V) -> for the regular, O(n+m) -> for the modified
## Where n is the number of cities, m is the number of flights and k is the number of stops.
import collections
import heapq


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        n = 4
        flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
        src = 0
        dst = 3
        k = 1

        result = self.find_cheapest_price_dijkstra(n, flights, src, dst, k)
        assert result == 700, err_msg_invalid_result
        print(result)

        result = self.find_cheapest_price_dijkstra_modified(n, flights, src, dst, k)
        assert result == 700, err_msg_invalid_result
        print(result)

        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1

        result = self.find_cheapest_price_dijkstra(n, flights, src, dst, k)
        assert result == 200, err_msg_invalid_result
        print(result)

        result = self.find_cheapest_price_dijkstra_modified(n, flights, src, dst, k)
        assert result == 200, err_msg_invalid_result
        print(result)

        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0

        result = self.find_cheapest_price_dijkstra(n, flights, src, dst, k)
        assert result == 500, err_msg_invalid_result
        print(result)

        result = self.find_cheapest_price_dijkstra_modified(n, flights, src, dst, k)
        assert result == 500, err_msg_invalid_result
        print(result)

    def find_cheapest_price_dijkstra(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        if not flights or not flights[0] or n < 1:
            return -1

        # Step 1: Build the graph
        adj_list = collections.defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v, w))

        # Step 2: Priority queue to store (cost, current_city, stops)
        min_heap = [(0, src, 0)]  # (cost, city, stops)

        # Step 3: Dictionary to track the minimum cost to reach each city with a certain number of stops
        min_cost = {(src, 0): 0}  # {(city, stops): cost}

        while min_heap:
            cost, city, stops = heapq.heappop(min_heap)

            # If we have reached the destination and stops are within limit
            if city == dst:
                return cost

            # If stops are within limits, explore neighbors
            if stops <= k:
                for neigh, price in adj_list[city]:
                    new_cost = cost + price
                    dict_key = (neigh, stops + 1)
                    if dict_key not in min_cost or new_cost < min_cost[dict_key]:
                        min_cost[dict_key] = new_cost
                        heapq.heappush(min_heap, (new_cost, neigh, stops + 1))

        # If destination is not reachable within k stops
        return -1

    def find_cheapest_price_dijkstra_modified(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        if not flights or not flights[0] or n < 1:
            return -1

        prices = [float("inf")] * n
        prices[src] = 0

        adj_list = collections.defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append([v, w])  # {from : [to, cost]}

        q = collections.deque([(0, src, 0)])  # (cost, city, stops)

        while q:
            curr_cost, curr_city, stops = q.pop()

            if stops > k:
                continue

            for neigh, cost in adj_list[curr_city]:
                next_cost = curr_cost + cost
                prices[neigh] = next_cost
                q.appendleft((next_cost, neigh, stops + 1))

        return int(prices[dst] if prices[dst] != float("inf") else -1)


# Create an instance of the class
solution = Solution()

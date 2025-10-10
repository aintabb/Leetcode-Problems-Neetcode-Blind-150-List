"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.


Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

Example 3:
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.


Constraints:
The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The Graph is connected and all nodes can be visited starting from the given node.
"""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Time Complexity:  O(V+E)
# Space Complexity: O(V)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        node_one = Node(1)
        node_two = Node(2)
        node_three = Node(3)
        node_four = Node(4)

        node_one.neighbors = [node_two, node_four]
        node_two.neighbors = [node_one, node_three]
        node_three.neighbors = [node_two, node_four]
        node_four.neighbors = [node_one, node_three]

        result = self.clone_graph(node_one)
        assert self.are_graphs_equal(node_one, result) == True, err_msg_invalid_result
        self.print_graph(result)
        print("#######################")

        node_one = Node(1)

        result = self.clone_graph(node_one)
        assert self.are_graphs_equal(node_one, result), err_msg_invalid_result
        self.print_graph(result)
        print("#######################")

        node_one = None

        result = self.clone_graph(node_one)
        assert self.are_graphs_equal(node_one, result), err_msg_invalid_result
        self.print_graph(result)

    def clone_graph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return node

        old_to_new_map = {}

        def clone(node_to_clone: Node) -> Node:
            if node_to_clone in old_to_new_map:
                return old_to_new_map[node_to_clone]

            clone_node = Node(node_to_clone.val)
            old_to_new_map[node_to_clone] = clone_node

            for neigh in node_to_clone.neighbors:
                clone_node.neighbors.append(clone(neigh))

            return clone_node

        return clone(node)

    def are_graphs_equal(
        self, node_one: Optional[Node], node_two: Optional[Node]
    ) -> bool:
        if not node_one and not node_two:
            return True
        if not node_one or not node_two:
            return False

        visited_set = set()

        def dfs(n1: Node, n2: Node) -> bool:
            if n1.val != n2.val:
                return False

            visited_set.add(n1)

            if len(n1.neighbors) != len(n2.neighbors):
                return False

            for i in range(len(n1.neighbors)):
                if n1.neighbors[i] not in visited_set:
                    if not dfs(n1.neighbors[i], n2.neighbors[i]):
                        return False

            return True

        return dfs(node_one, node_two)

    def print_graph(self, node: Optional[Node]) -> None:
        if not node:
            print("Graph is empty!")
            return

        visited_set = set()
        node_stack = [node]

        while node_stack:
            current = node_stack.pop()
            if current in visited_set:
                continue

            visited_set.add(current)
            neighbors_vals = [neighbor.val for neighbor in current.neighbors]
            print(f"Node: {current.val}, Neighbors: {neighbors_vals}")

            for neighbor in current.neighbors:
                if neighbor not in visited_set:
                    node_stack.append(neighbor)


# Create an instance of the class
solution = Solution()

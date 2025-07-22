"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

import sys, os

# Add the parent directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import collections
from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert_no_order


# Time Complexity:  O(N) -> number of nodes, same for both recursion and bfs
# Space Complexity: O(N) -> same for both recursion and bfs
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        root = TreeNode(3)
        insert_no_order(root, 9, 20)
        insert_no_order(root.right, 15, 7)

        result = self.level_order_recursion(root)
        assert result == [[3], [9, 20], [15, 7]], err_msg_invalid_result
        print(result)

        result = self.level_order_bfs(root)
        assert result == [[3], [9, 20], [15, 7]], err_msg_invalid_result
        print(result)

        root = TreeNode(1)

        result = self.level_order_recursion(root)
        assert result == [[1]], err_msg_invalid_result
        print(result)

        result = self.level_order_bfs(root)
        assert result == [[1]], err_msg_invalid_result
        print(result)

        root = None

        result = self.level_order_recursion(root)
        assert result == [], err_msg_invalid_result
        print(result)

        result = self.level_order_recursion(root)
        assert result == [], err_msg_invalid_result
        print(result)

    def level_order_recursion(self, root: Optional[TreeNode]) -> list[list[int]]:
        result = []

        if not root:
            return result

        def traverse(root: Optional[TreeNode], level=0) -> None:
            if not root:
                return

            if len(result) == level:
                result.append([root.val])
            else:
                result[level].append(root.val)

            traverse(root.left, level + 1)
            traverse(root.right, level + 1)

        traverse(root)

        return result

    def level_order_bfs(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        result = []
        node_q = collections.deque([root])

        while node_q:
            len_q = len(node_q)
            curr_level = []

            for _ in range(len_q):
                curr_node = node_q.popleft()
                curr_level.append(curr_node.val)

                if curr_node.left:
                    node_q.append(curr_node.left)
                if curr_node.right:
                    node_q.append(curr_node.right)

            result.append(curr_level)

        return result


# Create an instance of the class
solution = Solution()

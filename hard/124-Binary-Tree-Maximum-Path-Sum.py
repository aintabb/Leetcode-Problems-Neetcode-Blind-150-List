"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.



Example 1:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


Constraints:
The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""

import sys, os

# Add the parent directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert_no_order


# Time Complexity:  O(N)
# Space Complexity: O(H)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        root = TreeNode(1)
        insert_no_order(root, 2, 3)

        result = self.max_path_sum(root)
        assert result == 6, err_msg_invalid_result
        print(result)

        root = TreeNode(-10)
        insert_no_order(root, 9, 20)
        insert_no_order(root.right, 15, 7)

        result = self.max_path_sum(root)
        assert result == 42, err_msg_invalid_result
        print(result)

    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return int(float("-inf"))

        self.max_sum = float("-inf")

        def traverse(curr_node: Optional[TreeNode]) -> int:
            if not curr_node:
                return 0

            left_sum = max(traverse(curr_node.left), 0)
            right_sum = max(traverse(curr_node.right), 0)

            price_new_path = left_sum + right_sum + curr_node.val
            self.max_sum = max(self.max_sum, price_new_path)

            return curr_node.val + max(left_sum, right_sum)

        traverse(root)
        return int(self.max_sum)


# Create an instance of the class
solution = Solution()

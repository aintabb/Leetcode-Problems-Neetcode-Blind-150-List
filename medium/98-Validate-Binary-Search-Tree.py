"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

import sys, os

# Add the parent directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert, insert_no_order


# Time Complexity:  O(N)
# Space Complexity: O(H)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        root = TreeNode(2)
        insert(root, 1)
        insert(root, 3)

        result = self.is_valid_bst(root)
        assert result == True, err_msg_invalid_result
        print(result)

        root = TreeNode(5)
        insert_no_order(root, 1, 4)
        insert_no_order(root.right, 3, 6)

        result = self.is_valid_bst(root)
        assert result == False, err_msg_invalid_result
        print(result)

    def is_valid_bst(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check_validity(
            curr_node: Optional[TreeNode], left_val: float, right_val: float
        ) -> bool:
            if not curr_node:
                return True

            if curr_node.val <= left_val or curr_node.val >= right_val:
                return False

            return check_validity(
                curr_node.left, left_val, curr_node.val
            ) and check_validity(curr_node.right, curr_node.val, right_val)

        return check_validity(root, float("-inf"), float("inf"))


# Create an instance of the class
solution = Solution()

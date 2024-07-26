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

from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert, insert_no_order

# Time Complexity:  O(N)
# Space Complexity: O(N)
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

        def traverse(tree_node: Optional[TreeNode], left_val: float, right_val: float) -> bool:
            # An empty tree is basically BST still
            if not tree_node:
                return True
            if not (tree_node.val > left_val and tree_node.val < right_val):
                return False

            return (
                    traverse(tree_node.left, left_val, tree_node.val) and traverse(tree_node.right, tree_node.val, right_val)
            )

        return traverse(root, -float("inf"), float("inf"))


# Create an instance of the class
solution = Solution()
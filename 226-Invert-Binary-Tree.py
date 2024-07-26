"""
Given the root of a binary tree, invert the tree, and return its root.



Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert, insert_no_order, compare_trees, print_tree

# Time Complexity:  R -> O(N), I -> O(N)
# Space Complexity: R -> O(N), I -> O(N)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        b_tree = TreeNode(4)
        insert(b_tree, 2)
        insert(b_tree, 7)
        insert(b_tree, 1)
        insert(b_tree, 3)
        insert(b_tree, 6)
        insert(b_tree, 9)

        inverted_b_tree = TreeNode(4)
        insert_no_order(inverted_b_tree, 7, 2)
        insert_no_order(inverted_b_tree.left, 9, 6)
        insert_no_order(inverted_b_tree.right, 3, 1)

        result = self.invert_tree_recursive(b_tree)
        assert compare_trees(inverted_b_tree, result) == True, err_msg_invalid_result
        print_tree(result)
        print("#" * 10)

        b_tree = TreeNode(4)
        insert(b_tree, 2)
        insert(b_tree, 7)
        insert(b_tree, 1)
        insert(b_tree, 3)
        insert(b_tree, 6)
        insert(b_tree, 9)

        result = self.invert_tree_iterative(b_tree)
        assert compare_trees(inverted_b_tree, result) == True, err_msg_invalid_result
        print_tree(result)
        print("#" * 10)

        b_tree = TreeNode(2, TreeNode(1), TreeNode(3))
        inverted_b_tree = TreeNode(2, TreeNode(3), TreeNode(1))

        result = self.invert_tree_recursive(b_tree)
        assert compare_trees(inverted_b_tree, result) == True, err_msg_invalid_result
        print_tree(result)
        print("#" * 10)

        b_tree = TreeNode(2, TreeNode(1), TreeNode(3))
        result = self.invert_tree_iterative(b_tree)
        assert compare_trees(inverted_b_tree, result) == True, err_msg_invalid_result
        print_tree(result)

        result = self.invert_tree_recursive(None)
        assert compare_trees(None, result) == True, err_msg_invalid_result
        print_tree(result)
        print("#" * 10)

        result = self.invert_tree_iterative(None)
        assert compare_trees(None, result) == True, err_msg_invalid_result
        print_tree(result)


    def invert_tree_recursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = root.right, root.left

        self.invert_tree_recursive(root.left)
        self.invert_tree_recursive(root.right)

        return root

    def invert_tree_iterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        tree_stack = [root]
        while (tree_stack):
            tree_node = tree_stack.pop()
            if not tree_node:
                continue

            tree_node.left, tree_node.right = tree_node.right, tree_node.left

            tree_stack.append(tree_node.left)
            tree_stack.append(tree_node.right)

        return root


# Create an instance of the class
solution = Solution()
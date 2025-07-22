"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

Constraints:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
"""

import sys, os

# Add the parent directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from typing import Optional
from data_structures.binary_search_tree import (
    TreeNode,
    compare_trees,
    insert_no_order,
    print_tree,
)


# Time Complexity:  O(N)
# Space Complexity: O(N) -> Worst case, O(logN) -> best case when tree is balanced
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        preorder, inorder = [3, 9, 20, 15, 7], [9, 3, 15, 20, 7]
        root = TreeNode(3)
        insert_no_order(root, 9, 20)
        insert_no_order(root.right, 15, 7)

        result = self.build_tree(preorder, inorder)
        assert compare_trees(root, result) == True, err_msg_invalid_result
        print_tree(result)

        preorder, inorder = [-1], [-1]
        root = TreeNode(-1)

        result = self.build_tree(preorder, inorder)
        assert compare_trees(root, result)
        print_tree(result)

    """
    preorder = [3, 9, 20, 15, 7]
                Ro L  R\Ro L  R

    inorder = [9, 3, 15, 20, 7]
               L  Ro R\L Ro  R
    """

    def build_tree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])

        root.left = self.build_tree(
            preorder[1 : root_index + 1], inorder[: root_index + 1]
        )
        root.right = self.build_tree(
            preorder[root_index + 1 :], inorder[root_index + 1 :]
        )

        return root


# Create an instance of the class
solution = Solution()

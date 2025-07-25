"""
Given a binary tree, determine if it is height-balanced.
[A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.]


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true


Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""

import sys, os

# Add the parent directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert_no_order


# Time Complexity:  O(N)
# Space Complexity: O(N) -> Worst Case, Unbalanced Tree, O(log(N)) -> Best\Average, Balanced Tree
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        b_tree = TreeNode(3)
        insert_no_order(b_tree, 9, 20)
        insert_no_order(b_tree.right, 15, 7)

        result = self.is_balanced(b_tree)
        assert result == True, err_msg_invalid_result
        print(result)

        b_tree = TreeNode(1)
        insert_no_order(b_tree, 2, 2)
        insert_no_order(b_tree.left, 3, 3)
        insert_no_order(b_tree.left.left, 4, 4)

        result = self.is_balanced(b_tree)
        assert result == False, err_msg_invalid_result
        print(result)

    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.balanced = True

        def check_balance(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            L = check_balance(node.left)
            R = check_balance(node.right)

            if abs(L - R) > 1:
                self.balanced = False

            return 1 + max(L, R)

        check_balance(root)
        return self.balanced


# Create an instance of the class
solution = Solution()

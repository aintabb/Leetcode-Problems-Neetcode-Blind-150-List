"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1


Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""

import sys, os

# Add the parent directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert, insert_no_order


# Time Complexity:  O(N)
# Space Complexity: O(H) -> Average, O(N) -> Worst Case, Unbalanced Tree, O(log(N)) -> Best, Balanced Tree
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        b_tree = TreeNode(1)
        insert_no_order(b_tree, 2, 3)
        insert_no_order(b_tree.left, 4, 5)

        result = self.diameter_of_binary_tree(b_tree)
        assert result == 3, err_msg_invalid_result
        print(result)

        b_tree = TreeNode(1)
        insert(b_tree, 2)

        result = self.diameter_of_binary_tree(b_tree)
        assert result == 1, err_msg_invalid_result
        print(result)

    """
                    1
                /       \
            2               3
        /       \
    4               5
    """

    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.diameter = 0

        def traverse(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            L = traverse(node.left)
            R = traverse(node.right)

            self.diameter = max(self.diameter, L + R)

            return 1 + max(L, R)

        traverse(root)
        return self.diameter


# Create an instance of the class
solution = Solution()

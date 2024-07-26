"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false


Constraints:
The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""


from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert_no_order


# Time Complexity:  O(P + Q)
# Space Complexity: O(H) -> The height of the tallest/deepest tree
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        b_tree_one = TreeNode(1)
        insert_no_order(b_tree_one, 2, 3)

        b_tree_two = TreeNode(1)
        insert_no_order(b_tree_two, 2, 3)

        result = self.is_same_tree(b_tree_one, b_tree_two)
        assert result == True, err_msg_invalid_result
        print(result)

        b_tree_one = TreeNode(1)
        insert_no_order(b_tree_one, 2, None)

        b_tree_two = TreeNode(1)
        insert_no_order(b_tree_two, None, 2)

        result = self.is_same_tree(b_tree_one, b_tree_two)
        assert result == False, err_msg_invalid_result
        print(result)

        b_tree_one = TreeNode(1)
        insert_no_order(b_tree_one, 2, 1)

        b_tree_two = TreeNode(1)
        insert_no_order(b_tree_two, 1, 2)

        result = self.is_same_tree(b_tree_one, b_tree_two)
        assert result == False, err_msg_invalid_result
        print(result)

        b_tree_one = TreeNode()
        b_tree_two = TreeNode()

        result = self.is_same_tree(b_tree_one, b_tree_two)
        assert result == True, err_msg_invalid_result
        print(result)


    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

# Create an instance of the class
solution = Solution()
"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree 'tree' could also be considered as a subtree of itself.



Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Example 2:
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false


Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""


from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert_no_order


# Time Complexity:  O(N*M)
# Space Complexity: O(N+M)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        root = TreeNode(3)
        insert_no_order(root, 4, 5)
        insert_no_order(root.left, 1, 2)

        sub_root = TreeNode(4)
        insert_no_order(sub_root, 1, 2)

        result = self.is_sub_tree(root, sub_root)
        assert result, err_msg_invalid_result
        print(result)

        insert_no_order(root.left.right, 0, None)

        result = self.is_sub_tree(root, sub_root)
        assert not result, err_msg_invalid_result
        print(result)


    def is_sub_tree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        if not sub_root:
            return True

        if not root:
            return False

        if (self.is_same(root, sub_root)):
            return True

        return (self.is_sub_tree(root.left, sub_root) or self.is_sub_tree(root.right, sub_root))

    def is_same(self, tree_node_one: Optional[TreeNode], tree_node_two: Optional[TreeNode]) -> bool:
        if not tree_node_one and not tree_node_two:
            return True

        if tree_node_one and tree_node_two and tree_node_one.val == tree_node_two.val:
            return (self.is_same(tree_node_one.left, tree_node_two.left)
                    and self.is_same(tree_node_one.right, tree_node_two.right))

        return False

# Create an instance of the class
solution = Solution()
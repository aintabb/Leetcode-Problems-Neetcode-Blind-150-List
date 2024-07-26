"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2


Constraints:
The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""


from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert

# Time Complexity:  O(logN) or O(H)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        root = TreeNode(6)
        insert(root, 2)
        insert(root, 8)
        insert(root, 0)
        insert(root, 4)
        insert(root, 7)
        insert(root, 9)
        insert(root, 3)
        insert(root, 5)

        p = TreeNode(2)
        q = TreeNode(8)

        result = self.lowest_common_ancestor(root, p, q)
        assert result.val == 6, err_msg_invalid_result
        print(result.val)

        q = TreeNode(4)

        result = self.lowest_common_ancestor(root, p, q)
        assert result.val == 2, err_msg_invalid_result
        print(result.val)


    def lowest_common_ancestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        curr_node = root

        while curr_node:
            if curr_node.val < p.val and curr_node.val < q.val:
                curr_node = curr_node.right
            elif curr_node.val > p.val and curr_node.val > q.val:
                curr_node = curr_node.left
            else:
                return curr_node

        return curr_node

# Create an instance of the class
solution = Solution()
"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.



Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.


Constraints:
The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
"""

from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert_no_order

# Time Complexity:  O(N)
# Space Complexity: O(H)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        root = TreeNode(3)
        insert_no_order(root, 1, 4)
        insert_no_order(root.left, 3, None)
        insert_no_order(root.right, 1, 5)

        result = self.good_nodes(root)
        assert result == 4, err_msg_invalid_result
        print(result)

        root = TreeNode(3)
        insert_no_order(root, 3, None)
        insert_no_order(root.left, 4, 2)

        result = self.good_nodes(root)
        assert result == 3, err_msg_invalid_result
        print(result)

        root = TreeNode(1)

        result = self.good_nodes(root)
        assert result == 1, err_msg_invalid_result
        print(result)


    def good_nodes(self, root: Optional[TreeNode]) -> int:

        def traverse(tree_node: Optional[TreeNode], max_val: int) -> int:
            if not tree_node:
                return 0

            result = 1 if (tree_node.val >= max_val) else 0
            max_val = max(max_val, tree_node.val)

            result += traverse(tree_node.left, max_val)
            result += traverse(tree_node.right, max_val)

            return result

        return traverse(root, root.val)


# Create an instance of the class
solution = Solution()
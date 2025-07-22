"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""

import sys, os

# Add the parent directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert


# Time Complexity:  O(N) -> for both
# Space Complexity: O(N) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        root = TreeNode(3)
        insert(root, 1)
        insert(root, 4)
        insert(root.left, 2)

        k = 1

        result = self.kth_smallest_iterative(root, k)
        assert result == 1, err_msg_invalid_result
        print(result)

        result = self.kth_smallest_recursive(root, k)
        assert result == 1, err_msg_invalid_result
        print(result)

        root = TreeNode(5)
        insert(root, 3)
        insert(root, 6)
        insert(root.left, 2)
        insert(root.left, 4)
        insert(root.left.left, 1)

        k = 3

        result = self.kth_smallest_iterative(root, k)
        assert result == 3, err_msg_invalid_result
        print(result)

        result = self.kth_smallest_recursive(root, k)
        assert result == 3, err_msg_invalid_result
        print(result)

    def kth_smallest_iterative(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        n_stack, curr = [], root

        # We are basically traversing the tree in-order
        while curr or n_stack:
            while curr:
                n_stack.append(curr)
                curr = curr.left

            curr = n_stack.pop()
            n += 1

            if n == k:
                return curr.val

            curr = curr.right

    def kth_smallest_recursive(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        values = []

        def in_order_traverse(curr_node: Optional[TreeNode]) -> None:
            if not curr_node:
                return

            in_order_traverse(curr_node.left)
            values.append(curr_node.val)
            in_order_traverse(curr_node.right)

        in_order_traverse(root)
        return values[k - 1]


# Create an instance of the class
solution = Solution()

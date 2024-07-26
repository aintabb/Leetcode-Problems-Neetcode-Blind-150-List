"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

import collections
from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert, insert_no_order

# Time Complexity:  O(N)
# Space Complexity: O(N)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        root = TreeNode(1)
        insert_no_order(root, 2, 3)
        insert_no_order(root.left, None, 5)
        insert_no_order(root.right, None, 4)

        result = self.right_side_view(root)
        assert result == [1, 3, 4], err_msg_invalid_result
        print(result)

        root = TreeNode(1)
        insert(root, 3)

        result = self.right_side_view(root)
        assert result == [1, 3], err_msg_invalid_result
        print(result)

        root = None

        result = self.right_side_view(root)
        assert result == [], err_msg_invalid_result
        print(result)


    def right_side_view(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        if not root:
            return result

        tree_q = collections.deque([root])

        while tree_q:
            n = len(tree_q)

            for _ in range(n):
                curr_node = tree_q.popleft()

                if curr_node.left:
                    tree_q.append(curr_node.left)
                if curr_node.right:
                    tree_q.append(curr_node.right)

            result.append(curr_node.val)

        return result


# Create an instance of the class
solution = Solution()
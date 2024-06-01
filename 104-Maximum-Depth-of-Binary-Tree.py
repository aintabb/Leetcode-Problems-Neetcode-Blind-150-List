"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2


Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""


from collections import deque
from typing import Optional
from data_structures.binary_search_tree import TreeNode, insert, insert_no_order

# Time Complexity:  R -> O(N), BFS -> O(N), DFS -> O(N)
# Space Complexity: R -> O(N) ~ O(H), BFS -> O(W), DFS -> O(N) ~ O(H)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        b_tree = TreeNode(3)
        insert_no_order(b_tree, 9, 20)
        insert_no_order(b_tree.right, 15, 7)

        result = self.max_depth_recursive(b_tree)
        assert result == 3, err_msg_invalid_result
        print(result, end=" - Recursive\n")

        result = self.max_depth_iterative_dfs(b_tree)
        assert result == 3, err_msg_invalid_result
        print(result, end=" - Iterative DFS\n")

        result = self.max_depth_iterative_bfs(b_tree)
        assert result == 3, err_msg_invalid_result
        print(result, end=" - Iterative BFS\n")

        b_tree = TreeNode(1)
        insert(b_tree, 2)

        result = self.max_depth_recursive(b_tree)
        assert result == 2, err_msg_invalid_result
        print(result, end=" - Recursive\n")

        result = self.max_depth_iterative_dfs(b_tree)
        assert result == 2, err_msg_invalid_result
        print(result, end=" - Iterative DFS\n")

        result = self.max_depth_iterative_bfs(b_tree)
        assert result == 2, err_msg_invalid_result
        print(result, end=" - Iterative BFS\n")


    def max_depth_recursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(
            1 + self.max_depth_recursive(root.left),
            1 + self.max_depth_recursive(root.right)
        )

    # DFS
    def max_depth_iterative_dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        tree_stack = []
        tree_stack.append((root, 1))

        max_depth = 1

        while (tree_stack):
            node, depth = tree_stack.pop()

            if (node.left):
                tree_stack.append((node.left, depth + 1))
            if (node.right):
                tree_stack.append((node.right, depth + 1))

            max_depth = max(max_depth, depth)

        return max_depth

    # BFS
    def max_depth_iterative_bfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        tree_queue = deque([root])

        max_depth = 0

        while (tree_queue):
            for i in range(len(tree_queue)):
                node = tree_queue.popleft()
                if node.left:
                    tree_queue.append(node.left)
                if node.right:
                    tree_queue.append(node.right)

            max_depth += 1

        return max_depth


# Create an instance of the class
solution = Solution()
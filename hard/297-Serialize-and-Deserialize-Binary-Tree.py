"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.



Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
"""

import sys, os
from typing import Optional

# Add the parent directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_structures.binary_search_tree import (
    TreeNode,
    compare_trees,
    insert_no_order,
    print_tree,
)


# Time Complexity:  O(N)
# Space Complexity: O(N)
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        def dfs(curr_node: Optional[TreeNode]) -> None:
            if curr_node:
                serialized_vals.append(str(curr_node.val))
                dfs(curr_node.left)
                dfs(curr_node.right)
            else:
                serialized_vals.append("#")

        serialized_vals = []
        dfs(root)
        return " ".join(serialized_vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        def dfs() -> Optional[TreeNode]:
            curr_val = vals_iter.__next__()
            if curr_val == "#":
                return None

            curr_node = TreeNode(int(curr_val))
            curr_node.left = dfs()
            curr_node.right = dfs()

            return curr_node

        vals_iter = iter(data.split())
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

# Create an instances of the class
ser = Codec()
deser = Codec()

# Test Case - 1
root = TreeNode(1, TreeNode(2), TreeNode(3))
insert_no_order(root.right, 4, 5)

expected_tree = TreeNode(1, TreeNode(2), TreeNode(3))
insert_no_order(expected_tree.right, 4, 5)

ans = deser.deserialize(ser.serialize(root))

assert compare_trees(ans, expected_tree) == True, err_msg_invalid_result
print("#" * 10)
print_tree(ans)
print("#" * 10)

# Test Case - 2
root = None

ans = deser.deserialize(ser.serialize(root))
assert ans == None, err_msg_invalid_result
print(ans)


from typing import Optional

class TreeNode:
  def __init__(self, val = 0, left = None, right = None) -> None:
    self.left  = None
    self.right = None
    self.val   = val

def insert(root: Optional[TreeNode], key: int) -> TreeNode:
  if root is None:
    return TreeNode(val = key)
  else:
    if (root.val < key):
      root.right = insert(root.right, key)
    else:
      root.left = insert(root.left, key)

  return root

def insert_no_order(root: Optional[TreeNode], left_key: int | None, right_key: int | None) -> None:
  if root is None:
    return

  root.left  = TreeNode(left_key)
  root.right = TreeNode(right_key)

def inorder_traversal(root):
  if root:
    inorder_traversal(root.left)
    print(root.val)
    inorder_traversal(root.right)


def compare_trees(root_one: Optional[TreeNode], root_two: Optional[TreeNode]) -> bool:
  if not root_one and not root_two:
    return True
  if root_one is None or root_two is None or (root_one.val != root_two.val):
    return False

  return compare_trees(root_one.left, root_two.left) and compare_trees(root_one.right, root_two.right)

# # Example usage:
# root = TreeNode(50)
# root = insert(root, 30)
# root = insert(root, 20)
# root = insert(root, 40)
# root = insert(root, 70)
# root = insert(root, 60)
# root = insert(root, 80)

# """
# Output:
#                 50
#             /        \
#           30          70
#         /     \\     /     \
#       20       40   60       80
# """

# root_dup = TreeNode(50)
# insert_no_order(root_dup, 70, 30)
# insert_no_order(root_dup.left, 20, 40)
# insert_no_order(root_dup.right, 60, 80)

# """
# Output:
#                 50
#             /         \
#           70            30
#         /     \\       /     \
#       80       60    40       20
# """

# inorder_traversal(root)  # Output: 20 30 40 50 60 70 80
# print(compare_trees(root, root_dup)) # Output: False
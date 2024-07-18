"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to
any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has
its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should
point to new nodes in the copied list such that the pointers in the original list and copied list represent the same
list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding
two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of
[val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not
point to any node.

Your code will only be given the head of the original linked list.



Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]


Constraints:
0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""


from typing import cast
from typing import Optional
from data_structures.linked_list import LinkedList, Node

# Time Complexity:  O(N)
# Space Complexity: O(N)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        ll = LinkedList()

        node_seven = ll.append(7, random = None)
        ll.append(13, random = node_seven)
        node_one = Node(1, None, node_seven)
        node_eleven = ll.append(11, random = node_one)
        node_ten = ll.append(10, random = node_eleven)
        node_ten.next = node_one

        result = self.copy_random_list(cast(Node, ll.head))
        assert ll.compare_lists(ll.head, result) == True, err_msg_invalid_result
        ll.print_list(result)

        ll = LinkedList()

        node_one = ll.append(1, random = None)
        node_two = ll.append(2, random = None)
        node_one.next = node_two
        node_one.random = node_two
        node_two.random = node_two

        result = self.copy_random_list(cast(Node, ll.head))
        assert ll.compare_lists(ll.head, result) == True, err_msg_invalid_result
        ll.print_list(ll.head)

        ll = LinkedList()

        node_one = ll.append(3, random = None)
        node_two = ll.append(3, random = node_one)
        node_one.next = node_two
        node_two.random = node_one
        node_three = ll.append(3, random = None)
        node_two.next = node_three

        result = self.copy_random_list(cast(Node, ll.head))
        assert ll.compare_lists(ll.head, result) == True, err_msg_invalid_result
        ll.print_list(ll.head)


    def copy_random_list(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return head

        old_to_copy = { None: None }

        curr = head

        while curr:
            copy = Node(x = curr.val)
            old_to_copy[curr] = copy
            curr = curr.next

        curr = head

        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]

            curr = curr.next

        return old_to_copy[head]



# Create an instance of the class
solution = Solution()
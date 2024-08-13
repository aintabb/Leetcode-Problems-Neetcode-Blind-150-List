"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]


Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
"""


from typing import Optional
from data_structures.linked_list import ListNode, LinkedList

# Time Complexity:  O(N)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)

        n = 2

        result_ll = LinkedList()
        result_ll.append(1)
        result_ll.append(2)
        result_ll.append(3)
        result_ll.append(5)

        result = self.remove_nth_from_end(ll.head, n)
        assert ll.compare_lists(result_ll.head, result) == True, err_msg_invalid_result
        ll.print_list(result)

        ll = LinkedList()
        ll.append(1)

        n = 1

        result_ll = LinkedList()

        result = self.remove_nth_from_end(ll.head, n)
        assert ll.compare_lists(result_ll.head, result), err_msg_invalid_result
        ll.print_list(result)

        ll = LinkedList()
        ll.append(1)
        ll.append(2)

        n = 1

        result_ll = LinkedList()
        result_ll.append(1)

        result = self.remove_nth_from_end(ll.head, n)
        assert ll.compare_lists(result_ll.head, result), err_msg_invalid_result
        ll.print_list(result)


    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy
        right = head

        # Setting up the offset, n.
        while n > 0:
            right = right.next
            n -= 1

        # Moving up the nodes while keep the offset same.
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next

# Create an instance of the class
solution = Solution()
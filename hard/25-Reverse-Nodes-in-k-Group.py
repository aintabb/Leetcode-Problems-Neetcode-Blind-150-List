"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.



Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]


Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000


Follow-up: Can you solve the problem in O(1) extra memory space?
"""

import sys, os

# Add the parent directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from typing import Optional
from data_structures.linked_list import LinkedList, ListNode
from typing import Tuple


# Time Complexity: O(N) where N is the number of nodes in the linked list
# Space Complexity: O(1) as we only use constant extra space
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        l1 = LinkedList()
        l1.append(1)
        l1.append(2)
        l1.append(3)
        l1.append(4)
        l1.append(5)

        result_ll = LinkedList()
        result_ll.append(2)
        result_ll.append(1)
        result_ll.append(4)
        result_ll.append(3)
        result_ll.append(5)

        k = 2

        result = self.reverse_k_group(l1.head, k)
        assert (
            result_ll.compare_lists(result_ll.head, result) == True
        ), err_msg_invalid_result
        result_ll.print_list(result)

        l1 = LinkedList()
        l1.append(1)
        l1.append(2)
        l1.append(3)
        l1.append(4)
        l1.append(5)

        result_ll = LinkedList()
        result_ll.append(3)
        result_ll.append(2)
        result_ll.append(1)
        result_ll.append(4)
        result_ll.append(5)

        k = 3

        result = self.reverse_k_group(l1.head, k)
        assert (
            result_ll.compare_lists(result_ll.head, result) == True
        ), err_msg_invalid_result
        result_ll.print_list(result)

    def reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            group_start = group_prev.next
            group_end = self.get_next(group_start, k - 1)

            if not group_end:
                return dummy.next

            group_next = group_end.next

            rev_head, rev_tail = self.reverse(group_start, k)

            group_prev.next = rev_head
            rev_tail.next = group_next
            group_prev = rev_tail

    def get_next(self, curr, k) -> Optional[ListNode]:
        while curr and k:
            curr = curr.next
            k -= 1

        return curr

    def reverse(self, head, k) -> Tuple[Optional[ListNode], Optional[ListNode]]:
        prev, curr = None, head

        while curr and k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

            k -= 1

        return prev, head


# Create an instance of the class
solution = Solution()

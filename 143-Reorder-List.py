"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]


Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000

# Notes:

# Approach:
- use a pointer to move to the end of curr linked list
- continue until exhausting of the linked list
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

        result_ll = LinkedList()
        result_ll.append(1)
        result_ll.append(4)
        result_ll.append(2)
        result_ll.append(3)

        # Operation will be in-order and modify the given linked list
        self.reorder_list(ll.head)
        assert ll.compare_lists(ll.head, result_ll.head) == True, err_msg_invalid_result
        ll.print_list(ll.head)

        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)
        ll.append(5)

        result_ll = LinkedList()
        result_ll.append(1)
        result_ll.append(5)
        result_ll.append(2)
        result_ll.append(4)
        result_ll.append(3)

        # Operation will be in-order and modify the given linked list
        self.reorder_list(ll.head)
        assert ll.compare_lists(ll.head, result_ll.head) == True, err_msg_invalid_result
        ll.print_list(ll.head)


    """
        Do not return anything, modify head in-place instead.
    """
    def reorder_list(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # Find the middle node
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the other half
        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge halves
        first, second = head, prev

        while second:
            temp_one, temp_two = first.next, second.next
            first.next = second
            second.next = temp_one
            first, second = temp_one, temp_two


# Create an instance of the class
solution = Solution()
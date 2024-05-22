"""
Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []


Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Time Complexity:  I, R -> O(N)
# Space Complexity: I -> O(1), R -> O(N) # Recursive calls on the stack
from typing import Optional
from data_structures.linked_list import ListNode, LinkedList

class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        # Regular list
        ll       = LinkedList()
        head_one = ListNode(1)
        prev_one = head_one

        for i in range(2, 6, 1):
            curr_one      = ListNode(i)
            prev_one.next = curr_one
            prev_one      = curr_one

        copy_head_one    = ll.copy_list(head_one)
        result           = self.reverse_list_iterative(head_one)
        recursive_result = self.reverse_list_recursive(copy_head_one)

        # Reversed list
        head_two = ListNode(5)
        prev_two = head_two

        for i in range(4, 0, -1):
            reverse_curr      = ListNode(i)
            prev_two.next     = reverse_curr
            prev_two          = reverse_curr

        assert ll.compare_lists(result, head_two) == True, err_msg_invalid_result
        assert ll.compare_lists(recursive_result, head_two) == True, err_msg_invalid_result

        ll.print_list(head_one)
        ll.print_list(copy_head_one)

        # Regular list
        head_three      = ListNode(1)
        head_three.next = ListNode(2)

        copy_head_three = ll.copy_list(head_three)

        # Reversed list
        head_four      = ListNode(2)
        head_four.next = ListNode(1)

        result           = self.reverse_list_iterative(head_three)
        recursive_result = self.reverse_list_recursive(copy_head_three)

        assert ll.compare_lists(result, head_four), err_msg_invalid_result
        assert ll.compare_lists(recursive_result, head_four), err_msg_invalid_result

        ll.print_list(result)
        ll.print_list(recursive_result)

        head_one = None

        result           = self.reverse_list_iterative(head_one)
        recursive_result = self.reverse_list_recursive(head_one)

        assert ll.compare_lists(result, head_one), err_msg_invalid_result
        assert ll.compare_lists(recursive_result, head_one), err_msg_invalid_result

        ll.print_list(result)
        ll.print_list(recursive_result)


    def reverse_list_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        curr, prev = head, None

        while (curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def reverse_list_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        def reverse(curr, prev):
            if curr is None:
                return prev
            else:
                temp = curr.next
                curr.next = prev

                return reverse(temp, curr)

        return reverse(head, None)


# Create an instance of the class
solution = Solution()
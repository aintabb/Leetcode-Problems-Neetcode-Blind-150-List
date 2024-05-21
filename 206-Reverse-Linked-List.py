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

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val  = val
        self.next = next



# Time Complexity:  I, R -> O(N)
# Space Complexity: I -> O(1), R -> O(N) # Recursive calls on the stack
from typing import Optional

class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        # Regular list
        head_one = ListNode(1)
        prev_one = head_one

        for i in range(2, 6, 1):
            curr_one      = ListNode(i)
            prev_one.next = curr_one
            prev_one      = curr_one

        copy_head_one    = self.copy_list(head_one)
        result           = self.reverse_list_iterative(head_one)
        recursive_result = self.reverse_list_recursive(copy_head_one)

        # Reversed list
        head_two = ListNode(5)
        prev_two = head_two

        for i in range(4, 0, -1):
            reverse_curr      = ListNode(i)
            prev_two.next     = reverse_curr
            prev_two          = reverse_curr

        assert self.compare_lists(result, head_two) == True, err_msg_invalid_result
        assert self.compare_lists(recursive_result, head_two) == True, err_msg_invalid_result

        self.print_list(head_one)
        self.print_list(copy_head_one)

        # Regular list
        head_three      = ListNode(1)
        head_three.next = ListNode(2)

        copy_head_three = self.copy_list(head_three)

        # Reversed list
        head_four      = ListNode(2)
        head_four.next = ListNode(1)

        result           = self.reverse_list_iterative(head_three)
        recursive_result = self.reverse_list_recursive(copy_head_three)

        assert self.compare_lists(result, head_four), err_msg_invalid_result
        assert self.compare_lists(recursive_result, head_four), err_msg_invalid_result

        self.print_list(result)
        self.print_list(recursive_result)

        head_one = None

        result           = self.reverse_list_iterative(head_one)
        recursive_result = self.reverse_list_recursive(head_one)

        assert self.compare_lists(result, head_one), err_msg_invalid_result
        assert self.compare_lists(recursive_result, head_one), err_msg_invalid_result

        self.print_list(result)
        self.print_list(recursive_result)


    def reverse_list_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr, prev = head, None

        while (curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def reverse_list_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        def reverse(curr, prev) -> Optional[ListNode]:
            if (curr is None):
                return prev
            else:
                temp = curr.next
                curr.next = prev
                return reverse(temp, curr)

        return reverse(head, None)


    def print_list(self, head: Optional[ListNode]) -> None:
        if not head:
            print("None")
            return

        curr = head
        while (curr):
            print(curr.val, end = " -> ")
            curr = curr.next

        print("None")

    def compare_lists(self, head_one: Optional[ListNode], head_two: Optional[ListNode]) -> bool:
        current_one = head_one
        current_two = head_two

        while (current_one and current_two):
            if (current_one.val != current_two.val):
                return False

            current_one = current_one.next
            current_two = current_two.next

        return current_one is None and current_two is None

    def copy_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_head      = ListNode(head.val)
        curr_new_node = new_head
        old_next      = head.next

        while (old_next):
            new_node           = ListNode(old_next.val)
            curr_new_node.next = new_node
            curr_new_node      = new_node
            old_next           = old_next.next

        return new_head


# Create an instance of the class
solution = Solution()
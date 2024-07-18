"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


from typing import Optional, cast
from data_structures.linked_list import ListNode, LinkedList

# Time Complexity:  O(N)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        l1 = LinkedList()
        l1.append(2)
        l1.append(4)
        l1.append(3)

        l2 = LinkedList()
        l2.append(5)
        l2.append(6)
        l2.append(4)

        result_ll = LinkedList()
        result_ll.append(7)
        result_ll.append(0)
        result_ll.append(8)

        result = self.add_two_numbers(cast(ListNode, l1.head), cast(ListNode, l2.head))
        assert result_ll.compare_lists(result_ll.head, result) == True, err_msg_invalid_result
        result_ll.print_list(result)

        l1 = LinkedList()
        l1.append(0)

        l2 = LinkedList()
        l2.append(0)

        result_ll = LinkedList()
        result_ll.append(0)

        result = self.add_two_numbers(cast(ListNode, l1.head), cast(ListNode, l2.head))
        assert result_ll.compare_lists(result_ll.head, result) == True, err_msg_invalid_result
        result_ll.print_list(result)

        l1 = LinkedList()
        l1.append(9)
        l1.append(9)
        l1.append(9)
        l1.append(9)
        l1.append(9)
        l1.append(9)
        l1.append(9)

        l2 = LinkedList()
        l2.append(9)
        l2.append(9)
        l2.append(9)
        l2.append(9)

        result_ll = LinkedList()
        result_ll.append(8)
        result_ll.append(9)
        result_ll.append(9)
        result_ll.append(9)
        result_ll.append(0)
        result_ll.append(0)
        result_ll.append(0)
        result_ll.append(1)

        result = self.add_two_numbers(cast(ListNode, l1.head), cast(ListNode, l2.head))
        assert result_ll.compare_lists(result_ll.head, result) == True, err_msg_invalid_result
        result_ll.print_list(result)


    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            # Calculate digits
            value_one = l1.val if l1 else 0
            value_two = l2.val if l2 else 0

            sum_of_two = value_one + value_two + carry
            carry = sum_of_two // 10
            sum_of_two = sum_of_two % 10

            curr.next = ListNode(sum_of_two)

            # Update pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return dummy.next


# Create an instance of the class
solution = Solution()
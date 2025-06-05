"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]


Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

import sys, os

# Add the parent directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from typing import Optional
from data_structures.linked_list import ListNode, LinkedList


# Time Complexity:  O(N)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        ll_one = LinkedList()
        ll_one.append(1)
        ll_one.append(3)
        ll_one.append(4)

        ll_two = LinkedList()
        ll_two.append(1)
        ll_two.append(2)
        ll_two.append(4)

        ll_result = LinkedList()
        ll_result.append(1)
        ll_result.append(1)
        ll_result.append(2)
        ll_result.append(3)
        ll_result.append(4)
        ll_result.append(4)

        result = self.merge_two_lists(ll_one.head, ll_two.head)
        assert ll_result.compare_lists(result, ll_result.head), err_msg_invalid_result
        ll_result.print_list(result)

        ll_one.head = None
        ll_two.head = None
        ll_result.head = None

        result = self.merge_two_lists(ll_one.head, ll_two.head)
        assert ll_result.compare_lists(result, ll_result.head), err_msg_invalid_result
        ll_result.print_list(result)

        ll_one.head = None
        ll_two.append(0)
        ll_result.append(0)

        result = self.merge_two_lists(ll_one.head, ll_two.head)
        assert ll_result.compare_lists(result, ll_result.head), err_msg_invalid_result
        ll_result.print_list(result)

    def merge_two_lists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        head = ListNode()
        curr = head

        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next

            curr = curr.next

        while list1:
            curr.next = list1
            list1 = list1.next
            curr = curr.next

        while list2:
            curr.next = list2
            list2 = list2.next
            curr = curr.next

        return head.next


# Create an instance of the class
solution = Solution()

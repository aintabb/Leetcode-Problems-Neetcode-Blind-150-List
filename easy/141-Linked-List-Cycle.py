"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.


Follow up: Can you solve it using O(1) (i.e. constant) memory?
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

        ll = LinkedList()
        ll.append(3)
        ll.append(2)
        ll.append(0)
        ll.append(-4)

        pos = 1

        temp = ll.head
        while temp.val != -4:
            temp = temp.next

        temp.next = ll.head.next

        result = self.has_cycle(ll.head)
        assert result, err_msg_invalid_result
        print(result)

        ll = LinkedList()
        ll.append(1)
        ll.append(2)

        ll.head.next.next = ll.head

        pos = 0

        result = self.has_cycle(ll.head)
        assert result, err_msg_invalid_result
        print(result)

        ll = LinkedList()
        ll.append(1)

        pos = -1

        result = self.has_cycle(ll.head)
        assert result == False, err_msg_invalid_result
        print(result)

    def has_cycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        # Floyd's Tortoise & Hare Algorithm
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False


# Create an instance of the class
solution = Solution()

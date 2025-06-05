"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.


Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []


Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""

import sys, os

# Add the parent directory to the Python module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from typing import Optional, cast
from data_structures.linked_list import LinkedList, ListNode
import heapq


# Time Complexity:  O(N*log(k)) -> where 'N' is the total number of nodes and 'k' is the number of linked lists
# Space Complexity: O(k)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        l1 = LinkedList()
        l1.append(1)
        l1.append(4)
        l1.append(5)

        l2 = LinkedList()
        l2.append(1)
        l2.append(3)
        l2.append(4)

        l3 = LinkedList()
        l3.append(2)
        l3.append(6)

        lists = [l1.head, l2.head, l3.head]

        result_ll = LinkedList()
        result_ll.append(1)
        result_ll.append(1)
        result_ll.append(2)
        result_ll.append(3)
        result_ll.append(4)
        result_ll.append(4)
        result_ll.append(5)
        result_ll.append(6)

        result = self.merge_k_lists(cast(list, lists))
        assert (
            result_ll.compare_lists(result_ll.head, result) == True
        ), err_msg_invalid_result
        result_ll.print_list(result)

        lists = []

        result = self.merge_k_lists(cast(list, lists))
        assert result == None, err_msg_invalid_result
        print(result)

        lists = [[]]

        result = self.merge_k_lists(cast(list, lists))
        assert result == None, err_msg_invalid_result
        print(result)

    def merge_k_lists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        # Min-heap to store (value, index, node)
        min_heap = []

        # Initialize the heap with the head of each linked list
        for idx, node in enumerate(lists):
            if node:
                # Push (value, idx, node) to avoid comparison errors
                heapq.heappush(min_heap, (node.val, idx, node))

        dummy = ListNode()
        curr = dummy

        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

        return dummy.next


# Create an instance of the class
solution = Solution()

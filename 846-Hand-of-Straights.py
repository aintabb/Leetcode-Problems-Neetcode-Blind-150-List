"""
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.



Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.



Constraints:
1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length


Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""

# Time Complexity:  O(N**2) -> for both memo and dp, O(N) -> for the greedy
# Space Complexity: O(N) -> for both memo and dp, O(1) -> for the greedy

import collections


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        hand, group_size = [1, 2, 3, 6, 2, 3, 4, 7, 8], 3

        result = self.is_n_straight_hand(hand, group_size)
        assert result == True, err_msg_invalid_result
        print(result)

        hand, group_size = [1, 2, 3, 4, 5], 4

        result = self.is_n_straight_hand(hand, group_size)
        assert result == False, err_msg_invalid_result
        print(result)

        hand, group_size = [8, 10, 12], 3

        result = self.is_n_straight_hand(hand, group_size)
        assert result == False, err_msg_invalid_result
        print(result)

    # There are many ways to solve this. I will use sorting only
    def is_n_straight_hand(self, hand: list[int], group_size: int) -> bool:
        if len(hand) % group_size != 0:
            return False

        hand.sort()
        freq_map = collections.defaultdict(int)

        for num in hand:
            freq_map[num] = 1 + freq_map.get(num, 0)

        for num in hand:
            if freq_map[num]:
                for next_num in range(num, num + group_size):
                    if not freq_map[next_num]:
                        return False
                    freq_map[next_num] -= 1

        return True


# Create an instance of the class
solution = Solution()

"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.



Example 1:
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:
Input: s = "eccbbbbdec"
Output: [10]


Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
"""

# Time Complexity:  O(n)
# Space Complexity: O(m)
## Where 'n' is the length of the string 's' and 'm' is the number of unique characters in 's'


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s = "ababcbacadefegdehijhklij"

        result = self.partition_labels(s)
        assert result == [9, 7, 8], err_msg_invalid_result
        print(result)

        s = "eccbbbbdec"

        result = self.partition_labels(s)
        assert result == [10], err_msg_invalid_result
        print(result)

    def partition_labels(self, s: str) -> list[int]:
        if not s:
            return [0]

        if len(s) == 1:
            return [1]

        last_index_map = {}
        for idx, ch in enumerate(s):
            last_index_map[ch] = idx

        end = size = 0
        result = []

        for idx, ch in enumerate(s):
            size += 1
            end = max(end, last_index_map[ch])

            if idx == end:
                result.append(size)
                size = 0

        return result


# Create an instance of the class
solution = Solution()

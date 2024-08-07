"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.




Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]


Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""


# Time Complexity:  O(4^N)
# Space Complexity: O(N*(4^N))
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        digits = "23"

        result = self.letter_combinations(digits)
        assert result == ["ad","ae","af","bd","be","bf","cd","ce","cf"], err_msg_invalid_result
        print(result)

        digits = ""

        result = self.letter_combinations(digits)
        assert result == [], err_msg_invalid_result
        print(result)

        digits = "2"

        result = self.letter_combinations(digits)
        assert result == ["a", "b", "c"], err_msg_invalid_result
        print(result)


    def letter_combinations(self, digits: str) -> list[str]:
        result = []
        n = len(digits)

        digit_to_letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(idx: int, curr_str: str) -> None:
            if (len(curr_str) == n):
                result.append(curr_str)
                return

            for ch in digit_to_letter_map[digits[idx]]:
                backtrack(idx + 1, curr_str + ch)


        if digits:
            backtrack(0, "")

        return result


# Create an instance of the class
solution = Solution()
"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "(*)"
Output: true

Example 3:
Input: s = "(*))"
Output: true


Constraints:
1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""

# Time Complexity:  O(N) -> for both
# Space Complexity: O(N) -> for the stack, O(1) -> for the greedy


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        s = "()"

        result = self.check_valid_string_stack(s)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.check_valid_string_greedy(s)
        assert result == True, err_msg_invalid_result
        print(result)

        s = "(*)"

        result = self.check_valid_string_stack(s)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.check_valid_string_greedy(s)
        assert result == True, err_msg_invalid_result
        print(result)

        s = "(*))"

        result = self.check_valid_string_stack(s)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.check_valid_string_greedy(s)
        assert result == True, err_msg_invalid_result
        print(result)

        s = "**"

        result = self.check_valid_string_stack(s)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.check_valid_string_greedy(s)
        assert result == True, err_msg_invalid_result
        print(result)

        s = "())*"

        result = self.check_valid_string_stack(s)
        assert result == False, err_msg_invalid_result
        print(result)

        result = self.check_valid_string_greedy(s)
        assert result == False, err_msg_invalid_result
        print(result)

        s = "("

        result = self.check_valid_string_stack(s)
        assert result == False, err_msg_invalid_result
        print(result)

        result = self.check_valid_string_greedy(s)
        assert result == False, err_msg_invalid_result
        print(result)

    def check_valid_string_stack(self, s: str) -> bool:
        if not s:
            return False

        left_p_stack = []
        star_stack = []

        for idx, ch in enumerate(s):
            if ch == "(":
                left_p_stack.append(idx)
            elif ch == "*":
                star_stack.append(idx)
            else:
                if not left_p_stack and not star_stack:
                    return False
                if left_p_stack:
                    left_p_stack.pop()
                else:
                    star_stack.pop()

        while left_p_stack and star_stack:
            if left_p_stack.pop() > star_stack.pop():
                return False

        return len(left_p_stack) == 0

    def check_valid_string_greedy(self, s: str) -> bool:
        if not s:
            return False
        # We use two variables lo and hi to keep track of the minimum and
        # maximum possible number of open parentheses.
        low = high = 0
        for ch in s:
            # If the character is '(', we increment both lo and hi by 1.
            # If the character is ')', we decrement both lo and hi by 1.
            # If the character is '', we increment hi by 1 (because '' can be treated as a '(') and
            # decrement lo by 1 (because '*' can be treated as a ')')
            low += 1 if ch == "(" else -1
            high += 1 if ch != ")" else -1

            # If hi ever becomes negative, it means that we have more ')' than '(' and '*' combined,
            # so we return False.
            if high < 0:
                return False

            # we also make sure that lo does not go below 0, because we cannot have a negative number of
            # open parentheses.
            low = max(low, 0)

        # we return True if lo is 0, which means that we have exactly the right number of '(' and ')' to match
        # each other.
        return low == 0


# Create an instance of the class
solution = Solution()

"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:
Input: n = 19
Output: true
Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1

Example 2:
Input: n = 2
Output: false


Constraints:
1 <= n <= 231 - 1
"""


# Time Complexity:  O(logN) -> for both
# Space Complexity: O(logN) -> for is_happy_with_set, O(1) -> for is_happy_with_floyds_cycle_algorithm
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        n = 19

        result = self.is_happy_with_set(n)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.is_happy_with_floyds_cycle_algorithm(n)
        assert result == True, err_msg_invalid_result
        print(result)

        n = 2

        result = self.is_happy_with_set(n)
        assert result == False, err_msg_invalid_result
        print(result)

        result = self.is_happy_with_floyds_cycle_algorithm(n)
        assert result == False, err_msg_invalid_result
        print(result)

        n = 6703

        result = self.is_happy_with_set(n)
        assert result == True, err_msg_invalid_result
        print(result)

        result = self.is_happy_with_floyds_cycle_algorithm(n)
        assert result == True, err_msg_invalid_result
        print(result)


    def is_happy_with_set(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            visited.add(n)

            n = self.sum_of_digits(n)

            if n == 1:
                return True

        return False

    def sum_of_digits(self, n: int) -> int:
        output = 0

        while n:
            output += (n % 10) ** 2
            n = n // 10

        return output

    def is_happy_with_floyds_cycle_algorithm(self, n: int) -> bool:
        slow, fast = n, self.sum_of_digits(n)

        while (slow != fast):
            slow = self.sum_of_digits(slow)
            fast = self.sum_of_digits(fast)
            fast = self.sum_of_digits(fast)

        return True if fast == 1 else False

# Create an instance of the class
solution = Solution()
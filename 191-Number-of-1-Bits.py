"""
Write a function that takes the binary representation of a positive integer and returns the number of
set bits it has (also known as the Hamming weight).



Example 1:
Input: n = 11
Output: 3

Explanation:
The input binary string 1011 has a total of three set bits.


Example 2:
Input: n = 128
Output: 1

Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30

Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.



Constraints:
1 <= n <= 231 - 1


Follow up: If this function is called many times, how would you optimize it?
"""


# Time Complexity:  O(k) or O(logN) -> for both (k is number of bits)
# Space Complexity: O(1) -> for both
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        n = 11

        result = self.hamming_weight_shifting(n)
        assert result == 3, err_msg_invalid_result
        print(result)

        result = self.hamming_weight_subtraction_with_and_operator(n)
        assert result == 3, err_msg_invalid_result
        print(result)

        n = 128

        result = self.hamming_weight_shifting(n)
        assert result == 1, err_msg_invalid_result
        print(result)

        result = self.hamming_weight_subtraction_with_and_operator(n)
        assert result == 1, err_msg_invalid_result
        print(result)

        n = 2147483645

        result = self.hamming_weight_shifting(n)
        assert result == 30, err_msg_invalid_result
        print(result)

        result = self.hamming_weight_subtraction_with_and_operator(n)
        assert result == 30, err_msg_invalid_result
        print(result)


    def hamming_weight_shifting(self, n: int) -> int:
        result = 0

        while n:
            result += n % 2
            n = n >> 1

        return result


    def hamming_weight_subtraction_with_and_operator(self, n: int) -> int:
        result = 0

        while n:
            n &= n - 1
            result += 1

        return result


# Create an instance of the class
solution = Solution()
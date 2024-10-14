"""
Reverse bits of a given 32 bits unsigned integer.

Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.


Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.


Constraints:
The input must be a binary string of length 32


Follow up: If this function is called many times, how would you optimize it?
"""


# Time Complexity:  O(1)
# Space Complexity: O(1)
class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        n = int('0b00000010100101000001111010011100', 2)

        result = self.reverse_bits(n)
        assert result == 964176192, err_msg_invalid_result
        print(result)

        n = int('0b11111111111111111111111111111101', 2)
        result = self.reverse_bits(n)
        assert result == 3221225471, err_msg_invalid_result
        print(result)


    def reverse_bits(self, n: int) -> int:
        result = 0

        for i in range(32):
            '''
            Shifts the bits of n to the right by i positions, effectively isolating the bit at the i-th position.
            Uses the bitwise AND operation with 1 to keep only the least significant bit (i.e., the bit at the i-th position) and discards all other bits. This gives us the i-th bit of n.
            '''
            bit_to_reverse = (n >> i) & 1
            # Shifts the bit_to_reverse left by (31 - i) positions. This places the i-th bit of n in its reversed position.
            result |= (bit_to_reverse << (31 - i))

        return result


# Create an instance of the class
solution = Solution()
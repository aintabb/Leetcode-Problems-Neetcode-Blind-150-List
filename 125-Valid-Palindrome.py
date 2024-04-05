'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

# Time Complexity:  O(N)
# Space Complexity: O(N)
class ValidPalindrome:
    def __init__(self) -> None:
        err_msg_invalid_palindrome = "Provided string is not a palindrome. Something is wrong!"

        s = "A man, a plan, a canal: Panama"

        result = self.valid_palindrome_with_memory(s)
        assert result == True, err_msg_invalid_palindrome
        print(result)

        s = "race a car"

        result = self.valid_palindrome_with_memory(s)
        assert result == False, err_msg_invalid_palindrome
        print(result)

        s = " "

        result = self.valid_palindrome_with_memory(s)
        assert result == True, err_msg_invalid_palindrome
        print(result)

        s = ".,"
        result = self.valid_palindrome_with_memory(s)
        assert result == True, err_msg_invalid_palindrome
        print(result)

        s = "a."
        result = self.valid_palindrome_with_memory(s)
        assert result == True, err_msg_invalid_palindrome
        print(result)

        s = ".aa"
        result = self.valid_palindrome_with_memory(s)
        assert result == True, err_msg_invalid_palindrome
        print(result)


    """
      A function to check if a given string is a valid palindrome without using extra memory.

      Parameters:
          self (class): The class instance.
          s (str): The input string to be checked for palindrome validity.

      Returns:
          bool: True if the input string is a valid palindrome, False otherwise.
    """
    def valid_palindrome_no_memory(self, s: str) -> bool:
      len_of_s = len(s)
      if (len_of_s == 1):
        return True

      s = s.lower()
      l, r = 0, len_of_s - 1
      while l < r:
        while l < r and not s[l].isalnum():
          l += 1
        while r > l and not s[r].isalnum():
          r -= 1

        if (s[l] != s[r]):
          return False

        l += 1
        r -= 1

      return True



    """
      A function that checks if a given string is a valid palindrome with memory.

      Parameters:
          self (class): The class instance.
          s (str): The input string to be checked for palindrome validity.

      Returns:
          bool: True if the input string is a valid palindrome, False otherwise.
    """
    def valid_palindrome_with_memory(self, s: str) -> bool:
      new_str = ""
      s = s.lower()
      for ch in s:
        if (ch.isalnum()):
          new_str += ch

      return new_str == new_str[::-1]

# Create an instance of the class
valid_palindrome = ValidPalindrome()
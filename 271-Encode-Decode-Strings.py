'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]

Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

'''

# Time Complexity:  O(N)
# Space Complexity: O(N)
class EncodeDecodeStrings:
    def __init__(self) -> None:
        err_msg_invalid_string = "Provided string is not correct. Something is wrong!"
        strs = ["neet","code","love","you"]

        result = self.decode(self.encode(strs))

        assert result == strs, err_msg_invalid_string
        print(result)

        strs = ["we","say",":","yes"]

        result = self.decode(self.encode(strs))
        assert result == ["we","say",":","yes"], err_msg_invalid_string
        print(result)

        strs = [""]

        result = self.decode(self.encode(strs))
        assert result == [""], err_msg_invalid_string
        print(result)

        strs = []

        result = self.decode(self.encode(strs))
        assert result == [], err_msg_invalid_string
        print(result)


    """
    Encode a list of strings into a single encoded string.

    :param strs: A list of strings to be encoded.
    :return: A single encoded string representing the input list of strings.
    """
    def encode(self, strs: list[str]) -> str:
      encoded_str = ""
      for s in strs:
        encoded_str += str(len(s)) + "#" + s

      return encoded_str

    """
    Decode the given string by extracting substrings based on the '#' delimiter.

    Args:
        s (str): The input string to be decoded.

    Returns:
        list[str]: The list of decoded substrings.
    """
    def decode(self, s: str) -> list[str]:
      decoded_str, i = [], 0
      len_of_s = len(s)

      while (i < len_of_s):
        j = i
        while (s[j] != '#'):
          j += 1

        len_of_curr_str = int(s[i:j])
        decoded_str.append(s[j + 1: j + 1 + len_of_curr_str])
        i = j + 1 + len_of_curr_str

      return decoded_str

# Create an instance of the class
encode_decode_strings = EncodeDecodeStrings()
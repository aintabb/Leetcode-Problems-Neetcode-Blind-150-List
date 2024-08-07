"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""

class TrieNode :
  def __init__(self) -> None:
    self.end_word = False
    self.children = [None] * 26

class Trie:
  def __init__(self) -> None:
    self.root = TrieNode()

  # Time Complexity:  O(N)
  # Space Complexity: O(N)
  def insert(self, word: str) -> None:
    curr = self.root

    for ch in word:
      ch_index = ord(ch) - ord("a")

      if (curr.children[ch_index] == None):
        curr.children[ch_index] = TrieNode()

      curr = curr.children[ch_index]

    curr.end_word = True

  # Time Complexity:  O(N)
  # Space Complexity: O(1)
  def search(self, word: str) -> bool:
    curr = self.root

    for ch in word:
      ch_index = ord(ch) - ord("a")

      if (curr.children[ch_index] == None):
        return False

      curr = curr.children[ch_index]

    return curr.end_word

  # Time Complexity:  O(N)
  # Space Complexity: O(1)
  def startsWith(self, prefix: str) -> bool:
    curr = self.root

    for ch in prefix:
      ch_index = ord(ch) - ord("a")

      if (curr.children[ch_index] == None):
        return False

      curr = curr.children[ch_index]

    return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

ops_dict = {
  "Trie": Trie,
  "insert": Trie.insert,
  "search": Trie.search,
  "startsWith": Trie.startsWith
}

err_msg_invalid_result = "Provided result is not correct for the given function. Something is wrong!"

test_cases  = []

# Test Case - 1
ops_one   = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
vals_one  = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
expected_results = [None, None, True, False, True, None, True]

# Not a clever way to test this, but it works for our purposes
for op, val, expected_result in zip(ops_one, vals_one, expected_results):
    if op == "Trie":
      trie = Trie()
      # Update the "trie" instance
      ops_dict[op] = trie
      continue

    result = ops_dict[op](trie, val[0])

    assert result == expected_result, err_msg_invalid_result
    print(result)

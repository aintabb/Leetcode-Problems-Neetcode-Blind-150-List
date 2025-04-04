"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:
1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""


class TrieNode:
    def __init__(self) -> None:
        self.end_word = False
        self.children = {}


class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

        curr.end_word = True

    def search(self, word: str) -> bool:
        def dfs(j: int, root: TrieNode) -> bool:
            curr = root

            for i in range(j, len(word)):
                ch = word[i]

                if ch == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True

                    return False
                else:
                    if ch not in curr.children:
                        return False

                    curr = curr.children[ch]

            return curr.end_word

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

ops_dict = {
    "WordDictionary": WordDictionary,
    "addWord": WordDictionary.addWord,
    "search": WordDictionary.search,
}

err_msg_invalid_result = (
    "Provided result is not correct for the given function. Something is wrong!"
)

test_cases = []

# Test Case - 1
ops_one = [
    "WordDictionary",
    "addWord",
    "addWord",
    "addWord",
    "search",
    "search",
    "search",
    "search",
]
vals_one = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
expected_results_one = [None, None, None, None, False, True, True, True]

test_cases.append(list(zip(ops_one, vals_one, expected_results_one)))

# Test Case - 2
ops_two = [
    "WordDictionary",
    "addWord",
    "addWord",
    "search",
    "search",
    "search",
    "search",
    "search",
    "search",
]
vals_two = [[], ["a"], ["a"], ["."], ["a"], ["aa"], ["a"], [".a"], ["a."]]
expected_results_two = [None, None, None, True, True, False, True, False, False]

test_cases.append(list(zip(ops_two, vals_two, expected_results_two)))


for test_case in test_cases:
    # Not a clever way to test this, but it works for our purposes
    for op, val, expected_result in test_case:
        if op == "WordDictionary":
            trie = WordDictionary()
            # Update the "trie" instance
            ops_dict[op] = trie
            continue

        result = ops_dict[op](trie, val[0])

        assert result == expected_result, err_msg_invalid_result
        print(result)

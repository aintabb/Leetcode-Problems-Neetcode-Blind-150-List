"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.



Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

from collections import OrderedDict


class Node:
    # Doubly-linked list
    def __init__(self, key: int, val: int) -> None:
        self.key, self.val = key, val
        self.prev = self.next = None

# Time Complexity:  O(1) -> for both get and put methods
# Space Complexity: O(capacity)
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = { } # { key: Node }

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left


    # Remove a node
    def remove(self, node: Node) -> None:
        node_prev, node_next = node.prev, node.next

        node_prev.next, node_next.prev = node_next, node_prev

    # Insert a new node to the right
    # Make it MRU, LRU -> ....... -> MRU
    def insert(self, node: Node) -> None:
        node_prev, node_next = self.right.prev, self.right
        node_prev.next = node_next.prev = node
        node.prev, node.next = node_prev, node_next


    def get(self, key: int) -> int:
        if key in self.cache:
            # Remove and insert so that it becomes MRU.
            # We are inserting most recently used nodes to the right
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if (len(self.cache) > self.capacity):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Create an instance of the class
lru_cache = LRUCache(0)

err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

# Test Case
ops = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
vals = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

expected_results = [None, None, None, 1, None, -1, None, -1, 3, 4]

for op, val, expected_result in zip(ops, vals, expected_results):
    if op == "LRUCache":
        lru_cache = LRUCache(int(val[0]))
    else:
        if (op == "put"):
            result = lru_cache.put(int(val[0]), int(val[1]))
        else:
            result = lru_cache.get(int(val[0]))

        assert result == expected_result, err_msg_invalid_result
        print(result)
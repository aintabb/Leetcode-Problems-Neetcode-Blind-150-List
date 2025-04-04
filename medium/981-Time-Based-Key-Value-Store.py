"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


Example 1:
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"


Constraints:
1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.
"""


# Time Complexity: O(1) -> for set(), O(logN) -> for get()
# Space Complexity: O(N) -> for the overall structure, O(1) -> for set() and get()
class TimeMap:
    def __init__(self) -> None:
        self.store_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store_map:
            self.store_map[key] = []

        self.store_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store_map:
            return ""

        pairs = self.store_map[key]
        result = ""
        left, right = 0, len(pairs) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if pairs[mid][1] <= timestamp:
                result = pairs[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# Create an instance of the class
time_map = TimeMap()

err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

test_cases = []

# Test Case - 1
ops = ["TimeMap", "set", "get", "get", "set", "get", "get"]
vals = [
    [],
    ["foo", "bar", 1],
    ["foo", 1],
    ["foo", 3],
    ["foo", "bar2", 4],
    ["foo", 4],
    ["foo", 5],
]

expected_results = [None, None, "bar", "bar", None, "bar2", "bar2"]
test_cases.append(list(zip(ops, vals, expected_results)))

# Test Case - 2
ops = ["TimeMap", "set", "set", "get", "get", "get", "get", "get"]
vals = [
    [],
    ["love", "high", 10],
    ["love", "low", 20],
    ["love", 5],
    ["love", 10],
    ["love", 15],
    ["love", 20],
    ["love", 25],
]

expected_results = [None, None, None, "", "high", "high", "low", "low"]
test_cases.append(list(zip(ops, vals, expected_results)))

for test_case in test_cases:
    for op, val, expected_result in test_case:
        if op == "TimeMap":
            time_map = TimeMap()
        else:
            if op == "set":
                result = time_map.set(val[0], val[1], val[2])
            else:
                result = time_map.get(val[0], val[1])

            assert result == expected_result, err_msg_invalid_result
            print(result)

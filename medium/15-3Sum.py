"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []

Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

# Time Complexity:  O(N^2)
# Space Complexity: O(1)


class ThreeSum:
    def __init__(self) -> None:
        err_msg_invalid_numbers = (
            "Provided numbers does not add up to the sum. Something is wrong!"
        )

        numbers = [-1, 0, 1, 2, -1, -4]

        result = self.three_sum(numbers)
        assert result == [[-1, -1, 2], [-1, 0, 1]], err_msg_invalid_numbers
        print(result)

        numbers = [0, 1, 1]

        result = self.three_sum(numbers)
        assert result == [], err_msg_invalid_numbers
        print(result)

        numbers = [0, 0, 0]

        result = self.three_sum(numbers)
        assert result == [[0, 0, 0]], err_msg_invalid_numbers
        print(result)

        numbers = [0, 0, 0, 0]

        result = self.three_sum(numbers)
        assert result == [[0, 0, 0]], err_msg_invalid_numbers
        print(result)

        numbers = [1, -1, -1, 0]

        result = self.three_sum(numbers)
        assert result == [[-1, 0, 1]], err_msg_invalid_numbers
        print(result)

    def three_sum(self, nums: list[int]) -> list[list[int]]:
        result = []
        # Makes our job easier
        nums.sort()

        for idx in range(len(nums)):
            # Just to prevent duplicates triplets
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left, right = idx + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[idx] + nums[left] + nums[right]

                if curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    result.append([nums[idx], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result


# Create an instance of the class
three_sum = ThreeSum()

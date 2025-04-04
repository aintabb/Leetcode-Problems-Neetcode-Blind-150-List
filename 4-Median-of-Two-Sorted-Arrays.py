"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log(m+n)).



Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

####
nums1 = [1, 3, 5, 7, 8]
nums2 = [2, 4]
####
"""

# Time Complexity:  O((N+M*(log(M+N)))) -> for the brute-force, O(log(min(m,n))) -> fro the optimal
# Space Complexity: O(M+N) -> for the brute-force, O(1) -> for the optimal


class Solution:
    def __init__(self) -> None:
        err_msg_invalid_result = "Provided result is not correct. Something is wrong!"

        nums1, nums2 = [1, 3], [2]

        result = self.find_median_sorted_arrays_brute_force(nums1, nums2)
        assert result == 2.00000, err_msg_invalid_result
        print(result)

        result = self.find_median_sorted_arrays_optimal(nums1, nums2)
        assert result == 2.00000, err_msg_invalid_result
        print(result)

        nums1, nums2 = [1, 2], [3, 4]

        result = self.find_median_sorted_arrays_brute_force(nums1, nums2)
        assert result == 2.50000, err_msg_invalid_result
        print(result)

        result = self.find_median_sorted_arrays_optimal(nums1, nums2)
        assert result == 2.50000, err_msg_invalid_result
        print(result)

    def find_median_sorted_arrays_brute_force(
        self, nums1: list[int], nums2: list[int]
    ) -> float:
        if not nums1 and not nums2:
            return 0.0

        merged_arr = nums1 + nums2
        merged_arr.sort()

        total_len = len(merged_arr)

        if total_len % 2 == 0:
            return (merged_arr[(total_len // 2) - 1] + merged_arr[total_len // 2]) / 2.0
        else:
            return merged_arr[total_len // 2]

    def find_median_sorted_arrays_optimal(
        self, nums1: list[int], nums2: list[int]
    ) -> float:
        if not nums1 and not nums2:
            return 0.0

        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len_nums1, len_nums2 = len(nums1), len(nums2)
        low, high = 0, len_nums1

        while low <= high:
            partition_x = (low + high) // 2
            partition_y = (len_nums1 + len_nums2 + 1) // 2 - partition_x

            # Get partition elements
            max_left_x = float("-inf") if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = (
                float("inf") if partition_x == len_nums1 else nums1[partition_x]
            )

            max_left_y = float("-inf") if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = (
                float("inf") if partition_y == len_nums2 else nums2[partition_y]
            )

            # Check if we found the correct partition
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                # If total length is even
                if (len_nums1 + len_nums2) % 2 == 0:
                    return (
                        max(max_left_x, max_left_y) + min(min_right_x, min_right_y)
                    ) / 2
                # If total length is odd
                return max(max_left_x, max_left_y)

            # Adjust binary search boundaries
            elif max_left_x > min_right_y:
                high = partition_x - 1
            else:
                low = partition_x + 1

        # If we reach here, the input arrays are not valid
        raise ValueError("Input arrays are not valid for finding median.")


# Create an instance of the class
solution = Solution()

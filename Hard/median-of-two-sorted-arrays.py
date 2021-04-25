"""
Challenge Website: https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
"""


class Solution:
    """
    Solution has time complexity of O(m+n) and space complexity of O(1)
    """

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        idx1, idx2 = 0, 0
        m, n = len(nums1), len(nums2)

        is_even_len = (m + n) % 2 == 0
        if is_even_len:
            target = (m + n) / 2 + 1
        else:
            target = (m + n + 1) / 2

        last2items = [0, 0]
        while idx1 + idx2 < target:
            if idx2 >= n or (idx1 < m and nums1[idx1] <= nums2[idx2]):
                last2items.pop(0)
                last2items.append(nums1[idx1])
                idx1 += 1
            else:
                last2items.pop(0)
                last2items.append(nums2[idx2])
                idx2 += 1

        if is_even_len:
            return sum(last2items) / 2
        else:
            return last2items[-1]


if __name__ == "__main__":
    solution = Solution()

    assert solution.findMedianSortedArrays([1, 3], [2, ]) == 2
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert solution.findMedianSortedArrays([0, 0], [0, 0]) == 0
    assert solution.findMedianSortedArrays([], [1, ]) == 1
    assert solution.findMedianSortedArrays([2, ], []) == 2
    assert solution.findMedianSortedArrays([1, 3], [2, 7]) == 2.5

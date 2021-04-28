"""
Challenge Website: https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array nums, find the smallest missing positive integer.
"""


class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(1, len(nums) + 1):
            x = i
            n_at_x = nums[x - 1]
            while n_at_x != x and 0 < n_at_x <= len(nums):
                x = n_at_x
                n_at_x, nums[x - 1] = nums[x - 1], n_at_x

        for x in range(1, len(nums) + 1):
            if nums[x - 1] != x:
                return x
        return len(nums) + 1


if __name__ == "__main__":
    solution = Solution()

    assert solution.firstMissingPositive([1, 2, 0]) == 3
    assert solution.firstMissingPositive([3, 4, -1, 1]) == 2
    assert solution.firstMissingPositive([7, 8, 9, 11, 12]) == 1

"""
Challenge Website: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == nums[i + 1]:
                nums.pop(i)

        return len(nums)


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 1, 2]
    assert solution.removeDuplicates(nums) == 2
    assert nums == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert solution.removeDuplicates(nums) == 5
    assert nums == [0, 1, 2, 3, 4]

    nums = []
    assert solution.removeDuplicates(nums) == 0
    assert nums == []

    nums = [1]
    assert solution.removeDuplicates(nums) == 1
    assert nums == [1]

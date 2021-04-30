"""
Challenge Website: https://leetcode.com/problems/running-sum-of-1d-array/

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

import numpy as np


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        if nums == []:
            return []

        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(sums[i - 1] + nums[i])
        return sums

    def runningSumNp(self, nums: list[int]) -> list[int]:
        return list(np.cumsum(nums))


if __name__ == "__main__":
    solution = Solution()

    assert solution.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert solution.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert solution.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]

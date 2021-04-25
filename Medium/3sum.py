"""
Challenge Website: https://leetcode.com/problems/3sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def threeSum(self, nums: list[int]) -> set[tuple[int]]:
        sums = set()
        count = dict()
        for n in nums:
            count[n] = count.get(n, 0) + 1

        sorted_keys = sorted(count.keys())
        for i, n1 in enumerate(sorted_keys):
            for n2 in sorted_keys[i:]:
                missing_number = -(n1 + n2)
                if missing_number not in count:
                    continue
                c1 = count[n1]
                if n1 == n2 == 0 and c1 < 3:  # edge case triple zero
                    continue
                if n1 == n2 and c1 == 1:  # avoid using number too often
                    continue
                c2 = count[n2]
                if missing_number == n1 and c1 == 1 or missing_number == n2 and c2 == 1:  # avoid using number too often
                    continue
                sums.add(tuple(sorted([n1, n2, missing_number])))
        return sums


if __name__ == "__main__":
    solution = Solution()

    assert solution.threeSum([-1, 0, 1, 2, -1, -4]) == {(-1, -1, 2), (-1, 0, 1)}
    assert solution.threeSum([]) == set()
    assert solution.threeSum([0]) == set()
    assert solution.threeSum([0, 0]) == set()
    assert solution.threeSum([0, 0, 0]) == {(0, 0, 0)}

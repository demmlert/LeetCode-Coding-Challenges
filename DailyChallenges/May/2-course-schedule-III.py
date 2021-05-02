"""
Challenge Website: https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3729/

There are n different online courses numbered from 1 to n. You are given an array courses where
courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days
and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.
"""

import heapq as hq


class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        courses.sort(key=lambda c: c[1])

        selected_courses = []

        current_total_time = 0
        for duration, time_limit in courses:
            if current_total_time + duration <= time_limit:
                current_total_time += duration
                hq.heappush(selected_courses, -duration)
            elif selected_courses and duration < -(selected_courses[0]):
                current_total_time += duration
                current_total_time += hq.heappop(selected_courses)
                hq.heappush(selected_courses, -duration)
        return len(selected_courses)


if __name__ == "__main__":
    s = Solution()

    assert s.scheduleCourse([[1, 2]]) == 1
    assert s.scheduleCourse([[3, 2], [4, 3]]) == 0
    assert s.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]) == 3
    assert s.scheduleCourse([[1, 2], [2, 3]]) == 2
    assert s.scheduleCourse([[5, 5], [4, 6], [2, 6]]) == 2

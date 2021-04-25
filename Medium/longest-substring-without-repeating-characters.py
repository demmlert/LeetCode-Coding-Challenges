class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        contained = dict()
        start = 0
        longest = 0
        for i, c in enumerate(s):
            start = max(start, contained.get(c, -1) + 1)
            contained[c] = i
            longest = max(longest, i + 1 - start)
        return longest

if __name__ == "__main__":
    solution = Solution()

    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("") == 0
    assert solution.lengthOfLongestSubstring("abba") == 2

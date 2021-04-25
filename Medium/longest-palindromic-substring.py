class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""

        longest = s[0]
        for i in range(len(s)):
            longest = max_palindrome(s, i - 1, i + 1, longest)  # odd length
            longest = max_palindrome(s, i, i + 1, longest)      # even length
        return longest


def max_palindrome(s: str, l: int, r: int, longest: str):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if len(longest) < r - l + 1:
            longest = s[l:r + 1]
        l -= 1
        r += 1
    return longest


if __name__ == "__main__":
    solution = Solution()

    assert solution.longestPalindrome("babad") == "bab" or solution.longestPalindrome("babad") == "aba"
    assert solution.longestPalindrome("cbbd") == "bb"
    assert solution.longestPalindrome("a") == "a"
    assert solution.longestPalindrome("ac") == "a" or solution.longestPalindrome("ac") == "c"
    assert solution.longestPalindrome("aaaa") == "aaaa"

"""
Challenge Website: https://leetcode.com/problems/string-to-integer-atoi/

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

    1. Read in and ignore any leading whitespace.
    2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either.
       This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    3. Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
    4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
       If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range.
       Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    6. Return the integer as the final result.

Note:

    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""
import re

class Solution:
    def myAtoiRegex(self, s: str) -> int:
        """
        Quick implementation using regex
        """
        number = re.search("^ *([+-]?\d+)", s)
        return max(-(2 ** 31), min(int(number.group()), 2 ** 31 - 1)) if number else 0

    def myAtoi(self, s: str) -> int:
        """
        Exact implementation of the given algorithm (as asked for)
        """
        try:
            # step 1
            i = 0
            while s[i] == " ":
                i += 1

            # step 2
            sign = 1
            if s[i] == "-":
                sign = -1
                i += 1
            elif s[i] == "+":
                i += 1

            # step 3
            start = i
            while i < len(s) and s[i] in "0123456789":
                i += 1
            end = i

            # step 4
            if start == end:
                number = 0
            else:
                number = int(s[start:end])
            number *= sign

            # step 5
            number = max(number, -2**31)
            number = min(number, 2**31 - 1)

            # step 6
            return number
        except IndexError:
            return 0

if __name__ == "__main__":
    solution = Solution()

    assert solution.myAtoi("42") == 42
    assert solution.myAtoi("   -42") == -42
    assert solution.myAtoi("4193 with words") == 4193
    assert solution.myAtoi("words and 987") == 0
    assert solution.myAtoi("-91283472332") == -2147483648
    assert solution.myAtoi("") == 0
    assert solution.myAtoi(" ") == 0
    assert solution.myAtoi(" +") == 0
    assert solution.myAtoi(" -") == 0
    assert solution.myAtoi(" a") == 0

    assert solution.myAtoiRegex("42") == 42
    assert solution.myAtoiRegex("   -42") == -42
    assert solution.myAtoiRegex("4193 with words") == 4193
    assert solution.myAtoiRegex("words and 987") == 0
    assert solution.myAtoiRegex("-91283472332") == -2147483648
    assert solution.myAtoiRegex("") == 0
    assert solution.myAtoiRegex(" ") == 0
    assert solution.myAtoiRegex(" +") == 0
    assert solution.myAtoiRegex(" -") == 0
    assert solution.myAtoiRegex(" a") == 0






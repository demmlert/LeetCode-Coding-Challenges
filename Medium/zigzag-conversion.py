"""
Challenge Website: https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        lines = ["" for _ in range(numRows)]
        for idx, c in enumerate(s):
            idx = idx % (2 * numRows - 2)
            if idx >= numRows:
                idx = numRows - idx - 2
            lines[idx] += c
        return "".join(lines)


if __name__ == "__main__":
    solution = Solution()

    assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert solution.convert("A", 1) == "A"
    assert solution.convert("ABCD", 1) == "ABCD"

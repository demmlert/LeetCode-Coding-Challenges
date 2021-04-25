"""
Challenge Website: https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
from functools import lru_cache


class Solution:
    def generateParenthesis(self, n: int) -> set[str]:
        return generateParenthesisRec(n, 0)


@lru_cache(maxsize=None)
def generateParenthesisRec(available_opening: int, available_closing: int) -> set[str]:
    if available_opening == 0 and available_closing == 0:
        return {""}

    res = set()
    if available_opening > 0:
        [res.add("(" + x) for x in generateParenthesisRec(available_opening - 1, available_closing + 1)]
    if available_closing > 0:
        [res.add(")" + x) for x in generateParenthesisRec(available_opening, available_closing - 1)]
    return res


if __name__ == "__main__":
    solution = Solution()

    assert solution.generateParenthesis(0) == {""}
    assert solution.generateParenthesis(1) == {"()"}
    assert solution.generateParenthesis(2) == {"()()", "(())"}
    assert solution.generateParenthesis(3) == {"((()))", "(()())", "(())()", "()(())", "()()()"}
    assert solution.generateParenthesis(4) == {"(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()",
                                               "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"}

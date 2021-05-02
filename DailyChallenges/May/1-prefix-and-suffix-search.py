"""
Challenge Website: https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3728/

Design a special dictionary which has some words and allows you to search the words in it by a prefix and a suffix.

Implement the WordFilter class:

    - WordFilter(string[] words) Initializes the object with the words in the dictionary.
    - f(string prefix, string suffix) Returns the index of the word in the dictionary
      which has the prefix prefix and the suffix suffix. If there is more than one valid index,
      return the largest of them. If there is no such word in the dictionary, return -1.

"""

from collections import defaultdict


class WordFilter:

    def __init__(self, words: list[str]):
        self.words = dict()

        for i, word in enumerate(words):
            self.words[word] = i

        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)

        for word, i in self.words.items():
            for j in range(1, len(word) + 1):
                self.prefixes[word[:j]].add(i)
                self.suffixes[word[:-j - 1:-1]].add(i)

    def f(self, prefix: str, suffix: str) -> int:
        idx = self.prefixes[prefix].intersection(self.suffixes[suffix[::-1]])
        idx.add(-1)
        return max(idx)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

if __name__ == "__main__":
    wf = WordFilter(["apple"])
    assert wf.f("a", "e") == 0

    wf = WordFilter(["apple"])
    assert wf.f("app", "ple") == 0

    wf = WordFilter(["apple"])
    assert wf.f("app", "a") == -1

    wf = WordFilter(["apple", "peach"])
    assert wf.f("pe", "ch") == 1

    wf = WordFilter(["apple", "peach", "applepie"])
    assert wf.f("a", "e") == 2

    wf = WordFilter(
        ["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa", "accabaccaa", "cabcbbbcca", "ababccabcb",
         "caccbbcbab", "bccbacbcba"])
    assert wf.f("a", "aa") == 5

    wf = WordFilter(["cabaabaaaa", "ccbcababac", "bacaabccba", "bcbbcbacaa", "abcaccbcaa", "accabaccaa", "cabcbbbcca",
                     "ababccabcb", "caccbbcbab", "bccbacbcba"])
    assert wf.f("bccbacbcba", "a") == 9
    assert wf.f("ab", "abcaccbcaa") == 4

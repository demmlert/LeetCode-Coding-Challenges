"""
Challeng Website: https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/592/week-5-march-29th-march-31st/3689/

You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n.
You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

Any node in the binary tree can be flipped by swapping its left and right subtrees. For example, flipping node 1 will have the following effect:

     1                 1
    / \               / \
   2   3     -->     3   2
      / \           / \
     4   5         4   5

Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.

Return a list of the values of all flipped nodes. You may return the answer in any order.
If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: list[int]) -> list[int]:
        if root.val != voyage[0]:
            return [-1]

        i = 1
        flips = []
        try:
            flipMatchVoyageRec(root, voyage, i, flips)
        except ValueError:
            return [-1]

        return flips


def flipMatchVoyageRec(node: TreeNode, voyage: list[int], i: int, flips: list[int]) -> int:
    if node.left is not None:
        if node.left.val == voyage[i]:  # if left node is correct, continue with children
            i = flipMatchVoyageRec(node.left, voyage, i + 1, flips)
        elif node.right is not None and node.right.val == voyage[i]:  # if right node is supposed to be at left node flip them
            node.left, node.right = node.right, node.left
            flips.append(node.val)
            i = flipMatchVoyageRec(node.left, voyage, i + 1, flips)
        else:  # impossible voyage
            raise ValueError

    if node.right is not None:
        if node.right.val == voyage[i]:  # if right node is correct, continue with children
            i = flipMatchVoyageRec(node.right, voyage, i + 1, flips)
        else:  # impossible voyage
            raise ValueError

    return i


if __name__ == "__main__":
    solution = Solution()

    assert solution.flipMatchVoyage(TreeNode(1, TreeNode(2)), [2, 1]) == [-1]
    assert solution.flipMatchVoyage(TreeNode(1, TreeNode(2), TreeNode(3)), [1, 3, 2]) == [1]
    assert solution.flipMatchVoyage(TreeNode(1, TreeNode(2), TreeNode(3)), [1, 2, 3]) == []
    assert solution.flipMatchVoyage(TreeNode(1, TreeNode(2, TreeNode(3))), [1, 3, 2]) == [-1]
    assert solution.flipMatchVoyage(TreeNode(1, None, TreeNode(2)), [1, 2]) == []

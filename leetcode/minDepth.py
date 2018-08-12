# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, x):

        if x is None:
            return

        if not self.val:
            self.val = x
            return

        if x < self.val and self.left is None:
            self.left = TreeNode(x)
            return
        if x < self.val and self.left is not None:
            self.left.insert(x)
            return
        if x > self.val and self.right is None:
            self.right = TreeNode(x)
            return
        if x > self.val and self.right is not None:
            self.right.insert(x)
            return


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

if __name__ == '__main__':
    n = [3, 9, 20, None, None, 15, 7]

    root = TreeNode(n.pop(0))
    for i in n:
        root.insert(i)

    from pprint import pprint
    s = Solution().minDepth(root)

    pprint(s)

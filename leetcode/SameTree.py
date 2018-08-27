# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False


if __name__ == '__main__':
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.left = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.left = TreeNode(3)

    a = Solution().isSameTree()
    b = Solution().isSameTree([1, 2], [1, None, 2])


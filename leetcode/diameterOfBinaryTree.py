class Solution:

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def depth(node):

            if node is None:
                return 0

            l = depth(node.left)
            r = depth(node.right)
            self.num_nodes = max(self.num_nodes, l + r + 1)
            return max(l, r) + 1

        self.num_nodes = 1
        depth(root)
        return self.num_nodes - 1


if __name__ == '__main__':
    # n = [3, 9, 20, None, None, 15, 7]

    n = [1, 2, 3, 4, 5]

    from lib.struct import TreeNode

    root = TreeNode(n.pop(0))
    for i in n:
        root.insert(i)

    from pprint import pprint

    s = Solution().diameterOfBinaryTree(root)

    pprint(s)

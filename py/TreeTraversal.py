from collections import deque


class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def insert(self, x):

        if x is None:
            return

        if not self.value:
            self.value = x
            return

        if x < self.value and self.left is None:
            self.left = TreeNode(x)
            return
        if x < self.value and self.left is not None:
            self.left.insert(x)
            return
        if x > self.value and self.right is None:
            self.right = TreeNode(x)
            return
        if x > self.value and self.right is not None:
            self.right.insert(x)
            return


def preorder(node: TreeNode):
    if node is None:
        return

    print(node.value)
    if node.left is not None:
        preorder(node.left)
    if node.right is not None:
        preorder(node.right)


def inorder(node: TreeNode):
    if node is None:
        return

    if node.left is not None:
        inorder(node.left)

    print(node.value)

    if node.right is not None:
        inorder(node.right)


def postorder(node: TreeNode):
    if node is None:
        return

    if node.left is not None:
        postorder(node.left)

    if node.right is not None:
        postorder(node.right)

    print(node.value)


def levelorder(root: TreeNode):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node: TreeNode = queue.popleft()
        print(node.value)
        if node.left is not None: queue.append(node.left)
        if node.right is not None: queue.append(node.right)

if __name__ == '__main__':
    tree = ['F', 'B', 'A', 'D', "C", "E", "G", "I", "H"]

    root = TreeNode(tree.pop(0))
    for i in tree: root.insert(i)

    levelorder(root)

#!/usr/bin/python


class Node:
    def __init__(self):
        self.value = None
        self.children = {}  # children is of type {char, Node}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, key):  # key is of type string
        # key should be a low-case string, this must be checked here!
        node = self.root
        for char in key:
            if char not in node.children:
                child = Node()
                node.children[char] = child
                node = child
            else:
                node = node.children[char]
        node.value = key

    def search(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                return None
            else:
                node = node.children[char]
        return node.value

    def display_node(self, node):
        if node.value is not None:
            print(node.value)
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if char in node.children:
                self.display_node(node.children[char])
        return

    def display(self):
        self.display_node(self.root)


if __name__ == '__main__':
    trie = Trie()
    trie.insert('hello')
    trie.insert('nice')
    trie.insert('to')
    trie.insert('meet')
    trie.insert('you')
    trie.display()

    print(trie.search('hello'))
    print(trie.search('HELLO'))

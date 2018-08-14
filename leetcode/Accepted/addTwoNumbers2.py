# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, x):
        if self.next is None:
            self.next = ListNode(x)
            return

        self.next.add(x)
        return


class Solution:
    def addTwoNumbers(self, l1, l2):
        def flatten(l: ListNode):
            if l.next is None:
                return str(l.val)
            return str(l.val) + flatten(l.next)

        def add(l: ListNode, x):
            if l.val is None:
                l.val = x
                return
            if l.next is None:
                l.next = ListNode(x)
                return
            add(l.next, x)
            return

        sum = int(flatten(l1)) + int(flatten(l2))
        seq = ListNode(None)
        for i in list(str(sum)):
            add(seq, i)

        return seq


if __name__ == '__main__':
    l1 = ListNode(7)
    l1.add(2)
    l1.add(4)
    l1.add(3)

    l2 = ListNode(5)
    l2.add(6)
    l2.add(4)

    s = Solution().addTwoNumbers(l1, l2)
    print(s)

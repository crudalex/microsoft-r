# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def insert(self, x):
        if not self.next:
            self.next = ListNode(x)
        else:
            self.next.insert(x)


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if head is None:
            return None

        if head.val == val:
            return self.removeElements(head.next, val)

        head.next = self.removeElements(head.next, val)
        return head


if __name__ == '__main__':

    l = [1, 2, 6, 3, 4, 5, 6]
    h = ListNode(l.pop(0))
    for i in l:
        h.insert(i)
    v = 6

    s = Solution().removeElements(h, v)
    from pprint import pprint

    pprint(s)

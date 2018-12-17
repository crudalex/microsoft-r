# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        """
        :rtype: ListNode
        :type x: int
        """
        self.val = x
        self.next = None

    def add(self, x):
        """

        :type x: int
        """
        if self.val is None:
            self.val = x
            return
        if self.next is None:
            self.next = ListNode(x)
            return
        self.next.add(x)
        return

    @classmethod
    def from_list(cls, l):
        # noinspection PyTypeChecker
        n = cls(None)
        for i in l:
            n.add(i)
        return n


class Solution:
    def sortList(self, head):
        dummyNode = ListNode(0)
        dummyNode.next = head

        if head is not None:
            self.qsortList(dummyNode, None)
        return dummyNode.next

    def qsortList(self, dummyNode, tail):
        pNode = self.partion(dummyNode, tail)
        if dummyNode.next != pNode:
            self.qsortList(dummyNode, pNode)

        if pNode.next != tail:
            self.qsortList(pNode, tail)

    def partion(self, dummyNode, tail):
        pivot = dummyNode.next
        fastPre = dummyNode.next

        while fastPre.next != tail:
            if fastPre.next.val < pivot.val:
                tmp = fastPre.next
                fastPre.next = tmp.next

                tmp.next = dummyNode.next
                dummyNode.next=tmp
            else:
                fastPre = fastPre.next

        return pivot

if __name__ == '__main__':
    s = Solution()
    j = ListNode.from_list([4, 2, 1, 3])
    k = ListNode.from_list([-1, 5, 3, 4, 0])
    x = s.sortList(j)
    y = s.sortList(k)

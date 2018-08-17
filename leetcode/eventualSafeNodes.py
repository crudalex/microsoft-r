class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """


if __name__ == '__main__':
    
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    s = Solution().eventualSafeNodes(graph)

    from pprint import pprint
    pprint(s)

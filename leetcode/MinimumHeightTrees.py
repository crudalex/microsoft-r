class Solution:

    def findMinHeightTrees(self, n, edges):
        adjacency = [set() for i in range(n)]
        for e in edges:
            adjacency[e[0]].add(e[1])
            adjacency[e[1]].add(e[0])

        return adjacency

if __name__ == '__main__':
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    s1 = Solution().findMinHeightTrees(n, edges)

    n = 6
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    s2 = Solution().findMinHeightTrees(n, edges)

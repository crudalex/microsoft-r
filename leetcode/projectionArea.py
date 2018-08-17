class Solution:
    def projectionArea(self, grid):
        pass

if __name__ == '__main__':
    grids = [
        [[2]],
        [[1, 2], [3, 4]],
        [[1, 0], [0, 2]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[2, 2, 2], [2, 1, 2], [2, 2, 2]],
    ]
    areas = [5, 17, 8, 14, 21]
    for (grid, area) in zip(grids, areas):
        s = Solution().projectionArea(grid)
        print(s == area)

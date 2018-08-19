class Solution:
    def canFinish(self, numCourses, prerequisites):

        adjacency = [set() for i in range(numCourses)]
        for e in prerequisites:
            adjacency[e[0]].add(e[1])
            adjacency[e[1]].add(e[0])

        result = True
        for i in range(numCourses):
            result = result and walk(i, [])

        def walk(i, j, walked):
            if len(adjacency[i]) == 0:
                return True

            if edge in walked:
                return False


        return result



if __name__ == '__main__':
    s1 = Solution().canFinish(2, [[1, 0]])
    s2 = Solution().canFinish(2, [[1, 0], [0, 1]])

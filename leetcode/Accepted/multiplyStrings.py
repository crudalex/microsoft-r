class Solution:
    def multiply(self, num1, num2):
        sum = int(num1) * int(num2)
        return str(sum)

if __name__ == '__main__':
    s1 = Solution().multiply('2', '3')
    s2 = Solution().multiply('123', '456')

    print(s1)
    print(s2)

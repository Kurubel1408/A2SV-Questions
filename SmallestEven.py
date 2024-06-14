class Solution(object):
    def smallestEvenMultiple(self, n):
        if n % 2 == 0:
            return n
        else:
            return 2 * n

sol = Solution()

print(sol.smallestEvenMultiple(5))  
print(sol.smallestEvenMultiple(6))

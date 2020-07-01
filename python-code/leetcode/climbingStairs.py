class Solution(object):
    
    lookup = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        
        if n in Solution.lookup:
            return Solution.lookup[n]
        
        x = self.climbStairs(n - 1)
        
        if (n - 1) not in Solution.lookup:
            Solution.lookup[n-1] = x

        y = self.climbStairs(n - 2)
        
        return x + y
    
    ''' iterative solution
    class Solution(object):
    
    lookup = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        Solution.lookup[0] = Solution.lookup[1] = 1
        Solution.lookup[2] = 2
        
        for x in range(3, n+1):
            Solution.lookup[x] = Solution.lookup[x-1] + Solution.lookup[x-2]
            
        return Solution.lookup[n]
        
        
    '''
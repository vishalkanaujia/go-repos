class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        localMax = globalMax = nums[0]
        
        index = 1
        while index < len(nums):
            localMax = max(localMax + nums[index], nums[index])
            
            globalMax = max(localMax, globalMax)
            index += 1
            
        return globalMax
        
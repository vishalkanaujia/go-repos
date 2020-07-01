class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeros = 0
        j = 0
        
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            else:
                zeros += 1
            j += 1
            
            
        while zeros > 0:
            nums[i] = 0
            i += 1
            zeros -= 1
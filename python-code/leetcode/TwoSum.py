'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''

# Solve with a hash
def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []
    
class Solution:
    def twoSum(self, nums, target):
        mapping = {}
        index = 0
        for num in nums:
            if num in mapping:
                mapping[num].append(index)
            else:    
                mapping[num] = [index]
            index += 1
            
        complement = 0
        index = 0
        
        for num in nums:
            complement = target - num
            if complement in mapping:
                # special case: complement is same as num
                if complement == num:
                    if len(mapping[complement]) > 1:
                        return [index, mapping[complement][1]]
                    else:
                        index += 1
                        continue
                return [index, mapping[complement][0]]
            index += 1
            
        return [-1, -1]
        
s = Solution()
print(s.twoSum([1,1], 2))
print(s.twoSum([3,2,4], 6))

mylist = [5,6,7]
for index, value in enumerate(mylist, start= 1):
    print(index, value)
    
d = {1: "name", 2: "age"}
for k, v in d.items():
    print(k, v)

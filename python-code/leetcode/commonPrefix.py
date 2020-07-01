'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []
        
        list_strs = []
        for s in strs:
            list_strs.append(list(s))
            
        result = zip(*list_strs)
        for r in result:
            print(r)
            if r[0] == r[1] and r[1] == r[2]:
                prefix.append(r[0])                

        if len(prefix) > 0:
            return ''..join(prefix)
        else:
            return ""
        
s = Solution()
s.longestCommonPrefix(["flower", "flow", "flat"])
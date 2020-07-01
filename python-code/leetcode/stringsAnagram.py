class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Keep a frequency array
        frequency = {}
        for c in s:
            if c not in frequency:
                frequency[c] = 1
            else:
                frequency[c] += 1
        
        # Go over the other string 
        for d in t:
            if d in frequency:
                frequency[d] -= 1
                if frequency[d] == 0:
                    # Just keep deleting what is not required
                    del frequency[d]
            else:
                # Anything not in dict, just say Not an Anagram.
                return False

        if len(frequency) == 0:
            return True
        
        return False
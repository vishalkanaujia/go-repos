def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1

        d = collections.OrderedDict()
        
        for index, c in enumerate(s):
            if c in d:
                d[c][0] += 1
            else:
                d[c] = [1, index]
        
        for k in d:
            if d[k][0] == 1:
                return d[k][1]
        
        return -1
    
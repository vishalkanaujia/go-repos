class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.all_min = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append(x)
        if len(self.all_min) == 0:
            self.all_min.append(x)
            return
        if x <= self.all_min[-1]:
            self.all_min.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.data) == 0:
            return -1
        
        x = self.data.pop()        
        if x == self.all_min[-1]:
            self.all_min.pop()
        return x
    
    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]    

    def getMin(self):
        """
        :rtype: int
        """
        return self.all_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
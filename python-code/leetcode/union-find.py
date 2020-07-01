class Solution(object):
    def __init__(self, nodesCount):
        self.nodes = list(range(nodesCount + 1))

    def union(self, p, q):
        currentRoot = self.root(p)
        for index, num in enumerate(self.nodes):
            if num == currentRoot:
                self.nodes[index] = q
                
        print(self.nodes)

    def find(self, p, q):
        return self.root(p) == self.root(q)
    
    def root(self, p):
        return self.nodes[p]
    
if __name__ == "__main__":
    s = Solution(6)
    s.union(1, 2)
    s.union(2, 3)
    s.union(2, 4)
    
    print(s.find(1, 3))
    print(s.find(3, 4))
    print(s.find(3, 6))
#Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

###DO NOT WORK FOR SELF LOOPS
##OUTPUTS - 529 [3 191 388 388 430 944 ]    3 [166 191 388 388 430 529 944 ]    191 [3 166 191 195 388 430 529 ]    388 [3 166 195 388 388 430 529 944 ]    430 [3 166 191 195 388 388 430 529 944 ]    944 [3 166 195 388 388 430 529 ]    166 [3 166 191 195 388 388 430 944 ]    195 [166 191 195 388 388 430 944 ]    
##EXPECTED - 529 [3 191 388 388 430 944 ]    3 [166 191 388 388 430 529 944 ]    191 [3 166 191 195 388 430 529 ]    388 [3 166 195 388 388 430 529 944 ]    388 [3 166 191 195 388 430 529 944 ]    430 [3 166 191 195 388 388 430 529 944 ]    944 [3 166 195 388 388 430 529 ]    166 [3 166 191 195 388 388 430 944 ]    195 [166 191 195 388 388 430 944 ]    


# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return node
        
        old = self.dfs1(node)
        new = {}
        for key in old:
            n  = UndirectedGraphNode(key)
            new[key] = n
        
        for key in old:
            for mem in old[key]:
                new[key].neighbors.append(new[mem.label])
        return new[node.label]
        
    def dfs1(self,node):
        queue = deque()
        queue.append(node)
        d = {}
        while len(queue) != 0:
            n = queue.popleft()
            if n.label not in d:
                d[n.label] = n.neighbors
                
                for elem in n.neighbors:
                    queue.append(elem)
        return d

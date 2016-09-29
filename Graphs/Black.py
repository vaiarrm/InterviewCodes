#Given N * M field of O's and X's, where O=white, X=black
#Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)

# Time Complexity: N * M + V * E
# Space Complexity: N * M + 2 * V

# Basic Graph API for converting X's inta graph vertexs
class Graph:
    def __init__(self):
        # Constructor
        self.vertexDic = {}
    
    def addVertex(self,vertex):
        # Adding a vertex
        if vertex in self.vertexDic:
            pass
        else:
            self.vertexDic[vertex] = set()

    def addEdge(self,vertex1,vertex2):
        #Adding an Edge
        self.addVertex(vertex1)
        self.addVertex(vertex2)
        self.vertexDic[vertex1].add(vertex2)
        self.vertexDic[vertex2].add(vertex1)

class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        if len(A) == 0: #if length is zero we can not process anything
            return 0
        G = Graph()
    
        for i in range(len(A)):
            for j in range(len(A[i])):
                curr = (i,j)
                if A[i][j] != "X":
                    continue
                else:
                    G.addVertex(curr)
                
                # North Vertex
                x = i - 1
                y = j
            
                if x < 0 or j >= len(A[i-1]):
                    pass
                else:
                    if A[x][y] == "X":
                        G.addEdge(curr,(x,y))
            
                #South Vertex
                x = i + 1
                y = j
            
                if x >= len(A) or j >= len(A[i+1]):
                    pass
                else:
                    if A[x][y] == "X":
                        G.addEdge(curr,(x,y))
            
                #West Vertex
                x = i
                y = j - 1
            
                if j < 0:
                    pass
                else:
                    if A[x][y] == "X":
                        G.addEdge(curr,(x,y))
            
                #East Vertex
                x = i
                y = j + 1
            
                if j < len(A[i]):
                    pass
                else:
                    if A[x][y] == "X":
                        G.addEdge(curr,(x,y))
        
        # Connected Components Logic
        marked = {}
        for v in G.vertexDic.keys():
            marked[v] = False
        count = 0
        for v in G.vertexDic.keys():
            if marked[v]:
                continue
            else:
                count += 1
                self.dfs(v,marked,G)
        
        return count
    def dfs(self,ver,marked,G):
        marked[ver] = True
        
        for v in G.vertexDic[ver]:
            if marked[v]:
                          continue
            self.dfs(v,marked,G)
        
        
        
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

from collections import deque
class Solution:
    # @param A : integer
    # @return a strings
    def multiple(self, A):
        if A == 0: #base case 1
            return 0
        elif A == 1: #base case 2
            return 1
        x = 1
        d = deque()
        d.append(x)
        isEven = False
        
        while len(d) != 0:
            y = d.popleft()
            if y % A == 0:
                return str(y)
            b = y * 10
            d.append(b)
            a = y * 10 + 1
            d.append(a)

# Generating Follwing tree/Graph
                                          #1
                                     #/      #\
                                 #10          #11
                            #/     #\     #/     #\ 
                       #100    #101  #110   #111
#....so on
            

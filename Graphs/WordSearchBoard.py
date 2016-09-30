#Given a 2D board and a word, find if the word exists in the grid.
#The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells
#are those horizontally or vertically neighboring. The cell itself does not count as an adjacent cell. 
#The same letter cell may be used more than once.

class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, A, B):
        if A == None or B == None:
            return 0
        B = B.strip()
        for i in xrange(len(A)):
            for j in xrange(len(A[i])):
                found = False
                if B[0] == A[i][j]:
                    found = self.helper(A,B,i,j,1)
                if found:
                    return 1
        return 0
    
    def helper(self,a,b,i,j,curr):
        print i,j,curr
        if curr == len(b):
            return True
        
        found = False
        #center Not Allowed
        #print "center"
        i#f a[i][j] == b[curr]:
#            found = self.helper(a,b,i,j,curr+1)
        
        if found:
            return found 
            
        #North
        print "North"
        x = i+1
        y = j
        
        if 0 <= x < len(a) and 0 <= y < len(a[x]):
            if a[x][y] == b[curr]:
                found = self.helper(a,b,x,y,curr+1)
        
        if found:
            return found
        
        #South
        print "South"
        x = i - 1
        y = j
        
        if 0 <= x < len(a) and 0 <= y < len(a[x]):
            if a[x][y] == b[curr]:
                found = self.helper(a,b,x,y,curr+1)
        
        if found:
            return found
        
        #West
        print "West"
        x = i
        y = j - 1
        
        if 0 <= x < len(a) and 0 <= y < len(a[x]):
            if a[x][y] == b[curr]:
                found = self.helper(a,b,x,y,curr+1)
        
        if found:
            return found
        
        #East
        print "east"
        x = i
        y = j + 1
        
        if 0 <= x < len(a) and 0 <= y < len(a[x]):
            if a[x][y] == b[curr]:
                found = self.helper(a,b,x,y,curr+1)
        
        if found:
            return found
        
        return found
        
s = Solution()
lst = [ "FEDCBECD", "FABBGACG", "CDEDGAEC", "BFFEGGBA", "FCEEAFDA", "AGFADEAC", "ADGDCBAA", "EAABDDFF" ]#[ "FEDCBECD", "FABBGACG", "CDEDGAEC", "BFFEGGBA", "FCEEAFDA", "AGFADEAC", "ADGDCBAA", "EAABDDFF" ]
word = "BCDCB"
print s.exist(lst,word)
        
        
        
        

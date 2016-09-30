

class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        if len(A) == 0:
            return A
        self.pr(A)
        for i in range(len(A)):
            A[i] = list(A[i])
            
        for i in range(len(A)):
            for j in range(len(A[i])):
                if i >= 1 and j < 5:
                        print i,j
                        self.pr( A)
                if A[i][j] == 'O' or A[i][j] == '-':
                    self.floodFill(A,i,j)
        self.pr(A)
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == "+":
                    A[i][j] = 'O'
                if A[i][j] == "-":
                    A[i][j] = 'X'
        self.pr(A)
        return A
    def pr(self,A):
        for elem in A:
                print elem
        print
        
    def floodFill(self,A,i,j):
        yesToFlip = False
        if A[i][j] == "+":
                return yesToFlip
        A[i][j] = "-"
        
        #North
        x = i - 1
        y = j
        yesToFlip = self.verify(A,x,y)
        if not yesToFlip:
            A[i][j] = '+'
            return yesToFlip
        
        #South
        x = i + 1
        y = j
        yesToFlip = self.verify(A,x,y)
        if not yesToFlip:
            A[i][j] = '+'
            return yesToFlip
            
        #East
        x = i
        y = j + 1
        yesToFlip = self.verify(A,x,y)
        if not yesToFlip:
            A[i][j] = '+'
            return yesToFlip
        
        #West
        x = i
        y = j - 1
        yesToFlip = self.verify(A,x,y)
        if not yesToFlip:
            A[i][j] = '+'
            return yesToFlip
        
        if yesToFlip:
            A[i][j] = "-"
        else:
            A[i][j] = '+'
        return yesToFlip
        
    def verify(self,A,x,y):
        yesToFlip = False
        
        if 0<= x < len(A) and 0 <= y < len(A[x]):
            if A[x][y] == "X" or A[x][y] == "-":
                yesToFlip = True
            else:
                yesToFlip =  self.floodFill(A,x,y)
        else:
                yesToFlip = False
        
        return yesToFlip
A = ["XOXXOOX", "OXOOXXX", "OXOXOXO", "OOOOOXX", "XXXXOXX" ]
s = Solution()
s.solve(A)

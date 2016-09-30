# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:10:39 2016

@author: vaibhavsharma
"""


class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        if len(A) == 0:
            return 0
        count = 0
        for i in range(len(A)):
            A[i] = list(A[i])
            
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == "X":
                    count += 1
                    self.floodFill(A,i,j)
        return count      
    def floodFill(self,A,i,j):
        A[i][j] = "0"
        # Going North
        x = i - 1
        y = j
        if 0 <= x < len(A) and 0 <= y < len(A[x]) and A[x][y] == "X":
            self.floodFill(A,x,y)
        
        #Going South
        x = i + 1
        y = j        
        if 0 <= x < len(A) and 0 <= y < len(A[x]) and A[x][y] == "X":
            self.floodFill(A,x,y)
            
        # Going East
        x = i
        y = j  - 1      
        if 0 <= y < len(A[i]) and A[x][y] == "X":
            self.floodFill(A,x,y)
        
        #Going West
        x = i
        y = j + 1        
        if 0 <= y < len(A[i])and A[x][y] == "X":
            self.floodFill(A,x,y)        
        
        
                

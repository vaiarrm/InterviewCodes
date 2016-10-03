# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 06:55:11 2016

@author: vaibhavsharma
"""
"""
Remove Element

Given an array and a value, remove all the instances of that value in the array. 
Also return the number of elements left in the array after the operation.
It does not matter what is left beyond the expected length.

 Example:
If array A is [4, 1, 1, 2, 1, 3]
and value elem is 1, 
then new length is 3, and A is now [4, 2, 3] 
Try to do it in less than linear additional space complexity.

"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        if A == None or len(A) == 0:
            return 0
        
        i = 0
        j = 0
        while j < len(A):
            if A[i] != B and A[j] != B:
                i += 1
                j += 1
            elif A[i] == B and A[j] != B:
                A[i],A[j] = A[j],A[i]
                i += 1
                j += 1
            elif A[i] == B and A[j] == B:
                j+=1
            else:
                j+=1
        count = 0
        for k in range(len(A)):
            if A[k] != B:
                count += 1
            else:
                break
        A = A[:k]
        return count
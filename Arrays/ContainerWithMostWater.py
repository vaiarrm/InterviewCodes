# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 17:32:45 2016

@author: vaibhavsharma
"""
"""

Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is
at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Your program should return an integer which corresponds to the maximum 
area of water that can be contained ( Yes, we know maximum area instead of 
maximum volume sounds weird. But this is 2D plane we are working with for 
simplicity ).

Input : [1, 5, 4, 3]
Output : 6

Explanation : 5 and 3 are distance 2 apart. So size of the base = 2. 
Height of container = min(5, 3) = 3. So total area = 3 * 2 = 6

"""



class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        if A == None or len(A) < 2:
            return 0
        j = 0
        maxA = 0
        for i in range(1,len(A)):
            h1 = min (A[i],A[j])
            a1 = h1 * (i -j)
            
            h2 = min (A[i],A[i-1])
            a2 = h2 * 1
            
            print "a1 = ", str(a1)
            print "a2 = ", str(a2)
            print "h1 = ", str(h1)
            print "h2 = ", str(h2)
            
            if a2 > a1:
                j = i-1
                maxA = a2
            else:
                maxA = max(a1,maxA)
                
        return maxA

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 07:10:02 2016

@author: vaibhavsharma
"""
"""
Given an array with n objects colored red, white or blue, 
sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: Using library sort function is not allowed.

Example :

Input : [0 1 2 0 1 2]
Modify array so that it becomes : [0 0 1 1 2 2]
"""
class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        if A == None or len(A) <2:
            return A
        zero = 0
        one = 0
        two = 0
        for num in A:
            if num == 0:
                zero += 1
            elif num == 1:
                one += 1
            elif num == 2:
                two += 1
        A = [0] * zero + [1] * one + [2] * two
        return A
                
"""
#Solution using Three Pointers
class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        n = len(A)
        i = 0
        j = n - 1
        k = n - 1
        while i < k:
            if A[i] == 0:
                i += 1
            elif A[i] == 1:
                if i < j:
                    A[i],A[j] = A[j],A[i]
                    j-=1
                else:
                    i+= 1
            else:
                A[i],A[k] = A[k],A[i]
                k -= 1
                if j > k:
                    j = k
        return A
"""
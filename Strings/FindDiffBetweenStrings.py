# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 20:14:45 2016

@author: vaibhavsharma
"""

# Given two strings s and t which consist of only lowercase letters.
# String t is generated by random shuffling string s and then add one more letter at a random position.
# Find the letter that was added in t.

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # O(NlgN) Solution
        # s = list(s)
        # s.sort()
        # print s
        # t = list(t)
        # t.sort()
        # print t
        # i=0
        # while i < len(s):
        #     if s[i] != t[i]:
        #         return t[i]
        #     i+=1
        # return t[i]
        
        
        # O(N) solution
        # Use of ord and chr function
        k = 0
        i = 0
        while i < len(s):
            k -= ord(s[i])
            k += ord(t[i])
            i+=1
        k += ord(t[i])
        return chr(k)
            
            
            
        
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 08:39:49 2016

@author: vaibhavsharma
"""
"""

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) +len(s2) != len(s3):
            return False
        
        i = 0
        j = 0
        k = 0
        last = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s3[k] and s2[j] == s3[k]:
                pass
            if s1[i] == s3[k]:
                i+=1
                k+=1
                last = 1
            elif s2[j] == s3[k]:
                j+=1
                k+=1
                last = 2
            else:                    
                return False
        while i < len(s1):
            if s1[i] != s3[k]:
                print i
                print j
                print k
                return False
            i+=1
            k+=1
        while j < len(s2):
            if s2[j] != s3[k]:
                print i
                print j
                print k
                return False
            j+=1
            k+=1
        return True
"""

Unsolved for this case
s = Solution()
s1 = "aa"
s2 = "ab"
s3 = "aaba"
print s.isInterleave(s1,s2,s3)

"""
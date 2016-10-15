# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 05:56:36 2016

@author: vaibhavsharma
"""
"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        if len(s) == 0:
            return s
        s = s.split()
        if len(s) == 1:
            return s[0]
        else:
            s.reverse()
            return " ".join(s)        
        
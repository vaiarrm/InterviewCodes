# -*- coding: utf-8 -*-
"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

"""

"""
Created on Sun Oct  2 11:47:39 2016

@author: vaibhavsharma
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None or type(s) != str:
            return None
        if len(s) == 1:
            return s
        l = list(s)
        i = 0
        j = len(s) -1
        vowels = "aeiouAEIOU"
        while i<j:
            if l[i] in vowels and l[j] in vowels:
                l[i],l[j] = l[j],l[i]
                i += 1
                j -= 1
            elif l[i] in vowels and l[j] not in vowels:
                j -= 1
            elif l[i] not in vowels and l[j] in vowels:
                i += 1
            else:
                i+=1
                j-=1
        return "".join(l)
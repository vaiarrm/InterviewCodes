# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 08:00:47 2016

@author: vaibhavsharma
"""
"""

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        
        if s == None:
            return False
        #s = str(s)
        if len(s) < 2:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i].lower() != s[j].lower():
                return False
            else:
                i+=1
                j-=1
        return True
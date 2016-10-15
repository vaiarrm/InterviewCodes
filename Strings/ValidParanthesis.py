# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 05:03:07 2016

@author: vaibhavsharma
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if s == None or type(s) != str:
            return False
            
        stack = []
        open = "{(["
        close = "})]"
        
        for char in s:
            if char in open:
                stack.append(char)
            elif char in close:
                if len(stack) == 0:
                    return False
                tempChar = stack.pop(-1)
                if char == "}" and tempChar != "{":
                    return False
                elif char == ")" and tempChar != "(":
                    return False
                elif char == "]" and tempChar != "[":
                    return False
            else:
                continue
        if len(stack) != 0:
            return False
        return True
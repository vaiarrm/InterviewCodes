# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 21:39:25 2016

@author: vaibhavsharma
"""

'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, 
otherwise return 0.

You may assume that the version strings are non-empty and contain only 
digits and the . character.
The . character does not represent a decimal point and is used to 
separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        i = 0
        m = min(len(v1),len(v2))
        while i <  m:
            a = self.clean(v1[i])
            b = self.clean(v2[i])
            
            if a == b:
                pass
            elif a < b:
                return -1
            else:
                return 1
            i += 1
        if len(v1) == len(v2):
            return 0
        if len(v1) > len(v2):
            while i < len(v1):
                a = eval(v1[i])
                if a != 0:
                    return 1
                i+=1
            return 0
        if len(v2) > len(v1):
            while i < len(v2):
                a = eval(v2[i])
                if a != 0:
                    return -1
                i+=1
            return 0
    def clean(self,num):
        for i  in range (len(num)):
            if num[i] == "0":
                continue
            else:
                break
        ret = num[i:]
        if ret == "":
            ret = "0"
        
        return eval(ret)
                
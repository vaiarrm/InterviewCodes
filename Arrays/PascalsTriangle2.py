# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:40:49 2016

@author: vaibhavsharma
"""

"""
Pascal's triangle II
"""
class Solution(object):
    def getRow(self, rowNum):

        if rowNum == 0:
            return [1]
        
        first = [1]
        sec = []        
        for i in range(1,rowNum+1):
            sec.append(1)
            for j in range(1,i):
                x = first[j-1]+first[j]
                sec.append(x)
            sec.append(1)
            #print sec
            first =sec
            sec = []
        return first
        

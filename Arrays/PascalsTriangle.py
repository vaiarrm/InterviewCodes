# -*- coding: utf-8 -*-
"""

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""

"""
Created on Sun Oct  2 11:57:02 2016

@author: vaibhavsharma
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return list()
        out = [[1]]
        for i in range(1,numRows):
            lst = list()
            lst.append(1)
            for j in range(1,i):
                k = out[i-1][j-1]+out[i-1][j]
                lst.append(k)
            lst.append(1)
            out.append(lst)
        return out
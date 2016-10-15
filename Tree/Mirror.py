# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 19:00:17 2016

@author: vaibhavsharma
"""
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        y = self.inorderT(root,"")
        i = 0
        j = len(y) -1 
        while i < j:
            if y[i] != y[j]:
                return False
            i += 1
            j -= 1
        return True
        
    def inorderT(self,node,s):
        
        if node == None:
            return s
        x = self.inorderT(node.left,s)
        s = x + str(node.val)
        return self.inorderT(node.right,s)

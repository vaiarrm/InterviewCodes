# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 20:15:36 2016

@author: vaibhavsharma
"""
'''
Find the sum of all left leaves in a given binary tree.
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in 
the binary tree, with values 9 and 15 respectively. Return 24.
'''

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root,False)
    
    def helper(self,node,type):
        if node == None:
            return 0
        if type:
            if node.left == None and node.right == None:
                return node.val
        l = self.helper(node.left,True)
        r = self.helper(node.right,False)
        return l+r
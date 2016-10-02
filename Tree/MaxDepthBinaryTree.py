# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 18:35:39 2016

@author: vaibhavsharma
"""
"""
Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.helper(root)
    
    def helper(self,node):
        if node == None:
            return 0
        d1 = self.helper(node.left)
        d2 = self.helper(node.right)
        d = max(d1,d2)
        return d+1
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:38:44 2016

@author: vaibhavsharma
Comments:
1. This version is exceeding time limit
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

"""
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        #created a dicitonary for inorder
        io = {}
        for i in range(len(inorder)):
            io[inorder[i]] = i
        
        return self.createTree(preorder,io)
        
    def createTree(self,preorder,io):
        root = None
        for key in preorder:
            root = self.put(key,io,root)
        return root
        
    def put(self,key,io,node):
        if node == None:
            return TreeNode(key)
        if io[key] < io[node.val]:
            node.left = self.put(key,io,node.left)
        else:
            node.right = self.put(key,io,node.right)
        return node

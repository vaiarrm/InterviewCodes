# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 13:52:07 2016

@author: vaibhavsharma
Comment:
"""
"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
"""
In-order: A, B, C, D, E, F, G, H, I.
Post-order: A, C, E, D, B, H, I, G, F.
https://en.wikipedia.org/wiki/Tree_traversal#/media/File:Sorted_binary_tree_postorder.svg
"""


#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder == None or postorder == None:
            return None
        if len(inorder) != len(postorder):
            return None
            
        return self.createTree(inorder,postorder,0,len(inorder)-1,len(inorder)-1)
        
    def createTree(self,inorder,postorder,start,end,rootPos):
        if start > end or rootPos < 0:
            return None
        node = TreeNode(postorder[rootPos])
        
        count = None
        for i in range(start,end+1):
            if inorder[i] == node.val:
                count = i
        
        node.left = self.createTree(inorder,postorder,start,count-1,rootPos-end+count-1)
        node.right = self.createTree(inorder,postorder,count+1,end,rootPos -1)
        return node
            
            
        
        
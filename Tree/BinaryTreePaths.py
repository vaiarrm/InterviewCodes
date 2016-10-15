# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 08:47:45 2016

@author: vaibhavsharma
"""
"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
            print node.val
            print path
            print nodetracker
"""
# Definition for a binary tree node.
class Node:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        path = []
        nodetracker = []
        self.helper(root,path,nodetracker)
        return path
    
    def helper(self,node,path,nodetracker):
        if node == None:
            return
        nodetracker.append(node.val)
        if node.left == None and node.right == None:
            s = ""
            for i in nodetracker:
                s += str(i)+"->"
            path.append(s[:-2])
        else:
            self.helper(node.left,path,nodetracker)
            self.helper(node.right,path,nodetracker)
        nodetracker.pop(-1)
        #nodetracker.remove(node.key) ##VERY BAD SOLUTION!!!
"""
x=Node(1)
y = Node(2)
z = Node(3)
x.left = y
x.right = z
a = Node(5)
y.right = a
s = Solution()
print s.binaryTreePaths(x)
"""
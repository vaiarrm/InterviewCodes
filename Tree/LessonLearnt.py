# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:30:36 2016

@author: vaibhavsharma
"""

"""
1. Lists are mutable
    a. if you want to save a current copy of the list which you are 
    going to modify make sure to creat a deep copy of the list
    ex: 1. Working Solution
        lst = [1,2,3]
        deepCopied = list(lst)
        lst.appen(4)
        print lst
        print deepCopied
        
        2. Not working Solution
        lst = [1,2,3]
        shallowCopied = lst
        lst.appen(4)
        print lst
        print shallowCopied

2. Tree can have duplicate values.
    a. In the example of finding path to leaves we are saving the node
    on the stack. I did not considered the case of duplicate values and
    used remove funciton. This removed the root node and created all set of 
    problems. Solution was to use pop

3. Given inorder and postorder create a tree:
    Algorithm1 
    n lgn (Easy to come up wiht)
    a: Inorder gives you the  order of keys from left to right
    b. Postorder gives you the root (last element).
    Sol:
        1. Generate a dictionary from indorder array where keys are the inorder
        values and their indices as the values
        2. create a root node from the last element of postorder array
        3. For every element in postorder array (going backwards)
            3a. using the dictionary determine standing at a node whether you
            have to go left or right till you reach null.
            3b. after reaching null create th node and return that node
    
    Algorithm 2:
    Time Complexity N (Nifty solution)
    Soln
    1. Set up 3 varaibles:
        start - start of the inorder array
        end - end of the inorder array
        rootPos - position of current root between start and end
    2. first time:
        start = 0
        end = len(inoder) - 1
        rootPos = len(postorder) - 1
        
        Create the root node. 
        
        Find the the index of root node in inorder array. Name it mid
        for node.right:
            start = mid + 1
            end = end
            rootPos = rootPos - 1
        for node.left:
            start = start
            end = mid -1
            rootPos = rootPos - end + mid - 1
        Do this recursively till:
            start < end
            rootPos < 0
4. Given inorder and preorder
    - You can use same algorithms as before
    - for the second alg following will be the changes:
        node.right:
            start = mid + 1
            end = end
            rootPos = rrootpos - start + mid - 1
        for node.left:
            start = start
            end = mid -1
            rootPos = rootPos + 1
        
    
    

"""
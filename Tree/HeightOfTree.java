/*

The height of a binary tree is the number of edges between the tree's root and its furthest leaf. 
This means that a tree containing a single node has a height of 0.

Complete the height function provided in your editor so that it returns the height of a binary tree.
This function has a parameter, root, which is a pointer to the root node of a binary tree
*/

   /*
    
    class Node 
       int data;
       Node left;
       Node right;
   */
   int height(Node root)
    {
       if (root == null){
           return -1;
       }
       int hl = height(root.left);
       int hr = height(root.right);         
       return Math.max(hl,hr) + 1;
    }
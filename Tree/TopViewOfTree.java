/*

You are given a pointer to the root of a binary tree. Print the top view of the binary tree. 
You only have to complete the function. 
For example :

     3
   /   \
  5     2
 / \   / \
1   4 6   7
 \       /
  9     8
Top View : 1 -> 5 -> 3 -> 2 -> 7

*/

/*
   class Node 
       int data;
       Node left;
       Node right;
*/
void top_view(Node root)
{
  if (root == null) return;
    top_viewLeft(root.left);
    //System.out.print(" ");
    System.out.print(root.data);
    top_viewRight(root.right);
}
void top_viewLeft(Node root)
{
    if (root == null) return;
    top_viewLeft(root.left);
    System.out.print(root.data);
    System.out.print(" ");
}
void top_viewRight(Node root)
{
      if (root == null) return;
    System.out.print(" ");  
      System.out.print(root.data);
    top_viewRight(root.right);  

}


 /* Node is defined as :
 class Node 
    int data;
    Node left;
    Node right;
    
    */

/*

Comments:
This program passed all the test cases in HackerRank
But there is a edge case that if we enconter of the values as the root.data
*/

static Node lca(Node root,int v1,int v2)
    {
        
       if (root == null){
           return null;
       }
       if (v1 < root.data && v2 < root.data){
           return lca(root.left,v1,v2);
       }else if (v1 > root.data && v2 > root.data){
           return lca(root.right,v1,v2);
       }
        return root;
       
    }





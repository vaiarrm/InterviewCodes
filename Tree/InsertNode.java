 /* Node is defined as :
 class Node 
    int data;
    Node left;
    Node right;
    
    */

static Node Insert(Node root,int value)
    {
        if (root == null){
            Node n =  new Node();
            n.data = value;
            return n;
        }
        if (value < root.data){
            root.left = Insert(root.left,value);
        }else if (value > root.data){
            root.right = Insert(root.right,value);
        }
        return root;
       
    }



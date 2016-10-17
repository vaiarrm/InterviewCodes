   void LevelOrder(Node root)
    {
       if (root == null) return;
       LinkedList<Node> ll = new LinkedList<>();
       ll.addLast(root);
       while (!ll.isEmpty()){
           Node n = ll.removeFirst();
           System.out.print(n.data);
           System.out.print(" ");
           if (n.left != null) ll.addLast(n.left);
           if (n.right != null) ll.addLast(n.right);
               
       }
    }
   
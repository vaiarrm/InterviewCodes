/*
Merge k sorted linked lists and return it as one sorted list.

Example :

1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
will result in

1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
*/

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
	public ListNode mergeKLists(ArrayList<ListNode> a) {
	    TreeMap<ListNode,Integer> tree = new TreeMap<>(new Comparator<ListNode>(){
	        public int compare(ListNode o1, ListNode o2) {
				return o1.val - o2.val;
			}
	        }
	    );
	    
	    for (ListNode v: a){
	        while (v != null){
	            tree.put(v,1);
	        }
	    }
	    
	    ListNode head = new ListNode(-100);
	    ListNode f = head;
	    while (!tree.isEmpty()){
	        ListNode minNow = tree.firstKey();
	        tree.remove(minNow);
	        f.next = minNow;
	        f = f.next;
	    }
	    return head.next;
}
}

/*

# Python Quadratic time solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        if A == None or len(A) == 0:
            return list()
        if len(A) == 1:
            return A[0]
        
        head = ListNode(1)
        head.next = A[0]
        for i in range(1,len(A)):
            f = head.next
            s = A[i]
            if s == None:
                continue
            if f == None:
                head.next = s
                continue
            if f != None and s != None:
                if f.val > s.val:
                    head.next = s
                    s = f
                    f = head.next
            
            prev = head
            while f != None and s != None:
                if f.val < s.val:
                    f = f.next
                    prev = prev.next
                else:
                    temp = s.next
                    prev.next = s
                    s.next = f
                    prev = s
                    s = temp
            if s!= None:
                    prev.next = s 
                    
        return head.next
*/
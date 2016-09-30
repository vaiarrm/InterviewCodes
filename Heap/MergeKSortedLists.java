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
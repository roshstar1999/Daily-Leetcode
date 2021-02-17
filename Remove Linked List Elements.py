class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        h=head
        
        while(h):
            if h.val==val and h==head:
                head=head.next
            elif h.val!=val:
                prev=h
            else:
                prev.next=h.next
            h=h.next
        return head

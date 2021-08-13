def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        if head.next == None:
            return head
        
        nn = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return nn
    

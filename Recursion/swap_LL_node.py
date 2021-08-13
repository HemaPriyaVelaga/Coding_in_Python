def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head== None:
            return None
        
        elif head.next == None:
            return head
        
        else:
            
            curr = head.next
            head.next = self.swapPairs(head.next.next)
            curr.next = head
            return curr
          

def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()
        
        if not l1 and not l2:
            return None
        
        elif not l1:
            return l2
        
        elif not l2:
            return l1
        
        
        if l1.val<=l2.val:
            result = l1
            result.next = self.mergeTwoLists(l1.next, l2)
            #return l2
            
        else:
            result = l2
            result.next = self.mergeTwoLists(l1, l2.next)
            
        return result

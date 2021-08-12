def detectCycle(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        
        slow = head
        fast = slow
        
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                fast = head
                while fast is not slow:
                    fast = fast.next
                    slow = slow.next
                return fast          
        
        return None
        

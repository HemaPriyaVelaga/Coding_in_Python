    def rob(self, nums: List[int]) -> int:
        adj = 0
        prev = 0 
        
        for i in nums:
            
            curr = max(i + prev, adj)
            prev = adj
            adj = curr
            
        return adj
      
      
  # The intuition is to decide whether to rob the current house based on the adjacent left house and the house before the adjacent house (prev)

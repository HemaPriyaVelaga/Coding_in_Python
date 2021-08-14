def fib(self, n: int) -> int:
        
        memo = {}
        
        def rec(n):
            
            if n in memo:
                return memo[n]
            
            if n<=1:
                return n
            
            else:
                
                memo[n] = rec(n-1) + rec(n-2)
                return memo[n]
            
    
        return rec(n)

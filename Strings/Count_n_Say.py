# SOlution to the leetcode question: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/


def countAndSay(self, n: int) -> str:
        
         def say(s):
            
            count_say = list(s)
            
            count_int = ""
            count = 1
            
            # For loop to count occurrence of continuous repeating elements
            # and to create the final count and say string
            
            for i in range (1, len(count_say)):
                if count_say[i]==count_say[i-1]:
                    count+=1
                else:
                    count_int+=str(count)
                    count_int+=count_say[i-1]
                    count = 1
            count_int+= str(count) + count_say[-1]
            
            return count_int
            
            
        def recurse(n):
            if n == 1:
                return '1'
            if n==2:
                return '11'
        
            else:
                return say(recurse(n-1))
        
        
        
        return recurse(n)
        

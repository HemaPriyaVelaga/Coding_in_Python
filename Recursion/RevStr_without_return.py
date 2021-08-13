 def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        if len(s)==0:
            return
        
        #print (s[-1])
        
        else: 
            s[0], s[-1] = s[-1], s[0]  ## Swap the last and first element in the list of string
            slice = s[1:-1] ## Now, take only that part of the string where swap has not been performed
            self.reverseString(slice)  ## Repeat the above two steps recursively for that sliced part
            s[1:-1] = slice  ## assign the slice back to original s[]

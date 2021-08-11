## Function to return each level of the pascal's triangle as a list and the combined solution is a list of lists.

def generate(self, numRows: int) -> List[List[int]]:
       
        pascal = []
        
        if numRows == 0:
            return pascal
        
        pascal.append([1])
        
        if numRows == 1:
            return pascal
        
        pascal.append([1,1])
        
        if numRows == 2:
            return pascal
       
        for i in range(2,numRows):
            
            pascal.append([1])
            
            
            
            for j in range(1, i):
                pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
                #print('Row: ', i+1, '   j: ', j, pascal)
               
            pascal[i].append(1)
            
        print(pascal)
        return pascal
            
        

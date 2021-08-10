## Solution to the Valid Sudoku check problem in Leetcode

class Solution:
    
    
    ## Function to check if there are any repetitions in a row
    
    def not_in_row(self, board, row)-> bool:
        
        st = set()
        for i in range(9):
            
            if board[row][i] in st:
                return False
            elif board[row][i] != ".":
                st.add(board[row][i])
        return True
    
        
    ## Function to check if there are any repetitions in column
    def not_in_col(self, board, col):
        st = set()
        for i in range(9):
            
            if board[i][col] in st:
                return False
            elif board[i][col]!=".":
                st.add(board[i][col])
        return True
    
    
    ## Function to check if there are any repetitions in a 3 x 3 box
    def not_in_box(self, board, row, col)-> bool:
        
        st = set()
        
        for i in range(3):
            
            for j in range(3):
                
                curr = board[row + i][col+j]
                
                if curr in st:
                    return False
                elif curr!=".":
                    st.add(curr)
        return True
                   
    
    def isValid(self, board, row, col)-> bool:
         return self.not_in_row(board, row) and self.not_in_col(board, col) and self.not_in_box(board, row - row % 3, col - col % 3 )
      
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        for i in range(len(board)):
            for j in range(len(board)):
                if not self.isValid(board, i, j):
                    return False
            
        return True
        

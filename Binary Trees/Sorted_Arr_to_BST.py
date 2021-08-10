def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums:
            return None
        
        mid = int(len(nums)/2)
        
        root = TreeNode(nums[mid])
        
        root.left = self.sortedArrayToBST(nums[:mid])
        
        root.right = self.sortedArrayToBST(nums[mid+1:])   
        
        ## Here, mid + 1 because the mid element is already added 
        ## as the parent before coming to this point
        
        
        return root
      
      
 ''' 
 LOGIC (Array is already sorted in ascending order):
 
 1. Get the mid element of the array and make it root
 2. Now, find the mid of the left half sub array and make it as the roots left child
 3. Find the mid of the right half of the sub array and make it as the root's right child
 
 repeat it recusrsively till all the elements are covered.
 
 '''
      
   

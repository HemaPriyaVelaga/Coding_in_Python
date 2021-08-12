class Node (object):
    
    def __init__(self, data):
        
        self.data = data
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0
    
    
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        
            
        n = self.size
        
        if(index>=n or index < 0 or self.head == None):
            return -1
        
        temp = self.head
        for i in range(index):
                temp = temp.next
                #index-=1
            
        return temp.data
                
                    
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        temp = Node(val)   
        temp.next = self.head
        self.head = temp
        self.size+=1

        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        
        temp = self.head
        
        if self.head == None:
            self.head = Node(val)
        else:
            while(temp.next):
                temp = temp.next
        
            temp.next = Node(val)
            
        self.size+=1
        return
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        n = self.size
    
            
        if index== 0 :
            return self.addAtHead(val)
            
        elif index >n or index<0:
            return
        
        else:
            curr = self.head
            newnode = Node(val)
            for i in range(index-1):
                curr = curr.next
            
            newnode.next = curr.next
            curr.next = newnode
            
            self.size+=1
            return
            
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        n = self.size
        
        if index >=n or index <0:
            return
        
        else:
            curr = self.head
            if index == 0:
                self.head = curr.next
            else:
                for i in range(index-1):
                    curr  = curr.next
            
                curr.next = curr.next.next
                
                self.size-=1
            return
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

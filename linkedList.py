from node import Node

class LinkedList:
    def __init__(self):
        
        self.head = Node(0, -1) # the number is 0 and the value is -1
        
        
        
        

    def add_node(self, number, value):
        new_Node = Node(number, value)
        
        if self.head.next == None:
            self.head.next = new_Node
            new_Node.prev = self.head
            
        else:
            current = self.head.next
            while current.next != None and current.next.number < number:
                current = current.next
            
            new_Node.next = current.next
            new_Node.prev = current
            current.next = new_Node
            new_Node.next.prev = new_Node
            
            
    
            
            
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    def check_node_empty(self, input_number):
        
        sw = 1
        current = self.head.next
        
        while current != None:
            if current.number == input_number:
                sw = 0
        
        if sw == 0:
            return False
        else:
            return True
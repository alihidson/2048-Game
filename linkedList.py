from node import Node

class LinkedList:
    def __init__(self):
        self.head = Node(0, -1) # number == 0 and value == -1 for head1
        
        self.head.down = Node(0, -1)
        self.head.down.up = self.head
        self.head = self.head.down
        
        self.head.down = Node(0, -1)
        self.head.down.up = self.head
        self.head = self.head.down
        
        self.head.down = Node(0, -1)
        self.head.down.up = self.head
        self.head = self.head.down
        
        self.head = self.head.up.up.up
        
        
        

    def add_node(self, number, value):
        
        newNode = Node(number, value)
        current = self.head
        
        if 1 <= number and number <= 4:
            if current.next == None:
                current.next = newNode
                
            else:
                while current.next.number < newNode.number:
                    current = current.next
                    
                newNode.next = current.next
                current.next = newNode
                
                
        elif 5 <= number and number <= 8:
            current = self.head.down
            
            if current.next == None:
                current.next = newNode
                
            else:
                while current.next.number < newNode.number:
                    current = current.next
                    
                newNode.next = current.next
                current.next = newNode
                
                
        elif 9 <= number and number <= 12:
            current = self.head.down.down
            
            if current.next == None:
                current.next = newNode
                
            else:
                while current.next.number < newNode.number:
                    current = current.next
                    
                newNode.next = current.next
                current.next = newNode
                
                
        elif 13 <= number and number <= 16:
            current = self.head.down.down.down
            
            if current.next == None:
                current.next = newNode
                
            else:
                while current.next.number < newNode.number:
                    current = current.next
                    
                newNode.next = current.next
                current.next = newNode
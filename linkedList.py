from node import Node

class LinkedList:
    def __init__(self):
        self.head = Node(0, -1) # create head
        
        # create nodes for rows
        self.row1 = Node(0, -1)
        self.head.down = self.row1
        self.row1.up = self.head
        
        self.row2 = Node(0, -1)
        self.row1.down = self.row2
        self.row2.up = self.row1
        
        self.row3 = Node(0, -1)
        self.row2.down = self.row3
        self.row3.up = self.row2
        
        self.row4 = Node(0, -1)
        self.row3.down = self.row4
        self.row4.up = self.row3
        
        
        # create nodes for columns
        self.col1 = Node(0, -1)
        self.head.next = self.col1
        self.col1.prev = self.head
        
        self.col2 = Node(0, -1)
        self.col1.next = self.col2
        self.col2.prev = self.col1
        
        self.col3 = Node(0, -1)
        self.col2.next = self.col3
        self.col3.prev = self.col2
        
        self.col4 = Node(0, -1)
        self.col3.next = self.col4
        self.col4.prev = self.col3
        
        
        

    def add_node(self, number, value):
        
        newNode = Node(number, value)
        current = self.row1
        
        if 1 <= number and number <= 4:
            if current.next == None:
                current.next = newNode
                
            else:
                while current.next != None and current.next.number < newNode.number:
                    current = current.next
                    
                newNode.next = current.next
                current.next = newNode
                
                
        elif 5 <= number and number <= 8:
            current = self.head.down
            
            if current.next == None:
                current.next = newNode
                
            else:
                while current.next != None and current.next.number < newNode.number:
                    current = current.next
                    
                newNode.next = current.next
                current.next = newNode
                
                
        elif 9 <= number and number <= 12:
            current = self.head.down.down
            
            if current.next == None:
                current.next = newNode
                
            else:
                while current.next != None and current.next.number < newNode.number:
                    current = current.next
                    
                newNode.next = current.next
                current.next = newNode
                
                
        elif 13 <= number and number <= 16:
            current = self.head.down.down.down
            
            if current.next == None:
                current.next = newNode
                
            else:
                while current.next != None and current.next.number < newNode.number:
                    current = current.next
                    
                newNode.next = current.next
                current.next = newNode
                
    
    
    
    
    
    
    def check_node_empty(self, input_number):
        
        if 1 <= input_number and input_number <= 4:
            current = self.head.next
            
            sw = 1
            while current != None:
                
                if current.number == input_number:
                    sw = 0
                current = current.next
            
            if sw == 0:
                return False
            else:
                return True
        
        
        
        
        if 5 <= input_number and input_number <= 8:
            current = self.head.down.next
            
            sw = 1
            while current != None:
                
                if current.number == input_number:
                    sw = 0
                current = current.next
            
            if sw == 0:
                return False
            else:
                return True
            
            
        if 9 <= input_number and input_number <= 12:
            current = self.head.down.down.next
            
            sw = 1
            while current != None:
                
                if current.number == input_number:
                    sw = 0
                current = current.next
            
            if sw == 0:
                return False
            else:
                return True
            
            
        
        if 13 <= input_number and input_number <= 16:
            current = self.head.down.down.down.next
            
            sw = 1
            while current != None:
                
                if current.number == input_number:
                    sw = 0
                current = current.next
            
            if sw == 0:
                return False
            else:
                return True
        
        

# def move_right(self):
#     current = self.head.next
    
#     if current.value == current.next.value:
#         current.next.value += current.value
        
    
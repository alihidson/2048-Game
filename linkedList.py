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
            if new_Node.next != None:
                new_Node.next.prev = new_Node
            
    
    
    
    
    def check_node_empty(self, input_number):
        
        current = self.head.next
        
        if current == None:
            return True
        
        while current != None:
            if current.number == input_number:
                return False
            current = current.next
        
        return True
        
        
    
    
    
    
    def is_board_full(self):
        current = self.head.next
        filled_nodes = 0

        while current:
            filled_nodes += 1
            current = current.next
            
        if filled_nodes == 16:
            return True
        else:
            return False
        
        
        
        
        
        
        
    def remove_zero_nodes(self):
        current = self.head.next
        while current:
            if current.value == 0:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
            current = current.next
        
        
        
        
    def move_up(self):
        for col_start in range(1, 5):
            first = None
            second = None
            third = None
            fourth = None
            
            current = self.head.next

            while current:
                if current.number == col_start:
                    first = current
                elif current.number == col_start + 4:
                    second = current
                elif current.number == col_start + 8:
                    third = current
                elif current.number == col_start + 12:
                    fourth = current
                current = current.next

            if first and second and first.value == second.value:
                first.value += second.value
                second.value = 0
            if second and third and second.value == third.value:
                second.value += third.value
                third.value = 0
            if third and fourth and third.value == fourth.value:
                third.value += fourth.value
                fourth.value = 0

            next_position = col_start
            for node in [first, second, third, fourth]:
                if node and node.value != 0:
                    node.number = next_position
                    next_position += 4

        self.remove_zero_nodes()
        
        
    
    
    def move_down(self):
        for col_start in range(1, 5):
            first = None
            second = None
            third = None
            fourth = None
            
            current = self.head.next

            while current:
                if current.number == col_start:
                    first = current
                elif current.number == col_start + 4:
                    second = current
                elif current.number == col_start + 8:
                    third = current
                elif current.number == col_start + 12:
                    fourth = current
                current = current.next

            if fourth and third and fourth.value == third.value:
                fourth.value += third.value
                third.value = 0
            if third and second and third.value == second.value:
                third.value += second.value
                second.value = 0
            if second and first and second.value == first.value:
                second.value += first.value
                first.value = 0

            next_position = col_start + 12
            for node in [fourth, third, second, first]:
                if node and node.value != 0:
                    node.number = next_position
                    next_position -= 4

        self.remove_zero_nodes()
        
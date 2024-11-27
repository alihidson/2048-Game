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


        current = self.head.next
        while current:
            if current.value == 0:
                current.prev.next = current.next
                if current.next != None:
                    current.next.prev = current.prev
            current = current.next
        
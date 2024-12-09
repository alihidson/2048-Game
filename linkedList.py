from node import Node

class LinkedList:
    def __init__(self):
        
        self.head = Node(0, -1) # the number is 0 and the value is -1
        self.score = 0
        
        
    def get_score(self):
        return self.score

        
    def clear(self):
        self.head.next = None
        
        
    def find_node(self, number):
        current = self.head.next
        while current != None:
            if current.number == number:
                return current
            current = current.next
        return None


    def has_won(self):
        current = self.head.next
        count = 0

        while current:
            if current.value == 2048:
                return True
            count += 1
            current = current.next

        if count < 16:
            return None

        grid = [[0 for _ in range(4)] for _ in range(4)]
        current = self.head.next

        while current:
            row = (current.number - 1) // 4
            col = (current.number - 1) % 4
            grid[row][col] = current.value
            current = current.next

        for i in range(4):
            for j in range(4):
                if j < 3 and grid[i][j] == grid[i][j + 1]:
                    return None
                if i < 3 and grid[i][j] == grid[i + 1][j]:
                    return None

        # the game is over and we can not mave anymore
        return False

        

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
        
        
        
    
    def to_array(self):
        result = []
        current = self.head.next
        
        while current:
            result.append((current.number, current.value))
            current = current.next
        return result
    
    
    
    def has_changed(self, first_state):
        current_state = self.to_array()
        
        if current_state != first_state:
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
                self.score += first.value
            if second and third and second.value == third.value:
                second.value += third.value
                third.value = 0
                self.score += second.value
            if third and fourth and third.value == fourth.value:
                third.value += fourth.value
                fourth.value = 0
                self.score += third.value
            if first and third and second == None and first.value == third.value:
                first.value += third.value
                third.value = 0
                self.score += first.value
            if second and fourth and third == None and second.value == fourth.value:
                second.value += fourth.value
                fourth.value = 0
                self.score += second.value
            if first and fourth and second == None and third == None and first.value == fourth.value:
                first.value += fourth.value
                fourth.value = 0
                self.score += first.value

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
                self.score += fourth.value
            if third and second and third.value == second.value:
                third.value += second.value
                second.value = 0
                self.score += third.value
            if second and first and second.value == first.value:
                second.value += first.value
                first.value = 0
                self.score += second.value
            if fourth and second and third == None and fourth.value == second.value:
                fourth.value += second.value
                second.value = 0
                self.score += fourth.value
            if third and first and second == None and third.value == first.value:
                third.value += first.value
                first.value = 0
                self.score += third.value
            if fourth and first and third == None and second == None and fourth.value == first.value:
                fourth.value += first.value
                first.value = 0
                self.score += fourth.value
                

            next_position = col_start + 12
            for node in [fourth, third, second, first]:
                if node and node.value != 0:
                    node.number = next_position
                    next_position -= 4

        self.remove_zero_nodes()
        
        
        
        
        
        
    def move_left(self):
        for row_start in range(1, 14, 4):
            first = None
            second = None
            third = None
            fourth = None
            
            current = self.head.next
            
            while current:
                if current.number == row_start:
                    first = current
                elif current.number == row_start + 1:
                    second = current
                elif current.number == row_start + 2:
                    third = current
                elif current.number == row_start + 3:
                    fourth = current
                current = current.next
                
                
            if first and second and first.value == second.value:
                first.value += second.value
                second.value = 0
                self.score += first.value
            if second and third and second.value == third.value:
                second.value += third.value
                third.value = 0
                self.score += second.value
            if third and fourth and third.value == fourth.value:
                third.value += fourth.value
                fourth.value = 0
                self.score += third.value
            if first and third and second == None and first.value == third.value:
                first.value += third.value
                third.value = 0
                self.score += first.value
            if second and fourth and third == None and second.value == fourth.value:
                second.value += fourth.value
                fourth.value = 0
                self.score += second.value
            if first and fourth and second == None and third == None and first.value == fourth.value:
                first.value += fourth.value
                fourth.value = 0
                self.score += first.value
                
                
            next_position = row_start
            for node in [first, second, third, fourth]:
                if node and node.value != 0:
                    node.number = next_position
                    next_position += 1
                    
        self.remove_zero_nodes()
                    
                    
    
    def move_right(self):
        for row_start in range(1, 14, 4):
            first = None
            second = None
            third = None
            fourth = None
            
            current = self.head.next
            
            while current:
                if current.number == row_start:
                    first = current
                elif current.number == row_start + 1:
                    second = current
                elif current.number == row_start + 2:
                    third = current
                elif current.number == row_start + 3:
                    fourth = current
                current = current.next
                
                
            if fourth and third and fourth.value == third.value:
                fourth.value += third.value
                third.value = 0
                self.score += fourth.value
            if third and second and third.value == second.value:
                third.value += second.value
                second.value = 0
                self.score += third.value
            if second and first and second.value == first.value:
                second.value += first.value
                first.value = 0
                self.score += second.value
            if fourth and second and third == None and fourth.value == second.value:
                fourth.value += second.value
                second.value = 0
                self.score += fourth.value
            if third and first and second == None and third.value == first.value:
                third.value += first.value
                first.value = 0
                self.score += third.value
            if fourth and first and third == None and second == None and fourth.value == first.value:
                fourth.value += first.value
                first.value = 0
                self.score += fourth.value
                
                
            next_position = row_start + 3
            for node in [fourth, third, second, first]:
                if node and node.value != 0:
                    node.number = next_position
                    next_position -= 1

        self.remove_zero_nodes()               
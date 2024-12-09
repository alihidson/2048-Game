class Deque:
    
    def __init__(self):
        self.save = []
        self.max_number = 5 
        
        
    def save_state(self, linkedList):
        
        state = linkedList.to_array()
        self.save.append(state)
        
        if len(self.save) > self.max_number:
            self.save.pop(0)
            
            
    def put_back(self, linkedList):
        
        if self.save:
            
            last_state = self.save.pop()
            linkedList.clear()
            
            for number, value in last_state:
                linkedList.add_node(number, value)
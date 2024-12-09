import copy
import random
import time

class AI:
    def __init__(self, game, simulations_per_move=100):
        self.game = game
        self.simulations = simulations_per_move
    
    def simulate_game(self, direction):
       
        temp_game = copy.deepcopy(self.game)
        
        if direction == 'UP':
            temp_game.move_up()
        elif direction == 'DOWN':
            temp_game.move_down()
        elif direction == 'LEFT':
            temp_game.move_left()
        elif direction == 'RIGHT':
            temp_game.move_right()
        
        if not temp_game.has_changed(self.game.to_array()):
            return 0

        for _ in range(50):
            random_move = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
            if random_move == 'UP':
                temp_game.move_up()
            elif random_move == 'DOWN':
                temp_game.move_down()
            elif random_move == 'LEFT':
                temp_game.move_left()
            elif random_move == 'RIGHT':
                temp_game.move_right()
            
            
            if not temp_game.has_changed(temp_game.to_array()):
                break
        
        return temp_game.get_score()
    
   
    def find_best_move(self):
        
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        scores = {direction: 0 for direction in directions}
        
        for direction in directions:
            total_score = 0
            for _ in range(self.simulations):
                total_score += self.simulate_game(direction)
            scores[direction] = total_score / self.simulations
        
        best_move = max(scores, key=scores.get)
        return best_move
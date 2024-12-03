import pygame
import sys

import random

from linkedList import LinkedList
from deque import Deque



def get_cell_position(number):
    cell_size = 125
    offset_x = 55
    offset_y = 53
    row = (number - 1) // 4
    col = (number - 1) % 4
    x = offset_x + col * cell_size
    y = offset_y + row * cell_size
    return x, y



def get_tile_color(value):
    if value == 2:
        return (255, 88, 88)
    
    elif value == 4:
        return (237, 224, 200)
    
    elif value == 8:
        return (242, 177, 121)
    
    elif value == 16:
        return (245, 149, 99)
    
    elif value == 32:
        return (246, 124, 95)
    
    elif value == 64:
        return (246, 94, 59)
    
    elif value == 128:
        return (237, 207, 114)
    
    elif value == 256:
        return (237, 204, 97)
    
    elif value == 512:
        return (237, 200, 80)
    
    elif value == 1024:
        return (237, 197, 63)
    
    elif value == 2048:
        return (237, 194, 46)
    
    else:
        return (255, 255, 255)





def draw_nodes_with_colors(screen, linkedList):
    
    current = linkedList.head.next
    cell_size = 115
    font = pygame.font.Font("./Font/PinyonScript-Regular.ttf", 80)

    while current != None:
        x, y = get_cell_position(current.number)

        color = get_tile_color(current.value)
        pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))

        text = font.render(str(current.value), True, BLACK)
        text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
        screen.blit(text, text_rect)

        current = current.next
            





pygame.init()
screen_width = 800
screen_height = 600

screen_game = pygame.display.set_mode((screen_width, screen_height))
screen_Finish = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("2048")
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (195, 0, 0)
GREEN = (50, 149, 0)
LIGHT_BROWN = (255, 222, 162)


game = LinkedList()

save_for_undo = Deque()
save_for_redo = Deque()

number_can_undo = 5
number_can_redo = 5


Play = True
sw_random_append = True
Finish = False

Game_Over1 = False
Game_Over2 = False
Game_Over3 = False
Game_Over4 = False

while Play:
    
    pygame.event.pump()
    
    first_state = game.to_array()
    

    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        Play = False
        
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            save_for_undo.save_state(game)
            game.move_up()
            if game.has_changed(first_state) == True:
                sw_random_append = True
                Game_Over1 = False
                Game_Over2 = False
                Game_Over3 = False
                Game_Over4 = False
            else:
                Game_Over1 = True
                
        elif event.key == pygame.K_DOWN:
            save_for_undo.save_state(game)
            game.move_down()
            if game.has_changed(first_state) == True:
                sw_random_append = True
                Game_Over1 = False
                Game_Over2 = False
                Game_Over3 = False
                Game_Over4 = False
            else:
                Game_Over2 = True
            
        elif event.key == pygame.K_LEFT:
            save_for_undo.save_state(game)
            game.move_left()
            if game.has_changed(first_state) == True:
                sw_random_append = True
                Game_Over1 = False
                Game_Over2 = False
                Game_Over3 = False
                Game_Over4 = False
            else:
                Game_Over3 = True
            
        elif event.key == pygame.K_RIGHT:
            save_for_undo.save_state(game)
            game.move_right()
            if game.has_changed(first_state) == True:
                sw_random_append = True
                Game_Over1 = False
                Game_Over2 = False
                Game_Over3 = False
                Game_Over4 = False
            else:
                Game_Over4 = True
                
        elif event.key == pygame.K_z:
            if number_can_undo > 0:
                save_for_redo.save_state(game)
                save_for_undo.put_back(game)
                number_can_undo -= 1
            
        elif event.key == pygame.K_x:
            if number_can_redo > 0:
                save_for_redo.put_back(game)
                number_can_redo -= 1
                
    
    if game.has_won() == True:
        print("you have won")
            
    
    
    
    # Define the numbers and their corresponding probabilities
    numbers = [2, 4]
    weights = [70, 30]
    
    # Generate a random choice with the given probabilities
    value_created_with_chance = random.choices(numbers, weights=weights, k=1)[0]
    
    
    
    attempts = 0
    maxAttempts = 50
        
    while sw_random_append == True:
        
        # Generate a random integer between 1 and 16 (inclusive)
        node_number_created_with_chance = random.randint(1, 16)
        
        if game.check_node_empty(node_number_created_with_chance) == True:
            game.add_node(node_number_created_with_chance, value_created_with_chance)
            sw_random_append = False
        
        attempts += 1
        # avoid to infinity loop
        if attempts > maxAttempts:
            sw_random_append = False
            
    if Game_Over1 and Game_Over2 and Game_Over3 and Game_Over4: 
        Play = False
        Finish = True
        print("Game Over")
        
        
        
    
    screen_game.fill(LIGHT_BROWN)
    
        
    cell_size = 125
    for row in range(4):
        for col in range(4):
            x = 50 + (col * cell_size)
            y = 50 + (row * cell_size)
            pygame.draw.rect(screen_game, RED, (x, y, cell_size, cell_size), 3)
            
    pygame.draw.rect(screen_game, RED, (50, 50, 500, 500), 5) # x, y, width, height

    draw_nodes_with_colors(screen_game, game)
    
    pygame.display.flip()
    clock.tick(60)
    
    




while Finish:
    
    screen_Finish.fill(GREEN)
    
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        Finish = False
        
        
    pygame.display.flip()
    clock.tick(60)
    
    


pygame.quit()
sys.exit()
import pygame
import sys

import random

from linkedList import LinkedList
from deque import Deque
from ai import AI



def get_cell_position(number):
    cell_size = 85
    offset_x = 53
    offset_y = 53
    row = (number - 1) // 4
    col = (number - 1) % 4
    x = offset_x + col * cell_size
    y = offset_y + row * cell_size
    return x, y



def get_tile_color(value):
    if value == 2:
        return (255, 0, 0)
    
    elif value == 4:
        return (0, 255, 0)
    
    elif value == 8:
        return (255, 120, 0)
    
    elif value == 16:
        return (0, 255, 255)
    
    elif value == 32:
        return (255, 0, 255)
    
    elif value == 64:
        return (255, 255, 0)
    
    elif value == 128:
        return (255, 50, 145)
    
    elif value == 256:
        return (151, 181, 0)
    
    elif value == 512:
        return (94, 115, 255)
    
    elif value == 1024:
        return (237, 197, 63)
    
    elif value == 2048:
        return (237, 194, 46)
    
    else:
        return (255, 255, 255)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (195, 0, 0)
GREEN = (50, 149, 0)
LIGHT_BROWN = (255, 222, 162)
PURPLE = (150, 0, 195)
BACK_GROUND = (60, 164, 255)



def draw_nodes_with_colors(screen, linkedList):
    
    current = linkedList.head.next
    cell_size = 77
    font = pygame.font.Font("./Font/PinyonScript-Regular.ttf", 45)

    while current != None:
        x, y = get_cell_position(current.number)

        color = get_tile_color(current.value)
        pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))

        text = font.render(str(current.value), True, BLACK)
        text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
        screen.blit(text, text_rect)

        current = current.next
        

def show_alert(screen, message):
    WIDTH, HEIGHT = 600, 450
    
    font = pygame.font.Font("./Font/PinyonScript-Regular.ttf", 30)
    
    # Draw a semi-transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))  # Semi-transparent black
    screen.blit(overlay, (0, 0))

    # Alert box
    alert_width, alert_height = 400, 200
    alert_x, alert_y = (WIDTH - alert_width) // 2, (HEIGHT - alert_height) // 2
    pygame.draw.rect(screen, GRAY, (alert_x, alert_y, alert_width, alert_height))
    pygame.draw.rect(screen, BLACK, (alert_x, alert_y, alert_width, alert_height), 3)

    # Render the message
    text = font.render(message, True, PURPLE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    screen.blit(text, text_rect)
    
    font = pygame.font.Font(None, 36)
    
    # OK Button
    button_width, button_height = 100, 40
    button_x, button_y = WIDTH // 2 - button_width // 2, HEIGHT // 2 + 40
    pygame.draw.rect(screen, RED, (button_x, button_y, button_width, button_height))
    pygame.draw.rect(screen, BLACK, (button_x, button_y, button_width, button_height), 3)
    button_text = font.render("OK", True, WHITE)
    button_text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(button_text, button_text_rect)

    pygame.display.flip()

    # Wait for user to click OK
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    return  # Close the alert
                
def random_append(game, sw_random_append, first_add_node):
    # Define the numbers and their corresponding probabilities
    numbers = [2, 4]
    weights = [70, 30]
    
    # Generate a random choice with the given probabilities
    value_created_with_chance = random.choices(numbers, weights=weights, k=1)[0]
    if first_add_node:
        value_created_with_chance_2 = random.choices(numbers, weights=weights, k=1)[0]
    
    
    attempts = 0
    maxAttempts = 50
        
    while sw_random_append == True:
        
        # Generate a random integer between 1 and 16 (inclusive)
        node_number_created_with_chance = random.randint(1, 16)
        if first_add_node:
            node_number_created_with_chance_2 = random.randint(1, 16)
        
        if game.check_node_empty(node_number_created_with_chance) == True:
            game.add_node(node_number_created_with_chance, value_created_with_chance)
            if first_add_node:
                if game.check_node_empty(node_number_created_with_chance_2) == True:
                    game.add_node(node_number_created_with_chance_2, value_created_with_chance_2)
                    first_add_node = False
            if first_add_node == False:
                sw_random_append = False
        
        attempts += 1
        # avoid to infinity loop
        if attempts > maxAttempts:
            sw_random_append = False
    
    return sw_random_append, first_add_node
            



pygame.init()
screen_width = 600
screen_height = 450

screen_welcome = pygame.display.set_mode((screen_width, screen_height))
screen_game = pygame.display.set_mode((screen_width, screen_height))
# screen_Game_Over = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("2048")
clock = pygame.time.Clock()


play_button_color = (70, 130, 180)
play_button_hover_color = (100, 149, 237)
play_button_shadow_color = (40, 80, 150)
play_text_color = (255, 255, 255)
play_button_x, play_button_y = 250, 100
play_button_width, play_button_height = 100, 60

ai_button_color = (70, 130, 180)
ai_button_hover_color = (100, 149, 237)
ai_button_shadow_color = (40, 80, 150)
ai_text_color = (255, 255, 255)
ai_button_x, ai_button_y = 250, 300
ai_button_width, ai_button_height = 100, 60




undo_button_color = (70, 130, 180)
undo_button_hover_color = (100, 149, 237)
undo_button_shadow_color = (40, 80, 150)
undo_text_color = (255, 255, 255)
undo_button_x, undo_button_y = 450, 100
undo_button_width, undo_button_height = 100, 60

redo_button_color = (70, 130, 180)
redo_button_hover_color = (100, 149, 237)
redo_button_shadow_color = (40, 80, 150)
redo_text_color = (255, 255, 255)
redo_button_x, redo_button_y = 450, 300
redo_button_width, redo_button_height = 100, 60

font = pygame.font.Font(None, 36)


game = LinkedList()
save_for_undo = Deque()
save_for_redo = Deque()
ai_player = AI(game, simulations_per_move=1000)

number_can_undo = 5
number_can_redo = 5

Welcome = True
Play = False
AI_Mode = False
sw_random_append = True
Game_Over = False

first_add_node = True


while Welcome:
    
    screen_welcome.fill(BACK_GROUND)
    
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        Welcome = False
        
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (play_button_x <= mouse_x <= play_button_x + play_button_width and
            play_button_y <= mouse_y <= play_button_y + play_button_height):
            
            Welcome = False
            Play = True
                
        elif (ai_button_x <= mouse_x <= ai_button_x + ai_button_width and
            ai_button_y <= mouse_y <= ai_button_y + ai_button_height):
            
            Welcome = False
            AI_Mode = True
        
    
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # button for Play user
    
    is_hovered = (play_button_x <= mouse_x <= play_button_x + play_button_width and
                  play_button_y <= mouse_y <= play_button_y + play_button_height)

    current_button_color = play_button_hover_color if is_hovered else play_button_color

    pygame.draw.rect(screen_welcome, current_button_color,
                     (play_button_x, play_button_y, play_button_width, play_button_height), border_radius=10)

    border_color = (255, 255, 255)
    border_thickness = 2
    pygame.draw.rect(screen_welcome, border_color,
                     (play_button_x, play_button_y, play_button_width, play_button_height), border_radius=10, width=border_thickness)

    play_text = font.render("Play", True, undo_text_color)
    play_text_rect = play_text.get_rect(center=(play_button_x + play_button_width // 2, play_button_y + play_button_height // 2))
    screen_welcome.blit(play_text, play_text_rect)
    
    
   
   # button for AI
    
    is_hovered = (ai_button_x <= mouse_x <= ai_button_x + ai_button_width and
                  ai_button_y <= mouse_y <= ai_button_y + ai_button_height)

    current_button_color = ai_button_hover_color if is_hovered else ai_button_color

    pygame.draw.rect(screen_welcome, current_button_color,
                     (ai_button_x, ai_button_y, ai_button_width, ai_button_height), border_radius=10)

    border_color = (255, 255, 255)
    border_thickness = 2
    pygame.draw.rect(screen_welcome, border_color,
                     (ai_button_x, ai_button_y, ai_button_width, ai_button_height), border_radius=10, width=border_thickness)

    ai_text = font.render("AI", True, ai_text_color)
    ai_text_rect = ai_text.get_rect(center=(ai_button_x + ai_button_width // 2, ai_button_y + ai_button_height // 2))
    screen_welcome.blit(ai_text, ai_text_rect)
    
        
        
    pygame.display.flip()
    clock.tick(60)
        


while AI_Mode:
    
    pygame.event.pump()

    best_move = ai_player.find_best_move()

    first_state = game.to_array()

    if best_move == 'UP':
        game.move_up()
    elif best_move == 'DOWN':
        game.move_down()
    elif best_move == 'LEFT':
        game.move_left()
    elif best_move == 'RIGHT':
        game.move_right()

    if game.has_changed(first_state):
        sw_random_append = True
        
        
    if game.has_won() == True:
        show_alert(screen_game, "You won!")
    elif game.has_won() == False:
        show_alert(screen_game, "Game over!")
        
            
    sw_random_append, first_add_node = random_append(game, sw_random_append, first_add_node)


    screen_game.fill(BACK_GROUND)
    cell_size = 85
    for row in range(4):
        for col in range(4):
            x = 50 + (col * cell_size)
            y = 50 + (row * cell_size)
            pygame.draw.rect(screen_game, PURPLE, (x, y, cell_size, cell_size), 5)

    draw_nodes_with_colors(screen_game, game)
    
    # display score of user
    font = pygame.font.Font(None, 36)
    score_text = f"Score: {game.get_score()}"
    score_surface = font.render(score_text, True, (0, 0, 0))
    screen_game.blit(score_surface, (450, 200))

    pygame.display.flip()
    clock.tick(10)

    

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
                
        elif event.key == pygame.K_DOWN:
            save_for_undo.save_state(game)
            game.move_down()
            if game.has_changed(first_state) == True:
                sw_random_append = True
            
        elif event.key == pygame.K_LEFT:
            save_for_undo.save_state(game)
            game.move_left()
            if game.has_changed(first_state) == True:
                sw_random_append = True
            
        elif event.key == pygame.K_RIGHT:
            save_for_undo.save_state(game)
            game.move_right()
            if game.has_changed(first_state) == True:
                sw_random_append = True
        
        
                
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (undo_button_x <= mouse_x <= undo_button_x + undo_button_width and
            undo_button_y <= mouse_y <= undo_button_y + undo_button_height):
            if number_can_undo > 0:
                save_for_redo.save_state(game)
                save_for_undo.put_back(game)
                number_can_undo -= 1
            else:
                show_alert(screen_game, "You have reached the limit of undo!")
                
        elif (redo_button_x <= mouse_x <= redo_button_x + redo_button_width and
            redo_button_y <= mouse_y <= redo_button_y + redo_button_height):
            if number_can_redo > 0:
                save_for_redo.put_back(game)
                number_can_redo -= 1
            else:
                show_alert(screen_game, "You have reached the limit of redo!")
                

    
    if game.has_won() == True:
        show_alert(screen_game, "You won!")
    elif game.has_won() == False:
        show_alert(screen_game, "Game over!")
        
            
    sw_random_append, first_add_node = random_append(game, sw_random_append, first_add_node)
    
    
    screen_game.fill(BACK_GROUND)
    
        
    cell_size = 85
    for row in range(4):
        for col in range(4):
            x = 50 + (col * cell_size)
            y = 50 + (row * cell_size)
            pygame.draw.rect(screen_game, PURPLE, (x, y, cell_size, cell_size), 5)
            
            
    pygame.draw.rect(screen_game, PURPLE, (40, 40, 360, 360), 10) # x, y, width, height

    draw_nodes_with_colors(screen_game, game)
    
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # button for undo
    
    is_hovered = (undo_button_x <= mouse_x <= undo_button_x + undo_button_width and
                  undo_button_y <= mouse_y <= undo_button_y + undo_button_height)

    current_button_color = undo_button_hover_color if is_hovered else undo_button_color

    pygame.draw.rect(screen_game, current_button_color,
                     (undo_button_x, undo_button_y, undo_button_width, undo_button_height), border_radius=10)

    border_color = (255, 255, 255)
    border_thickness = 2
    pygame.draw.rect(screen_game, border_color,
                     (undo_button_x, undo_button_y, undo_button_width, undo_button_height), border_radius=10, width=border_thickness)

    undo_text = font.render("Undo", True, undo_text_color)
    undo_text_rect = undo_text.get_rect(center=(undo_button_x + undo_button_width // 2, undo_button_y + undo_button_height // 2))
    screen_game.blit(undo_text, undo_text_rect)
    
    
    # button for redo
    
    is_hovered = (redo_button_x <= mouse_x <= redo_button_x + redo_button_width and
                  redo_button_y <= mouse_y <= redo_button_y + redo_button_height)

    current_button_color = redo_button_hover_color if is_hovered else redo_button_color

    pygame.draw.rect(screen_game, current_button_color,
                     (redo_button_x, redo_button_y, redo_button_width, redo_button_height), border_radius=10)

    border_color = (255, 255, 255)
    border_thickness = 2
    pygame.draw.rect(screen_game, border_color,
                     (redo_button_x, redo_button_y, redo_button_width, redo_button_height), border_radius=10, width=border_thickness)

    redo_text = font.render("Redo", True, redo_text_color)
    redo_text_rect = redo_text.get_rect(center=(redo_button_x + redo_button_width // 2, redo_button_y + redo_button_height // 2))
    screen_game.blit(redo_text, redo_text_rect)
    
    
    # display score of user
    font = pygame.font.Font(None, 36)
    score_text = f"Score: {game.get_score()}"
    score_surface = font.render(score_text, True, (0, 0, 0))
    screen_game.blit(score_surface, (450, 200))

    
    pygame.display.flip()
    clock.tick(60)
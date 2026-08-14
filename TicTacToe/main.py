import pygame
import time
import sys
import os

# TODO: Add different themes

def kaynak_yolu(dosya):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, dosya)
    return os.path.join(os.path.abspath("."), dosya)

pygame.init()
click_sound = pygame.mixer.Sound(kaynak_yolu("click.wav"))
game_over_sound = pygame.mixer.Sound(kaynak_yolu("game over.mp3"))
block_size = 200
screen = pygame.display.set_mode((block_size*3, block_size*3))
clock = pygame.time.Clock()
running = True
grid_color = (230, 230, 230)
x_color = (200, 0, 50)
o_color = (0, 50, 200)
char_width = 15
grid_distance = 20
game_finished = False
line_color = (0,0,0)
line_width = 15
whos_turn = True
font = pygame.font.SysFont("Corbel", 40)
font_color = (230, 230, 230)
bg = (40, 40, 40)
button_color = (100, 100, 100)
light_button_color = (200, 200, 200)
in_game = False
in_game_bot = False

map = [
    [None]*3,
    [None]*3,
    [None]*3
]

def is_game_finished():
    global game_finished, line_start, line_end, whowin
    if map[0][0] == map[1][1] == map[2][2] and map[0][0] is not None:
        line_start = (block_size // 2, block_size // 2)
        line_end = (block_size*5 // 2, block_size*5 // 2)
        game_finished = True
        if map[0][0] == 0:
            print("X Wins!")
        else:
            print("O Wins!")
    elif map[0][0] == map[1][0] == map[2][0] and map[0][0] is not None:
        line_start = (block_size // 2, block_size // 2)
        line_end = (block_size // 2, block_size*5 // 2)
        game_finished = True
        if map[0][0] == 0:
            print("X Wins!")
        else:
            print("O Wins!")
    elif map[0][0] == map[0][1] == map[0][2] and map[0][0] is not None:
        line_start = (block_size // 2, block_size // 2)
        line_end = (block_size*5 // 2, block_size // 2)
        game_finished = True
        if map[0][0] == 0:
            print("X Wins!")
        else:
            print("O Wins!")
    elif map[0][1] == map[1][1] == map[2][1] and map[1][1] is not None:
        line_start = (block_size*3 // 2, block_size // 2)
        line_end = (block_size*3 // 2, block_size*5 // 2)
        game_finished = True
        if map[1][1] == 0:
            print("X Wins!")
        else:
            print("O Wins!")
    elif map[1][0] == map[1][1] == map[1][2] and map[1][1] is not None:
        line_start = (block_size // 2, block_size*3 // 2)
        line_end = (block_size*5 // 2, block_size*3 // 2)
        game_finished = True
        if map[1][1] == 0:
            print("X Wins!")
        else:
            print("O Wins!")
    elif map[2][2] == map[1][2] == map[0][2] and map[0][2] is not None:
        line_start = (block_size*5 // 2, block_size // 2)
        line_end = (block_size*5 // 2, block_size*5 // 2)
        game_finished = True
        if map[0][2] == 0:
            print("X Wins!")
        else:
            print("O Wins!")
    elif map[0][2] == map[1][1] == map[2][0] and map[0][2] is not None:
        line_start = (block_size*5 // 2, block_size // 2)
        line_end = (block_size // 2, block_size*5 // 2)
        game_finished = True
        if map[0][2] == 0:
            print("X Wins!")
        else:
            print("O Wins!")
    elif map[2][2] == map[2][1] == map[2][0] and map[2][2] is not None:
        line_start = (block_size // 2, block_size*5 // 2)
        line_end = (block_size*5 // 2, block_size*5 // 2)
        game_finished = True
        if map[2][2] == 0:
            print("X Wins!")
        else:
            print("O Wins!")
    elif map[0][0] is not None and map[0][1] is not None and map[0][2] is not None and map[1][0] is not None and map[1][1] is not None and map[1][2] is not None and map[2][0] is not None and map[2][1] is not None and map[2][2] is not None:
        game_finished = True
        print("Draw!")
        
def game():
    global whos_turn, running, game_finished, in_game, in_game_bot
    pygame.display.set_caption("Tic-Tac-Toe!")
    while in_game and running and in_game_bot == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and game_finished == False:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_column = mouse_x // block_size
                mouse_row = mouse_y // block_size
                if map[mouse_row][mouse_column] is not None:
                    pass
                elif map[mouse_row][mouse_column] is None:
                    if whos_turn:
                        map[mouse_row][mouse_column] = 0
                        whos_turn = False
                        click_sound.play()
                        is_game_finished()
                        if game_finished:
                            game_over_sound.play()
                    else:
                        map[mouse_row][mouse_column] = 1
                        whos_turn = True
                        click_sound.play()
                        is_game_finished()
                        if game_finished:
                            game_over_sound.play()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_game = False
                    menu()

        screen.fill("gray")

        for row in range(3):
            for column in range(3):
                x = column*block_size
                y = row*block_size
                pygame.draw.rect(screen, grid_color, (x, y, block_size, block_size), 10)
                if map[row][column] == 0:
                    pygame.draw.line(screen, x_color, (x + grid_distance, y + grid_distance), (x + block_size - grid_distance, y + block_size - grid_distance), char_width)
                    pygame.draw.line(screen, x_color, (x + grid_distance, y + block_size - grid_distance), (x + block_size - grid_distance, y + grid_distance), char_width)
                elif map[row][column] == 1:
                    pygame.draw.circle(screen, o_color, (x + block_size//2, y + block_size//2), (block_size - grid_distance)//2, char_width)
                else:
                    pass
        try:  
            if game_finished:
                pygame.draw.line(screen, line_color, line_start, line_end, line_width)
        except:
            pass
        
        pygame.display.flip()    
        
        if game_finished:
            time.sleep(1.5)
            in_game = False    

        clock.tick(60)

def computer_move():
    global whos_turn, map
    whos_turn = False
    bestScore = -800
    bestMove = 0
    for satir in range(3):
        for sutun in range(3):
            if map[satir][sutun] is None:
                map[satir][sutun] = 0
                score = minimax(map, False)
                map[satir][sutun] = None
                if score > bestScore:
                    bestScore = score
                    bestMove = (satir, sutun)
    map[bestMove[0]][bestMove[1]] = 0
    return

def winner_check():
    if map[0][0] == map[1][1] == map[2][2] and map[0][0] is not None:
        if map[0][0] == 0:
            return 0
        else:
            return 1
    elif map[0][0] == map[1][0] == map[2][0] and map[0][0] is not None:
        if map[0][0] == 0:
            return 0
        else:
            return 1
    elif map[0][0] == map[0][1] == map[0][2] and map[0][0] is not None:
        if map[0][0] == 0:
            return 0
        else:
            return 1
    elif map[0][1] == map[1][1] == map[2][1] and map[1][1] is not None:
        if map[1][1] == 0:
            return 0
        else:
            return 1
    elif map[1][0] == map[1][1] == map[1][2] and map[1][1] is not None:
        if map[1][1] == 0:
            return 0
        else:
            return 1
    elif map[2][2] == map[1][2] == map[0][2] and map[0][2] is not None:
        if map[0][2] == 0:
            return 0
        else:
            return 1
    elif map[0][2] == map[1][1] == map[2][0] and map[0][2] is not None:
        if map[0][2] == 0:
            return 0
        else:
            return 1
    elif map[2][2] == map[2][1] == map[2][0] and map[2][2] is not None:
        if map[2][2] == 0:
            return 0
        else:
            return 1
    elif map[0][0] is not None and map[0][1] is not None and map[0][2] is not None and map[1][0] is not None and map[1][1] is not None and map[1][2] is not None and map[2][0] is not None and map[2][1] is not None and map[2][2] is not None:
        return 2

def minimax(map, isMaximizing):
    result = winner_check()
    try:
        if result == 0:
            return 1
        elif result == 1:
            return -1
        elif result == 2:
            return 0
    except:
        pass
    
    if isMaximizing:
        bestScore = -800
        for satir in range(3):
            for sutun in range(3):
                if map[satir][sutun] is None:
                    map[satir][sutun] = 0
                    score = minimax(map, False)
                    map[satir][sutun] = None
                    if score > bestScore:
                        bestScore = score
        return bestScore
    else:
        bestScore = 800
        for satir in range(3):
            for sutun in range(3):
                if map[satir][sutun] is None:
                    map[satir][sutun] = 1
                    score = minimax(map, True)
                    map[satir][sutun] = None
                    if score < bestScore:
                        bestScore = score
        return bestScore

def menu():
    global running, game_finished, map, in_game, in_game_bot, whos_turn
    pygame.display.set_caption("...")
    while in_game == False and in_game_bot == False and running:
        screen.fill(bg)
        mouse = pygame.mouse.get_pos()
        
        resume_button = pygame.Rect(100, 300, 400, 50)
        newgame_button = pygame.Rect(100, 380, 400, 50)
        bot_button = pygame.Rect(100, 460, 400, 50)
        
        pygame.draw.rect(screen, light_button_color if resume_button.collidepoint(mouse) else button_color, resume_button)
        pygame.draw.rect(screen, light_button_color if newgame_button.collidepoint(mouse) else button_color, newgame_button)
        pygame.draw.rect(screen, light_button_color if bot_button.collidepoint(mouse) else button_color, bot_button)
        
        resume_text = font.render("Resume", True, font_color)
        newgame_text = font.render("New Game", True, font_color)
        bot_text = font.render("Play Against Bot", True, font_color)
        
        screen.blit(resume_text, (235, 305))
        screen.blit(newgame_text, (215, 385))
        screen.blit(bot_text, (175, 465))
        
        text = font.render("Tic Tac Toe!", True, font_color)
        screen.blit(text, (205, 150))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_game = True
                    game()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if resume_button.collidepoint(mouse):
                    in_game = True
                    game()

                if newgame_button.collidepoint(mouse):
                    map = [
                        [None]*3,
                        [None]*3,
                        [None]*3
                    ]
                    game_finished = False
                    whos_turn = True
                    in_game = True
                    game()

                if bot_button.collidepoint(mouse):
                    map = [
                        [None]*3,
                        [None]*3,
                        [None]*3
                    ]
                    game_finished = False
                    whos_turn = True
                    in_game_bot = True
                    computer_game()

        pygame.display.flip()
        clock.tick(60)

def computer_game():
    global whos_turn, running, game_finished, in_game_bot, in_game
    pygame.display.set_caption("You Can't Beat Me!")
    while in_game_bot and running and in_game == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and game_finished == False:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_column = mouse_x // block_size
                mouse_row = mouse_y // block_size
                if map[mouse_row][mouse_column] is not None:
                    pass
                elif map[mouse_row][mouse_column] is None:
                    if whos_turn == False:
                        map[mouse_row][mouse_column] = 1
                        whos_turn = True
                        click_sound.play()
                        is_game_finished()
                        if game_finished:
                            game_over_sound.play()
                        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_game_bot = False
                    menu()
                    
        if whos_turn and not game_finished:
            computer_move()
            whos_turn = False
            is_game_finished()
            if game_finished:
                game_over_sound.play()

        screen.fill("gray")

        for row in range(3):
            for column in range(3):
                x = column*block_size
                y = row*block_size
                pygame.draw.rect(screen, grid_color, (x, y, block_size, block_size), 10)
                if map[row][column] == 0:
                    pygame.draw.line(screen, x_color, (x + grid_distance, y + grid_distance), (x + block_size - grid_distance, y + block_size - grid_distance), char_width)
                    pygame.draw.line(screen, x_color, (x + grid_distance, y + block_size - grid_distance), (x + block_size - grid_distance, y + grid_distance), char_width)
                elif map[row][column] == 1:
                    pygame.draw.circle(screen, o_color, (x + block_size//2, y + block_size//2), (block_size - grid_distance)//2, char_width)
                else:
                    pass
        try:  
            if game_finished:
                pygame.draw.line(screen, line_color, line_start, line_end, line_width)
        except:
            pass
        
        pygame.display.flip()    
        
        if game_finished:
            time.sleep(1.5)
            in_game_bot = False    

        clock.tick(60)

        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if in_game == False and in_game_bot == False:
        menu()
    else:
        if in_game and in_game_bot == False:
            game()
        elif in_game_bot and in_game == False:
            computer_game()

pygame.quit()

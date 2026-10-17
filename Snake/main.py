import pygame
from random import randrange

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True

SKY_BLUE = (153,255,255)
ANOTHER_BLUE = (153,204,255)
GREEN = (0,255,128)

def gridBackground():
    for row in range(11):
        pygame.draw.line(screen, ANOTHER_BLUE, (0,(row-1)*50), (500,(row-1)*50))
    for column in range(11):
        pygame.draw.line(screen, ANOTHER_BLUE, ((column-1)*50,0), ((column-1)*50,500))
        
snake = [[2,5], [1,5], [0,5]]
apple = [5,2]
snakeRotation = 'R'
skip = False

def resetApple():
    global apple, skip
    skip = True
    appleX = randrange(11)
    appleY = randrange(11)
    apple = [appleX,appleY] #rand yap
    

def drawSnake():
    global skip
    score = len(snake)
    snakeHeadPositionX = snake[0][0]
    snakeHeadPositionY = snake[0][1]
    
    if snakeRotation == 'R':
        snake.insert(0, [snakeHeadPositionX+1,snakeHeadPositionY])
    if snakeRotation == 'L':
        snake.insert(0, [snakeHeadPositionX-1,snakeHeadPositionY])
    if snakeRotation == 'D':
        snake.insert(0, [snakeHeadPositionX,snakeHeadPositionY+1])
    if snakeRotation == 'U':
        snake.insert(0, [snakeHeadPositionX,snakeHeadPositionY-1])
    
    if skip:
        pass
    else:
        snake.pop(score)
    
    skip = False
    
    for i in range(score):
        snakeBlockX = snake[i-1][0]
        snakeBlockY = snake[i-1][1]
        pygame.draw.rect(screen, GREEN,(snakeBlockX*50,snakeBlockY*50,50,50))
        if snakeBlockX == apple[0] and snakeBlockY == apple[1]:
            resetApple()
            
    pygame.draw.rect(screen, (255,0,0),(apple[0]*50,apple[1]*50,50,50))
    
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snakeRotation != 'R':
                snakeRotation = 'L'
            elif event.key == pygame.K_RIGHT and snakeRotation != 'L':
                snakeRotation = 'R'
            elif event.key == pygame.K_UP and snakeRotation != 'D':
                snakeRotation = 'U'
            elif event.key == pygame.K_DOWN and snakeRotation != 'U':
                snakeRotation = 'D'

    screen.fill(SKY_BLUE)
    gridBackground()
    drawSnake()
    pygame.display.flip()

    clock.tick(3)  # limits FPS to 60

pygame.quit()
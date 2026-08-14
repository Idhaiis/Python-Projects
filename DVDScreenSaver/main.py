import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

dvdSprite = pygame.transform.scale(pygame.image.load('w.png'), (200, 200))

pygame.mouse.set_visible(False)
pygame.display.toggle_fullscreen()

velocity = 3
velX = velocity
velY = velocity
cordX = 100
cordY = 400

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    if cordX < 0:
        velX = velocity
    if cordY < 0:
        velY = velocity
    if cordY + 200 > 1080:
        velY = -velocity
    if cordX + 200 > 1920:
        velX = -velocity
    
    cordX += velX
    cordY += velY
    
    # RENDER YOUR GAME HERE
    screen.fill("black")
    screen.blit(dvdSprite, pygame.rect.Rect(cordX, cordY, 200, 200))

    pygame.display.flip()

    clock.tick(60)  

pygame.quit()
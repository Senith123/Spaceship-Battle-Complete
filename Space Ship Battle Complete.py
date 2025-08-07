import pygame
import time
pygame.init()
#set dimensions of the screen
w = 1700
h = 1000
font = pygame.font.SysFont("Agency FB",36)
font1 = pygame.font.SysFont("Agnecy FB", 100)
rh = 100
yh = 100
rtext=font.render(str(rh),True,(255,0,0))
ytext=font.render(str(yh),True,(255,255,0))
screen = pygame.display.set_mode((w,h))
redx = 150
redy = 450
yelx = 1400
yely = 450
pic1 = pygame.image.load("BG.png")
pic2 = pygame.image.load("Red Spaceship.png")
pic2 = pygame.transform.scale(pic2,(150,150))
pic2 = pygame.transform.rotate(pic2,90)
pic3 = pygame.image.load("Yellow Spaceship.png")
pic3 = pygame.transform.scale(pic3,(150,150))
pic3 = pygame.transform.rotate(pic3,270)
red = pygame.Rect(redx,redy,150,150)
yel = pygame.Rect(yelx,yely,150,150)
redb = []
yelb = []
run = True
while run:
    screen.blit(pic1,(0,0))
    screen.blit(pic2,(red.x,red.y))
    screen.blit(pic3,(yel.x,yel.y))
    rtext=font.render(str(rh),True,(255,0,0))
    ytext=font.render(str(yh),True,(255,255,0))
    screen.blit(rtext,(100,100))
    screen.blit(ytext,(1600,100))
    pygame.draw.rect(screen,"white",(830,0,20,1000))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(red.x + 150,red.y + 75,10,5)
                redb.append(bullet)
            if event.key == pygame.K_q:
                bullet = pygame.Rect(yel.x + 0,yel.y + 75,10,5)
                yelb.append(bullet)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and red.y < h-150:
        red.y += 5
    if keys[pygame.K_UP] and red.y > 0:
        red.y -= 5
    if keys[pygame.K_LEFT] and red.x > 0:
        red.x -= 5
    if keys[pygame.K_RIGHT] and red.x < 830-150:
        red.x += 5
    if keys[pygame.K_s] and yel.y < h-150:
        yel.y += 5
    if keys[pygame.K_w] and yel.y > 0:
        yel.y -= 5
    if keys[pygame.K_a] and yel.x > 830:
        yel.x -= 5
    if keys[pygame.K_d] and yel.x < w-150:
        yel.x += 5
    for bullet in redb:
        pygame.draw.rect(screen,"red",bullet)
        bullet.x += 5
        if bullet.colliderect(yel):
            redb.remove(bullet)
            yh -= 5
    for bullet in yelb:
        pygame.draw.rect(screen,"yellow",bullet)
        bullet.x -= 5
        if bullet.colliderect(red):
            yelb.remove(bullet)
            rh -= 5
    if rh <= 0:
        ywt=font1.render("Yellow Wins!",True,(255,255,0))
        screen.blit(ywt,(724,500))
        pygame.display.update()
        time.sleep(5)
        break
    if yh <= 0:
        rwt=font1.render("Red Wins!",True,(255,0,0))
        screen.blit(rwt,(724,500))
        pygame.display.update()
        time.sleep(5)
        break
    pygame.display.update()
    

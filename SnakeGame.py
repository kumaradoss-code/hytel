# Snake Game
import pygame
import time
import sys
import random
restart=1
check_error=pygame.init()
if check_error[1]>0:
    print('Found{0} an error'.format(check_error[1]))
    sys.exit(-1)
else:
    print('Game is successfully executed')
playsurface=pygame.display.set_mode((720,460))
pygame.display.set_caption('Snake Game')
#colour
red=(255,0,0) #game over
green=(0,255,0) #snake
blue=(0,0,255) #score
white=(255,255,255) #background
black=(0,0,0) #food
#fps
fpsController=pygame.time.Clock()
snakepos=[100,50]
snakebody=[[100,50],[90,50],[80,50]]
foodpos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodspawn=True
direction="RIGHT"
change_to=direction
score=0
playsurface.fill(white)
pfont=pygame.font.SysFont('monoco',35)
pSurf=pfont.render('SNAKE GAME',True,blue)
pRect=pSurf.get_rect()
pRect.midtop=(360,200)
playsurface.blit(pSurf,pRect)
pygame.display.flip()
time.sleep(3)
def gameOver():
    gfont=pygame.font.SysFont('monoco',72)
    gsurf=gfont.render('GAME OVER',True,red)
    grect=gsurf.get_rect()
    grect.midtop=(360,15)
    playsurface.blit(gsurf,grect)
    showScore(0)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit() #pygame exit
    sys.exit() #console exit
#showscore
def showScore(choice=1):
    sFont=pygame.font.SysFont('arial',24)
    sfFont=pygame.font.SysFont('monoco',42)
    ssurf=sFont.render('score:{0}'.format(score),True,black)
    srect=ssurf.get_rect()
    if choice==1:
        srect.midtop=(40,10)
    else:
        ssurf=sfFont.render('score:{0}'.format(score),True,black)
        srect.midtop=(340,120)
    playsurface.blit(ssurf,srect)
#Main logic of the game
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                change_to='RIGHT'
            if event.key==pygame.K_LEFT:
                change_to='LEFT'
            if event.key==pygame.K_UP:
                change_to='UP'
            if event.key==pygame.K_DOWN:
                change_to='DOWN'
            if event.key==pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
#validating the direction
    if change_to=='RIGHT' and not direction=='LEFT':
        direction='RIGHT'
    if change_to=='LEFT' and not direction=='RIGHT':
        direction='LEFT'
    if change_to=='UP' and not direction=='DOWN':
        direction='UP'
    if change_to=='DOWN' and not direction=='UP':
        direction='DOWN'
#More on direction
    if direction=='RIGHT':
        snakepos[0]+=10
    if direction=='LEFT':
        snakepos[0]-=10
    if direction=='UP':
        snakepos[1]-=10
    if direction=='DOWN':
        snakepos[1]+=10
#snake mechanics
    snakebody.insert(0,list(snakepos))
    if snakepos[0]==foodpos[0] and snakepos[1]==foodpos[1]:
        score+=1
        foodspawn=False
    else:
        snakebody.pop()
    if foodspawn==False:
        foodpos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodspawn=True
#drawings
    playsurface.fill(white)
    for pos in snakebody:
       pygame.draw.rect(playsurface,green,pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(playsurface,blue,pygame.Rect(foodpos[0], foodpos[1], 10, 10))

    if snakepos[0]>710 or snakepos[0]<0:
        gameOver()
    if snakepos[1]>450 or snakepos[1]<0:
        gameOver()
    for block in snakebody[1:]:
        if snakepos[0]==block[0] and snakepos[1]==block[1]:
            gameOver()
    showScore()
    pygame.display.flip()
    fpsController.tick(20)














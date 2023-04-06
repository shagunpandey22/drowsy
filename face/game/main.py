import pygame as pg
import sys
import random
import math
pg.init()  #intialize
screen=pg.display.set_mode((1000,800))
#background
bmig=pg.image.load('space.jpg')
pg.display.set_caption('GAME')
img=pg.image.load('icon.png')
pg.display.set_icon(img)
x=370
y=630
x1=0
#adding and subtracting the values from the coordinates of the player image we can create the movement
#score
score=0
font=pg.font.Font('freesansbold.ttf',32)
textx=10
texty=10
def show(x,y):
    s=font.render("SCORE: "+str(score),True,(255,255,255))
    screen.blit(s,(x,y))

pimg=pg.image.load('r1.png')
def player(x,y): #creating the player
    screen.blit(pimg,(x,y)) #to make image appear on the screem



#enemy
eimg=[]
ex=[]
ey=[]
e1=[]
e2=[]

num_of_enemy=6
for i in range(num_of_enemy):
    eimg.append(pg.image.load('enemy.png'))
    ex.append(random.randint(0,800))   #randomly generate the position of the enemy on the screen
    ey.append(random.randint(50,150))
    e1.append(0.3)
    e2.append(40)  #move down by 40 px  

#bullet
buimg=pg.image.load('bullet.png')
bux=0   
buy=630  
bu1=0
bu2=10
bs="ready"   #you cant see bullet on screen


def fire_bullet(x,y):
    global bs
    bs="fire" #in motion
    screen.blit(buimg,(x+16,y+10))


def iscollision(ex,ey,bux,buy):
    distance=math.sqrt(math.pow((ex-bux),2)+math.pow((ey-buy),2))
    if distance<27:
        return True
    else:
        return False
def enemy(ex,ey,i):
    screen.blit(eimg[i],(ex,ey)) 



while 1:
    screen.fill((0,0,0)) #background image
    #background iamge
    screen.blit(bmig,(0,0))
    #x=x-0.1  #creating the movement
    #y=y-0.1 
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
        #if keyst oke is pressed check whther its right or left 
        if event.type==pg.KEYDOWN:   #if key is pressed 
            #print("KEY PRESSED") 
            if event.key==pg.K_LEFT:  #left arrow key 
                #print("LEFT PRESSED")
                x1=-5
            if event.key==pg.K_RIGHT: #right arrow key
                #print("RIGHT PRESSED")
                x1=5
            if event.key==pg.K_SPACE:
                if bs is "ready":
                    bx=x
                    fire_bullet(bx,buy)
        if event.type==pg.KEYUP: #if key is released 
               if event.key==pg.K_LEFT or event.key==pg.K_RIGHT:
                   #print("RELEASED")
                   x1=0
    x=x+x1 #player moment
    #creating the boundary of the game screen
    if x<=0:
        x=0
    elif x>=736:
        #800-64 px
        x=736
    #same for enemy protectiong it from boundary
    for i in range(num_of_enemy):
        ex[i]=ex[i]+e1[i] 
        if ex[i]<=0: 
            e1[i]=0.3
            ey[i]=ey[i]+e2[i]
        elif ex[i]>=736:
            e1[i]=-0.3
            ey[i]=ey[i]+e2[i]
        #collision
        collision=iscollision(ex[i],ey[i],bux,buy)
        if collision:
            buy=630
            bs="ready"
            #score=score+1
            #print(score)
            ex[i]=random.randint(0,800)   #randomly generate the position of the enemy on the screen
            ey[i]=random.randint(50,150) 
        enemy(ex[i],ey[i],i) 
    #bulletmovement
    if buy<=0: #multiple bullets
        buy=480
        bs="ready"
    if bs is "fire":
        fire_bullet(bx,buy)
        buy=buy-bu2
    
    
    player(x,y)
    show(textx,texty)
    
    pg.display.update() #updating the screen
 
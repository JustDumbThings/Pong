from cmath import sin
from math import cos
import pygame
from pygame.locals import*
import numpy.matlib 


pygame.init()

black   = ( 0, 0, 0)

ScreenWidth = 1500
ScreenHight = 1000 
screen = pygame.display.set_mode((ScreenWidth, ScreenHight))
pygame.display.set_caption("Spin")
GameRun = True

clock = pygame.time.Clock()

PaddleWith = 10
Paddle_Hight = 300
Paddle_R_X = ScreenWidth - PaddleWith - 10
Paddle_L_Y = ScreenHight / 2 - Paddle_Hight / 2
Paddle_L_X = 10
Paddle_R_Y = ScreenHight / 2 - Paddle_Hight / 2


BallRad = 2
BallX = ScreenWidth / 2 - BallRad 
BallY = ScreenHight / 2 - BallRad
VelocityY = 5
VelocityX = 5

def KeyListener():

    global GameRun, Paddle_L_Y, Paddle_R_Y, BallY

    keys = pygame.key.get_pressed()
    
    # Reaktion auf das Drücken der Tasten
    if keys[pygame.K_w]:
        Paddle_L_Y -= 10
    if keys[pygame.K_s]:
        Paddle_L_Y += 10
    if keys[pygame.K_UP]:
        Paddle_R_Y -= 10
    if keys[pygame.K_DOWN]:
        Paddle_R_Y += 10
    

    # Reaktion auf das Loslassen der Tasten (optional)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRun = False
        elif keys[pygame.K_ESCAPE]:
            GameRun = False
    

def Reset():
    global PaddleWith, Paddle_Hight, ScreenWidth, Paddle_R_X, Paddle_R_Y, Paddle_L_X, Paddle_L_Y, BallRad, BallX, BallY, VelocityX, VelocityY

  
  
    Paddle_L_Y = ScreenHight / 2 - Paddle_Hight / 2
  
    Paddle_R_Y = ScreenHight / 2 - Paddle_Hight / 2


    
    BallX = ScreenWidth / 2 - BallRad 
    BallY = ScreenHight / 2 - BallRad
    VelocityY = 1
    VelocityX = 1
    

    

def Redraw_Paddle():
    global Paddle_R_X, Paddle_L_X, PaddleWith, Pddle_Hight, Paddle_L_Y, Paddle_R_Y
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(Paddle_L_X, Paddle_L_Y, PaddleWith, Paddle_Hight))
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(Paddle_R_X, Paddle_R_Y, PaddleWith, Paddle_Hight))
    

def DrawBall():
    global BallY, BallX, Paddle_R_Y, Paddle_L_Y, Paddle_Hight

    VelocityX, VelocityY = Coll()

    BallX = BallX + VelocityX

    BallY = BallY + VelocityY

    pygame.draw.circle(screen, (255,255,255), (BallX, BallY ), BallRad)

def Coll():
    global PaddleWith, Paddle_Hight, ScreenWidth, Paddle_R_X, Paddle_R_Y, Paddle_L_X, Paddle_L_Y, BallRad, BallX, BallY, VelocityX, VelocityY
  
    if BallX + BallRad >= Paddle_R_X:
        CalcVelocity(Paddle_R_Y)
        BallX =  Paddle_R_X - BallRad - 1
        if  BallY < Paddle_R_Y:
            
            Reset()
        elif BallY > Paddle_R_Y + Paddle_Hight:
            
            Reset()
    if BallX - BallRad <= Paddle_L_X + PaddleWith:
        CalcVelocity(Paddle_L_Y)
        BallX =  Paddle_L_X + PaddleWith + BallRad + 1
        if  BallY < Paddle_L_Y:
            
            Reset()
        elif BallY > Paddle_L_Y + Paddle_Hight:
            
            Reset()

    if BallY - BallRad < 0 or BallY + BallRad > ScreenHight:
        VelocityY = -VelocityY


    return VelocityX, VelocityY

def CalcVelocity(Paddle_Y):
    global VelocityY, VelocityX, Paddle_Hight
    VelocityX += 1
    VelocityX = -VelocityX
    
    VelocityY = - (( (Paddle_Y + Paddle_Hight / 2) - BallY ) / (Paddle_Hight / 2)) * abs(VelocityX)
    
    print(VelocityY, (Paddle_Y + Paddle_Hight / 2) - BallY , Paddle_Y)
    

   


while GameRun:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
   
    KeyListener()
    
    
  

    screen.fill(black)

    # Spielfeld/figuren zeichnen
    
    Redraw_Paddle()
    DrawBall()
    buffer = pygame.surfarray.array3d(screen)

    
    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(120)

    

pygame.quit()





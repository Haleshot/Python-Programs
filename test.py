#Project XII A

#Import library

import pygame
import random
import time
import math
import os
from pygame.locals import *
import sys
import turtle
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

#Creating the Button (Start Menu)

def process():
    pygame.init()

def Rules():
    button = tk.Toplevel()
    button.geometry("1366x768")
    Rules_img = ImageTk.PhotoImage(Image.open("G:/Old_Laptop_Documents/Class 12 Project All Files/Project Files/Images/RULES_Project.jpg"))
    l = Label(button, image = Rules_img)
    l.pack()
    button. mainloop()

def Restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def Button1():
    button = tk.Tk()
    button. geometry("1366x768")

    #Start Screen Image
    img = ImageTk.PhotoImage(Image.open("G:/Old_Laptop_Documents/Class 12 Project All Files/Project Files/Images/R8b2ce7d31e7ae8ce5fccc77b0e92067e.jpg"))
    l = Label(image = img)
    l.pack()
    
    #Start Button
    b1 = Button(button, text = "START", width = 40, height = 9, bg = "green", command = button.destroy)
    b1.place(relx = 0.5, rely = 0.25, anchor = CENTER)

    #Rules Button
    b2 = Button(button, text = "RULES", width = 30, height = 5, bg = "cyan", command = Rules)
    b2.place(relx = 0.5, rely = 0.45, anchor = CENTER)

    #Quit Button
    b3 = Button(button, text = "QUIT", width = 20, height = 4,  bg = "red",   command = quit)
    b3.place(relx = 0.5, rely = 0.65, anchor = CENTER)

    button .mainloop()

def Button2():
    button = tk.Tk()
    button. geometry("1366x768")

    #Start Screen Image
    img = ImageTk.PhotoImage(Image.open("G:/Old_Laptop_Documents/Class 12 Project All Files/Project Files/Images/R8b2ce7d31e7ae8ce5fccc77b0e92067e.jpg"))
    l = Label(image = img)
    l.pack()
    
    #Start Button
    b1 = Button(button, text = "RESTART", width = 40, height = 9, bg = "green", command = Restart)
    b1.place(relx = 0.5, rely = 0.25, anchor = CENTER)

    #Rules Button
    b2 = Button(button, text = "RULES", width = 30, height = 5, bg = "cyan", command = Rules)
    b2.place(relx = 0.5, rely = 0.45, anchor = CENTER)

    #Quit Button
    b3 = Button(button, text = "QUIT", width = 20, height = 4,  bg = "red",   command = quit)
    b3.place(relx = 0.5, rely = 0.65, anchor = CENTER)

    button .mainloop()

Button1()

#Centering the Screen for Python
os.environ['SDL_VIDEO_WINDOW_POS'] = "1"

#Processing all the modules

process()



#Creating Screen
width, height = 1366, 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paddles Or Balls?")

#Creating Colors
Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 255)
Green = (0, 128, 0)


#text color
text_color = (0, 0, 255)


#Creating Ball Size
BALL_SIZE = 25

#Paddle Coord
Paddle1 = pygame.rect.Rect((640, 135, 90, 15))
Paddle2 = pygame.rect.Rect((640, 633, 90, 15))


#To Create the Ball and give it speed and Direction
class Ball(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0

    def Make_Ball(self):
        ball = Ball()
        ball.x =random.randrange(BALL_SIZE, width-BALL_SIZE)
        ball.y =random.randrange(BALL_SIZE, height-BALL_SIZE)
        ball.dx =random.randrange(-2 ,3)
        ball.dy =random.randrange(-2, 3)
    
    def draw(self, surface):
        pygame.draw.circle(screen, (12, 155, 126), (circle_x, circle_y), 8)


        
#Object Created to Use Class
pong = Ball()

#To Calculate Frame Rendering of Screen
clock = pygame.time.Clock()

#To Create the Players(Paddles)
class Player(object):
    def __init__(self):
        Paddle1 = pygame.rect.Rect((640, 11.5, 90, 15))
        Paddle2 = pygame.rect.Rect((640, 640, 90, 15))

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        a = 7
        
        if key[pygame.K_LEFT]:
           Paddle1.move_ip(-a, 0)
           
        if key[pygame.K_RIGHT]:
           Paddle1.move_ip(a, 0)

        if key[pygame.K_a]:
           Paddle2.move_ip(-a, 0)

        if key[pygame.K_d]:
           Paddle2.move_ip(a, 0)

        #if key[pygame.K_SPACE]:
            #ball.move_ip(0, 500)
            
            
    def draw(self, surface):
        pygame.draw.rect(screen, (255, 215, 0), Paddle1)
        pygame.draw.rect(screen, (255, 215, 0), Paddle2)

Score1 = 0
Score2 = 0


#Object Created to Use Class
player = Player()

#To Calculate Frame Rendering of Screen
clock = pygame.time.Clock()

#Initialising Variable Coordinates for Text Boxes
X1 = 68
Y1 = 25
X2 = 68
Y2 = 409
X3 = 1250
Y3 = 25
X4 = 1250
Y4 = 409
X5 = 1340
Y5 = 25
X6 = 1340
Y6 = 409


#Creating Text Box For Player 1
font = pygame.font.SysFont('Comic Sans MS', 34)
text1 = font.render('Player 1', True, Blue)
textRect1 = text1.get_rect()
textRect1.center = (X1, Y1)

#Creating Text Box For Player 2
font = pygame.font.SysFont('Comic Sans MS', 34)
text2 = font.render('Player 2', True, Blue)
textRect2 = text2.get_rect()
textRect2.center = (X2, Y2)

#Creating Text Box for Score 1
font = pygame.font.SysFont('Comic Sans MS', 34)
text3 = font.render('SCORE = ', True, Blue)
textRect3 = text3.get_rect()
textRect3.center = (X3, Y3)

#Creating Text Box for Score 2
font = pygame.font.SysFont('Comic Sans MS', 34)
text4 = font.render('SCORE = ', True, Blue)
textRect4 = text4.get_rect()
textRect4.center = (X4, Y4)


move_x = 0
move_y = 0

some1 = True
some2 = True

Repeat = True

circle_x = width//2  #683
circle_y = height//2 #384

#Loop Count Variable
lcnt = 0

running = True
if lcnt == 0:
    lcnt += 1
    while running:
        if Repeat == True:
                c_x, c_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                        exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        move_x, move_y = random.randint(-3, 3), random.randint(-3, 3)

        circle_x += move_x
        circle_y += move_y

        #Creating Text Box for Score Value 1
        font = pygame.font.SysFont('Comic Sans MS', 34)
        text5 = font.render(str(Score1), True, Blue)
        textRect5 = text5.get_rect()
        textRect5.center = (X5, Y5)

        #Creating Text Box for Score Value 2
        font = pygame.font.SysFont('Comic Sans MS', 34)
        text6 = font.render(str(Score2), True, Blue)
        textRect6 = text6.get_rect()
        textRect6.center = (X6, Y6)
        
            
        screen.fill(Black)
        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        screen.blit(text3, textRect3)
        screen.blit(text4, textRect4)
        screen.blit(text5, textRect5)
        screen.blit(text6, textRect6)
    
    
    
        pygame.draw.line(screen, White, (0, 384), (1366, 384))
    


        #Bouncing on the Sides
        if circle_x < 19 or circle_x > 1347:
            move_x = -move_x
        if circle_y < 35 or circle_y > 768 :
            move_y = -move_y
 
        #Bouncing on the Top and Bottom
        if circle_y < 35:
            if some1 == True:
                Score2 += 1
                pong.Make_Ball()
                pong.draw(screen)
                player.draw(screen)
                player.handle_keys()
                pygame.display.update()
                continue
            
        if circle_y > 768:
            if some2 == True:
                Score1 += 1
                pong.Make_Ball()
                pong.draw(screen)
                player.draw(screen)
                player.handle_keys()
                pygame.display.update()
                continue

        if Score1 >= 10 or Score2 >= 10:
            Button2()
        
        
       #Paddle Collision Logic

        if ( circle_x > Paddle1.left or circle_x > Paddle1.right ) and ( circle_x < Paddle1.left + 90 or circle_x < Paddle1.right + 90 ):
            if circle_y > Paddle1.bottom and circle_y < Paddle1.bottom + 15:
                move_y = -move_y

        if ( circle_x > Paddle2.left or circle_x > Paddle2.right ) and ( circle_x < Paddle2.left + 90 or circle_x < Paddle2.right + 90 ):
            if circle_y > Paddle2.top and circle_y < Paddle2.top + 15:
                move_y = -move_y
        
        movement = pygame.mouse.get_pos()

        player.draw(screen)
        player.handle_keys()

        pong.Make_Ball()
        pong.draw(screen)

        pygame.display.update()

        clock.tick(490)

    
elif lcnt > 0:
    Button1()
    pong = Ball()
    player = player.draw(screen)
    player.handle_keys()


    pong.Make_Ball()
    pong.draw(screen)

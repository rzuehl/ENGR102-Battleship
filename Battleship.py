# import package and making objects
import turtle as t
from turtle import *

import numpy as np

scr = t.Screen()
tr = t.Turtle()


# Title of the game
def title():
    '''Title for Board'''
    t.setposition(-75,300)
    t.color('SlateGrey')
    t.write('Battleship', font=('Verdana', 30, 'normal'))


# The next few work with creating a legend
def hit():
    '''Legend location for the hit marker '''
    t.setposition(75, 20)
    t.write('Hit', font=('Verdana', 15, 'normal'))
    t.setposition(150, 40)
    t.pendown()
    t.color('FireBrick')
    t.fillcolor('FireBrick')
    t.begin_fill()
    for i in range(4):
        t.forward(15)
        t.right(90)
    t.end_fill()
    t.penup()

def miss() :
    '''Legend location for the miss marker '''
    t.setposition(75, -10)
    t.color('SlateGrey')
    t.write('Miss', font=('Verdana', 15, 'normal'))
    t.setposition(150, 10)
    t.pendown()
    t.color('dimgrey')
    t.fillcolor('dimgrey')
    t.begin_fill()
    for i in range(4):
        t.forward(15)
        t.right(90)
    t.end_fill()
    t.penup()
def ship() :
    '''Legend location for the ship marker '''
    t.setposition(75, -40)
    t.color('SlateGrey')
    t.write('Ship', font=('Verdana', 15, 'normal'))
    t.setposition(150, -20)
    t.pendown()
    t.color('RoyalBlue')
    t.fillcolor('RoyalBlue')
    t.begin_fill()
    for i in range(4):
        t.forward(15)
        t.right(90)
    t.end_fill()
    t.penup()

def legend():
    '''The whole function that writes the Legend'''
    t.setposition(50,50)
    t.color('SlateGrey')
    t.write('Legend:', font=('Verdana', 20, 'normal'))
    hit()
    miss()
    ship()

#the amount of ships
def ships():
    '''The description of all the ships'''
    t.setposition(50, -150)
    t.color('SlateGrey')
    t.write('Ships:', font=('Verdana', 20, 'normal'))
    t.setposition(75, -180)
    t.write('Battleship (4x1)', font=('Verdana', 15, 'normal'))
    t.setposition(75, -210)
    t.write('Cruiser (3x1)', font=('Verdana', 15, 'normal'))
    t.setposition(75, -240)
    t.write('Submarine (3x1)', font=('Verdana', 15, 'normal'))
    t.setposition(75, -270)
    t.write('Destroyer (2x1)', font=('Verdana', 15, 'normal'))

def board_titles():
    '''The written board titles'''
    t.setposition(-285, -90)
    t.color('SlateGrey')
    t.write('Player Board', font=('Verdana', 20, 'normal'))
    t.setposition(-310, 260)
    t.write('Opponent Board', font=('Verdana', 20, 'normal'))


#
#Drawing the grids
#
def draw_s():
    '''Draws a square'''
    for i in range(4):
        t.forward(50)
        t.right(90)
    t.forward(50)

#drawing the grid
def draw_grid(x,y,player):
    '''Loops draw_s while refering to the player matrix to figure out
     whether or not to display any information'''
    for j in range(6):
        for i in range(6):
            if player[j][i] == 1:
                t.fillcolor('RoyalBlue')
                t.begin_fill()
                draw_s()
                t.end_fill()
            elif player[j][i] == 2:
                t.fillcolor('FireBrick')
                t.begin_fill()
                draw_s()
                t.end_fill()
            elif player[j][i] == 3:
                t.fillcolor('dimgrey')
                t.begin_fill()
                draw_s()
                t.end_fill()
            else:
                draw_s()
        t.penup()
        y -= 50
        t.setposition(x,y)
        t.pendown()

def draw_grid2(x,y,oppon):
    '''Loops draw_s while refering to the opponet's matrix to figure out
     whether or not to display any information'''
    for j in range(6):
        for i in range(6):
            if oppon[j][i] == 2:
                t.fillcolor('FireBrick')
                t.begin_fill()
                draw_s()
                t.end_fill()
            elif oppon[j][i] == 3:
                t.fillcolor('dimgrey')
                t.begin_fill()
                draw_s()
                t.end_fill()
            else:
                draw_s()
        t.penup()
        y -= 50
        t.setposition(x,y)
        t.pendown()

def edit(x,y):
    '''Using the cords to edit the matrix'''
    if x >= -350 and x <= -300 and y <= 255 and y >= 205:
        if mat_2[0][0] == 1:
             mat_2[0][0] = 2
        else:
            mat_2[0][0] = 3
    elif x >= -300 and x <= -250 and y <= 255 and y >= 205:
        if mat_2[0][1] == 1:
            mat_2[0][1] = 2
        else:
            mat_2[0][1] = 3
    elif x >= -250 and x <= -200 and y <= 255 and y >= 205:
        if mat_2[0][2] == 1:
            mat_2[0][2] = 2
        else:
            mat_2[0][2] = 3
    elif x >= -200 and x <= -150 and y <= 255 and y >= 205:
        if mat_2[0][3] == 1:
            mat_2[0][3] = 2
        else:
            mat_2[0][3] = 3
    elif x >= -150 and x <= -100 and y <= 255 and y >= 205:
        if mat_2[0][4] == 1:
            mat_2[0][4] = 2
        else:
            mat_2[0][4] = 3
    elif x >= -100 and x <= -50 and y <= 255 and y >= 205:
        if mat_2[0][5] == 1:
            mat_2[0][5] = 2
        else:
            mat_2[0][5] = 3
    elif  x >= -350 and x <= -300 and y <= 205 and y >= 155:
        if mat_2[1][0] == 1:
             mat_2[1][0] = 2
        else:
            mat_2[1][0] = 3
    elif x >= -300 and x <= -250 and y <= 205 and y >= 155:
        if mat_2[1][1] == 1:
            mat_2[1][1] = 2
        else:
            mat_2[1][1] = 3
    elif x >= -250 and x <= -200 and y <= 205 and y >= 155:
        if mat_2[1][2] == 1:
            mat_2[1][2] = 2
        else:
            mat_2[1][2] = 3
    elif x >= -200 and x <= -150 and y <= 205 and y >= 155:
        if mat_2[1][3] == 1:
            mat_2[1][3] = 2
        else:
            mat_2[1][3] = 3
    elif x >= -150 and x <= -100 and y <= 205 and y >= 155:
        if mat_2[1][4] == 1:
            mat_2[1][4] = 2
        else:
            mat_2[1][4] = 3
    elif x >= -100 and x <= -50 and y <= 205 and y >= 155:
        if mat_2[1][5] == 1:
            mat_2[1][5] = 2
        else:
            mat_2[1][5] = 3
    elif  x >= -350 and x <= -300 and y <= 155 and y >= 105:
        if mat_2[2][0] == 1:
             mat_2[2][0] = 2
        else:
            mat_2[2][0] = 3
    elif x >= -300 and x <= -250 and y <= 155 and y >= 105:
        if mat_2[2][1] == 1:
            mat_2[2][1] = 2
        else:
            mat_2[2][1] = 3
    elif x >= -250 and x <= -200 and y <= 155 and y >= 105:
        if mat_2[2][2] == 1:
            mat_2[2][2] = 2
        else:
            mat_2[2][2] = 3
    elif x >= -200 and x <= -150 and y <= 155 and y >= 105:
        if mat_2[2][3] == 1:
            mat_2[2][3] = 2
        else:
            mat_2[2][3] = 3
    elif x >= -150 and x <= -100 and y <= 155 and y >= 105:
        if mat_2[2][4] == 1:
            mat_2[2][4] = 2
        else:
            mat_2[2][4] = 3
    elif x >= -100 and x <= -50 and y <= 155 and y >= 105:
        if mat_2[2][5] == 1:
            mat_2[2][5] = 2
        else:
            mat_2[2][5] = 3

    elif  x >= -350 and x <= -300 and y <= 105 and y >= 55:
        if mat_2[3][0] == 1:
             mat_2[3][0] = 2
        else:
            mat_2[3][0] = 3
    elif x >= -300 and x <= -250 and y <= 105 and y >= 55:
        if mat_2[3][1] == 1:
            mat_2[3][1] = 2
        else:
            mat_2[3][1] = 3
    elif x >= -250 and x <= -200 and y <= 105 and y >= 55:
        if mat_2[3][2] == 1:
            mat_2[3][2] = 2
        else:
            mat_2[3][2] = 3
    elif x >= -200 and x <= -150 and y <= 105 and y >= 55:
        if mat_2[3][3] == 1:
            mat_2[3][3] = 2
        else:
            mat_2[3][3] = 3
    elif x >= -150 and x <= -100 and y <= 105 and y >= 55:
        if mat_2[3][4] == 1:
            mat_2[3][4] = 2
        else:
            mat_2[3][4] = 3
    elif x >= -100 and x <= -50 and y <= 105 and y >= 55:
        if mat_2[3][5] == 1:
            mat_2[3][5] = 2
        else:
            mat_2[3][5] = 3
    elif  x >= -350 and x <= -300 and y <= 55 and y >= 5:
        if mat_2[4][0] == 1:
             mat_2[4][0] = 2
        else:
            mat_2[4][0] = 3
    elif x >= -300 and x <= -250 and y <= 55 and y >= 5:
        if mat_2[4][1] == 1:
            mat_2[4][1] = 2
        else:
            mat_2[4][1] = 3
    elif x >= -250 and x <= -200 and y <= 55 and y >= 5:
        if mat_2[4][2] == 1:
            mat_2[4][2] = 2
        else:
            mat_2[4][2] = 3
    elif x >= -200 and x <= -150 and y <= 55 and y >= 5:
        if mat_2[4][3] == 1:
            mat_2[4][3] = 2
        else:
            mat_2[4][3] = 3
    elif x >= -150 and x <= -100 and y <= 55 and y >= 5:
        if mat_2[4][4] == 1:
            mat_2[4][4] = 2
        else:
            mat_2[4][4] = 3
    elif x >= -100 and x <= -50 and y <= 55 and y >= 5:
        if mat_2[4][5] == 1:
            mat_2[4][5] = 2
        else:
            mat_2[4][5] = 3
    elif  x >= -350 and x <= -300 and y <= 5 and y >= -45:
        if mat_2[5][0] == 1:
             mat_2[5][0] = 2
        else:
            mat_2[5][0] = 3
    elif x >= -300 and x <= -250 and y <= 5 and y >= -45:
        if mat_2[5][1] == 1:
            mat_2[5][1] = 2
        else:
            mat_2[5][1] = 3
    elif x >= -250 and x <= -200 and y <= 5 and y >= -45:
        if mat_2[5][2] == 1:
            mat_2[5][2] = 2
        else:
            mat_2[5][2] = 3
    elif x >= -200 and x <= -150 and y <= 5 and y >= -45:
        if mat_2[5][3] == 1:
            mat_2[5][3] = 2
        else:
            mat_2[5][3] = 3
    elif x >= -150 and x <= -100 and y <= 5 and y >= -45:
        if mat_2[5][4] == 1:
            mat_2[5][4] = 2
        else:
            mat_2[5][4] = 3
    elif x >= -100 and x <= -50 and y <= 5 and y >= -45:
        if mat_2[5][5] == 1:
            mat_2[5][5] = 2
        elif mat_2[5][5] == 0:
            mat_2[5][5] = 3
        else:
            mat_2[5][5] = 2
    x = -350
    y = 255
    t.setposition(x, y)
    draw_grid2(x,y, mat_2)
    return mat_2


def fun(x,y):
    '''Interaction from click that allows the hit/ miss to make sense'''
    x_sys = int(x)
    y_sys = int(y)
    if (y_sys > -50 and y_sys < 255) and (x_sys < -50 and x_sys > -350):
        x = edit(x_sys, y_sys)
        print(x)
         #with open('mat_2.txt', w) as myfile:
             #myfile.write(edit(x_sys,y_sys))


    else:
        print('INVALID SELECTION')

#PLACEHOLDER MATRIX 1
# mat = [[0,0,0,0,0,0],
#        [0,1,1,1,0,0],
#        [0,2,3,0,0,0],
#        [0,2,0,3,0,0],
#        [0,2,0,0,0,0],
#        [1,1,0,3,0,3]]

#PLACEHOLDER MATRIX 2
# mat_2 = [[1,1,1,0,0,0],
#        [0,1,2,2,2,0],
#        [3,0,0,3,0,0],
#        [0,2,0,3,0,0],
#        [0,2,0,0,0,0],
#         [0,0,0,0,0,0]]


mat = np.zeros((6, 6))
mat_2 = np.zeros((6, 6))

#
#Turtle Features that set the overall setting and
#backround of the board
#
t.title('Battleship Player 1')
s = getscreen()
t.speed(0)
s.tracer(4,5)
t.screensize(canvwidth=0, canvheight=10, bg='lightgrey')
t.width(3)
t.hideturtle()
t.penup()

#
#setting the title and
#written portions of the board
#
title()
legend()
ships()


#Setting player board position
x = -350
y = -95
t.setposition(x, y)


#draw player board
t.pendown()
t.color('black')
draw_grid(x,y,mat)
t.penup()
t.pencolor('Black')


#setting opponents board position
x = -350
y = 255
t.setposition(x, y)


#draw opponets board
t.pendown()
draw_grid2(x,y,mat_2)
t.penup()

#name each board
board_titles()

a = 0
t.onscreenclick(fun)


def turtle_selection(x, y):
    '''Using the cords to edit the matrix'''
    if -350 <= x <= -300 and 255 >= y >= 205:
        start = [1, 1]
    elif -300 <= x <= -250 and 255 >= y >= 205:
        start = [1, 2]
    elif -250 <= x <= -200 and 255 >= y >= 205:
        start = [1, 3]
    elif -200 <= x <= -150 and 255 >= y >= 205:
        start = [1, 4]
    elif -150 <= x <= -100 and 255 >= y >= 205:
        start = [1, 5]
    elif x >= -100 and x <= -50 and y <= 255 and y >= 205:
        start = [1, 6]
    elif x >= -350 and x <= -300 and y <= 205 and y >= 155:
        start = [2, 1]
    elif x >= -300 and x <= -250 and y <= 205 and y >= 155:
        start = [2, 2]
    elif x >= -250 and x <= -200 and y <= 205 and y >= 155:
        start = [2, 3]
    elif x >= -200 and x <= -150 and y <= 205 and y >= 155:
        start = [2, 4]
    elif x >= -150 and x <= -100 and y <= 205 and y >= 155:
        start = [2, 5]
    elif x >= -100 and x <= -50 and y <= 205 and y >= 155:
        start = [2, 6]
    elif x >= -350 and x <= -300 and y <= 155 and y >= 105:
        start = [3, 1]
    elif x >= -300 and x <= -250 and y <= 155 and y >= 105:
        start = [3, 2]
    elif x >= -250 and x <= -200 and y <= 155 and y >= 105:
        start = [3, 3]
    elif x >= -200 and x <= -150 and y <= 155 and y >= 105:
        start = [3, 4]
    elif x >= -150 and x <= -100 and y <= 155 and y >= 105:
        start = [3, 5]
    elif x >= -100 and x <= -50 and y <= 155 and y >= 105:
        start = [3, 6]
    elif x >= -350 and x <= -300 and y <= 105 and y >= 55:
        start = [4, 1]
    elif x >= -300 and x <= -250 and y <= 105 and y >= 55:
        start = [4, 2]
    elif x >= -250 and x <= -200 and y <= 105 and y >= 55:
        start = [4, 3]
    elif x >= -200 and x <= -150 and y <= 105 and y >= 55:
        start = [4, 4]
    elif x >= -150 and x <= -100 and y <= 105 and y >= 55:
        start = [4, 5]
    elif x >= -100 and x <= -50 and y <= 105 and y >= 55:
        start = [4, 6]
    elif x >= -350 and x <= -300 and y <= 55 and y >= 5:
        start = [5, 1]
    elif x >= -300 and x <= -250 and y <= 55 and y >= 5:
        start = [5, 2]
    elif x >= -250 and x <= -200 and y <= 55 and y >= 5:
        start = [5, 3]
    elif x >= -200 and x <= -150 and y <= 55 and y >= 5:
        start = [5, 4]
    elif x >= -150 and x <= -100 and y <= 55 and y >= 5:
        start = [5, 5]
    elif x >= -100 and x <= -50 and y <= 55 and y >= 5:
        start = [5, 6]
    elif x >= -350 and x <= -300 and y <= 5 and y >= -45:
        start = [6, 1]
    elif x >= -300 and x <= -250 and y <= 5 and y >= -45:
        start = [6, 2]
    elif x >= -250 and x <= -200 and y <= 5 and y >= -45:
        start = [6, 3]
    elif x >= -200 and x <= -150 and y <= 5 and y >= -45:
        start = [6, 4]
    elif x >= -150 and x <= -100 and y <= 5 and y >= -45:
        start = [6, 5]
    elif x >= -100 and x <= -50 and y <= 5 and y >= -45:
        start = [6, 6]
    x = -350
    y = 255
    t.setposition(x, y)
    draw_grid2(x, y, mat_2)
    return start




print(mat_2)




###################
# End of the code #
t.penup()


t.mainloop()


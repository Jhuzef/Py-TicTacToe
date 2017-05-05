# Joseph Gonzales
#TTT Project, Nov 20, 2016

#Initialize
import turtle #The turtle by default should always be facing the right.
print("Instructions: ")
print ("The numbers represent each box starting from left to right.")
print ("For example: ")
print (" 012")
print (" 345")
print (" 678")
print ("")
board = [0,1,2,3,4,5,6,7,8]
movesX=[]
movesO=[]
winValues=['012','345','678','036','147','258','048','246']
win=''

def restartWin():
    global winValues
    global movesX
    global movesO
    global board
    global win
    board = [0,1,2,3,4,5,6,7,8]
    movesX=[]
    movesO=[]
    winValues=['012','345','678','036','147','258','048','246']
    win=''

def drawboard(t,cellsize): #each center of a box is cellsize/2
    t.up()
    t.goto(0,cellsize/2)
    drawMidline(t,cellsize*3)
    t.up()
    t.goto(0,-cellsize/2)
    drawMidline(t,cellsize*3)
    t.up()
    t.goto(-cellsize/2,0)
    t.left(90)
    drawMidline(t,cellsize*3)
    t.up()
    t.goto(cellsize/2,0)
    drawMidline(t,cellsize*3)
    t.right(90)
    t.up()
    t.goto(0,0)



def drawMidline(t,length):
    t.down()
    t.forward(length/2)
    t.back(length)
    t.forward(length/2)

def xTurtle(t,cellsize):
    t.down()
    t.left(45)
    drawMidline(t,cellsize/2)
    t.left(90)
    drawMidline(t,cellsize/2)
    t.right(135)

def oTurtle(t,cellsize):
    t.up()
    t.right(90)
    t.forward(40)
    t.left(90)
    t.down()
    t.circle(cellsize/4)
    t.up()

def drawX(t,cell,cellsize):
    for i in range(3):
        if cell == i:
            t.up()
            t.goto(-cellsize+(cellsize*i),cellsize)
            xTurtle(t,cellsize)
            t.up()
            t.goto(0,0)
            return
    for i in range(3,6):
        if cell == i:
            t.up()
            t.goto(-cellsize+(cellsize*(i-3)),0)
            xTurtle(t,cellsize)
            t.up()
            t.goto(0,0)
            return
    for i in range(6,9):
        if cell == i:
            t.up()
            t.goto(-cellsize+(cellsize*(i-6)),-cellsize)
            xTurtle(t,cellsize)
            t.up()
            t.goto(0,0)
            return

def drawO(t,cell,cellsize):
    for i in range(3):
        if cell == i:
            t.up()
            t.goto(-cellsize+(cellsize*i),cellsize)
            oTurtle(t,cellsize)
            t.up()
            t.goto(0,0)
            return
    for i in range(3,6):
        if cell == i:
            t.up()
            t.goto(-cellsize+(cellsize*(i-3)),0)
            oTurtle(t,cellsize)
            t.up()
            t.goto(0,0)
            return
    for i in range(6,9):
        if cell == i:
            t.up()
            t.goto(-cellsize+(cellsize*(i-6)),-cellsize)
            oTurtle(t,cellsize)
            t.up()
            t.goto(0,0)
            return

def getPlayerNames():
    names=[]
    while True:
        name1=input('Enter Player 1\'s name: (X) ')
        if name1 == '':
            print('No name was detected.')
            continue
        break
    while True:
        name2=input('Enter Player 2\'s name: (O) ')
        if name2 == '':
            print('No name was detected.')
            continue
        break
                
    names.append(name1)
    names.append(name2)
    return tuple(names)

def getmoveO():
    while True:
        global board
        global names
        move=input('Enter your move, '+names[1]+' (0 - 8): ')
        if move=='' or move not in '0123456789':
            print('Please enter a correct entry.')
            continue
        if int(move) not in board:
            print('Invalid entry or position already taken.')
            continue
        break
    global movesO
    board.remove(int(move))
    movesO.append(int(move))
    movesO.sort()
    return int(move)

def getmoveX():
    while True:
        global board
        global names
        move=input('Enter your move, '+names[0]+' (0 - 8): ')
        if move=='' or move not in '0123456789':
            print('Please enter a correct entry.')
            continue
        if int(move) not in board:
            print('Invalid entry or position already taken.')
            continue
        break
    global movesX
    board.remove(int(move))
    movesX.append(int(move))
    movesX.sort()
    return int(move)

def winCross(t,win):
    global cellsize
    t.up()
    for cell in win:
        cell=int(cell)
        for i in range(3):
            if cell == i:
                t.goto(-cellsize+(cellsize*i),cellsize)
                t.down()
                break
        for i in range(3,6):
            if cell == i:
                t.goto(-cellsize+(cellsize*(i-3)),0)
                t.down()
                break
        for i in range(6,9):
            if cell == i:
                t.goto(-cellsize+(cellsize*(i-6)),-cellsize)
                t.down()
                break
    t.up()
    t.goto(0,0)
    t.down()

def checkWinX(board,winValues,movesX):
    if len(movesX)>=3:
        global win
        for values in winValues:
            counter=0
            for moves in movesX:
                moves=str(moves)
                if moves in values:
                    counter+=1
                if counter==3:
                    win=values
                    winCross(t,win)
                    return True
    return False

def checkWinO(board,winValues,movesO):
    if len(movesO)>=3:
        global win
        for values in winValues:
            counter=0
            for moves in movesO:
                moves=str(moves)
                if moves in values:
                    counter+=1
                if counter==3:
                    win = values
                    winCross(t,win)
                    return True
    return False

def gameOver(board,winValues,movesO,movesX):
    if checkWinO(board,winValues,movesO):
        return 'O'
    if checkWinX(board,winValues,movesX):
        return 'X'
    if len(board)==0:
        return 'D'
    return '-'


#Main

cellsize=100
names = getPlayerNames()
s=turtle.Screen()

while True:
    t=turtle.Turtle()
    drawboard(t, cellsize)
    while True:
        movex=getmoveX()
        drawX(t,movex,cellsize)
        check=gameOver(board,winValues,movesO,movesX)
        if check == 'X' or check=='O' or check=='D':
            break
        
        moveo=getmoveO()
        drawO(t,moveo,cellsize)
        
        check=gameOver(board,winValues,movesO,movesX)
        if check == 'X' or check=='O' or check=='D':
            break

    if check == 'X':
        print('Congratulations, '+names[0]+'. You won.')
    if check == 'O':
        print('Congratulations, '+names[1]+'. You won.')
    if check == 'D':
        print('Sorry, it was a draw.')
    
    restart=input('Would you like to play again? ("y" or "n"): ')
    if restart == 'n':
        break
    s.clear()
    restartWin()
print('Game Over')




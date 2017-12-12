import hl.colours as col
import pygame
import os
import levels

pygame.init()

clock = pygame.time.Clock()

def cls():
    os.system('clear')

dimensions = ['1']

def intro():
    global dimensions
    
    print(col.bblue("Time Array"))

    cls()
    print(col.byellow("Welcome to ")+col.bblue("Time Array")+col.byellow("!!!"))
    print(col.yellow("Press Enter to Start"))
    print ""


    raw_input("->")
    
    dim1()

        

def initDim1(pos = 0,port = 1,colour = 'blue'):
    seq = []
    for i in range(5):
        seq += [['*','green']]
    
    seq[pos] = ['H','red']
    seq[port] = ['O',colour]
    return seq


def dim1():
    cls()
    print(col.green("You are a time traveling interdimensional being\nYou were captured, and to escape you need to make your way through a maze.\nThere is a portal at the end of each maze.\nA ")+col.bblue("blue ")+col.green("portal will take you to the next level.\nA ")+col.byellow("yellow ") + col.green("portal will take you to the next dimension\nThat is all you need to know for now. You will learn everything else later\nGood Luck!"))
    raw_input(col.red('Press Enter to Continue'))
    cls()
    
    print(col.green("Please place and click your mouse in the window to continue."))
    
    display = pygame.display.set_mode((60,60))
    display.fill((255,255,0))
    
    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                exit = True
    
    mainLoop([1,0])


def l30intro():
    cls()
    print(col.green("Now for the confusing part...\nFor each Y position (Up and down) there will/won't be dashes above and bellow the maze\nThese tell you if you can move back and forth between the layers\nIf the dash is above the maze then the available spot is one layer down and\nif it is below the maze then there is an available spot is one layer up"))
    print(col.red('Press j to continue'))
    exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    exit = True

def mainLoop(level):
    cls()
    
    game = True
    charX = 0
    charY = 0
    charZ = 0
    charW = 0
    addition  = ""
    String = ""
    array = []
    printList = []
    
    if level[0] == 1:
        if level[1] == 0:
            info = levels.level10()
        
        if level[1] == 1:
            info = levels.level11()
        
    if level[0] == 2:
        if level[1] == 0:
            info = levels.level20()
                
        if level[1] == 1:
            info = levels.level21()
            
    if level[0] == 3:
        if level[1] == 0:
            info = levels.level30()
    
    charX = int(info[2][0])
    charY = int(info[2][1])
    charZ = int(info[2][2])
    charW = int(info[2][3])
    goalX = int(info[1][0])
    goalY = int(info[1][1])
    goalZ = int(info[1][2])
    goalW = int(info[1][3])
    array = info[0]
    goalType = str(info[3])
    special = info[4]
    
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if charX > 0 and array[charW][charZ][charY][charX-1][0] != ' ':
                        array[charW][charZ][charY][charX] = ['*','green']
                        charX -= 1
                        array[charW][charZ][charY][charX] = ['H','red']
                
                if event.key == pygame.K_d:
                    if charX < len(array[charW][charZ][charY])-1 and array[charW][charZ][charY][charX + 1][0] != ' ':
                        array[charW][charZ][charY][charX] = ['*','green']
                        charX += 1
                        array[charW][charZ][charY][charX] = ['H','red']
                
                if event.key == pygame.K_w:
                    if charY > 0 and array[charW][charZ][charY -1][charX][0] != ' ':
                        array[charW][charZ][charY][charX] = ['*','green']
                        charY -= 1
                        array[charW][charZ][charY][charX] = ['H','red']
                
                if event.key == pygame.K_s:
                    if charY < len(array[charW][charZ])-1 and array[charW][charZ][charY + 1][charX][0] != ' ':
                        array[charW][charZ][charY][charX] = ['*','green']
                        charY += 1
                        array[charW][charZ][charY][charX] = ['H','red']
                
                if event.key == pygame.K_r:
                    if charZ < len(array[charW])-1 and array[charW][charZ+1][charY][charX][0] != ' ':
                        array[charW][charZ][charY][charX] = ['*','green']
                        charZ += 1
                        array[charW][charZ][charY][charX] = ['H','red']
                
                if event.key == pygame.K_f:
                    if charZ > 0 and array[charW][charZ - 1][charY][charX][0] != ' ':
                        array[charW][charZ][charY][charX] = ['*','green']
                        charZ -= 1
                        array[charW][charZ][charY][charX] = ['H','red']
                
                if event.key == pygame.K_q:
                    if charW > 0 and array[charW - 1][charZ][charY][charX][0] != ' ':
                        array[charW][charZ][charY][charX] = ['*','green']
                        charW -= 1
                        array[charW][charZ][charY][charX] = ['H','red']
                
                if event.key == pygame.K_e:
                    if charW < len(array)-1 and array[charW + 1][charZ][charY][charX][0] != ' ':
                        array[charW][charZ][charY][charX] = ['*','green']
                        charW += 1
                        array[charW][charZ][charY][charX] = ['H','red']
        
        for Y in range(len(array[charW][charZ])):
            
            if charW > 0 and array[charW-1][charZ][charY][charX][0] != ' ':
                String = col.green(" |")
            
            else:
                String = '  '
            for X in array[charW][charZ][Y]:
                String += getattr(col,X[1])(X[0]) + " "# + addition
            
            if charW < len(array)-1 and array[charW + 1][charZ][charY][charX][0] != ' ':
                String += col.green('| ')
            
            printList += [String]

        
        cls()
        #print charY
        
        print special
        
        availableUp = '  '
        if charZ < len(array[charW])-1:
            for i in array[charW][charZ+1][charY]:
                if i[0] == ' ':
                    availableUp += "  "
                
                else:
                    availableUp += col.green('- ')
        
        print(availableUp)
        
        for X in printList:
            print(X)
            
        
        availableDown = '  '
        if charZ > 0:
            for i in array[charW][charZ-1][charY]:
                if i[0] == ' ':
                    availableDown += "  "
                
                else:
                    availableDown += col.green('- ')
        
        print availableDown
        
        
        
        if charX == goalX and charY == goalY and charZ == goalZ and charW == goalW:
            if goalType == "lvl":
                level[1] += 1
            
            if goalType == "dim":
                level[0] += 1
                level[1] = 0
            
            if level[0] == 1:
                if level[1] == 0:
                    info = levels.level10()
                
                if level[1] == 1:
                    info = levels.level11()
            
            if level[0] == 2:
                if level[1] == 0:
                    info = levels.level20()
                
                if level[1] == 1:
                    info = levels.level21()
            
            if level[0] == 3:
                if level[1] == 0:
                    l30intro()
                    info = levels.level30()
                
                if level[1] == 1:
                    info = levels.level31()
            
            if level[0] == 4:
                if level[1] == 0:
                    info = levels.level40()
                
                if level[1] == 1:
                    info = levels.level41()
                
                if level[1] == 2:
                    winner()
            
            charX = int(info[2][0])
            charY = int(info[2][1])
            charZ = int(info[2][2])
            charW = int(info[2][3])
            goalX = int(info[1][0])
            goalY = int(info[1][1])
            goalZ = int(info[1][2])
            goalW = int(info[1][3])
            array = info[0]
            goalType = str(info[3])
            special = info[4]
            
            
            
        
        printList = []
        
        clock.tick(30)
    
        
        


def winner():
    cls()
    print col.byellow("YOU WON!!!")
    
intro()

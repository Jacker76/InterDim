import pygame
import hl.colours as col

BLANK = [' ','red']
BLROW = [[' ','red'],[' ','red'],[' ','red'],[' ','red'],[' ','red']]
SPACE = ['*','green']


def level10():
    array = [[[[['H','red'],SPACE,SPACE,SPACE,['O','bblue']]]]]
    goal = [4,0,0,0]
    coordinates = [0,0,0,0]
    special = (col.green("Press") + col.red(" A") + col.green(" and") + col.red(" D") + col.green(" to move left and right"))
    return [array,goal,coordinates,'lvl',special]

def level11():
    array = [[[[['H','red']],[SPACE],[SPACE],[SPACE],[['O','byellow']]]]]
    goal = [0,4,0,0]
    coordinates = [0,0,0,0]
    special = (col.green("Press") + col.red(" W") + col.green(" and") + col.red(" S") + col.green(" to move up and down"))
    return [array,goal,coordinates,'dim',special]

def level20():
    array = [[[[['H','red'],SPACE,SPACE,SPACE,SPACE],
               [SPACE,SPACE,SPACE,SPACE,SPACE],[SPACE,SPACE,SPACE,SPACE,SPACE],[SPACE,SPACE,SPACE,SPACE,SPACE],[SPACE,SPACE,SPACE,SPACE,['O','bblue']]]]]
    goal = [4,4,0,0]
    coordinates = [0,0,0,0]
    special = ""
    return [array,goal,coordinates,'lvl',special]

def level21():
    array = [[[[['H','red'],BLANK,SPACE,BLANK,BLANK],
               [SPACE,BLANK,SPACE,BLANK,BLANK],[SPACE,SPACE,SPACE,SPACE,BLANK],[BLANK,BLANK,BLANK,SPACE,BLANK],[SPACE,SPACE,SPACE,SPACE,['O','byellow']]]]]
    goal = [4,4,0,0]
    coordinates = [0,0,0,0]
    special = ""
    return [array,goal,coordinates,'dim',special]

def level30():
    array = [[[[['H','red'],BLANK,BLANK],[SPACE,BLANK,SPACE],[BLANK,BLANK,['O','blue']]],[[BLANK,SPACE,SPACE],[SPACE,BLANK,SPACE],[SPACE,SPACE,BLANK]],[[BLANK,SPACE,BLANK],[BLANK,SPACE,BLANK],[BLANK,SPACE,BLANK]]]]
    goal = [2,2,0,0]
    coordinates = [0,0,0,0]
    special = (col.green("Press")+col.red(' R ')+col.green('and')+col.red(' F ')+col.green('to go back and fourth in the 3rd Dimension'))
    return [array,goal,coordinates,'lvl',special]

def level31():
    array = [[[[['H','red'],BLANK,SPACE,SPACE,SPACE],[SPACE,BLANK,SPACE,BLANK,BLANK],[BLANK,BLANK,BLANK,BLANK,SPACE],[SPACE,['O','byellow'],BLANK,BLANK,SPACE],[BLANK,BLANK,BLANK,BLANK,SPACE]],[[BLANK,BLANK,BLANK,BLANK,SPACE],[SPACE,SPACE,SPACE,BLANK,BLANK],[BLANK,BLANK,BLANK,BLANK,SPACE],[SPACE,BLANK,BLANK,BLANK,BLANK],[SPACE,SPACE,SPACE,BLANK,SPACE]],[[BLANK,BLANK,BLANK,BLANK,SPACE],[BLANK,BLANK,BLANK,BLANK,SPACE],[BLANK,BLANK,BLANK,BLANK,SPACE],BLROW,[BLANK,BLANK,SPACE,SPACE,SPACE]]]]
    goal= [1,3,0,0]
    coordinates = [0,0,0,0]
    return [array,goal,coordinates,'dim',' ']

def level40():
    array = [[[[['H','red'],BLANK],[SPACE,BLANK]],[[BLANK,BLANK],[SPACE,SPACE]]],[[[BLANK,BLANK],[BLANK,SPACE]],[[BLANK,BLANK],[BLANK,SPACE]]],[[[['O','bblue'],['*','red']],[BLANK,BLANK]],[[BLANK,SPACE],[BLANK,SPACE]]]]
    goal = [0,0,0,2]
    coordinates = [0,0,0,0]
    special = (col.green("Press") + col.red(' Q') + col.green(' and') + col.red(' E') + col.green(' to move back and fourth in the fourth dimension'))
    return [array,goal,coordinates,'lvl',special]

def level41():
    array = [[[[['H','red'],BLANK,BLANK,BLANK,BLANK],
               [SPACE,BLANK,BLANK,BLANK,BLANK],
               BLROW,BLROW,
               BLROW],
    [BLROW,
     [SPACE,BLANK,BLANK,BLANK,BLANK],
     [SPACE,SPACE,SPACE,BLANK,BLANK],
     BLROW,BLROW],
    [BLROW,
     [BLANK,SPACE,SPACE,SPACE,SPACE],
     BLROW,
     [BLANK,BLANK,['O','bblue'],BLANK,BLANK],
     [BLANK,BLANK,SPACE,SPACE,SPACE]],
    [BLROW,
     [SPACE,SPACE,BLANK,BLANK,SPACE],
     [SPACE,BLANK,BLANK,BLANK,SPACE],
     [SPACE,BLANK,BLANK,BLANK,SPACE],
     [SPACE,BLANK,BLANK,BLANK,SPACE]]],
    [[BLROW,
      BLROW,
      BLROW,
      BLROW,
      [BLANK,BLANK,BLANK,BLANK,SPACE]],
    [BLROW,
     BLROW,
     [BLANK,BLANK,SPACE,BLANK,BLANK],
     [SPACE,SPACE,SPACE,BLANK,BLANK],
     [BLANK,BLANK,BLANK,BLANK,SPACE]],
    [[SPACE,SPACE,BLANK,BLANK,BLANK],
     [SPACE,BLANK,BLANK,BLANK,BLANK],
     [SPACE,BLANK,BLANK,BLANK,BLANK],
     [SPACE,BLANK,BLANK,BLANK,BLANK],
     [BLANK,BLANK,BLANK,BLANK,SPACE]],
    [[SPACE,BLANK,BLANK,BLANK,BLANK],
     [BLANK,BLANK,SPACE,SPACE,BLANK],
     [BLANK,BLANK,BLANK,SPACE,BLANK],
     [BLANK,BLANK,BLANK,SPACE,BLANK],
     [SPACE,SPACE,SPACE,SPACE,BLANK]]],
    [[BLROW,
      BLROW,
      [BLANK,BLANK,BLANK,BLANK,SPACE],
      [BLANK,BLANK,BLANK,BLANK,SPACE],
      [BLANK,BLANK,BLANK,BLANK,SPACE]],
    [[BLANK,BLANK,BLANK,SPACE,BLANK],
     [BLANK,BLANK,BLANK,SPACE,BLANK],
     [BLANK,BLANK,BLANK,SPACE,SPACE],
     BLROW,
     BLROW],
    [[BLANK,SPACE,SPACE,SPACE,BLANK],
     BLROW,
     BLROW,
     [BLANK,BLANK,SPACE,SPACE,SPACE],
     [BLANK,BLANK,BLANK,BLANK,SPACE]],
    [BLROW,
     [BLANK,SPACE,SPACE,BLANK,BLANK],
     [BLANK,SPACE,BLANK,BLANK,BLANK],
     [BLANK,SPACE,SPACE,BLANK,BLANK],
     BLROW]]]
    goal = [2,3,2,0]
    coordinates = [0,0,0,0]
    special = col.green('Good Luck')
    return [array,goal,coordinates,'lvl',special]
                                                                                                                                

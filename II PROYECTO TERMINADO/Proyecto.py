import pygame, sys
import random
from pygame.locals import *
import time
from threading import Thread
import random
import AnimationWin
import AnimationLose

sys.setrecursionlimit(1000000000)

#_________________________
#________/Main Definition.
size= (700,500)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("INICIO")

clock = pygame.time.Clock()

fuente = pygame.font.Font('freesansbold.ttf',15)

Draw_cashDiamond = fuente.render(str(150),True,(255,255,255),(0,0,0))
Draw_cashGold = fuente.render(str(150),True,(255,255,255),(0,0,0))
Draw_cashStone = fuente.render(str(100),True,(255,255,255),(0,0,0))
Draw_cashWood = fuente.render(str(50),True,(255,255,255),(0,0,0))
display_time= fuente.render("Tiempo:",True,(255,255,255),(0,0,0))
Kills= fuente.render("Kills:",True,(255,255,255),(0,0,0))
Exit= fuente.render("Salir",True,(255,255,255),(0,0,0))

#__________________
#_______/Variables.
loseAnimation = AnimationLose.AnimationLose((0, 0))
winAnimation= AnimationWin.AnimationWin((0, 0))
Attack_roock = 5 
user_text=''
BG = (32,30,32)
WHITE = (255, 255, 255)
BLACK=(0,0,0)
COLOR_TEXT = (50, 60, 80)
image_panel = pygame.image.load("./images/fondos/fondo.png")#load image background
image_botton = pygame.image.load("./images/bon.png")#load image button
image_botton_pressed = pygame.image.load("./images/bon.png")
image_botton_square = pygame.image.load("./images/bon.png")
image_botton_square_pressed = pygame.image.load("./images/bon.png")
image_text = pygame.image.load("./images/bon.png")
font = pygame.font.SysFont('Courier', 20)
font_num = pygame.font.SysFont('Pacifico Regular', 30)

########################### VARIABLE #########################

Game = True

level_1 = True

level_2 = False

level_3 = False

Win = False

Lose = False

level1 = False

level2 = False

level3 = False

#-------------------------------------------------------------
# VARIABLE COINS
#-------------------------------------------------------------
    
cash = 1111111111110

Coin = False

coins = []

value = [25,50,100]

#-------------------------------------------------------------
# VARIABLE AVATAR
#-------------------------------------------------------------

Archer = False
MoveArcher = False
Goblin = False
MoveGoblin = False
Warrior = False
MoveWarrior = False
Axeman = False
MoveAxeman = False
AttackArcher = False
AttackGoblins = False
AttackAxemans = False
AttactWarriors= False

Archers = []
Goblins = []
Warriors = []
Axemans = []

moveArrow = 0

Avatars = [Archers,Goblins,Warriors,Axemans]

count_enemies = 0

#-------------------------------------------------------------
# VARIABLE ROOKS
#-------------------------------------------------------------

Diamond = False
Gold = False
Ston = False
Wood = False

Diamonds = []
Golds = []
Stons = []
Woods = []

Rooks= [Diamonds,Golds,Stons,Woods]

#-------------------------------------------------------------
# MATRIX
#-------------------------------------------------------------

matriz = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
second = 0

frequency = 10

#-------------------------------------------------------------
# FILA DE LA MATRIZ
#-------------------------------------------------------------

posFila = [42,125,220,307,390]

###########################IMAGENES###########################

#-------------------------------------------------------------
# BG
#-------------------------------------------------------------

background1 = pygame.image.load("./Imagenes/Fondos/fondo1.png").convert()

background2 = pygame.image.load("./Imagenes/Fondos/fondo2.png").convert()

background3 = pygame.image.load("./Imagenes/Fondos/fondo3.png").convert()

#-------------------------------------------------------------
# AVATAR
#-------------------------------------------------------------

arquero = pygame.image.load("./Imagenes/Avatars/arquero.png")
arquero.set_colorkey([0, 0, 0])

goblin = pygame.image.load("./Imagenes/Avatars/goblin.png")
goblin.set_colorkey([0, 0, 0])

goblinAttack = pygame.image.load("./Imagenes/Avatars/goblinataque.png")
goblinAttack.set_colorkey([0, 0, 0])

guerrero = pygame.image.load("./Imagenes/Avatars/guerrero.png")
guerrero.set_colorkey([0, 0, 0])

guerreroAttack = pygame.image.load("./Imagenes/Avatars/guerreroataque.png")
guerreroAttack.set_colorkey([0, 0, 0])

hachero = pygame.image.load("./Imagenes/Avatars/hachero.png")
hachero.set_colorkey([0, 0, 0])

hacheroAttack = pygame.image.load("./Imagenes/Avatars/ataqueHachero.png")
hacheroAttack.set_colorkey([0, 0, 0])

flecha = pygame.image.load("./Imagenes/Proyectiles/flecha.png")
flecha.set_colorkey([0, 0, 0])

#-------------------------------------------------------------
# ROOKS
#-------------------------------------------------------------

B_diamante = pygame.image.load("./Imagenes/Botones/B_diamante.png").convert()

B_oro = pygame.image.load("./Imagenes/Botones/B_oro.png").convert()

B_madera = pygame.image.load("./Imagenes/Botones/B_madera.png").convert()

B_piedra = pygame.image.load("./Imagenes/Botones/B_piedra.png").convert()

diamante = pygame.image.load("./Imagenes/Rooks/R_Diamante.png").convert()
diamante.set_colorkey([0, 0, 0])

madera = pygame.image.load("./Imagenes/Rooks/R_madera.png").convert()
madera.set_colorkey([0, 0, 0])

oro = pygame.image.load("./Imagenes/Rooks/R_oro.png").convert()
oro.set_colorkey([0, 0, 0])

piedra = pygame.image.load("./Imagenes/Rooks/R_piedra.png").convert()
piedra.set_colorkey([0, 0, 0])

d_madera = pygame.image.load("./Imagenes/Proyectiles/d_madera.png").convert()
d_madera.set_colorkey([0, 0, 0])

d_oro = pygame.image.load("./Imagenes/Proyectiles/d_oro.png").convert()
d_oro.set_colorkey([0, 0, 0])

d_piedra = pygame.image.load("./Imagenes/Proyectiles/d_piedra.png").convert()
d_piedra.set_colorkey([0, 0, 0])

d_diamante = pygame.image.load("./Imagenes/Proyectiles/d_diamante.png").convert()
d_diamante.set_colorkey([0, 0, 0])

#-------------------------------------------------------------
# COINS
#-------------------------------------------------------------

moneda = pygame.image.load("./Imagenes/moneda.png")
moneda.set_colorkey([0, 0, 0])

#___________________
#_____/DATE OF BASE.
loginsRegister=[]#from file txt
pointsFile = "dataBase.txt" #names file 
def cleanDataBase():#clean file
    openFile= open(pointsFile, 'w')
    openFile.write("")
def getDataBase(array):# file shape
    openFile= open(pointsFile, 'r')
    n=0
    word=""
    for linea in openFile:
        i=0
        while linea[i]!= "\n":
            word=word+linea[i]
            i=i+1
        array.append(word)#long check-in list
        word=""
    openFile.close()#it doesn't work without this
def addToDataBase(array, newName):#add the name to the file
    openFile= open(pointsFile, 'a')
    openFile.write(newName+"\n")
    loginsRegister.append(newName)
    openFile.close()
getDataBase(loginsRegister)#call the list

########################## FUNTIONS #########################

#-------------------------------------------------------------
# SAVE BEST RESULT
#-------------------------------------------------------------

def Read():
    path="scores.txt"
    file=open(path, "r")
    txt=file.readlines()
    file.close()
    return Delete(txt)

def Write(txt):
    path="scores.txt"
    file=open(path, "a")
    file.write(txt+"\n") 
    file.close()

def Write2(player, point, list_com, name, best,control):

    if best == 0:
        return []
    elif control:
        return [name[0] + "," + list_com[0]] + Write2(player, point, list_com[1:], name[1:], best - 1,True)
    else:
        if point < int(list_com[0]):
            return [player + "," + str(point)] + Write2(player,point, list_com, name,best - 1,True)
        else:
            return [name[0] + "," + list_com[0]] + Write2(player, point, list_com[1:], name[1:], best - 1,False)

def Delete(txt):
    if txt == []:
        return []
    else:
        leng = len(txt[0])
        return [txt[0][:leng - 1]] + Delete(txt[1:])
 
def TheBestScore(score):

    path="scores.txt"
    ScoreFile=open(path, "w")
    ScoreFile.write(str(score[0])+"\n")
    ScoreFile.write(str(score[1])+"\n")
    ScoreFile.write(str(score[2])+"\n")
    ScoreFile.write(str(score[3])+"\n")
    ScoreFile.write(str(score[4])+"\n")
    ScoreFile.write(str(score[5])+"\n")
    ScoreFile.write(str(score[6])+"\n")
    ScoreFile.close()

def TakeNames(txt):
    
    if txt == []:

        return []
    
    else:
        
        return [txt[0].split(",")[0]] + TakeNames(txt[1:])

def TakePoints(txt):
    
    if txt == []:
        
        return []
    
    else:
        
        return [txt[0].split(",")[1]] + TakePoints(txt[1:])

#-------------------------------------------------------------
# TIME
#-------------------------------------------------------------

def Time():

    """ CALCULATE TIME AND CONTROL GLOBAL  VARIABLE"""

    global second,MoveArcher,MoveGoblin,MoveAxeman,MoveWarrior,AttackArcher,Coin,AttackGoblin,AttackAxeman,AttackWarrior,Archer,Warrior,Axeman,Goblin
    global level_1,level_2,level_3,Win, second, frequency,count_enemies,level1,level2,level3
    global Diamonds,Golds,Stons, Woods,Archers,Goblins,Warriors,Axemans,matriz
    
        
    while Game:

        #CHANGE LEVEL
        if level1:

            level1 = False

            pygame.mixer.quit()
            pygame.mixer.init()
            pygame.mixer.music.load('level_2.mp3')
            pygame.mixer.music.play(10)

            level_1 = False

            level_2 = True

            matriz = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

            DestroyRookAvatar(len(Avatars[0]),Avatars[0],0,Avatars)
            DestroyRookAvatar(len(Rooks[0]),Rooks[0],0,Rooks)

            time.sleep(2)
            
            frequency = 7

        #CHANGE LEVEL
        if level2:

            level2 = False

            pygame.mixer.quit()
            pygame.mixer.init()
            pygame.mixer.music.load('level_3.mp3')
            pygame.mixer.music.play(10)

            level_2 = False

            level_3 = True
            
            matriz = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

            DestroyRookAvatar(len(Avatars[0]),Avatars[0],0,Avatars)
            DestroyRookAvatar(len(Rooks[0]),Rooks[0],0,Rooks)


            frequency = 5

            time.sleep(2)
            
        #WIN
        if level3:

            level3 = False

            pygame.mixer.quit()

            matriz = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

            DestroyRookAvatar(len(Avatars[0]),Avatars[0],0,Avatars)
            DestroyRookAvatar(len(Rooks[0]),Rooks[0],0,Rooks)
            DestroyCoins(len(coins),coins)

            second = 0
            count_enemies = 0
            frequency = 10

            count_enemies = 0

            level_1 = False

            level_2 = False

            level_3 = False

            Win = True
            
        # ATTACK GOBLIN AND AXEMAN
        if second%4 == 0 and second !=0:
            
            AttackGoblin = True
            AttackAxeman = True

        # CREATE COIN
        if second%7 == 0 or second == 0:

            Coin = True
            
        # CREATE ARCHER
        if (frequency-1)%9 == 0 and second != 0:
            
            Archer = True

        # ATTACK ARCHER
        if second%10 == 0 and second != 0:

            AttackArcher = True

        # CREATE AXEMAN
        if (frequency+5)%15 == 0 and second != 0 :
            
            Axeman = True

        # CREATE WARRIOR
        if (frequency+3)%13 == 0 and second != 0:

            Warrior = True #user_text

        # ATTACK WARRIOR
        if second%15 == 0 and second !=0:

            AttackWarrior = True

        # CREATE GOBLIN
        if (frequency+10)%20 == 0 and second != 0:

            Goblin = True

        if Game== False:
            break

        if second > 10:

            # MOVE WARRIOR 
            if second%10 == 0 and second != 0:

                MoveWarrior = True

            # MOVE ARCHER
            if second%11 == 0 and second != 0:

                MoveArcher = True

            # MOVE AXEMAN
            if second%13 == 0 and second != 0:
                
                MoveAxeman = True

            # MOVE GOBLIN
            if second%14 == 0 and second != 0:

                MoveGoblin = True
   
        second += 1
        frequency += 1
        time.sleep(1)

    return

#-------------------------------------------------------------
# SCREEN LEVELS
#-------------------------------------------------------------

def Display_game_1():

    """ SHOW DISPLAY GAME """

    #---------------------------------------------------------
    # GENERATE VARIABLE
    #---------------------------------------------------------
    
    Draw_cash = fuente.render(str(cash),True,(255,255,255),(0,0,0))
    Draw_cash = fuente.render(str(cash),True,(255,255,255),(0,0,0))
    Draw_second = fuente.render(str(second),True,(255,255,255),(0,0,0))
    Draw_Kills = fuente.render(str(count_enemies),True,(255,255,255),(0,0,0))

    #---------------------------------------------------------
    # SHOW IMAGE AND VARIABLE
    #---------------------------------------------------------

    game_screen.fill([0,0,0])
    
    game_screen.blit(background1,[0,0])
    game_screen.blit(B_diamante,[150,510])
    game_screen.blit(B_oro,[240,510])
    game_screen.blit(B_piedra,[330,510])
    game_screen.blit(B_madera,[420,510])
    game_screen.blit(moneda,(52,525))
    game_screen.blit(Draw_cash,(65,600))

    game_screen.blit(Draw_cashDiamond,(180,600))
    game_screen.blit(Draw_cashGold,(270,600))
    game_screen.blit(Draw_cashStone,(355,600))
    game_screen.blit(Draw_cashWood,(450,600))
    game_screen.blit(display_time,(520,530))
    game_screen.blit(Draw_second,(538,550))
    game_screen.blit(Kills,(530,570))
    game_screen.blit(Draw_Kills,(538,587))
    game_screen.blit(Exit,(610,560))
    


    #---------------------------------------------------------
    # FUNCIONS ROOKS
    #---------------------------------------------------------

    Click(pygame.mouse.get_pos())
    SecondClick()
    ShowRooks(0,len(Diamonds),Diamonds)
    ShowRooks(0,len(Golds),Golds)
    ShowRooks(0,len(Stons),Stons)
    ShowRooks(0,len(Woods),Woods)

    #---------------------------------------------------------
    # FUNCIONS COINS AND AVATARS
    #---------------------------------------------------------

    Generate()

    Loss()
    
    MoveArchers(0, len(Archers))
    MoveGoblins(0,len(Goblins))
    MoveWarrios(0,len(Warriors))
    MoveAxemans(0,len(Axemans))
    ShowCoins(0,len(coins))
    
    clock.tick(60)

def Display_game_2():

    """ SHOW DISPLAY GAME """

    #---------------------------------------------------------
    # GENERATE VARIABLE
    #---------------------------------------------------------
    
    Draw_cash = fuente.render(str(cash),True,(255,255,255),(0,0,0))
    Draw_cash = fuente.render(str(cash),True,(255,255,255),(0,0,0))
    Draw_second = fuente.render(str(second),True,(255,255,255),(0,0,0))
    Draw_Kills = fuente.render(str(count_enemies),True,(255,255,255),(0,0,0))

    #---------------------------------------------------------
    # SHOW IMAGE AND VARIABLE
    #---------------------------------------------------------

    game_screen.fill([0,0,0])
    
    game_screen.blit(background2,[0,0])
    game_screen.blit(B_diamante,[150,510])
    game_screen.blit(B_oro,[240,510])
    game_screen.blit(B_piedra,[330,510])
    game_screen.blit(B_madera,[420,510])
    game_screen.blit(moneda,(52,525))
    game_screen.blit(Draw_cash,(65,600))

    game_screen.blit(Draw_cashDiamond,(180,600))
    game_screen.blit(Draw_cashGold,(270,600))
    game_screen.blit(Draw_cashStone,(355,600))
    game_screen.blit(Draw_cashWood,(450,600))
    game_screen.blit(display_time,(520,530))
    game_screen.blit(Draw_second,(538,550))
    game_screen.blit(Kills,(530,570))
    game_screen.blit(Draw_Kills,(538,587))
    game_screen.blit(Exit,(610,560))

    #---------------------------------------------------------
    # FUNCIONS ROOKS
    #---------------------------------------------------------

    Click(pygame.mouse.get_pos())
    SecondClick()
    ShowRooks(0,len(Diamonds),Diamonds)
    ShowRooks(0,len(Golds),Golds)
    ShowRooks(0,len(Stons),Stons)
    ShowRooks(0,len(Woods),Woods)

    #---------------------------------------------------------
    # FUNCIONS COINS AND AVATARS
    #---------------------------------------------------------

    Generate()

    Loss()
    
    MoveArchers(0, len(Archers))
    MoveGoblins(0,len(Goblins))
    MoveWarrios(0,len(Warriors))
    MoveAxemans(0,len(Axemans))
    ShowCoins(0,len(coins))
    
    clock.tick(60)

def Display_game_3():

    """ SHOW DISPLAY GAME """

    #---------------------------------------------------------
    # GENERATE VARIABLE
    #---------------------------------------------------------
    
    Draw_cash = fuente.render(str(cash),True,(255,255,255),(0,0,0))
    Draw_cash = fuente.render(str(cash),True,(255,255,255),(0,0,0))
    Draw_second = fuente.render(str(second),True,(255,255,255),(0,0,0))
    Draw_Kills = fuente.render(str(count_enemies),True,(255,255,255),(0,0,0))

    #---------------------------------------------------------
    # SHOW IMAGE AND VARIABLE
    #---------------------------------------------------------

    game_screen.fill([0,0,0])
    
    game_screen.blit(background3,[0,0])
    game_screen.blit(B_diamante,[150,510])
    game_screen.blit(B_oro,[240,510])
    game_screen.blit(B_piedra,[330,510])
    game_screen.blit(B_madera,[420,510])
    game_screen.blit(moneda,(52,525))
    game_screen.blit(Draw_cash,(65,600))

    game_screen.blit(Draw_cashDiamond,(180,600))
    game_screen.blit(Draw_cashGold,(270,600))
    game_screen.blit(Draw_cashStone,(355,600))
    game_screen.blit(Draw_cashWood,(450,600))
    game_screen.blit(display_time,(520,530))
    game_screen.blit(Draw_second,(538,550))
    game_screen.blit(Kills,(530,570))
    game_screen.blit(Draw_Kills,(538,587))
    game_screen.blit(Exit,(610,560))

    #---------------------------------------------------------
    # FUNCIONS ROOKS
    #---------------------------------------------------------

    Click(pygame.mouse.get_pos())
    SecondClick()
    ShowRooks(0,len(Diamonds),Diamonds)
    ShowRooks(0,len(Golds),Golds)
    ShowRooks(0,len(Stons),Stons)
    ShowRooks(0,len(Woods),Woods)

    #---------------------------------------------------------
    # FUNCIONS COINS AND AVATARS
    #---------------------------------------------------------

    Generate()

    Loss()
    
    MoveArchers(0, len(Archers))
    MoveGoblins(0,len(Goblins))
    MoveWarrios(0,len(Warriors))
    MoveAxemans(0,len(Axemans))
    ShowCoins(0,len(coins))
    
    clock.tick(60)

def Display_Win():

    """ ANIMATION WIN """

    global size
    
    TheBestScore(Write2(user_text,second, TakePoints(Read()), TakeNames(Read()), 7,False))
    makeAnimation(winAnimation)
    size= (700,500)
    return main()

def Display_Lose():

    """ ANIMATION LOSE """

    global size

    makeAnimation(loseAnimation)
    size= (700,500)
    return main()

def Loss():

    """ CHECH IF HE LOST """

    global level_1,level_2,level_3,Lose, Win
    global Diamonds,Golds,Stons, Woods,Archers,Goblins,Warriors,Axemans,matriz,second,count_enemies,frequency

    for i in range(0,5):

        if matriz[i][0] == 1:

            level_1 = False
            level_2 = False
            level_3 = False
            Win = False
            Lose = True
            matriz = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
            DestroyRookAvatar(len(Avatars[0]),Avatars[0],0,Avatars)
            DestroyRookAvatar(len(Rooks[0]),Rooks[0],0,Rooks)
            second = 0
            count_enemies = 0
            frequency = 10
            pygame.mixer.quit()


#-------------------------------------------------------------
# ANIMATIONS
#-------------------------------------------------------------

def makeAnimation(animation):
    screen_animation= pygame.display.set_mode((800, 500))
    pygame.display.set_caption("WIN OR LOSE?")
    for i in range(0,5):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True         
        screen_animation.fill(pygame.Color('black'))
        screen_animation.blit(animation.image, animation.rect)#dentro de la pantalla se coloque la imagen
        animation.update()
        pygame.display.flip()#reflejo de pantalla
        clock.tick(3)

#-------------------------------------------------------------
# NEXT LEVEL
#-------------------------------------------------------------

def DestroyCoins(end,List):

    """ DELETE COINS """
    
    if 0 == end:

        return
    
    else:
        del coins[0]
        return DestroyCoins(end-1,List)

def DestroyRookAvatar(end,lists,count,List):

    """ DELETE ROOKS AND AVATAR """
    
    if 0 == end:

        count += 1

        if count == 4:
            
            return

        else:

            return DestroyRookAvatar(len(List[count]),List[count],count,List)  
    
    else:
        del lists[0]
        return DestroyRookAvatar(end-1,lists,count,List)
#-------------------------------------------------------------
# FUNCIONS AVATAR
#-------------------------------------------------------------
    

def MoveArchers(i, end):

    """ MOVE ARCHER """

    global MoveArcher
    
    if i == end:
        
        MoveArcher = False
        return
    
    Archers[i].Archer()
    return MoveArchers(i+1, end)

def MoveGoblins(i, end):

    """ MOVE GOBLIN """

    global MoveGoblin
    
    if i == end:
        
        MoveGoblin = False
        return
    
    Goblins[i].Goblin()
    return MoveGoblins(i+1, end)

def MoveWarrios(i, end):

    """ MOVE WARRIOR """

    global MoveWarrior
    
    if i == end:
        
        MoveWarrior = False
        return
    
    Warriors[i].Warrior()
    return MoveWarrios(i+1, end)

def MoveAxemans(i, end):

    """ MOVE AXEMAN """

    global MoveAxeman
    
    if i == end:
        
        MoveAxeman = False
        return
    
    Axemans[i].Axeman()
    return MoveAxemans(i+1, end)

def FindAvatar(i,j,first,end,lists,count,damage):

    """ FIND AVATAR AND DELETE AVATAR """

    global matriz, Avatars, Arqueros,Hacheros,Guerreros,Goblins,count_enemies,level1,level2,level3
    
    if first == end:

        count += 1

        if count == 4:
            
            return

        else:

            return FindAvatar(i,j,0,len(Avatars[count]),Avatars[count],count,damage)  
    
    elif lists[first].DamageAvatar(i,j,damage):
        
        del lists[first]
        matriz[i][j] = 0
        count_enemies += 1

        if count_enemies == 20:

            level1 = True

        elif count_enemies == 50:

            level2 = True

        elif count_enemies == 80:

            level3 = True
            
        return
    
    else:
        
        return FindAvatar(i,j,first+1,end,lists,count,damage)

#-------------------------------------------------------------
# FUNTIONS COINS
#-------------------------------------------------------------

def ShowCoins(i,end):

    """ SHOW COINS """

    if i == end:

        return

    coins[i].UpdateCoin()
    return ShowCoins(i+1,end)

def DetectClick(coor,i,end):

    """ DETECT CLICK """

    if i == end:
        i = 0
        return
    else:
        if coins[i].Click(coor[0],coor[1],coins[i]):
            del coins[i]
            i = 0
            return
        else:
            return DetectClick(coor,i+1,end)

#-------------------------------------------------------------
# FUNTIONS ROOKS
#-------------------------------------------------------------

def vefX(x):
    # DETECT IF THE CLICK IS INSIDE THE BOARD
    if x < 92 or x >=598:
        return 10
    # DETECTS THE POSITION J OF THE MATRIX AND THE POSITION AND OF THE BOARD
    elif 92<=x<154:
        posxMatriz= (0,88)
    elif 154<=x<214:
        posxMatriz= (1,150)
    elif 214<=x<278:
        posxMatriz= (2,212)
    elif 278<=x<344:
        posxMatriz= (3,276)
    elif 344<=x<408:
        posxMatriz= (4,340)
    elif 408<=x<472:
        posxMatriz= (5,404)
    elif 472<=x<538:
        posxMatriz= (6,468)
    elif 538<=x<598:
        posxMatriz= (7,532)
    return posxMatriz

def vefY(y):
    # DETECT IF THE CLICK IS INSIDE THE BOARD
    if y < 30 or y >=465:
        return 10
    # DETECTS THE POSITION I OF THE MATRIX AND THE POSITION AND OF THE BOARD
    elif 30<=y<114:
        posyMatriz= (0,40)
    elif 114<=y<202:
        posyMatriz= (1,126)
    elif 202<=y<300:
        posyMatriz= (2,216)
    elif 300<=y<384:
        posyMatriz= (3,310)
    elif 384<=y<465:
        posyMatriz= (4,394)
    return posyMatriz

def getPositionInMatriz(tupla,click,Diamond,Gold,Ston,Wood):

    """ get the rook positions on the board and in the matrix """
    
    x= tupla[0]
    y= tupla[1]
    posjMatriz= vefX(x)
    posiMatriz= vefY(y)

    if posjMatriz == 10 or posiMatriz == 10:
        return

    #GENERATE ROOK
    elif click:

        # CHECK IF YOU CAN CREATE THE ROOK
        if ModifyMatriz(0,0,len(matriz),len(matriz[0]),posjMatriz[0],posiMatriz[0],3):
            GenerateRook(posjMatriz,posiMatriz)
            return
        
    #DELETE ROOK                   
    else:
        
        ModifyMatriz(0,0,len(matriz),len(matriz[0]),posjMatriz[0],posiMatriz[0],0)
        FindRookDestroy(posjMatriz[0],posiMatriz[0],0,len(Rooks[0]),Rooks[0],0)
        return 

def ModifyMatriz(i,j,Filas, Columnas, posj,posi, new):

    global matriz

    """ find the rook you want to remove to remove it """ 

    if Filas == Columnas:
        return True
    elif i == posi and j == posj:
        if matriz[i][j] == 0 or matriz[i][j] != new:
            matriz[i][j] = new
            return ModifyMatriz(i,j,0,0, posj,posi, new)
        else:
            return False
    elif j == Columnas:
        return ModifyMatriz(i+1,0,Filas, Columnas, posj,posi, new)
    else:
        return ModifyMatriz(i,j+1,Filas, Columnas, posj,posi, new)

def FindRookDestroy(j,i,first,end,lists,count):

    """ encuentra el rook que se desea eliminar para eliminarlo """

    if first == end:

        count += 1

        if count == 4:
            
            return

        else:

            return FindRookDestroy(j,i,0,len(Rooks[count]),Rooks[count],count)  
    
    elif lists[first].Locate(i,j):
        
        del lists[first]
        return
    
    else:
        
        return FindRookDestroy(j,i,first+1,end,lists,count)

def Click(Coordenadas):

    global Diamond, Gold, Ston, Wood, Game

    """ check which was the selected rook """ 

    mouse = pygame.mouse.get_pressed()

    if mouse[0] == 1:

        if 150 < Coordenadas[0] < 230 and 510 < Coordenadas[1] < 590:
            if cash >= 150:    
                Diamond = True 
                return
            else:
                return 
        elif 240 < Coordenadas[0] < 320 and 510 < Coordenadas[1] < 590:
            if cash >= 150:    
                Gold = True 
                return
            else:
                return
        elif 330 < Coordenadas[0] < 410 and 510 < Coordenadas[1] < 590:
            if cash >= 100:    
                Ston = True 
                return
            else:
                return  
        elif 420 < Coordenadas[0] < 500 and 510 < Coordenadas[1] < 590:
            if cash >= 50:    
                Wood = True 
                return
            else:
                return
        elif 610 < Coordenadas[0] < 650 and 560 < Coordenadas[1] < 580:
            Game = False
            return main()
            
    else:
        
        return
    
def SecondClick():
    mouse = pygame.mouse.get_pressed()

    """ save the selected rook until the player selects where he wants to appear it """
    
    if Diamond:
        if mouse[0] == 1:
            getPositionInMatriz(pygame.mouse.get_pos(),True,True,False,False,False)
            return
        else:
            return
    if Gold:
        if mouse[0] == 1:
            getPositionInMatriz(pygame.mouse.get_pos(),True,False,True,False,False)
            return
        else:
            return
    if Ston:
        if mouse[0] == 1:
            getPositionInMatriz(pygame.mouse.get_pos(),True,False,False,True,False)
            return
        else:
            return
    if Wood:
        if mouse[0] == 1:
            getPositionInMatriz(pygame.mouse.get_pos(),True,False,False,False,True)
            return
        else:
            return
    else:
        return

def ShowRooks(i,end,Lists):

    """ muestra los rooks y los disparos """

    if i == end:

        return

    Lists[i].Update()
    Lists[i].Shoot()
    return ShowRooks(i+1,end,Lists)

def FindRook(i,j,first,end,Lists,count,attack):

    """ Delete and damage rooks """
    
    global matriz, Rooks, Archers,Goblins,Warriors,Axemans
    
    if first == end:

        count += 1

        if count == 4:
            
            return

        else:

            return FindRook(i,j,0,len(Rooks[count]),Rooks[count],count,attack)  
    
    elif Lists[first].DamageRooks(i,j,attack):
        
        del Lists[first]
        matriz[i][j] = 0
        return
    
    else:
        
        return FindRook(i,j,first+1,end,Lists,count,attack)
#-------------------------------------------------------------
# GENERATE ROOKS, COINS AND AVATARS
#-------------------------------------------------------------
    
def Generate():

    """ GENERATE ARCHER AND ADD TO THE LIST """
    
    global Archers,Goblins,Warriors,Axemans,Archer,Warrior,Goblin,Axeman,matriz,Coin,coins

    # pos = coordinate in and of the avatar

    pos = random.choice(posFila)
    
    # CALCULATE THE ROW IN WHICH THE AVATAR WILL APPEAR

    if pos == 42:
        i = 0
    if pos == 125:
        i = 1
    if pos == 220:
        i = 2
    if pos == 307:
        i = 3
    if pos == 390:
        i = 4

    # CREATE AN ARCHER AND PUT IT INTO HIS RESPECTIVE LIST
    if Archer:
        if matriz[i][8] != 1:
            matriz[i][8] = 1
            Archers += [Avatar(arquero,5,i,8,593,pos,2)]
            Archer = False
        else:
            return
    # CREA UN GOBLIN Y LO METE A SU RESPECTIVA LISTA
    if Goblin:
        if matriz[i][8] != 1:
            matriz[i][8] = 1
            Goblins += [Avatar(goblin,25,i,8,593,pos,12)]
            Goblin = False
        else:
            return
    # CREATE AN WARRIOR AND PUT IT INTO HIS RESPECTIVE LIST
    if Warrior:
        if matriz[i][8] != 1:
            matriz[i][8] = 1
            Warriors += [Avatar(guerrero,10,i,8,593,pos,5)]
            Warrior = False
        else:
            return
    # CREATE AN AXEMAN AND PUT IT INTO HIS RESPECTIVE LIST
    if Axeman:
        if matriz[i][8] != 1:
            matriz[i][8] = 1
            Axemans += [Avatar(hachero,10,i,8,593,pos,9)]
            Axeman = False
        else:
            return
    # CREATE THE CURRENCY AND THE METE IN ITS RESPECTIVE LIST
    if Coin:
        coins += [Coins(random.randint(0,600),random.randint(0,450),random.choice(value))]
        Coin = False

def GenerateRook(posx,posy):

    global Diamond,Diamonds,Golds,Gold,Stons,Ston,Woods,Wood,cash

    """ GENERATE ROOKS """

    # CREATE THE DIAMNOS ROOK AND ADD IT TO THE LIST
    if Diamond:
        Diamonds += [Rook(posx[1],posy[1],posy[0],posx[0],diamante,16,8,posx[1],posy[1],posy[0],posx[0],posx[1]+63,d_diamante)]
        Diamond = False
        cash -= 150
        return
    # CREATE THE GOLD ROOK AND ADD IT TO THE LIST
    elif Gold:
        Golds += [Rook(posx[1],posy[1],posy[0],posx[0],oro,16,8,posx[1],posy[1],posy[0],posx[0],posx[1]+63,d_oro)]
        Gold = False
        cash -= 150
        return
    # CREATE THE ROOK STONE AND ADD IT TO THE LIST
    elif Ston:
        Stons += [Rook(posx[1],posy[1],posy[0],posx[0],piedra,10,4,posx[1],posy[1],posy[0],posx[0],posx[1]+63,d_piedra)]
        Ston = False
        cash -= 100
        return
    # CREATE THE WOODEN ROOK AND ADD IT TO THE LIST
    elif Wood:
        Woods += [Rook(posx[1],posy[1],posy[0],posx[0],madera,5,2,posx[1],posy[1],posy[0],posx[0],posx[1]+63,d_madera)]
        Wood = False
        cash -= 50
        return

########################## CLASES ############################

#-------------------------------------------------------------
# CLASS OF AVATAR
#-------------------------------------------------------------

class Avatar:
    
    # avatar = imagen del avatar
    # life = cantidad de vida
    # i = fila de la matriz
    # j = columna de la matriz
    # posx = coordenadas en x
    # posy = coordenadas en y
    
    def __init__(self,avatar,life,i,j,x,y,attack):
        
        self.avatar = avatar
        self.life = life
        self.i = i
        self.j = j
        self.posx = x
        self.posy = y
        self.attack = attack
        
    def Archer(self):

        """ SHOOT AND MOVE AVATAR """

        global AttackArcher,moveArrow

        # MOVE AVATAR

        if MoveArcher:

            if self.j == 0:

                pass

            elif  matriz[self.i][self.j-1] != 0:
                
                return 

            else:
                self.j -= 1
                matriz[self.i][self.j+1] -= 1 
                self.posx-= 65
                matriz[self.i][self.j] += 1

        # ATTACK AVATAR
                
        if AttackArcher:

            if matriz[self.i][self.j-1] == 3:

                moveArrow += 3
                
                game_screen.blit(flecha,(self.posx-moveArrow,self.posy))

                FindRook(self.i,self.j-1,0,len(Rooks[0]),Rooks[0],0,self.attack)

                if self.posx-moveArrow < self.posx-130:

                    AttackArcher = False
                    moveArrow = 0

        game_screen.blit(arquero,[self.posx, self.posy])

    def Goblin(self):

        """ SHOOT AND MOVE AVATAR """

        global AttackGoblin
        
        # CHECK IF YOU HAVE A ROOK IN FRONT

        if matriz[self.i][self.j-1] == 3:

            # CALCULA CADA CUANTO TIENE QUE ATACAR Y MUESTRA LA ANIMACION DE ATAQUE
            if second%5 == 0:

                if AttackGoblin:

                    FindRook(self.i,self.j-1,0,len(Rooks[0]),Rooks[0],0,self.attack)

                    AttackGoblin = False
                
                    game_screen.blit(goblinAttack,[self.posx, self.posy])

                    return

                else:

                    game_screen.blit(goblinAttack,[self.posx, self.posy])

                    return

            else:

                game_screen.blit(goblinAttack,[self.posx, self.posy])

                return

            
        # MOVE AVATAR
        if MoveGoblin:

            if self.j == 0:

                pass

            elif  matriz[self.i][self.j-1] != 0:
                
                return 

            else:

                game_screen.blit(goblin,[self.posx, self.posy])
                
                #UPDATE MATRIX
                self.j -= 1
                matriz[self.i][self.j+1] -= 1 
                self.posx-= 65
                matriz[self.i][self.j] += 1

                return

        else:

            game_screen.blit(goblin,[self.posx, self.posy])

    def Warrior(self):

        """ SHOOT AND MOVE AVATAR """

        global AttackWarrior
        
        # CHECK IF YOU HAVE A ROOK IN FRONT
        if matriz[self.i][self.j-1] == 3:

            if second%15 == 0:

                if AttackWarrior:

                    FindRook(self.i,self.j-1,0,len(Rooks[0]),Rooks[0],0,self.attack)

                    AttackWarrior = False
                
                    game_screen.blit(guerreroAttack,[self.posx, self.posy])

                    return

                else:

                    game_screen.blit(guerreroAttack,[self.posx, self.posy])

                    return

            else:

                game_screen.blit(guerreroAttack,[self.posx, self.posy])

                return
            
        # MOVE AVATAR
        if MoveWarrior:

            if self.j == 0:

                pass

            elif  matriz[self.i][self.j-1] != 0:
                
                return 

            else:
                
                #UPDATE MATRIX

                game_screen.blit(guerrero,[self.posx, self.posy])
                
                self.j -= 1
                matriz[self.i][self.j+1] -= 1 
                self.posx-= 65
                matriz[self.i][self.j] += 1

                return

        else:

            game_screen.blit(guerrero,[self.posx, self.posy])

    def Axeman(self):

        """ SHOOT AND MOVE AVATAR """

        global AttackAxeman


        # CHECK IF YOU HAVE A ROOK IN FRONT    
        if matriz[self.i][self.j-1] == 3:

            if second%5 == 0:

                if AttackAxeman:

                    FindRook(self.i,self.j-1,0,len(Rooks[0]),Rooks[0],0,self.attack)

                    AttackAxeman = False
                
                    game_screen.blit(hacheroAttack,[self.posx, self.posy])

                    return

                else:

                    game_screen.blit(hacheroAttack,[self.posx, self.posy])

                    return

            else:

                game_screen.blit(hacheroAttack,[self.posx, self.posy])

        # MOVE AVATAR
        if MoveAxeman:

            if self.j == 0:

                pass

            elif  matriz[self.i][self.j-1] != 0:
                
                return 

            else:
                
                #UPDATE MATRIX

                game_screen.blit(hachero,[self.posx, self.posy])
                
                self.j -= 1
                matriz[self.i][self.j+1] -= 1 
                self.posx-= 65
                matriz[self.i][self.j] += 1

                return
                
        else:

            game_screen.blit(hachero,[self.posx, self.posy])

    def DamageAvatar(self,i,j,damage):

        """ damage avatar """

        if i == self.i and j == self.j:

            self.life -= damage

            if self.life <= 0:

                return True

            else:

                return False
        else:

            return False

#-------------------------------------------------------------
# CLASS OF ROOKS
#-------------------------------------------------------------
class Rook:
    
    # posx = position x of the rook
    # posy = y position of the rook
    # posi = position i of the rook in the matrix
    # posj = j position of the rook in the array
    # image = rook image
    # health = rook life
    # attack = magic damage the rook does
    # dx = position x of the shot
    # dy = position y of the shot
    # di = positioning of the shot in the matrix
    # dj = position j of the shot in the matrix
    # df = detect the change of position in the matrix
    # shoot = shot image

    def __init__(self,posx,posy,posi,posj,image,health,attack,dx,dy,di,dj,df,shoot):

        self.x = posx
        self.y = posy
        self.i = posi
        self.j = posj
        self.imagen = image
        self.health = health
        self.attack = attack
        self.dx = dx
        self.dy = dy
        self.di = di
        self.dj = dj
        self.df = df
        self.disparo = shoot
        self.M_S = False
        
    def Update(self):

        """ show rook """

        game_screen.blit(self.imagen,(self.x,self.y))

    def Locate(self,i,j):


        """gives the position of the rook in the array"""

        if i == self.i and j == self.j:
            return True
        else:
            return False
        
    def Shoot(self):

        """ move shoot and update matrix """

        global matriz

        if second%Attack_roock == 0:

            self.M_S = True

        if self.M_S:

            self.dx += 5

            if self.dx + 10 > 660:

                self.df = self.x + 63

                self.di = self.i

                self.dj = self.j

                self.M_S = False

                return

            if self.dx > self.df:

                self.dj += 1
                self.df += 63
                
                if matriz[self.di][self.dj] == 1:

                    FindAvatar(self.di,self.dj,0,len(Avatars[0]),Avatars[0],0,self.attack)

                    self.M_S = False

                    self.df = self.x + 63

                    self.di = self.i

                    self.dj = self.j

                    return

                else:

                    game_screen.blit(self.disparo,(self.dx,self.dy))
                    

            else:


                game_screen.blit(self.disparo,(self.dx,self.dy))

        else:

            self.dx = self.x

    def DamageRooks(self,i,j,attack):

        """ damage rook """

        if i == self.i and j == self.j:

            self.health -= attack

            if self.health <= 0:

                return True

            else:

                return False
        else:

            return False
#-------------------------------------------------------------
# CLASS COINS
#-------------------------------------------------------------

class Coins:

    # x = posicion en x
    # y = posicion en y
    # valor = valor random de la moneda

    def __init__(self,x,y,valor):
        
        self.posx = x
        self.posy = y
        self.valor = valor
        
    def UpdateCoin(self):

        """ show coins """
        
        game_screen.blit(moneda,(self.posx,self.posy))

    def Click(self,posx,posy,elemento):

        """ check if you clicked on the coins """

        global cash

        # COMPARE THE CLICK COORDINATES WITH THE CURRENCY

        if posx >= self.posx and posx <= self.posx + 50:

            if posy >= self.posy and posy <= self.posy + 50:

                cash += self.valor

                return True
            else:
                return False
        else:
            return False

def Game_diplay():

    global game_screen,user_text,Game

    Game= True

    game_screen = pygame.display.set_mode([700, 625])

    if user_text == '':

        user_text = "INVITADO"

    ######################### THREAD ################################

    time_second = Thread(target = Time, args= ())
    time_second.start()

    ######################### DISPLAY ###############################

    pygame.display.set_caption("AvatarsvsRooks")
    pygame.mixer.quit()
    pygame.mixer.init()
    pygame.mixer.music.load('level_1.mp3')
    pygame.mixer.music.play(10)
    
    while Game:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    DetectClick(pygame.mouse.get_pos(),0,len(coins))
                if event.button == 3:
                    getPositionInMatriz(pygame.mouse.get_pos(),False,False,False,False,False)
                
        if level_1:
            
            Display_game_1()

        elif level_2:

            Display_game_2()

        elif level_3:

            Display_game_3()

        elif Win:

            Display_Win()

        elif Lose:

            Display_Lose()

        pygame.display.flip()
#_______________________________
#________/Functions for bottons.
def draw_text(text, container_image, container_rec, font_render, color):#validate and draw the button
    text = font_render.render(text, 1, color)
    center = text.get_rect()
    dif_x = container_image.center[0] - center.center[0]
    dif_y = container_image.center[1] - center.center[1]
    screen.blit(text, [container_rec.left + dif_x, container_rec.top + dif_y])
def draw_botton_1(list_botton):
    panel = pygame.transform.scale(image_panel, [700, 500])
    screen.blit(panel, [0, 0])#position from which the background unfolds
    for boton in list_botton:
        if boton['on_click']:#validate the click
            screen.blit(boton['image_pressed'], boton['rect'])#repress the image
        else:
            screen.blit(boton['image'], boton['rect'])
        draw_text(boton['text'], boton['image'].get_rect(), boton['rect'], font, WHITE)#get the click
def set_text(place, text):#parameters butto.append
    draw_text(text, place['image'].get_rect(), place['rect'], font_num, COLOR_TEXT)
#____________
#______/Main.
def main():
    global Game,level_1
    Game = False
    level_1 = True
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("INICIO")
    #music
    pygame.mixer.init()
    pygame.mixer.music.load('music_menu.mp3')
    pygame.mixer.music.play(10)
    #variables
    clock = pygame.time.Clock()
    botton_square = pygame.transform.scale(image_botton_square, [120, 90])#button dimensions
    botton_square_pressed = pygame.transform.scale(image_botton_square_pressed, [90, 90])#button dimensions
    r_boton_2_1 = botton_square.get_rect()
    r_boton_2_2 = botton_square.get_rect()
    r_boton_2_3 = botton_square.get_rect()
    r_boton_2_4 = botton_square.get_rect()
    r_boton_2_5 = botton_square.get_rect()
    r_boton_2_6 = botton_square.get_rect()
    r_boton_2_7 = botton_square.get_rect()
    r_boton_2_8 = botton_square.get_rect()
    botones = []#enter buttons in list
    r_boton_2_1.topleft = [450, 300]#pos1/validate the function set_text
    botones.append({'text': "Ayuda", 'image': botton_square, 'image_pressed': botton_square_pressed, 'rect': r_boton_2_1, 'on_click': False})
    r_boton_2_2.topleft = [450, 400]#os2/validate the function set_text
    botones.append({'text': "Jugadores", 'image': botton_square, 'image_pressed': botton_square_pressed, 'rect': r_boton_2_2, 'on_click': False})
    r_boton_2_3.topleft = [580, 300]#pos3/validate the function set_text
    botones.append({'text': "Créditos", 'image': botton_square, 'image_pressed': botton_square_pressed, 'rect': r_boton_2_3, 'on_click': False})
    r_boton_2_4.topleft = [580, 400]#pos/validate the function set_text
    botones.append({'text': "Registro", 'image': botton_square, 'image_pressed': botton_square_pressed, 'rect': r_boton_2_4, 'on_click': False})
    r_boton_2_5.topleft = [10, 400]#pos4/validate the function set_text
    botones.append({'text': "5", 'image': botton_square, 'image_pressed': botton_square_pressed, 'rect': r_boton_2_5, 'on_click': False})
    r_boton_2_6.topleft = [130, 400]#pos5/validate the function set_text
    botones.append({'text': "7", 'image': botton_square, 'image_pressed': botton_square_pressed, 'rect': r_boton_2_6, 'on_click': False})
    r_boton_2_7.topleft = [250, 400]#pos6/validate the function set_text
    botones.append({'text': "10", 'image': botton_square, 'image_pressed': botton_square_pressed, 'rect': r_boton_2_7, 'on_click': False})
    r_boton_2_8.topleft = [270, 230]#pos6/validate the function set_text
    botones.append({'text': "JUGAR", 'image': botton_square, 'image_pressed': botton_square_pressed, 'rect': r_boton_2_8, 'on_click': False})
    text1=pygame.font.SysFont ("",35)#text
    text_= text1.render ("Selecciona la frecuencia:",True, BLACK)
    #_______________________________
    #________/Functions for bottons.
    def draw_text(text, container_image, container_rec, font_render, color):#validate and draw the button
        text = font_render.render(text, 1, color)
        center = text.get_rect()
        dif_x = container_image.center[0] - center.center[0]
        dif_y = container_image.center[1] - center.center[1]
        screen.blit(text, [container_rec.left + dif_x, container_rec.top + dif_y])
    def draw_botton_1(list_botton):
        for boton in list_botton:
            if boton['on_click']:#validate the click
                screen.blit(boton['image_pressed'], boton['rect'])#repress the image
            else:
                screen.blit(boton['image'], boton['rect'])
            draw_text(boton['text'], boton['image'].get_rect(), boton['rect'], font, WHITE)#get the click
    def set_text(place, text):#parameters butto.append
        draw_text(text, place['image'].get_rect(), place['rect'], font_num, COLOR_TEXT)
    botton_square = pygame.transform.scale(image_botton_square, [110, 90])
    botton_square_pressed = pygame.transform.scale(image_botton_square_pressed, [90, 90])

    #__________________
    #_______/Variables.
    LEFT = 1
    RIGHT = 3
    running = 1
    #_________________
    #____/help window.
    def Help ():
        global user_text
        #_________________________
        #________/Help Definition.
        pygame.init()
        helpp= pygame.display.set_mode ([700,500])
        pygame.display.set_caption ("AYUDA")
        bg= pygame.image.load("./images/fondos/fayu.png")                
        #___________________
        #________/Variables.
        WHITE = (255, 255, 255)
        COLOR_TEXT = (50, 60, 80)
        clock= pygame.time.Clock()
        Font= pygame.font.Font(None, 32)
        input_rect= pygame.Rect (180,0,140,32)
        color_a= pygame.Color ("lightskyblue3")#color entry
        color_p= pygame.Color ("gray15")#color entry
        color = color_p
        pygame.display.set_caption("Entrada de text")
        image_botton = pygame.image.load("images/bon.png")#load image button
        image_botton_pressed = pygame.image.load("./images/bon.png")
        image_botton_square = pygame.image.load("./images/bon.png")
        image_botton_square_pressed = pygame.image.load("./images/bon.png")
        font = pygame.font.SysFont('Courier', 20)
        font_num = pygame.font.SysFont('Pacifico Regular', 30)
        text=pygame.font.SysFont ("",30)
        text_help= text.render ("Bienvenido a la sección de ayuda, aquí",True, BLACK)#text
        text2=pygame.font.SysFont ("",30)
        text_help2= text2.render ("podras descubrir como funciona el juego.",True, BLACK)#text
        text3=pygame.font.SysFont ("",30)
        text_help3= text3.render ("Al iniciar tendras que ingresar tu nombre y",True, BLACK)#text
        text4=pygame.font.SysFont ("",30)
        text_help4= text4.render ("la frecuencia con la que quieres jugar.",True, BLACK)#text
        text5=pygame.font.SysFont ("",30)
        text_help5= text5.render ("Seguidamente presionarás en jugar.",True, BLACK)#text
        text6=pygame.font.SysFont ("",30)
        text_help6= text6.render ("En el juego contarás con cuatro ROOKS",True, BLACK)#text
        text7=pygame.font.SysFont ("",30)
        text_help7= text7.render ("que debes comprar y posicionar con click",True, BLACK)#text
        text8=pygame.font.SysFont ("",30)
        text_help8= text8.render ("izquierdo y borrar con el derecho, Debes",True, BLACK)#text
        text9=pygame.font.SysFont ("",30)
        text_help9= text9.render ("recoger las monedas que se muestran. Al ",True, BLACK)#text
        text10=pygame.font.SysFont ("",30)
        text_help10= text10.render ("disparar tu rook el avatar se incendiará.",True, BLACK)#text
        text11=pygame.font.SysFont ("",30)
        text_help11= text11.render ("Al ganar pasarás de nivel. Si ganas se te",True, BLACK)#text
        text12=pygame.font.SysFont ("",30)
        text_help12= text12.render ("reconocerá en la ventana de jugadores.",True, BLACK)#text
        text13=pygame.font.SysFont ("",30)
        text_help13= text13.render ("SUERTE!!.",True, BLACK)#text
        r_boton_1_1 = image_botton.get_rect()
        r_boton_1_2 = image_botton.get_rect()
        r_boton_2_1 = botton_square.get_rect()
        botones = []#button in list for get
        r_boton_2_1.topleft = [450, 400]
        botones.append({'text': "Atras", 'image': botton_square, 'image_pressed': botton_square_pressed, 'rect': r_boton_2_1, 'on_click': False})
        LEFT=  1
        RIGHT= 3
        running=1
        #user_text=''#from txt
        #____________________
        #____/main loop help.
        exxt= False#for exit
        while exxt != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exxt= True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    return main()
            helpp.blit(bg, [0,0])
            draw_botton_1(botones)
            helpp.blit(text_help, (145,120))
            helpp.blit(text_help2, (145,135))
            helpp.blit(text_help3, (145,170))
            helpp.blit(text_help4, (145,185))
            helpp.blit(text_help5, (145,220))
            helpp.blit(text_help6, (145,239))
            helpp.blit(text_help7, (145,255))
            helpp.blit(text_help8, (145,273))
            helpp.blit(text_help9, (145,290))
            helpp.blit(text_help10, (145,310))
            helpp.blit(text_help11, (145,340))
            helpp.blit(text_help12, (145,360))
            helpp.blit(text_help13, (145,400))
            pygame.display.update ()
            clock.tick(60)
        pygame.quit()
    #____________________
    #____/credits window.
    def Credits ():
        #_____________________
        #_____/Credits window.
        pygame.init()
        creditos= pygame.display.set_mode ([700,500])
        pygame.display.set_caption ("CREDITOS")
        bgc= pygame.image.load("./images/fondos/fcre.png")
        David= pygame.image.load("./images/autores/david.png")
        Montse= pygame.image.load("./images/autores/montse.png")
        #_________________
        #______/Variables.
        BG = (32, 30, 32)
        WHITE = (255, 255, 255)
        COLOR_TEXT = (50, 60, 80)
        image_panel = pygame.image.load("./images/fondos/fondo.png")
        image_botton = pygame.image.load("./images/bon.png")
        image_botton_pressed = pygame.image.load("./images/bon.png")
        image_botton_square = pygame.image.load("./images/bon.png")
        image_botton_square_pressed = pygame.image.load("./images/bon.png")
        font = pygame.font.SysFont('Courier', 20)
        font_num = pygame.font.SysFont('Pacifico Regular', 30)
        text1=pygame.font.SysFont ("",30)
        text_cre= text1.render ("Instituto Tecnológico de Costa Rica",True, BLACK)
        text_cre2= text1.render ("País de realización: Costa Rica.",True, BLACK)
        text_cre3= text1.render ("Curso: Taller de Programación.",True, BLACK)
        text_cre4= text1.render ("Profesor: Jason Leitón Jimenez.",True, BLACK)
        text_cre5= text1.render ("Creadores del programa:",True, BLACK)
        text_cre6= text1.render ("Luis David Richmond Soto.",True, BLACK)
        text_cre7= text1.render ("Carné: 2020077226.",True, BLACK)
        text_cre8= text1.render ("Montserrat Monge Téllez.",True, BLACK)
        text_cre9= text1.render ("Carné: 2019390571.",True, BLACK)
        text_cre10= text1.render ("Versión del programa:1.0.0",True, BLACK)
        text_cre11= text1.render ("I Semestre 2020.",True, BLACK)
        #_________________________
        #____/Function for button.
        def draw_text2(text, container_image, container_rec, font_render, color):#validate and draw the button
            text = font_render.render(text, 1, color)
            center = text.get_rect()
            dif_x = container_image.center[0] - center.center[0]
            dif_y = container_image.center[1] - center.center[1]
            screen.blit(text, [container_rec.left + dif_x, container_rec.top + dif_y])
        def draw_botton_12(list_botton):
            panel = pygame.transform.scale(image_panel, [560, 420])#position from which the background unfolds
            screen.blit(panel, [20, 20])
            for boton in list_botton:
                if boton['on_click']:#validate the click
                    screen.blit(boton['image_pressed'], boton['rect'])#repress the image
                else:
                    screen.blit(boton['image'], boton['rect'])
                draw_text(boton['text'], boton['image'].get_rect(), boton['rect'], font, WHITE)#get the click
        def set_text2(place, text):
            draw_text(text, place['image'].get_rect(), place['rect'], font_num, COLOR_TEXT)
        #__________________
        #_______/Variables.
        clock = pygame.time.Clock()
        botton_square = pygame.transform.scale(image_botton_square, [90, 90])
        botton_square_pressed = pygame.transform.scale(image_botton_square_pressed, [90, 90])
        r_boton_1_1 = image_botton.get_rect()
        r_boton_1_2 = image_botton.get_rect()
        r_boton_2_1 = botton_square.get_rect()
        botones = []
        r_boton_2_1.topleft = [470, 410]
        botones.append({'text': "Atras", 'image': botton_square, 'image_pressed': botton_square_pressed, 'rect': r_boton_2_1, 'on_click': False})
        LEFT=  1
        RIGHT= 3
        running=1
        #_______________________
        #____/Main Loop Credits.
        exxt= False
        while exxt != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exxt= True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    return main()
            #__________________
            #_______/Variables.
            creditos.blit(bgc, [0,0])
            draw_botton_1(botones)
            creditos.blit(David, [320,320])
            creditos.blit(Montse, [450,320])
            creditos.blit(text_cre, (145,95))
            creditos.blit(text_cre2, (145,120))
            creditos.blit(text_cre3, (145,140))
            creditos.blit(text_cre4, (145,160))
            creditos.blit(text_cre5, (145,180))
            creditos.blit(text_cre6, (145,200))
            creditos.blit(text_cre7, (145,220))
            creditos.blit(text_cre8, (145,240))
            creditos.blit(text_cre9, (145,260))
            creditos.blit(text_cre10, (145,280))
            creditos.blit(text_cre11, (145,300))
            pygame.display.update ()
        pygame.quit()
    

    #_______________________
    #_______/Players window.
    def Players ():
        #____________________________
        #________/Players Definition.
        pygame.init()
        jugadores= pygame.display.set_mode ([700,500])
        pygame.display.set_caption ("JUGADORES")
        bgp= pygame.image.load("./images/fondos/fju.png")
        #_________________
        #______/Variables.
        listplayers = Read()
        BG = (32, 30, 32)
        WHITE = (255, 255, 255)
        COLOR_TEXT = (50, 60, 80)
        image_panel = pygame.image.load("./images/fondos/fondo.png")
        image_botton = pygame.image.load("./images/bon.png")
        image_botton_pressed = pygame.image.load("./images/bon.png")
        image_botton_square = pygame.image.load("./images/bon.png")
        image_botton_square_pressed = pygame.image.load("./images/bon.png")
        font = pygame.font.SysFont('Courier', 20)
        font_num = pygame.font.SysFont('Pacifico Regular', 30)
        text1=pygame.font.SysFont ("",30)
        text_pos= text1.render ("Posición",True, BLACK)
        text_nam= text1.render ("Nombre/Tiempo",True, BLACK)
        text_first= text1.render ("Primer Lugar",True, BLACK)
        text_second= text1.render ("Segundo Lugar",True, BLACK)
        text_third= text1.render ("Tercer Lugar",True, BLACK)
        text_n1= text1.render (str(listplayers[0]),True, BLACK)
        text_n2= text1.render (str(listplayers[1]),True, BLACK)
        text_n3= text1.render (str(listplayers[2]),True, BLACK)
        #_________________________
        #____/Function for botton.
        def draw_text3(text, container_image, container_rec, font_render, color):#validate and draw the button
            text = font_render.render(text, 1, color)
            center = text.get_rect()
            dif_x = container_image.center[0] - center.center[0]
            dif_y = container_image.center[1] - center.center[1]
            screen.blit(text, [container_rec.left + dif_x, container_rec.top + dif_y])
        def draw_botton_13(list_botton):
            panel = pygame.transform.scale(image_panel, [560, 420])
            screen.blit(panel, [20, 20])#position from which the background unfolds
            for boton in list_botton:
                if boton['on_click']:#validate the click
                    screen.blit(boton['image_pressed'], boton['rect'])#repress the image
                else:
                    screen.blit(boton['image'], boton['rect'])
                draw_text(boton['text'], boton['image'].get_rect(), boton['rect'], font, WHITE)#get the click
        def set_text3(place, text):
            draw_text(text, place['image'].get_rect(), place['rect'], font_num, COLOR_TEXT)
        #__________________
        #_______/Variables.
        clock = pygame.time.Clock()
        botton_square = pygame.transform.scale(image_botton_square, [90, 90])
        botton_square_pressed = pygame.transform.scale(image_botton_square_pressed, [90, 90])
        r_boton_1_1 = image_botton.get_rect()
        r_boton_1_2 = image_botton.get_rect()
        r_boton_2_1 = botton_square.get_rect()
        botones = []
        r_boton_2_1.topleft = [470, 410]#validate the function set_text
        botones.append({'text': "Atras", 'image': botton_square, 'image_pressed': botton_square_pressed, 'rect': r_boton_2_1, 'on_click': False})
        LEFT=  1
        RIGHT= 3
        running=1
        #_______________________
        #____/Main Loop Players.
        exxt= False
        while exxt != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exxt= True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    print(event)
                    print ("click izquierdo (%d, %d)" % event.pos)
                    return main()
            jugadores.blit(bgp, [0,0])
            jugadores.blit(text_pos, (190,95))
            jugadores.blit(text_nam, (290,95))
            jugadores.blit(text_first, (145,140))
            jugadores.blit(text_second, (145,180))
            jugadores.blit(text_third, (145,210))
            jugadores.blit(text_n1, (300,140))
            jugadores.blit(text_n2, (300,180))
            jugadores.blit(text_n3, (300,210))
            draw_botton_1(botones)
            pygame.display.update ()
        pygame.quit()
    #_____________________
    #_______/Login window.
    def Login ():

        global user_text
        
        #__________________
        #____/login window.
        pygame.init()
        registros= pygame.display.set_mode ([700,500])
        pygame.display.set_caption ("REGISTROS")
        bgL= pygame.image.load("./images/fondos/fre.png")
        #_______________
        #____/Variables.
        BG = (32, 30, 32)
        WHITE = (255, 255, 255)
        COLOR_TEXT = (50, 60, 80)
        clock= pygame.time.Clock()
        Font= pygame.font.Font(None, 32)
        input_rect= pygame.Rect(370,100,140,32)
        color_a= pygame.Color("lightskyblue3")
        color_p= pygame.Color ("gray15")
        color= color_p
        image_panel = pygame.image.load("./images/fondos/fondo.png")
        image_botton = pygame.image.load("./images/bon.png")
        image_botton_pressed = pygame.image.load("./images/bon.png")
        image_botton_square = pygame.image.load("./images/bon.png")
        image_botton_square_pressed = pygame.image.load("./images/bon.png")
        image_botton_square2 = pygame.image.load("./images/bon.png")
        image_botton_square_pressed2 = pygame.image.load("./images/bon.png")
        font = pygame.font.SysFont('Courier', 20)
        font_num = pygame.font.SysFont('Pacifico Regular', 30)
        #_________________________
        #____/Function for botton.
        def draw_text4(text, container_image, container_rec, font_render, color):#validate and draw the button
            text = font_render.render(text, 1, color)
            center = text.get_rect()
            dif_x = container_image.center[0] - center.center[0]
            dif_y = container_image.center[1] - center.center[1]
            screen.blit(text, [container_rec.left + dif_x, container_rec.top + dif_y])
        def draw_botton_14(list_botton):
            panel = pygame.transform.scale(image_panel, [560, 420])
            screen.blit(panel, [20, 20])#position from which the background unfolds
            for boton in list_botton:
                if boton['on_click']:#validate the click
                    screen.blit(boton['image_pressed'], boton['rect'])#repress the image
                else:
                    screen.blit(boton['image'], boton['rect'])
                draw_text(boton['text'], boton['image'].get_rect(), boton['rect'], font, WHITE)#get the click
        def set_text4(place, text):
            draw_text(text, place['image'].get_rect(), place['rect'], font_num, COLOR_TEXT)
        #_______________
        #____/Variables.
        clock = pygame.time.Clock()
        botton_square2 = pygame.transform.scale(image_botton_square2, [400, 200])
        botton_square_pressed2 = pygame.transform.scale(image_botton_square_pressed2, [90, 90])  
        botton_square = pygame.transform.scale(image_botton_square, [90, 90])
        botton_square_pressed = pygame.transform.scale(image_botton_square_pressed, [90, 90])
        r_boton_1_1 = image_botton.get_rect()
        r_boton_1_2 = image_botton.get_rect()
        r_boton_2_1 = botton_square.get_rect()
        r_boton_2_2 = botton_square2.get_rect()
        r_boton_2_3 = botton_square.get_rect()
        botones = []
        r_boton_2_1.topleft = [470, 410]#validate the function set_text
        botones.append({'text': "Atras", 'image': botton_square, 'image_pressed': botton_square_pressed, 'rect': r_boton_2_1, 'on_click': False})
        r_boton_2_2.topleft = [150, 200]#validate the function set_text
        botones.append({'text': "", 'image': botton_square2, 'image_pressed': botton_square_pressed2, 'rect': r_boton_2_2, 'on_click': False})
        r_boton_2_3.topleft = [300, 150]#validate the function set_text
        botones.append({'text': "Guardar", 'image': botton_square, 'image_pressed': botton_square_pressed, 'rect': r_boton_2_3, 'on_click': False})
       
        #_____________________
        #____/Main Loop Login.
        user_text= ''#to file entry
        exxt= False
        active= False
        text=pygame.font.SysFont ("",30)
        text_entry= text.render ("Nombre Jugador:",True,(0,0,0))#text 

        while exxt != True:#for exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exxt= True#for exit 
                if event.type == MOUSEBUTTONDOWN:
                    if input_rect.collidepoint (event.pos):
                        active = True
                if event.type == pygame.KEYDOWN:
                    if active == True:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]#entry text
                        else:
                            user_text += event.unicode
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:#validate psoditions mouse
                    x= event.pos[0]
                    y= event.pos[1]
                    z=False
                    if 308<x<385 and 170<y<223:
                        userName= user_text
                        i=0
                        while i != len(loginsRegister):
                            if userName==loginsRegister[i]:
                                print("Ya estas registrad@! "+userName)
                                botones[1]= {'text': "Ya estas registrad@! "+userName, 'image': botton_square2, 'image_pressed': botton_square_pressed2, 'rect': r_boton_2_2, 'on_click': False}
                                z=True

                            i=i+1;

                        if(z==False):
                                addToDataBase(loginsRegister, userName)
                                botones[1]= {'text': "Te has registrado!", 'image': botton_square2, 'image_pressed': botton_square_pressed2, 'rect': r_boton_2_2, 'on_click': False}

                    if 479<x<546 and 439<475:
                        return main()
                    print ("click izquierdo (%d, %d)" % event.pos)


            if active:
                color= color_a#color for entry
            else:
                color= color_p#color for entry
                
            registros.blit(bgL, [0,0])
            draw_botton_1(botones)
            pygame.draw.rect (registros, color, input_rect,2)
            text_surface= Font.render (user_text, True, (0,0,0))
            registros.blit (text_surface, (input_rect.x +1, input_rect.y +1))
            input_rect.w= max(100, text_surface.get_width())+1
            registros.blit(text_entry, (170,100))
            pygame.display.update ()
        pygame.quit()
    #_______________________
    #_____/Frecuency Roocks.
    def Frecuency_Rooks (num):
        global Attack_roock
        Attack_roock= num


    
    #_______________
    #____/Main Loop.
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            x= event.pos[0]
            y= event.pos[1]
            if 464<x<557 and 327<y<366:    
                Help()
            elif 594<x<685 and 329<y<363:
                Credits()
            elif 465<x<551 and 428<y<462:
                Players()
            elif 594<x<685 and 428<y<463:
                Login()
            elif 25<x<117 and 429<y<464:
                print("La frecuencia será 5")
                Frecuency_Rooks(5);
            elif 145<x<233 and 429<y<463:
                print("La frecuencia será 7")
                Frecuency_Rooks(7);
            elif 263<x<355 and 428<y<463:
                print("La frecuencia será 10")
                Frecuency_Rooks(10)
            elif 278<x<381 and 252<y<304:
                Game_diplay()

        screen.blit(image_panel, (0,0))
        screen.blit(text_, (10,370))
        draw_botton_1(botones)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == '__main__':
    main()

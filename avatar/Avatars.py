########################### BIBLIOTCAS ########################
import pygame
import time
from threading import Thread
import random
########################### DISPLAY ###########################

pygame.init()

screen = pygame.display.set_mode([700, 600])
pygame.display.set_caption("Avatars")

fuente = pygame.font.Font('freesansbold.ttf',15)

########################### VARIABLES #########################

global Game
Game = True

Arquero = False
MoveArquero = False
Goblin = False
MoveGoblin = False
Guerrero = False
MoveGuerrero = False
Hachero = False
MoveHachero = False

Arqueros = []
Goblins = []
Guerreros = []
Hacheros = []

matriz = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

posFila = [42,125,220,307,390]

posicion = random.choice(posFila)
########################## FUNCIONES ##########################

""" calcula el tiempo de los eventos """

def Time(Game):

    global second
    global Arquero
    global MoveArquero
    global Goblin
    global MoveGoblin
    global Guerrero
    global MoveGuerrero
    global Hachero
    global MoveHachero
    
    second = 0
        
    while Game:
            
        # DA EL PASO A CREAR EL ARQUERO 
        if second%5 == 0 and second != 0:

            Arquero = True

        # DA EL PASO A MOVER EL ARQUERO 
        if second%12 == 0 and second != 0:

            MoveArquero = True

        # DA EL PASO A CREAR UN GOBLIN
        if second%7 == 0 and second != 0:

            Goblin = True

        # DA EL PASO A MOVER EL GOBLIN
        if second%15 == 0 and second != 0:

            MoveGoblin = True

        # DA EL PASO A CREAR EL GUERRERO
        if second%9 == 0 and second != 0:

            Guerrero = True
            
        # DA EL PASO A MOVER EL GUERRERO 
        if second%11 == 0 and second != 0:

            MoveGuerrero = True

        # DA EL PASO A CREAR EL HACHERO
        if second%6 == 0 and second != 0:

            Hachero = True

        # DA EL PASO A MOVER EL HACHERO
        if second%9 == 0 and second != 0:

            MoveHachero = True
   
        second += 1
        time.sleep(1)

def Display_game():

    """ Muestra la pantalla del juego """

    screen.blit(background,[0,0])
    screen.blit(MiTexto,(100,550))
    Generar()
    MoverArqueros(0, len(Arqueros))
    MoverGoblins(0,len(Goblins))
    MoverGuerreros(0,len(Guerreros))
    MoveHacheros(0,len(Hacheros))


def MoverArqueros(i, fin):

    """ mueve los arqueros de la lista """

    global MoveArquero
    
    if i == fin:
        
        MoveArquero = False
        return
    
    Arqueros[i].Archer()
    return MoverArqueros(i+1, fin)

def MoverGoblins(i, fin):

    """ mueve los arqueros de la lista """

    global MoveGoblin
    
    if i == fin:
        
        MoveGoblin = False
        return
    
    Goblins[i].Goblin()
    return MoverGoblins(i+1, fin)

def MoverGuerreros(i, fin):

    """ mueve los Guerreros de la lista """

    global MoveGuerrero
    
    if i == fin:
        
        MoveGuerrero = False
        return
    
    Guerreros[i].Warrior()
    return MoverGuerreros(i+1, fin)

def MoveHacheros(i, fin):

    """ mueve los Guerreros de la lista """

    global MoveHachero
    
    if i == fin:
        
        MoveHachero = False
        return
    
    Hacheros[i].Hachero()
    return MoveHacheros(i+1, fin)
    
def Generar():

    """ genera un arquero y lo mete en su respectiva lista """
    
    global Arquero, Arqueros, Goblin, Goblins, Guerrero, Guerreros,Hachero,Hacheros
    
    if Arquero:
        Arqueros += [Avatar(5,5,Comprobar(random.choice(posFila)),593,50,avatar1)]
        Arquero = False
    if Goblin:
        Goblins += [Avatar(5,5,Comprobar(random.choice(posFila)),593,50,goblin)]
        Goblin = False
    if Guerrero:
        Guerreros += [Avatar(5,5,Comprobar(random.choice(posFila)),593,50,guerrero)]
        Guerrero = False
    if Hachero:
        Hacheros += [Avatar(5,5,Comprobar(random.choice(posFila)),593,50,guerrero)]
        Hachero = False

def Comprobar(nuevaposicion):

    global posicion

    if posicion == nuevaposicion:

        return Comprobar(random.choice(posFila))

    else:
        posicion = nuevaposicion
        return nuevaposicion
        
###########################IMAGENES###########################  

background = pygame.image.load("fondo1.png").convert()

rook = pygame.image.load("rook.png").convert()
rook.set_colorkey([0, 0, 0])

avatar1 = pygame.image.load("avatar2.png")
avatar1.set_colorkey([0, 0, 0])

goblin = pygame.image.load("goblin.png")
goblin.set_colorkey([0, 0, 0])

guerrero = pygame.image.load("guerrero.png")
guerrero.set_colorkey([0, 0, 0])

hachero = pygame.image.load("hachero.png")
hachero.set_colorkey([0, 0, 0])

########################## CLASES ############################

class Avatar:
    
    # Attack: tipo de ataque
    # life : vida
    # row : fila en la que aparecerá
    # avatar: tipo de avatar con la imagen
    # x: posicion de x
    # range_attack: rango de ataque(distancia a la que puede atacar)
    
    def __init__(self,attack,life,row,x,range_attack,avatar):

        """ genera los avatars"""
        
        self.Attack = attack
        self.Life = life
        self.Row = row
        self.Avatar = avatar
        self.posx = x
        self.Range = range_attack
        
    def Archer(self):

        """ muestra, ataque y mueve los arqueros """

        if MoveArquero:

            self.posx -= 65

        screen.blit(avatar1,[self.posx, self.Row])

    def Goblin(self):

        """ muestra, ataca y mueve los golblins"""

        if MoveGoblin:

            self.posx-= 65

        screen.blit(goblin,[self.posx, self.Row])

    def Warrior(self):

        """ muestra, ataca y mueve los guerrero"""

        if MoveGuerrero:

            self.posx-= 65

        screen.blit(guerrero,[self.posx, self.Row])

    def Hachero(self):

        """ muestra, ataca y mueve los hacheros """

        if MoveHachero:

            self.posx-= 65

        screen.blit(hachero,[self.posx, self.Row])
            

######################### HILOS ################################

time_second = Thread(target = Time, args= (Game,))
time_second.start()

######################### LÓGICA DEL JUEGO #####################

while Game:
    MiTexto = fuente.render(str(pygame.mouse.get_pos()),True,(0,0,0),(50,50,50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
            
    if Game:
        Display_game()
    
    pygame.display.flip()

pygame.quit()
































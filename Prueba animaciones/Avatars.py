########################### BIBLIOTCAS ########################
import pygame,sys
import time
from threading import Thread
import random
########################### DISPLAY ###########################

pygame.init()

screen = pygame.display.set_mode([700, 600])
pygame.display.set_caption("Avatars")
clock = pygame.time.Clock()

fuente = pygame.font.Font('freesansbold.ttf',15)

########################### VARIABLES #########################

global Game
Game = True

""" VARIABLES DE LAS ACCIONES DE LOS AVATAR"""

Arquero = False
MoveArquero = False
Goblin = False
MoveGoblin = False
Guerrero = False
MoveGuerrero = False
Hachero = False
MoveHachero = False
AtaqueArquero = False

""" LISTAS DE LOS AVATARS """

Arqueros = []
Goblins = []
Guerreros = []
Hacheros = []

moveFlecha = 0

""" MATRICES DEL JUEGO """

matriz = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

""" FILA DE LA MATRIZ """

posFila = [42,125,220,307,390]

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
    global MoveHachero,lista
    global AtaqueArquero
    
    second = 0
        
    while Game:
            
        # DA EL PASO A CREAR EL ARQUERO 
        if second%10 == 0 and second != 0 or second == 2:

            Arquero = True
            AtaqueArquero = True

        """# DA EL PASO A CREAR EL HACHERO
        if second%12 == 0 and second != 0 or second == 7:

            Hachero = True

        # DA EL PASO A CREAR UN GOBLIN
        if second%15 == 0 and second != 0 or second == 5:

            Goblin = True

        # DA EL PASO A CREAR EL GUERRERO
        if second%17 == 0 and second != 0 or second == 9:

            Guerrero = True"""

        if second > 4:

            # DA EL PASO A MOVER EL ARQUERO 
            if second%5 == 0 and second != 0:

                MoveArquero = True

            """# DA EL PASO A MOVER EL HACHERO
            if second%13 == 0 and second != 0:

                MoveHachero = True

            # DA EL PASO A MOVER EL GOBLIN
            if second%14 == 0 and second != 0:

                MoveGoblin = True
                
            # DA EL PASO A MOVER EL GUERRERO 
            if second%10 == 0 and second != 0:

                MoveGuerrero = True"""
   
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
    clock.tick(30)
                
def MoverFlecha(i, fin):

    """ mueve las flechas """

    global AtaqueArquero

    if AtaqueArquero:
        
        if i == fin:
            AtaqueArquero = False
            return
        
        Flechas[i].update()
        return MoverFlecha(i+1, fin)
    

def MoverArqueros(i, fin):

    """ mueve los arqueros de la lista """

    global MoveArquero
    
    if i == fin:
        
        if fin != 0:
            if Arqueros[len(Arqueros)-1].Detener():
                MoveArquero = False
                return
            else:
                return
        else:
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

def EncontrarRook(i,j):

    return True
    
def Generar():

    """ genera un arquero y lo mete en su respectiva lista """
    
    global Arquero, Arqueros, Goblin, Goblins, Guerrero, Guerreros,Hachero,Hacheros

    # pos = coordenada en y de los avatar
    pos = random.choice(posFila)
    
    # CALCULA LA FILA EN LA QUE APERECERÁ EL AVATAR
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

    # CREA UN ARQUERO Y LO METE A SU RESPECTIVA LISTA
    if Arquero:
        if matriz[i][8] != 1:
            matriz[i][8] = 1
            Arqueros += [Avatar(arquero,5,i,8,593,pos,5,593-63,True)]
            Arquero = False
        else:
            return
    # CREA UN GOBLIN Y LO METE A SU RESPECTIVA LISTA
    if Goblin:
        if matriz[i][8] != 1:
            matriz[i][8] = 1
            Goblins += [Avatar(goblin,5,i,8,593,pos,5)]
            Goblin = False
        else:
            return
    # CREA UN GUERRERO Y LO METE A SU RESPECTIVA LISTA
    if Guerrero:
        if matriz[i][8] != 1:
            matriz[i][8] = 1
            Guerreros += [Avatar(guerrero,5,i,8,593,pos,5)]
            Guerrero = False
        else:
            return
    # CREA UN HACHERO Y LO METE A SU RESPECTIVA LISTA
    if Hachero:
        if matriz[i][8] != 1:
            matriz[i][8] = 1
            Hacheros += [Avatar(hachero,5,i,8,593,pos,5)]
            Hachero = False
        else:
            return

###########################IMAGENES###########################  

background = pygame.image.load("fondo1.png").convert()

arquero = pygame.image.load("arquero1.png")
arquero.set_colorkey([0, 0, 0])

arquero2 = pygame.image.load("arquero2.png")
arquero2.set_colorkey([0, 0, 0])

goblin = pygame.image.load("goblin.png")
goblin.set_colorkey([0, 0, 0])

guerrero = pygame.image.load("guerrero.png")
guerrero.set_colorkey([0, 0, 0])

hachero = pygame.image.load("hachero.png")
hachero.set_colorkey([0, 0, 0])

flecha = pygame.image.load("flecha.png")
flecha.set_colorkey([0, 0, 0])

########################## CLASES ############################

class Avatar:
    
    # avatar = imagen del avatar
    # life = cantidad de vida
    # i = fila de la matriz
    # j = columna de la matriz
    # posx = coordenadas en x
    # posy = coordenadas en y
    # final = donde el avatar se termina de mover
    # cambiar = variable que permite la animacion de movimiento
    
    def __init__(self,avatar,life,i,j,x,y,ataque,final,cambiar):

        """ genera los avatars"""
        
        self.avatar = avatar
        self.life = life
        self.i = i
        self.j = j
        self.posx = x
        self.posy = y
        self.ataque = ataque
        self.final = final
        self.cambiar = cambiar
        
    def Archer(self):

        """ muestra, ataque y mueve los arqueros """

        global AtaqueArquero,moveFlecha,MoveArquero


        if MoveArquero:

            if  matriz[self.i][self.j-1] != 0:

                screen.blit(arquero,[self.posx, self.posy])
                
                return


            elif self.posx != self.final:

                if self.cambiar:

                    self.posx -= 3

                    screen.blit(arquero2,[self.posx, self.posy])

                    self.cambiar = False

                    return

                else:

                    self.posx -= 3

                    screen.blit(arquero,[self.posx, self.posy])

                    self.cambiar = True

                    return
                
            elif self.posx == self.final:

                self.final -= 63

            else:
                # ACTUALIZA LA MATRIZ Y MUEVE EL AVATAR
                self.j -= 1
                matriz[self.i][self.j+1] -= 1 
                matriz[self.i][self.j] += 1
                
        if AtaqueArquero:

            if EncontrarRook(self.i,self.j):

                moveFlecha += 3

                screen.blit(flecha,(self.posx-moveFlecha,self.posy))

                if self.posx-moveFlecha < self.posx-130:

                    AtaqueArquero = False
                    moveFlecha = 0

        screen.blit(arquero,[self.posx, self.posy])

    def Goblin(self):

        """ muestra, ataca y mueve los golblins"""

        if MoveGoblin:

            if  matriz[self.i][self.j-1] != 0:
                
                return

            else:
                self.j -= 1
                matriz[self.i][self.j+1] -= 1 
                self.posx-= 65
                matriz[self.i][self.j] += 1

        screen.blit(goblin,[self.posx, self.posy])

    def Warrior(self):

        """ muestra, ataca y mueve los guerrero"""

        if MoveGuerrero:

            if  matriz[self.i][self.j-1] != 0:
                
                return 

            else:
                # ACTUALIZA LA MATRIZ Y MUEVE EL AVATAR
                self.j -= 1
                matriz[self.i][self.j+1] -= 1 
                self.posx-= 65
                matriz[self.i][self.j] += 1

        screen.blit(guerrero,[self.posx, self.posy])

    def Hachero(self):

        """ muestra, ataca y mueve los hacheros """

        if MoveHachero:

            if  matriz[self.i][self.j-1] != 0:
                
                return 

            else:
                # ACTUALIZA LA MATRIZ Y MUEVE EL AVATAR
                self.j -= 1
                matriz[self.i][self.j+1] -= 1 
                self.posx-= 65
                matriz[self.i][self.j] += 1
                
        screen.blit(hachero,[self.posx, self.posy])

    def Detener(self):

        if self.posx == self.final:

            return True

        else:

            return False

######################### HILOS ################################

time_second = Thread(target = Time, args= (Game,))
time_second.start()

######################### LÓGICA DEL JUEGO #####################

while Game:
    
    MiTexto = fuente.render(str(pygame.mouse.get_pos()),True,(255,255,255),(50,50,50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Game = False
            
    if Game:
        Display_game()
    
    pygame.display.flip()

pygame.quit()
































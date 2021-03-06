########################### BIBLIOTCAS ########################
import pygame
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

""" VARIABLES PARA LAS MONEDAS """
if:
    
cash = 0

Moneda = False

monedas = []

valores = [25,50,100]

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
    global AtaqueArquero,Moneda
    
    second = 0
        
    while Game:
            
        # DA EL PASO A CREAR EL ARQUERO 
        if second%10 == 0 and second != 0 or second == 2:

            Arquero = True
            AtaqueArquero = True

        # DA EL PASO A CREAR EL HACHERO
        if second%12 == 0 and second != 0 or second == 7:

            Hachero = True

        # DA EL PASO A CREAR UN GOBLIN
        if second%15 == 0 and second != 0 or second == 5:

            Goblin = True

        # DA EL PASO A CREAR EL GUERRERO
        if second%17 == 0 and second != 0 or second == 9:

            Guerrero = True

        # DA EL PASO A CREAR UNA MONEDA
        if second == 0 or second%10 == 0:

            Moneda = True

        if second > 4:

            # DA EL PASO A MOVER EL ARQUERO 
            if second%5 == 0 and second != 0:

                MoveArquero = True

            # DA EL PASO A MOVER EL HACHERO
            if second%13 == 0 and second != 0:

                MoveHachero = True

            # DA EL PASO A MOVER EL GOBLIN
            if second%14 == 0 and second != 0:

                MoveGoblin = True
                
            # DA EL PASO A MOVER EL GUERRERO 
            if second%10 == 0 and second != 0:

                MoveGuerrero = True
   
        second += 1
        time.sleep(1)

def Display_game():

    """ Muestra la pantalla del juego """
    
    Draw_cash = fuente.render(str(cash),True,(255,255,255),(0,0,0))
    screen.blit(background,[0,0])
    screen.blit(MiTexto,(600,550))
    screen.blit(moneda,(10,525))
    screen.blit(Draw_cash,(70,540))
    Generar()
    MoverArqueros(0, len(Arqueros))
    MoverGoblins(0,len(Goblins))
    MoverGuerreros(0,len(Guerreros))
    MoveHacheros(0,len(Hacheros))
    MostrarMonedas(0,len(monedas))
    clock.tick(60)
                
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

def MostrarMonedas(i,fin):

    """ muestra las monedas de la lista """

    if i == fin:

        return

    monedas[i].Update2()
    return MostrarMonedas(i+1,fin)

def DetectarClick(coordenadas,i,final):

    if i == final:
        i = 0
        return
    else:
        if monedas[i].Click(coordenadas[0],coordenadas[1],monedas[i]):
            del monedas[i]
            i = 0
            return
        else:
            return DetectarClick(coordenadas,i+1,final)

def EncontrarRook(i,j):

    return True
    
def Generar():

    """ genera un arquero y lo mete en su respectiva lista """
    
    global Arquero, Arqueros, Goblin, Goblins, Guerrero, Guerreros,Hachero,Hacheros, Moneda, monedas

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
            Arqueros += [Avatar(arquero,5,i,8,593,pos,5)]
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
    # CREA LA MONEDA Y LA METE EB SU RESPECTETIVA LISTA
    if Moneda:
        monedas += [Coins(random.randint(0,600),random.randint(0,500),random.choice(valores))]
        Moneda = False 

###########################IMAGENES###########################  

background = pygame.image.load("fondo1.png").convert()

arquero = pygame.image.load("avatar2.png")
arquero.set_colorkey([0, 0, 0])

goblin = pygame.image.load("goblin.png")
goblin.set_colorkey([0, 0, 0])

guerrero = pygame.image.load("guerrero.png")
guerrero.set_colorkey([0, 0, 0])

hachero = pygame.image.load("hachero.png")
hachero.set_colorkey([0, 0, 0])

flecha = pygame.image.load("flecha.png")
flecha.set_colorkey([0, 0, 0])

moneda = pygame.image.load("moneda.png")
moneda.set_colorkey([0, 0, 0])

########################## CLASES ############################

class Avatar:
    
    # avatar = imagen del avatar
    # life = cantidad de vida
    # i = fila de la matriz
    # j = columna de la matriz
    # posx = coordenadas en x
    # posy = coordenadas en y
    
    def __init__(self,avatar,life,i,j,x,y,ataque):

        """ genera los avatars"""
        
        self.avatar = avatar
        self.life = life
        self.i = i
        self.j = j
        self.posx = x
        self.posy = y
        self.ataque = ataque
        
    def Archer(self):

        """ muestra, ataque y mueve los arqueros """

        global AtaqueArquero,moveFlecha

        if MoveArquero:

            if  matriz[self.i][self.j-1] != 0:
                
                return 

            else:
                # ACTUALIZA LA MATRIZ Y MUEVE EL AVATAR
                self.j -= 1
                matriz[self.i][self.j+1] -= 1 
                self.posx-= 65
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

class Coins:

    # x = posicion en x
    # y = posicion en y
    # valor = valor random de la moneda

    def __init__(self,x,y,valor):
        
        self.posx = x
        self.posy = y
        self.valor = valor
        
    def Update2(self):

        """ muestra en pantalla las monedas"""
        
        screen.blit(moneda,(self.posx,self.posy))

    def Click(self,posx,posy,elemento):

        """ verifica si le dio click a las monedas """

        global cash

        # COMPARA LAS COORDENADAS DEL CLICK CON LAS DE LA MONEDA

        if posx >= self.posx and posx <= self.posx + 50:

            if posy >= self.posy and posy <= self.posy + 50:

                cash += self.valor

                return True
            else:
                return False
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                DetectarClick(pygame.mouse.get_pos(),0,len(monedas))
            
    if Game:
        Display_game()
    
    pygame.display.flip()

pygame.quit()































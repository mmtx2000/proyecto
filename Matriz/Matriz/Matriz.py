import pygame,sys
#############################################################
#ESTAS 3 FUNCIONES FUNCIONAN PARA SABER EN QUE DEL TABLERO GRAFICO
#SE HIZO CLICK Y TRADUCIRLO AL TABLERO LOGICO, CABE DECIR QUE
#ESTA SOLO RETORNA LA POSICION CORRESPONDIENTE EN LA MATRIZ COMO
#UNA TUPLA Y SOLO FUNCIONA PARA LAS PRIMERAS 3 LINEAS YA QUE ES DONDE
#SE PONDRÁN LAS DEFENSAS

pygame.init()

screen = pygame.display.set_mode([700, 600])
pygame.display.set_caption("Matriz")

Matriz = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

background = pygame.image.load("fondo1.png").convert()

fuente = pygame.font.Font('freesansbold.ttf',15)

Game = True

def vefX(x):
    # DETECTA EL SI EL CLICK ESTA DENTRO DEL TABLERO
    if x < 92 or x >=660:
        return 10
    # DETECTA LA POSICION J DE LA MATRIZ
    elif 92<=x<154:
        posxMatriz= 0
    elif 154<=x<214:
        posxMatriz= 1
    elif 214<=x<278:
        posxMatriz= 2
    elif 278<=x<344:
        posxMatriz= 3
    elif 344<=x<408:
        posxMatriz= 4
    elif 408<=x<472:
        posxMatriz= 5
    elif 472<=x<538:
        posxMatriz= 6
    elif 538<=x<598:
        posxMatriz= 7
    elif 598<=x<660:
        posxMatriz= 8
    return posxMatriz

def vefY(y):
    # DETECTA SI EL CLICK ESTA DENTRO DEL TABLERO
    if y < 30 or y >=465:
        return 10
    # DETECTA LA POSICION I DE LA MATRIZ
    elif 30<=y<114:
        posyMatriz= 0
    elif 114<=y<202:
        posyMatriz= 1
    elif 202<=y<300:
        posyMatriz= 2
    elif 300<=y<384:
        posyMatriz= 3
    elif 384<=y<465:
        posyMatriz= 4
    return posyMatriz

def getPositionInMatriz(tupla,click):
    
    x= tupla[0]
    y= tupla[1]
    posjMatriz= vefX(x)
    posiMatriz= vefY(y)

    if posjMatriz == 10 or posiMatriz == 10:
        return
    elif click:
        Matriz[posiMatriz][posjMatriz] = 1
        print(Matriz)
    else:
        Matriz[posiMatriz][posjMatriz] = 0
        print(Matriz)
    


#Esto se usa de la siguiente forma
#posicion= getPositionInMatriz(Y aca recibe la posicion del mouse DEBE SER UNA TUPLA)
#en posicion quedara en que parte de la matriz original hay que poner un uno
#posicion será igual a (y, x)
##########################################################

#######################################################
#OCUPO QUE POR FAVOR LOGRES QUE MIENTRAS CORRE EL JUEGO
#CUANDO PRESIONES CLICK DERECHO IMPRIMA EN COSSOLA, COMO EL EJEMPLO
#DE ABAJO YA QUE CUANDO INTENTO INTEGRAR AL CODIGO ESTE DA MUCHOS ERRORES
#YA QUE NO ENTIENDO DONDE SE ESTAN DANDO LOS CICLOS, SI LOGRAS ESO
#TODO LO DEMÁS SALDRÍA RELATIVAMENTE RAPIDO, GRACIAS
def Game(Game):
    
    while Game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    getPositionInMatriz(pygame.mouse.get_pos(),True)
                elif event.button == 3:
                    getPositionInMatriz(pygame.mouse.get_pos(),False)
                    
        screen.blit(background,[0,0])
        MiTexto = fuente.render(str(pygame.mouse.get_pos()),True,(255,255,255),(50,50,50))
        screen.blit(MiTexto,(600,550))
        pygame.display.flip()
        
Game(Game)
    #defenses= threading.Thread(target=addDefenses)
    #defenses.start()
############################################

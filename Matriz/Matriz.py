#############################################################
#ESTAS 3 FUNCIONES FUNCIONAN PARA SABER EN QUE DEL TABLERO GRAFICO
#SE HIZO CLICK Y TRADUCIRLO AL TABLERO LOGICO, CABE DECIR QUE
#ESTA SOLO RETORNA LA POSICION CORRESPONDIENTE EN LA MATRIZ COMO
#UNA TUPLA Y SOLO FUNCIONA PARA LAS PRIMERAS 3 LINEAS YA QUE ES DONDE
#SE PONDRÁN LAS DEFENSAS
def vefX(x):
    posxMatriz=7
    if 97<x<149:
        posxMatriz= 0
    elif 158<x<210:
        posxMatriz= 1
    elif 221<x<261:
        posxMatriz= 2
    return posxMatriz

def vefY(y):
    posyMatriz=7
    if 32<y<115:
        posyMatriz= 0
    elif 119<y<201:
        posyMatriz= 1
    elif 206<y<294:
        posyMatriz= 2
    elif 302<y<376:
        posyMatriz= 3
    elif 386<y<455:
        posyMatriz= 4
    return posyMatriz

def getPositionInMatriz(tupla):
    x= tupla[0]
    y= tupla[1]
    posxMatriz= vefX(x)
    posyMatriz= vefY(y)
    positions= (posyMatriz, posxMatriz)
    return positions


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
def addDefenses():
    global Game
    while Game:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            Game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Hola")
    defenses= threading.Thread(target=addDefenses)
    defenses.start()
############################################

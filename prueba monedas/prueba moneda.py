import pygame,random,time
from threading import Thread

pygame.init()

screen = pygame.display.set_mode([700, 600])
pygame.display.set_caption("MONEDAS")
clock = pygame.time.Clock()
fuente = pygame.font.Font('freesansbold.ttf',15)

moneda = pygame.image.load("moneda.png")
moneda.set_colorkey([0, 0, 0])

valores = [25,50,100]

cash = 0

Moneda = False

monedas = []

def Time():

    global second,Moneda

    second = 0

    while True:

        if second%3 == 0:

            Moneda = True

        second += 1

        time.sleep(1)

def GenerarMonedas():

    global Moneda,monedas

    if Moneda:
        
        monedas += [Coins(random.randint(0,600),random.randint(0,500),random.choice(valores))]
        Moneda = False

def MostrarMonedas(i,fin):

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
            
    return DetectarClick(coordenadas,i+1,final)
        
time_second = Thread(target = Time, args= ())
time_second.start()

class Coins:

    def __init__(self,x,y,valor):
        
        self.posx = x
        self.posy = y
        self.valor = valor
        
    def Update2(self):
        
        screen.blit(moneda,(self.posx,self.posy))

    def Click(self,posx,posy,elemento):

        global cash

        if posx >= self.posx and posx <= self.posx + 50:

            if posy >= self.posy and posy <= self.posy + 50:

                cash += self.valor

                return True
            else:
                return False
        else:
            return False            

while True:

    screen.fill([0, 0, 0])

    MiTexto = fuente.render(str(cash),True,(255,255,255),(0,0,0))
    screen.blit(MiTexto,(100,550))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                DetectarClick(pygame.mouse.get_pos(),0,len(monedas))
                
    GenerarMonedas()
    MostrarMonedas(0,len(monedas))

    pygame.display.flip()
     
    clock.tick(60)
    

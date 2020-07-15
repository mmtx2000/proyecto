import pygame, sys
import random
from pygame.locals import *
import time
#variables
FONDO = (0,0,0)
BLANCO = (255, 255, 255)
negro=(0,0,0)
rojo=(0,255,0)
azul=(0,0,255)
COLOR_TEXTO = (50, 60, 80)
size= (700,500)
pygame.init()
pantalla = pygame.display.set_mode(size)
pygame.display.set_caption("INICIO")
imagen_panel = pygame.image.load("fondo.png")
imagen_boton = pygame.image.load("bon.png")
imagen_boton_pressed = pygame.image.load("bon.png")
imagen_boton_cuadro = pygame.image.load("bon.png")
imagen_boton_cuadro_pressed = pygame.image.load("bon.png")
imagen_text = pygame.image.load("bon.png")
fuente = pygame.font.SysFont('Courier', 20)
fuente_numero = pygame.font.SysFont('Pacifico Regular', 30)
#dibuja textos
def dibujar_texto(texto, contenedor_imagen, contenedor_rec, fuente_render, color):
    text = fuente_render.render(texto, 1, color)
    centro = text.get_rect()
    diferencia_x = contenedor_imagen.center[0] - centro.center[0]
    diferencia_y = contenedor_imagen.center[1] - centro.center[1]
    pantalla.blit(text, [contenedor_rec.left + diferencia_x, contenedor_rec.top + diferencia_y])
#dibuja botones
def dibujar_botones_iniciales(lista_botones):
    panel = pygame.transform.scale(imagen_panel, [700, 500])
    pantalla.blit(panel, [0, 0])#posicion desde la que se despliega el fondo
    for boton in lista_botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])
        dibujar_texto(boton['texto'], boton['imagen'].get_rect(), boton['rect'], fuente, BLANCO)

def set_text(campo, texto):
    dibujar_texto(texto, campo['imagen'].get_rect(), campo['rect'], fuente_numero, COLOR_TEXTO)

#ventana principal
def main():
    #game_over = False
    clock = pygame.time.Clock()
    boton_cuadro = pygame.transform.scale(imagen_boton_cuadro, [120, 90])#diensiones botones
    boton_cuadro_pressed = pygame.transform.scale(imagen_boton_cuadro_pressed, [90, 90])
    r_boton_2_1 = boton_cuadro.get_rect()
    r_boton_2_2 = boton_cuadro.get_rect()
    r_boton_2_3 = boton_cuadro.get_rect()
    r_boton_2_4 = boton_cuadro.get_rect()
    botones = []
    r_boton_2_1.topleft = [450, 300]#pos1
    botones.append({'texto': "Ayuda", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_1, 'on_click': False})
    r_boton_2_2.topleft = [450, 400]#os2
    botones.append({'texto': "Jugadores", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_2, 'on_click': False})
    r_boton_2_3.topleft = [580, 300]#pos3
    botones.append({'texto': "Créditos", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_3, 'on_click': False})
    r_boton_2_4.topleft = [580, 400]#pos4
    botones.append({'texto': "Registro", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_4, 'on_click': False})
        
        
    #dibujar_botones_iniciales(botones)

    LEFT = 1
    RIGHT = 3

    running = 1

    

    
    #ventana ayuda
    def Help ():
        pygame.init()
        ayuda= pygame.display.set_mode ([700,500])
        pygame.display.set_caption ("AYUDA")
        bg= pygame.image.load("fayu.png")
        text=pygame.font.SysFont ("",30)
        text_help= text.render ("Bienvenido a la sección de ayuda, aquí",True, negro)
        text2=pygame.font.SysFont ("",30)
        text_help2= text2.render ("podras descubrir como funciona el juego.",True, negro)
        text3=pygame.font.SysFont ("",30)
        text_help3= text3.render ("Al iniciar tendras que ingresar tu nombre y",True, negro)
        text4=pygame.font.SysFont ("",30)
        text_help4= text4.render ("la frecuencia con la que quieres jugar.",True, negro)
        text5=pygame.font.SysFont ("",30)
        text_help5= text5.render ("Seguidamente presionarás en jugar.",True, negro)
        text6=pygame.font.SysFont ("",30)
        text_help6= text6.render ("En el juego contarás con cuatro ROOKS",True, negro)
        text7=pygame.font.SysFont ("",30)
        text_help7= text7.render ("que debes comprar y posicionar con click",True, negro)
        text8=pygame.font.SysFont ("",30)
        text_help8= text8.render ("izquierdo y borrar con el derecho, Debes",True, negro)
        text9=pygame.font.SysFont ("",30)
        text_help9= text9.render ("recoger las monedas que se muestran. Al ",True, negro)
        text10=pygame.font.SysFont ("",30)
        text_help10= text10.render ("disparar tu rook el avatar se incendiará.",True, negro)
        text11=pygame.font.SysFont ("",30)
        text_help11= text11.render ("Al ganar pasarás de nivel. Si ganas se te",True, negro)
        text12=pygame.font.SysFont ("",30)
        text_help12= text12.render ("reconocerá en la ventana de jugadores.",True, negro)
        text13=pygame.font.SysFont ("",30)
        text_help13= text13.render ("SUERTE!!.",True, negro)
        salir= False
        while salir != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir= True
            ayuda.blit(bg, [0,0])
            ayuda.blit(text_help, (145,120))
            ayuda.blit(text_help2, (145,135))
            ayuda.blit(text_help3, (145,170))
            ayuda.blit(text_help4, (145,185))
            ayuda.blit(text_help5, (145,220))
            ayuda.blit(text_help6, (145,239))
            ayuda.blit(text_help7, (145,255))
            ayuda.blit(text_help8, (145,273))
            ayuda.blit(text_help9, (145,290))
            ayuda.blit(text_help10, (145,310))
            ayuda.blit(text_help11, (145,340))
            ayuda.blit(text_help12, (145,360))
            ayuda.blit(text_help13, (145,400))
            pygame.display.update ()
        pygame.quit()
    

    #ventana creditos
    def Credits ():
        pygame.init()
        creditos= pygame.display.set_mode ([700,500])
        pygame.display.set_caption ("CREDITOS")
        bgc= pygame.image.load("fcre.png")
        David= pygame.image.load("david.png")
        Montse= pygame.image.load("montse.png")
        text1=pygame.font.SysFont ("",30)
        text_cre= text1.render ("Instituto Tecnológico de Costa Rica",True, negro)
        text_cre2= text1.render ("País de realización: Costa Rica.",True, negro)
        text_cre3= text1.render ("Curso: Taller de Programación.",True, negro)
        text_cre4= text1.render ("Profesor: Jason Leitón Jimenez.",True, negro)
        text_cre5= text1.render ("Creadores del programa:",True, negro)
        text_cre6= text1.render ("Luis David Richmond Soto.",True, negro)
        text_cre7= text1.render ("Carné: 2020077226.",True, negro)
        text_cre8= text1.render ("Montserrat Monge Téllez.",True, negro)
        text_cre9= text1.render ("Carné: 2019390571.",True, negro)
        text_cre10= text1.render ("Versión del programa:______",True, negro)
        text_cre11= text1.render ("I Semestre 2020.",True, negro)

        salir= False
        while salir != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir= True
            creditos.blit(bgc, [0,0])
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
    

    #ventana jugadores
    def Players ():
        pygame.init()
        jugadores= pygame.display.set_mode ([700,500])
        pygame.display.set_caption ("JUGADORES")
        bgp= pygame.image.load("fju.png")    
        salir= False
        while salir != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir= True
            jugadores.blit(bgp, [0,0])
            pygame.display.update ()
        pygame.quit()


    #ventana registros
    def Login ():
        pygame.init()
        registros= pygame.display.set_mode ([700,500])
        pygame.display.set_caption ("REGISTROS")
        bgL= pygame.image.load("fre.png")
        salir= False
        while salir != True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    salir= True
            registros.blit(bgL, [0,0])
            pygame.display.update ()
        pygame.quit()
    

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
                
            else:
                 print ("click izquierdo (%d, %d)" % event.pos)

        pantalla.fill(FONDO)
        dibujar_botones_iniciales(botones)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == '__main__':
    main()

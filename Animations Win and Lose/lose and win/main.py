import pygame
import AnimationWin
import AnimationLose
import time

pygame.init()

# Definimos algunas variables que usaremos en nuestro código

ancho_ventana = 800
alto_ventana = 500
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Tutorial sprites Piensa 3D")
clock = pygame.time.Clock()
loseAnimation = AnimationLose.AnimationLose((0, 0))
winAnimation= AnimationWin.AnimationWin((0, 0))
loseAnimation= AnimationLose.AnimationLose ((0,0))
def makeAnimation(animation):
    for i in range(0,5):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True         
        screen.fill(pygame.Color('black'))
        screen.blit(animation.image, animation.rect)#dentro de la pantalla se coloque la imagen
        animation.update()
        pygame.display.flip()#reflejo de pantalla
        clock.tick(3)

makeAnimation(winAnimation)
makeAnimation(loseAnimation)
pygame.quit ()

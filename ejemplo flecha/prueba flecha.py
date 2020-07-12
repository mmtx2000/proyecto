import pygame

pygame.init()

screen = pygame.display.set_mode([700, 600])
pygame.display.set_caption("Avatars")
clock = pygame.time.Clock()

flecha = pygame.image.load("flecha.png")
flecha.set_colorkey([0, 0, 0])

d_madera = pygame.image.load("d_madera.png")
d_madera.set_colorkey([0, 0, 0])

d_diamante = pygame.image.load("d_diamante.png")
d_diamante.set_colorkey([0, 0, 0])

d_oro = pygame.image.load("d_oro.png")
d_oro.set_colorkey([0, 0, 0])

d_piedra = pygame.image.load("d_piedra.png")
d_piedra.set_colorkey([0, 0, 0])

x=700
y=130

x_d = 0

def move():

    global x,x_d

    x_d += 5

    x -= 5

    if x == 0:

        x = 700

    if x_d == 700:

        x_d = 0

    screen.blit(flecha,(x,y))
    screen.blit(d_madera,(x_d,50))
    screen.blit(d_piedra,(x_d,100))
    screen.blit(d_oro,(x_d,150))
    screen.blit(d_diamante,(x_d,250))
    

while True:

    screen.fill([255, 255, 255])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Game = False

    move()
     
    clock.tick(60)
    pygame.display.flip()

import pygame,sys

pygame.init()

screen = pygame.display.set_mode([318, 159])
pygame.display.set_caption("Avatars")
clock = pygame.time.Clock()

menu = pygame.image.load("menu.png")
menu.set_colorkey([0, 0, 0])

fuente = pygame.font.Font('freesansbold.ttf',15)

entry_text = ""

input_rect = pygame.Rect(0, 0, 100, 50)
color = pygame.Color("lightskyblue3")
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                entry_text = entry_text[:-1]
            else:
                entry_text += event.unicode

    screen.blit(menu,(0,0))

    pygame.draw.rect(screen,color,input_rect,2)

    text_surface = fuente.render(entry_text,True,(0,0,0))

    screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))
     
    clock.tick(60)
    pygame.display.flip()

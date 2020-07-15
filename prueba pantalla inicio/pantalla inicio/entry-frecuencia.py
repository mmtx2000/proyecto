import pygame
import sys
from pygame import*
pygame.init()
clock= pygame.time.Clock()
screen= pygame.display.set_mode ([700,500])
Font= pygame.font.Font(None, 32)
user_text=''
user_frec= ''

input_rect= pygame.Rect (180,0,140,32)
input_rect2= pygame.Rect (235,35,140,32)
color_a= pygame.Color ("lightskyblue3")
color_p= pygame.Color ("gray15")
color = color_p

active= False
text=pygame.font.SysFont ("",30)
text_entry= text.render ("Nombre Jugador:",True,(255,255,255))
text_frec= text.render ("Numero de frecuencia:",True,(255,255,255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            if input_rect.collidepoint (event.pos) and input_rect2.collidepoint (event.pos):
                active = True
            else:
                active = False

        if event.type == pygame. KEYDOWN:
            if active == True:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text [:-1]
                    user_frec = user_frec [:-1]
                else:
                    user_text+= event.unicode
                    user_frec += event.unicode

    screen.fill ((0,0,0))

    if active:
        color= color_a
    else:
        color= color_p

    pygame.draw.rect (screen, color, input_rect,2)
    pygame.draw.rect (screen, color, input_rect2,2)    
    text_surface= Font.render (user_text, True, (255,255,255))
    text_surface2= Font.render (user_frec, True, (255,255,255))
    
    screen.blit (text_surface, (input_rect.x +1, input_rect.y +1))
    screen.blit (text_surface2, (input_rect2.x +1, input_rect2.y +1))
    input_rect.w= max(100, text_surface.get_width())+1
    input_rect2.w= max(100, text_surface2.get_width())+1    
    screen.blit(text_entry, (0,0))
    screen.blit(text_frec, (0,40))
    
    pygame.display.flip ()
    clock.tick(60)
    

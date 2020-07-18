import pygame

class AnimationLose(pygame.sprite.Sprite):#personaje
    def __init__(self, position):
        self.sheet = pygame.image.load('lose.png')
        self.sheet.set_clip(pygame.Rect(0,0,800,503))#definir cual iagen se tiene como inicio
        self.image = self.sheet.subsurface(self.sheet.get_clip())#define el rectangulo
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.frame_states = { 0: (0, 0, 800, 503), 1: (819, 0, 800, 503), 2: (1638, 0, 800, 503), 3: (2457, 0, 800, 503), 4: (3276, 0, 800, 503) }

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def update(self):
        self.clip(self.frame_states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())

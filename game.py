import pygame, os, sys, random

class GAME:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.widht, self.height = 500, 700
        self.screen = pygame.display.set_mode((self.widht, self.height))
        pygame.display.set_caption("Flappy")
        self.clock = pygame.time.Clock()
        self.FPS = 60
        
                
import pygame, os, sys, random

class Birds:
    def bird(self):
        self.x = 80
        self.y = self.heiht // 2
        self.jump = -8

class Games:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.widht, self.height = 500, 700
        self.screen = pygame.display.set_mode((self.widht, self.height))
        pygame.display.set_caption("Flappy")
        self.clock = pygame.time.Clock()
        self.FPS = 60

    def run(self):
        running = True
        while running:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird_velocity = jump
        pygame.quit()
        sys.exit()





if __name__ == '__main__':
    Games().run()
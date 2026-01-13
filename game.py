import pygame, os, sys, random

WIDHT, HEIGHT = 500, 700
white = (255,255,255)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,255)

#คลาสสำหรับนก
class Birds:
    def __init__(self):
        self.x = 80
        self.y = HEIGHT // 2
        self.jump_strength = -8
        self.radius = 15
        self.velocity = 0
        self.gravity = 0.5

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
    def jump(self):
        self.velocity = self.jump_strength
    def draw(self, screen):
        pygame.draw.circle(screen,red,(self.x,int(self.y)),self.radius)
    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius*  2)

#คลาสสำหรับท่อ
class Pipes:
    def __init__(self,x):
        self.x = x
        self.widht = 60
        self.gap = 160
        self.height = random.randint(100,400)
        self.top_rect = pygame.Rect(self.x, 0, self.widht, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + self.gap, self.widht, HEIGHT)
        self,passed = False
    def update(self,speed):
        self.x -= speed
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x
    def draw(self,screen):
        pygame.draw.rect(screen, green, self.top_rect)
        pygame.draw.rect(screen, green, self.bottom_rect)
#main class 
class Games:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

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
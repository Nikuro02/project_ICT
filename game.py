import pygame, random, sys

WIDTH = 400
HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird OOP")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 32)

# -----------------------------
# คลาส Bird
# -----------------------------
class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.radius = 15
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -8

    def jump(self):
        self.velocity = self.jump_strength

    def move(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, int(self.y)), self.radius)

    def get_rect(self):
        return pygame.Rect(self.x - self.radius,
                           self.y - self.radius,
                           self.radius * 2,
                           self.radius * 2)

# -----------------------------
# คลาส Pipe
# -----------------------------
class Pipe:
    GAP = 150
    SPEED = 3

    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(100, 400)
        self.top = self.height
        self.bottom = self.height + self.GAP
        self.width = 60
        self.passed = False

    def move(self):
        self.x -= self.SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, self.width, self.top))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.bottom, self.width, HEIGHT))

    def collide(self, bird):
        bird_rect = bird.get_rect()

        top_rect = pygame.Rect(self.x, 0, self.width, self.top)
        bottom_rect = pygame.Rect(self.x, self.bottom, self.width, HEIGHT)

        return bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect)

# -----------------------------
# คลาส Base (พื้นเลื่อน)
# -----------------------------
class Base:
    SPEED = 3

    def __init__(self):
        self.y = HEIGHT - 50
        self.x1 = 0
        self.x2 = WIDTH

    def move(self):
        self.x1 -= self.SPEED
        self.x2 -= self.SPEED

        if self.x1 + WIDTH < 0:
            self.x1 = self.x2 + WIDTH

        if self.x2 + WIDTH < 0:
            self.x2 = self.x1 + WIDTH

    def draw(self, screen):
        pygame.draw.rect(screen, (139, 69, 19), (self.x1, self.y, WIDTH, 50))
        pygame.draw.rect(screen, (139, 69, 19), (self.x2, self.y, WIDTH, 50))

# -----------------------------
# คลาส Game
# -----------------------------
class Game:
    def __init__(self):
        self.bird = Bird()
        self.pipes = [Pipe()]
        self.base = Base()
        self.score = 0
        self.running = True

    def run(self):
        while self.running:
            clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.jump()

    def update(self):
        self.bird.move()
        self.base.move()

        add_pipe = False
        remove_pipe = []

        for pipe in self.pipes:
            pipe.move()

            if pipe.collide(self.bird):
                self.running = False

            if pipe.x + pipe.width < 0:
                remove_pipe.append(pipe)

            if not pipe.passed and pipe.x < self.bird.x:
                pipe.passed = True
                add_pipe = True

        if add_pipe:
            self.score += 1
            self.pipes.append(Pipe())

        for pipe in remove_pipe:
            self.pipes.remove(pipe)

        # เช็คตกพื้นหรือออกจอ
        if self.bird.y > HEIGHT - 50 or self.bird.y < 0:
            self.running = False

    def draw(self):
        screen.fill((135, 206, 235))

        for pipe in self.pipes:
            pipe.draw(screen)

        self.base.draw(screen)
        self.bird.draw(screen)

        score_text = font.render(str(self.score), True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - 10, 20))

        pygame.display.update()


# -----------------------------
# เริ่มเกม
# -----------------------------
if __name__ == "__main__":
    game = Game()
    game.run()
import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

background = pygame.image.load("assets/background.png").convert()
screen.blit(background,(1200,800))
scroll = 0

tiles = math.ceil(1200 / background.get_width()) + 1

class FlappyBird:
    def __init__(self):
        self.bird_image = pygame.image.load("assets/bird.png").convert_alpha()
        self.bird_image = pygame.transform.scale(self.bird_image, (75,75))
        self.bird_rect = self.bird_image.get_rect()
        self.bird_rect.x = 200
        self.bird_rect.y = 300
        self.fall = 0.5
        self.fly = 6
        self.move = 0

    def update(self):
        self.move += self.fall
        self.bird_rect.y += self.move

    def jump(self):
        self.move = -self.fly

    def draw(self):
        screen.blit(self.bird_image, self.bird_rect)

bird = FlappyBird()

class Pipe:
    def __init__(self, x):
        self.pipe_image = pygame.image.load("assets/pipe.png").convert_alpha()
        self.pipe_image = pygame.transform.scale(self.pipe_image, (100, 500))
        self.pipe_rect_top = self.pipe_image.get_rect()
        self.pipe_rect_bottom = self.pipe_image.get_rect()
        self.pipe_rect_top.bottom = random.randint(200, 400)
        self.pipe_rect_bottom.top = self.pipe_rect_top.bottom + 200
        self.pipe_rect_top.x = x
        self.pipe_rect_bottom.x = x
        self.speed = 4

    def update(self):
        self.pipe_rect_top.x -= self.speed
        self.pipe_rect_bottom.x -= self.speed

    def draw(self):
        screen.blit(self.pipe_image, self.pipe_rect_top)
        screen.blit(self.pipe_image, self.pipe_rect_bottom)

pipes = []

class Ground:
    def __init__(self):
        self.ground_image = pygame.image.load("assets/ground.png").convert_alpha()
        self.ground_image = pygame.transform.scale(self.ground_image, (1200, 300))
        self.ground_rect = self.ground_image.get_rect()
        self.ground_rect.y = 500

    def update(self):
        self.ground_rect.x -= 3

    def draw(self):
        screen.blit(self.ground_image, self.ground_rect)

ground = Ground()
game_over = False

while True:
    clock.tick(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    if game_over == False:
        for i in range(tiles):
            screen.blit(background, (background.get_width() * i + scroll, 0))
    scroll -= 3

    if abs(scroll) > background.get_width():
        scroll = 0

    bird.update()
    bird.draw()

    if len(pipes) < 5:
        if len(pipes) == 0:
            pipes.append(Pipe(1200))
        elif pipes[-1].pipe_rect_top.x < 600:
            pipes.append(Pipe(1200))
            
    for pipe in pipes:
        pipe.update()
        pipe.draw()

        if bird.bird_rect.colliderect(pipe.pipe_rect_top): 
            game_over = True
        if bird.bird_rect.colliderect(pipe.pipe_rect_bottom): 
            game_over = True
        if bird.bird_rect.colliderect(ground.ground_rect): 
            game_over = True

    ground.update()
    ground.draw()

    if game_over:
        text = pygame.render("Your lost", True, "black")
        screen.fill("white")
        screen.blit(text, (100, 100))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.QUIT()
        exit()

    pygame.display.update()
import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
class Particle:
    def __init__(self) -> None:
        self.x = random.randint(-16,16)
        self.y = random.randint(-16,16)
        self.size = random.randint(2,5)
        self.frame = random.randint(0,124)
        self.color = (random.randint(0,25),random.randint(0,255),random.randint(0,25))
    def draw(self,player_pos,screen):
        if self.frame > 124:
            self.frame = 0
            self.x = random.randint(-50,50)
            self.y = random.randint(-30,30)
            self.size = random.randint(2,5)
        else:
            self.frame = self.frame+1
            self.y = self.y+-1
        pygame.draw.rect(screen,self.color,(player_pos.x+self.x,player_pos.y+self.y,self.size,self.size))
particles = [Particle() for _ in range(100)]
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((0,150,255))

    pygame.draw.circle(screen, (150,155,255), player_pos, 40)
    for particle in particles:
        particle.draw(player_pos,screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

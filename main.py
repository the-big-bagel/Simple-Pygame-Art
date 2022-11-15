import pygame
import random

sizeArr = [2000, 1000]
ballArr = []
size = 10000

pygame.init()
screen = pygame.display.set_mode((sizeArr[0], sizeArr[1]))
pygame.display.set_caption("Art")

class Ball:
    def __init__(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speedx = random.randint(-100, 100)/100
        self.speedy = random.randint(-100, 100)/100
        self.x = random.randint(0, sizeArr[0])
        self.y = random.randint(0, sizeArr[1])
        self.modx = random.randint(0, 100)/10000000
        self.mody = random.randint(0, 100)/10000000
    def update(self):
        self.x += self.speedx
        self.y += self.speedy
        self.speedx += self.modx
        self.speedy += self.mody


for i in range(size):
    ballArr.append(Ball())
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.image.save(screen, "image.jpg")
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.image.save(screen, "image.jpg")
                pygame.quit()
                break
    for item in ballArr:
        item.update()
    for item in ballArr:
        pygame.draw.circle(screen, item.color, (item.x, item.y), 1)
    pygame.display.update()
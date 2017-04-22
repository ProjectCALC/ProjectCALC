import pygame
import sys
import random
         
wizard_right = pygame.image.load('images\wizardright.png')
wizard_left = pygame.image.load('images\wizardleft.png')

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('CalcRPG')
done = False
x = 30
y = 30
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
        screen.fill((255,255,255))
        img = pygame.image.load('images\wizardright.png')
        sword_img = pygame.image.load('images\wizardswordleft.png')   
        screen.blit(img, (x, y, 20, 20))

        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_w]:
            y -= 3
        if pressed[pygame.K_s]:
            y += 3
        if pressed[pygame.K_a]:
            x -= 3
            screen.fill([255,255,255])
            screen.blit(wizard_left, (x, y, 20, 20))
        if pressed[pygame.K_d]:
            x += 3
            screen.fill([255,255,255])
            screen.blit(wizard_right, (x, y, 20, 20))


        pygame.display.flip()
        clock.tick(60)

import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('CalcRPG')
    done = False   
    clock = pygame.time.Clock()

    while not done:
     for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 done = True
     screen.fill((255,255,255))
     img = pygame.image.load('images\grass.jpg')
     test = 0
     x = -50
     y = 0
     while test != 46:           
             x = x + 50
             screen.blit(img, (x, y, 20, 20))
             test = test + 1
             while test == 8:
                 y = y + 50
                 x = x - 450
                 screen.blit(img, (x, y, 20, 20))
                 test = test + 1
                 while test == 16:
                     print('hey')
     pygame.display.flip()
     clock.tick(60)
main()


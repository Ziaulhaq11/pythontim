import pygame  #todo import other module

pygame.init()

pygame.display.set_mode((800,600))

running = True

while running:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:   #todo create other events
            running = False
    pygame.display.update()
    pygame.display.update()
    pygame.display.update()
    pygame.display.update()

run = 6













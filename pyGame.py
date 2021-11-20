import pygame

bg = pygame.image.load('BeijingStreetMap.png')
infected = pygame.image.load('redDot.png')
healthy = pygame.image.load('whiteDot.png')

area = 1

def healthCheck(val):
    if val:
        return infected
    else:
        return healthy

for _ in range(len(data)):
    blitList = []
    for i in range(len(list(data)[i])):
        blitList = blitList.append(infected[_], list(data.values())[1:2], area)
    pygame.Surface.blits(blitList)

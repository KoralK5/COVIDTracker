import pygame, pickle, random

with open("2008-02-02_13_30.pkl", 'rb') as f:
    data = pickle.load(f)
    data = {i:data[i] for i in sorted(data)}
        
location = []
for i in list(data):
    location.append(data[i][1:])

# top left = 40.193113, 115.796458
# bottom right = 39.725749, 116.844279

# x = 0.467364
# y = 1.04781
# 
# 1080 1920

background_image = pygame.image.load("maps_shot.png")
IMAGE_SMALL = pygame.transform.scale(background_image, (800, 600))
pygame.init()

BGCOLOR = (255, 255, 255)
RED = (255, 0, 0)

FPS = 30
screen = pygame.display.set_mode((800, 600))
pygame.display.update()

clock = pygame.time.Clock()

running = True

while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(BGCOLOR)
    screen.blit(IMAGE_SMALL, [0, 0])
    
    for i in range(len(location)):
        pygame.draw.circle(screen, RED, [location[i][1], location[i][0]], 1)
        
    pygame.display.flip()

pygame.quit()

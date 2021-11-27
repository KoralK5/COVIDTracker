import pygame, pickle, os
from pygame import *

x = -2738.7646
y = 977.266

background_image = pygame.image.load(f'maps_shot.png')
IMAGE_SMALL = pygame.transform.scale(background_image, (1280, 1024))
FPS = 45

pygame.init()

BGCOLOR = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (92, 92, 92)

f = 0
aph = 0
# buttons 
replay_button = pygame.Rect(490, 400, 300, 100)
simulation_button = pygame.Rect(490, 400, 300, 100)

day_night = pygame.Rect(0, 0, 1280, 1024)

font = pygame.font.SysFont('Ariel', 30, False, False)
font_two = pygame.font.SysFont('Times New Roman', 50, False, False)

screen = pygame.display.set_mode((1280, 1024))
pygame.display.update()
clock = pygame.time.Clock()

def grab(filename):
    return pickle.load(open(f'{os.getcwd()}\\spreadData\\{filename}', 'rb'))

files = os.listdir(os.getcwd() + '\\spreadData')


menu = 0
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            if replay_button.collidepoint(event.pos) and menu == 2:
                menu = 1
            elif simulation_button.collidepoint(event.pos) and menu == 0:
                menu = 1
            
    screen.fill(BGCOLOR)
    
    if menu == 0:
        #menu screen
        pygame.draw.rect(screen, GREY, replay_button)
        replay_m = font_two.render("Simulation", True, WHITE)
        screen.blit(replay_m, [530, 420])
        if simulation_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BLACK, replay_button, 5)
        
    elif menu == 1:
        screen.blit(IMAGE_SMALL, [0, 0])
        data = grab(files[f])
        infected, uninfected = 0, 0
        
        if f != 8786:
            for i in data.keys():
                color = RED if data[i][0] else BLUE
                infected += data[i][0]
                uninfected += not(data[i][0])
                pygame.draw.circle(screen, color, [(data[i][2] - 40.193113) * x, (data[i][1] - 115.796458) * y], 2)
            
            f += 1
        else:
            menu = 2
            f = 0

        t = files[f].split(' ')
        t = f'{t[0]} {t[1]}:{t[2][:2]} ----- {uninfected} uninfected ----- {infected} infected'
        time_of_day = int(t[11:13])
        
        s = pygame.Surface((1280, 1024))
        if 16 <= time_of_day <= 19 and aph != 180:
            aph += 1
        if 5 <= time_of_day <= 8 and aph != 0:
            aph -= 1

        s.set_alpha(aph)
        s.fill((0, 0, 0))
        screen.blit(s, (0, 0))

        pygame.draw.rect(screen, WHITE, [400, 0, 560, 40])
        time = font.render(t, True, BLACK)
        screen.blit(time, [410, 10])
        
    elif menu == 2:
        pygame.draw.rect(screen, GREY, replay_button)
        replay_m = font_two.render("Replay", True, WHITE)
        screen.blit(replay_m, [570, 420])
        
    pygame.display.flip()


pygame.quit()

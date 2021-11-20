import pygame, pickle, os

x = -2738.7646
y = 977.266

background_image = pygame.image.load(f'{os.getcwd()}\\Images\\maps_shot.png')
IMAGE_SMALL = pygame.transform.scale(background_image, (1280, 1024))
pygame.init()

BGCOLOR = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FPS = 30

screen = pygame.display.set_mode((1280, 1024))
pygame.display.update()
clock = pygame.time.Clock()

def grab(filename):
	return pickle.load(open(f'{os.getcwd()}\\spreadData\\{filename}', 'rb'))

files = os.listdir(os.getcwd() + '\\spreadData')

f = 0
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	screen.fill(BGCOLOR)
	screen.blit(IMAGE_SMALL, [0, 0])
	
	data = grab(files[f])
	for i in data.keys():
		color = RED if data[i][0] else BLUE
		pygame.draw.circle(screen, color, [(data[i][2] - 40.193113) * x, (data[i][1] - 115.796458) * y], 2)
	
	pygame.display.flip()
	f += 1

pygame.quit()

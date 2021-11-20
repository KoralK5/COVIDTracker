import pygame, pickle, os

for filename in os.listdir(os.getcwd()):
	with open(filename, 'rb') as f:
		data = pickle.load(f)
		data = {i:data[i] for i in sorted(data)}

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

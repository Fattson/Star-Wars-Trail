import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((956,560), 0, 32)

mecat = pygame.image.load("mecat.png")
mecat = pygame.transform.scale(mecat, (300,300))

mec = pygame.image.load("mec.png")

mec = pygame.transform.scale(mec, (300,300))

comp = pygame.image.load("comp.png")

comp = pygame.transform.scale(comp, (300,300))

i = 0

j = 0
clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
			if event.type == QUIT:
				exit()

	screen.blit(comp, (100,100))
	screen.blit(mec, (350,100))
	screen.blit(mecat, (600,100))
	pygame.display.update()

	"""while j < 10:
		if i == 0: # Computação
			screen.fill((0,0,0))
			screen.blit(mec, (350,100))
			screen.blit(mecat, (600,100))
			pygame.draw.rect(screen, (255,255,255), [99,99, 300, 300], 5)
			screen.blit(comp, (100,100))
			pygame.display.update()
			pygame.time.wait(100)
			i += 1

		if i == 1: # Mecanica
			screen.fill((0,0,0))
			screen.blit(comp, (100,100))
			screen.blit(mecat, (600,100))
			pygame.draw.rect(screen, (255,255,255), [399,99, 200, 300], 5)
			screen.blit(mec, (350,100))
			pygame.display.update()
			pygame.time.wait(100)
			i += 1

		if i == 2: # Mecatronica
			screen.fill((0,0,0))
			screen.blit(comp, (100,100))
			screen.blit(mec, (350,100))
			pygame.draw.rect(screen, (255,255,255), [650,99, 200, 300], 5)
			screen.blit(mecat, (600,100))
			pygame.display.update()
			pygame.time.wait(200)
			i += 1

		i = 0
		j += 1"""

	while j < 100:

		if i%2:
			pygame.draw.rect(screen, (255,255,255), [99,99, 300, 300], 5)
			pygame.draw.rect(screen, (255,255,255), [420,99, 160, 300], 5)
			pygame.draw.rect(screen, (255,255,255), [650,99, 200, 300], 5)
			pygame.display.update()
			pygame.time.wait(250)
			
			i += 1

		else:
			screen.fill((0,0,0))
			screen.blit(comp, (100,100))
			screen.blit(mec, (350,100))
			screen.blit(mecat, (600,100))
			pygame.display.update()
			pygame.time.wait(250)
			i += 1
		

		j += 1

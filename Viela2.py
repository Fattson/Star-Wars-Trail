import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((956,560), 0, 32)

background = pygame.image.load("viela3.png")
background = pygame.transform.scale(background, (956,560))


rect_transparente = pygame.image.load("carcomplex2.png")
rect_transparente = pygame.transform.scale(rect_transparente, (400,150))

i = 0

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
			if event.type == QUIT:
				exit()
    
	screen.blit(background, (0,0))
	if i == 60:
		screen.blit(rect_transparente,(300, 300))
	if i < 60:
		i += 1
	pygame.display.update()
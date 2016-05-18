import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((956,560), 0, 32)

background = pygame.image.load("estrelaspequeno.png")
background = pygame.transform.scale(background, (956,560))


texto = pygame.image.load("text1.png")
texto = pygame.transform.scale(texto, (956,2000))

position = {'x': 0, 'y': 0}

i = 0

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
			if event.type == QUIT:
				exit()
    

	screen.blit(background, (0,0))
	screen.blit(texto, (position['x'],position['y']))
	position['y'] -= 0.5
	pygame.display.update()


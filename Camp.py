import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((956,560), 0, 32)

background = pygame.image.load("campfire1.png")
background = pygame.transform.scale(background, (956,560))

carro = pygame.image.load("carrofogo.png")
carro1 = pygame.image.load("carrofogosimples.png")

carro = pygame.transform.scale(carro, (260,90))
carro1 = pygame.transform.scale(carro1, (300,100))
while True:
	for event in pygame.event.get():
			if event.type == QUIT:
				exit()

	screen.blit(background, (0,0))
	screen.blit(carro, (200,405))
	#screen.blit(carro1, (154,400))

	pygame.display.update()
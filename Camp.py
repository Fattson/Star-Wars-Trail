import pygame
from pygame.locals import *


def Camp():
	pygame.init()

	screen = pygame.display.set_mode((956,560), 0, 32)

	background = pygame.image.load("campfire1.png")
	background = pygame.transform.scale(background, (956,560))

	carro = pygame.image.load("carrofogo.png")

	carro = pygame.transform.scale(carro, (260,90))

	rect_transparente = pygame.image.load("campfire1_transparente1.png")

	rect_transparente= pygame.transform.scale(rect_transparente, (956,200))

	i = 0

	clock = pygame.time.Clock()

	while True:
		for event in pygame.event.get():
				if event.type == QUIT:
					exit()

		screen.blit(background, (0,0))
		screen.blit(carro, (190,405))
		if i == 60:
			pygame.draw.rect(screen, (0, 0, 0), [2,3,952,200])
			pygame.draw.rect(screen, (255, 255, 255), [2,3,952,200], 5)
			screen.blit(rect_transparente, (0,0))
		if i < 60:
			i += 1
		pygame.display.update()

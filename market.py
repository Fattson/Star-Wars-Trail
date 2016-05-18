import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((956,560), 0, 32)

background = pygame.image.load("market.png")
background = pygame.transform.scale(background, (956,560))


rect = pygame.image.load("market_preto.png")
rect = pygame.transform.scale(rect, (956,200))

rect_transparente = pygame.image.load("market_transp.png")
rect_transparente = pygame.transform.scale(rect_transparente, (956,200))


i = 0

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
			if event.type == QUIT:
				exit()
    
	screen.blit(background, (0,0))
	if i == 60:
		pygame.draw.rect(screen, (0, 0, 0), [2,2,952,200])
		screen.blit(rect,(0, 0))
		screen.blit(rect_transparente,(0, 0))
		pygame.draw.rect(screen, (255, 255, 255), [2,2,952,200], 5)
	if i < 60:
		i += 1
	pygame.display.update()
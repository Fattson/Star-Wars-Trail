import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((956,560), 0, 32)

background = pygame.image.load("estrelaspequeno.png")
background = pygame.transform.scale(background, (956,560))


texto = pygame.image.load("text1.png")
texto = pygame.transform.scale(texto, (956,2000))

position = {'x': 0, 'y': 400}

clock = pygame.time.Clock()

fonte = pygame.font.Font(None, 30)
espaco = fonte.render("Pressione espaço para roubar o carro!", 1, (255,255,255))

i = 0

while True:
	for event in pygame.event.get():
			if event.type == QUIT:
				exit()
    
	if position['y'] >= -1650:
		screen.blit(background, (0,0))
		screen.blit(texto, (position['x'],position['y']))
		position['y'] -= 0.5
		pygame.display.update()
		print(position['y'])

	else:
		while i < 200:
			for event in pygame.event.get():
				if event.type == QUIT:
					exit()
	    
			if i%2:
				screen.blit(espaco, (300,350))
				pygame.time.wait(250)
				i += 1
				pygame.display.update()
				
			else:
				pygame.draw.rect(screen, (0, 0, 0), [2,2,956,560])
				pygame.time.wait(250)
				i += 1
				pygame.display.update()

			clock.tick(30)

		

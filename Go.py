import pygame
from pygame.locals import *

pygame.init() # Iniciar pygame

# Configurações gerais da tela
screen = pygame.display.set_mode((956,560), 0, 32) # Tamanho da tela
pygame.display.set_caption("StarWars Trail") # Título

# Carregar imagens
#background = pygame.image.load("").convert()
#montanhas = pygame.image.load("").convert
#nuvens = pygame.image.load("").convert()
estrada = pygame.image.load("estrada.png")
carro = pygame.image.load("carro.png")
#sol = pygame.image.load("").convert()
pygame.transform.scale(carro, (10, 70))
# Posições
background_position = [0,0]
montanhas_position = [0,0]
nuvens_position = [0,0]
estrada_position = [0,20]
carro_position = [0,0]
sol_position = [0,0]

# Movimentos
montanhas_movimento = {'x': -2, 'y': 0}
nuvens_movimento = {'x': -3, 'y': 0}
carro_movimento = {'x': 0, 'y': 2}

# Relógio

time = pygame.time.Clock()

# Loop
while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	# Condição movimento carro vertical
	if carro_movimento['y'] == 2:
		carro_movimento['y'] = -2

	elif carro_movimento['y'] == -2:
		carro_movimento['y'] = 2

	# Movimentos
	montanhas_position[0] += montanhas_movimento['x']
	nuvens_position[0] += nuvens_movimento['x']
	carro_position[1] += carro_movimento['y']

	# Plotar na tela
	#screen.blit(background, background_position)
	#screen.blit(sol, sol_position)
	#screen.blit(montanhas, montanhas_position)
	#screen.blit(nuvens, nuvens_position)
	screen.blit(estrada, estrada_position)
	screen.blit(carro, carro_position)
	pygame.display.update()

	# relógio
	time.tick(30)
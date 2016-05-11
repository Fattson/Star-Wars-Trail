import pygame
from pygame.locals import *

pygame.init() # Iniciar pygame

# Configurações gerais da tela
screen = pygame.display.set_mode((956,500), 0, 32) # Tamanho da tela
pygame.display.set_caption("StarWars Trail") # Título

# Carregar imagens
background = pygame.image.load("").convert()
montanhas = pygame.image.load("").convert
nuvens = pygame.image.load("").convert()
estrada = pygame.image.load("").convert()
carro = pygame.image.load("").convert()
sol = pygame.image.load("").convert()

# Posições
background_position = [0,0]
montanhas_position = [0,0]
nuvens_position = [0,0]
estrada_position = [0,0]
carro_position = [0,0]
sol_position = [0,0]

# Movimentos
montanhas_movimento = {'x': -2, 'y': 0}
nuvens_movimento = {'x': -3, 'y': 0}
carro_movimento = {'x': 0, 'y': 0.5}

# Loop
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	# Condição movimento carro vertical
	if carro_movimento['y'] = 0.5:
		carro_movimento['y'] = -0.5
	elif carro_movimento['y'] = -0.5:
		carro_movimento['y'] = 0.5

	# Movimentos
	montanhas_position[0] += montanhas_movimento['x']
	nuvens_position[0] += nuvens_movimento['x']
	carro_position[0] += carro_movimento['x']

	# Plotar na tela
	screen.blint(background, background_position)
	screen.blint(sol, sol_position)
	screen.blint(montanhas, montanhas_position)
	screen.blint(nuvens, nuvens_position)
	screen.blint(estrada, estrada_position)
	screen.blint(carro, carro_position)


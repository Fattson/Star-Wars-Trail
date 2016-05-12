import pygame
from pygame.locals import *

pygame.init() # Iniciar pygame

# Configurações gerais da tela
screen = pygame.display.set_mode((956,560), 0, 32) # Tamanho da tela
pygame.display.set_caption("StarWars Trail") # Título

# Carregar imagens
background = pygame.image.load("background1.1.png").convert()
background2 = pygame.image.load("background1.1.png").convert()
#nuvens = pygame.image.load("").convert()
estrada = pygame.image.load("estrada.png")
estrada2 = pygame.image.load("estrada.png")

carro = pygame.image.load("carro.png")
#sol = pygame.image.load("").convert()
carro = pygame.transform.scale(carro, (50,50))

background = pygame.transform.scale(background, (956,300))
background2 = pygame.transform.scale(background, (956,300))
estrada = pygame.transform.scale(estrada, (956,200))
estrada2 = pygame.transform.scale(estrada, (956,200))

# Posições
background_position = [0,0]
background2_position = [956,0]
nuvens_position = [0,0]
estrada_position = [0,230]
estrada2_position =[956,230]
carro_position = [0,280]
sol_position = [0,0]

# Movimentos
background_movimento = {'x': -2, 'y': 0}
nuvens_movimento = {'x': -3, 'y': 0}
carro_movimento = {'x': 0, 'y': 2}

# Relógio

time = pygame.time.Clock()

# Loop
while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	tecla = pygame.key.get_pressed()

	# Condição movimento carro vertical
	if carro_movimento['y'] == 2:
		carro_movimento['y'] = -2

	elif carro_movimento['y'] == -2:
		carro_movimento['y'] = 2

	if background_position[0] == -956 or estrada_position[0] == -956:
		background_position[0] = 956
		estrada_position[0] = 956
	if background2_position[0] == -956 or estrada2_position[0] == -956:
		background2_position[0] = 956
		estrada_position[0] = 956


	if carro_position[1] > 260 and carro_position[1] < 290:
		if tecla[K_w]:
			carro_position[1] -= 1.5
		elif tecla[K_s]:
			carro_position[1] += 1.5
	elif carro_position[1] <= 260:
		if tecla[K_s]:
			carro_position[1] += 1.5
	elif carro_position[1] >= 290:
		if tecla[K_w]:
			carro_position[1] -= 1.5

	if carro_position[0] >= 0 and carro_position[0] <= 956:
		if tecla[K_a]:
			carro_position[0] -= 1.5
		elif tecla[K_d]:
			carro_position[0] += 1.5

	# Movimentos
	background_position[0] += background_movimento['x']
	background2_position[0] += background_movimento['x']
	nuvens_position[0] += nuvens_movimento['x']
	carro_position[1] += carro_movimento['y']

	estrada_position[0] += background_movimento['x']
	estrada2_position[0] += background_movimento['x']
	
	# Plotar na tela
	screen.blit(background, background_position)
	screen.blit(background2, background2_position)
	#screen.blit(sol, sol_position)
	#screen.blit(montanhas, montanhas_position)
	#screen.blit(nuvens, nuvens_position)
	screen.blit(estrada, estrada_position)
	screen.blit(estrada2, estrada2_position)
	screen.blit(carro, carro_position)
	pygame.display.update()

	# relógio
	time.tick(30)
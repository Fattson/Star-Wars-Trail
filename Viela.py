import pygame
from pygame.locals import *
# Iniciar e definir tela
pygame.init()
screen = pygame.display.set_mode((956,560), 0, 32)

# Carregar imagens e dimensioná-las
	# Background
background = pygame.image.load("viela.png")
background = pygame.transform.scale(background, (956,560))
	# Carro
carro = pygame.image.load("carcomplex2.png")
carro = pygame.transform.scale(carro, (400,150))
	# Personagens
comp = pygame.image.load("comp_dark.png")
comp = pygame.transform.scale(comp, (180,180))

# Movimentos
personagem_position = [-50,372]
personagem_velocity = [1,0]
# Variáveis
i = 0
flag = True
# Time
clock = pygame.time.Clock()

# Loop principal
while True:
	for event in pygame.event.get():
			if event.type == QUIT:
				exit()
	if personagem_position[0] <= 620 and flag:
		personagem_position[0] += personagem_velocity[0]
		if personagem_position[0] == 620:
			pygame.time.wait(500)
			flag = False
	screen.blit(background, (0,0))
	if personagem_position[0] > 620:
		pygame.time.wait(500)
	else:	
		screen.blit(comp, personagem_position)
	screen.blit(carro,(500, 400))
	
	pygame.display.update()
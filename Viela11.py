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

comp_head = pygame.image.load("comp_dark_head.png")
comp_head = pygame.transform.scale(comp_head, (180,180))

# Movimentos e posições
personagem_position = [-50,372]
carro_position = [500,400]
personagem_velocity = [3,0]

# Time
clock = pygame.time.Clock()

# Fazer texto de " Roubar o carro"
fonte = pygame.font.Font(None, 30)
espaco = fonte.render("Pressione espaço para roubar o carro!", 1, (255,255,255))

# Algumas variáveis
numet = 0
speedy_car = 0
espera = 0
i = 0
flag = True
Loop1 = True




while Loop1:
		for event in pygame.event.get(): # Se clicar
			if event.type == QUIT:
				exit()
		
		# Se apertar a tecla espaço "rouba o carro"
		if pygame.key.get_pressed()[K_SPACE]:
			Loop1 = False

		# Fazer a frase ficar piscando
		if i%2:
			screen.blit(espaco, (0,0))
			pygame.time.wait(250)
			i += 1
			pygame.display.update()
			for event in pygame.event.get(): # Se clicar
				if event.type == QUIT:
					exit()
		
		else:
			screen.blit(background,(0,0))
			screen.blit(carro,carro_position)
			pygame.time.wait(250)
			i += 1
			pygame.display.update()
			for event in pygame.event.get(): # Se clicar
				if event.type == QUIT:
					exit()
		


# Loop 2
while True:
	for event in pygame.event.get(): # Fechar a tela
			if event.type == QUIT:
				exit()

	# Enquanto o personagem não chega no carro ele caminha
	if personagem_position[0] <= 620 and flag:
		personagem_position[0] += personagem_velocity[0]
		if personagem_position[0] == 620:
			pygame.time.wait(500)
			flag = False

	# Alterar posição vertical do personagem
	if personagem_position[1] == 372:
		speedy = -1
	if personagem_position[1] == 360:
		speedy = 1

	personagem_position[1] += speedy
	
	# Blit no Background
	screen.blit(background, (0,0))

	# Se o personagem chega no carro, roda o Loop secundário
	if personagem_position[0] > 620:
		pygame.time.wait(500)

		# Loop Secundário
		while True:
			for event in pygame.event.get(): # Fechar a tela
				if event.type == QUIT:
					exit()
			# Personagem "entra" no carro
			if not personagem_position[1] == 400:
				personagem_position[1] += 1

			# Blit do Background
			screen.blit(background, (0,0))

			# Se o carro nao anda, ele plota a descida da cabeça do personagem
			if espera <= 40:
				screen.blit(comp_head, personagem_position)

			# Plota o carro
			screen.blit(carro,carro_position)
			# Se o personagem "está" no carro, o carro se movimenta
			if espera >= 40:
				if carro_position[1] == 400:
					speedy_car -= 2
				if carro_position[1] == 398:
					speedy_car += 2

				# Velocidade do carro 
				carro_position[1] += speedy_car
				carro_position[0] += 2
			
			pygame.display.update()
			espera += 1

	else:	
		screen.blit(comp, personagem_position)

	screen.blit(carro,carro_position)
	
	pygame.display.update()


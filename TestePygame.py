import pygame
from pygame.locals import *
from random import randint

pygame.init() # Iniciar pygame

screen = pygame.display.set_mode((956,560), 0, 32) # Definir tela e suas dimensões

pygame.display.set_caption("Testando, 1.. 2.. 3..") # Título da Sceen


imagem = pygame.image.load("oi.png").convert() # Carregar a imagem, .convert_alpha() serve para a imagem ficar em cima do Plano de Fundo
bg = pygame.image.load("desert8bitdaySCREEN.png").convert()
bg2 = pygame.image.load("desert8bitdaySCREEN.png").convert()  # Carregar a imagem, .convert() serve para a imagem ser o Plano de Fundo
xis = pygame.image.load("Xis.jpg").convert()
barra = pygame.image.load("barra_500x50.png").convert()
clock = pygame.time.Clock()# Tempo
image_position = [-500,0] # Colocar fora do while --'
circle_position = [100,100]

#imagem = pygame.transform.scale(imagem, (10, 70))

largura = 0
ya =  0
bg_x = 0
bg2_x = 956
while True: # Tem que ter haha
	
	for event in pygame.event.get(): # Todos os eventos do pygame
		if event.type == pygame.QUIT: # QUIT é para fechar a tela
			exit()


	speed = {'x': 2.5, 'y': 0} # Dicionário com as velocidades, não precisa ser dicionário, pode ser variávies. Mas é mais fácil
	Cspeed= {'x': 0, 'y': 0}

	tecla = pygame.key.get_pressed() # Registra as teclas pressionadas

	cair = {'y': 10}
	# Se tecla 'x' for pressionada, acontece 'y':
	if tecla[K_d]:
		speed['x'] = 5
	elif tecla[K_a]:
		speed['x'] = -5
	if tecla[K_s]:
		speed['y'] = 5
	elif tecla[K_w]:
		speed['y'] = -5
	if tecla[K_RIGHT]:
		Cspeed['x'] = 5
	elif tecla[K_LEFT]:
		Cspeed['x'] = -5
	if tecla[K_DOWN]:
		Cspeed['y'] = 5
	elif tecla[K_UP]:
		Cspeed['y'] = -5
	rand = randint(0, 956)
	bg_x -= 5
	bg2_x -= 5
	if bg_x <= -956:
		bg_x = 956
	if bg2_x <= -956:
		bg2_x = 956
	screen.blit(bg, (bg_x,0)) # Posicionar tela de fundo
	screen.blit(bg2, (bg2_x,0))
	image_position[0] += speed['x'] # Eixo X
	image_position[1] += speed['y'] # Lembrar que posição no eixo Y é invertida !
	circle_position[0] += Cspeed['x']
	circle_position[1] += Cspeed['y']
	screen.blit(imagem, image_position) # Plotar imagem na screen
	screen.blit(barra, (100,200))
	ya += cair['y'] 
	if largura <= 496:
		largura += 1
	retângulo = pygame.draw.rect(screen, (225, 0, 0), [103, 203, largura, 46])
	pygame.display.update() # Atualizar a tela constantemente, senão, ao mover, a imagem ela ficará arrastada
	time = clock.tick(60) # Definir frames per second


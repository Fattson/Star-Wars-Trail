import pygame
from pygame.locals import *
import testeInterface
from random import randint

jog = testeInterface.sw.Jogo()
def getStatusGO(jog, i):
	fonte = pygame.font.Font(None, 30)

	stat1 = "Gasolina: " + str(testeInterface.jog.gas - 0.06*i) 
	stat3 = "Durabilidade: " + str(testeInterface.jog.durab)
	stat8 = "Distancia restante: " + str(testeInterface.jog.distancia)
	stat9 = "Tempo restante: " + str(testeInterface.jog.temporestante)

	stat_gas = fonte.render(stat1, 1, (255,255,255))
	stat_dur = fonte.render(stat3, 1, (255,255,255))
	stat_dist = fonte.render(stat8, 1, (255,255,255))
	stat_temp = fonte.render(stat9, 1, (255,255,255))

	return stat_gas, stat_dur, stat_dist, stat_temp

def TelaGo(jog):
	pygame.init() # Iniciar pygame

	# Configurações gerais da tela
	screen = pygame.display.set_mode((956,560), 0, 32) # Tamanho da tela
	pygame.display.set_caption("StarWars Trail") # Título

	# Carregar imagens
	background = pygame.image.load("background1.1.png").convert()
	background2 = pygame.image.load("background1.1.png").convert()

	nuvens = pygame.image.load("nuvem_provisoria.png").convert()
	nuvens1 = pygame.image.load("nuvem_provisoria.png").convert()
	nuvens2 = pygame.image.load("nuvem_provisoria.png").convert()

	estrada = pygame.image.load("estrada.png")
	estrada2 = pygame.image.load("estrada.png")

	carro = pygame.image.load("carro.png")

	barra_limite = pygame.image.load("Barra_500x50.png").convert()
	#sol = pygame.image.load("").convert()

	carro = pygame.transform.scale(carro, (50,50))

	background = pygame.transform.scale(background, (956,300))
	background2 = pygame.transform.scale(background, (956,300))

	estrada = pygame.transform.scale(estrada, (956,200))
	estrada2 = pygame.transform.scale(estrada, (956,200))

	nuvens = pygame.transform.scale(nuvens, (50,30))
	nuvens2 = pygame.transform.scale(nuvens, (50,30))
	nuvens3 = pygame.transform.scale(nuvens, (50,30))

	# Posições
	barra_limite_position = [250,500]

	background_position = [0,0]
	background2_position = [956,0]

	nuvens_position = [950,100]
	nuvens2_position = [600,200]
	nuvens3_position = [300,50]

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

	#Algumas variáveis
	largura = 0
	py = 100 # 1o y da tela 
	esp = 35
	i = 0


	ev = randint(1,100)
	flag = 0
	lugar = randint(0,495)

	recta = pygame.Rect((150,350), (200,100))

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

		if background_position[0] == -956:
			background_position[0] = 956
		if background2_position[0] == -956:
			background2_position[0] = 956
		

		if estrada_position[0] == -956:
			estrada_position[0] = 956
		if estrada2_position[0] == -956:
			estrada2_position[0] = 956

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

		if nuvens_position[0] <= -100:
			nuvens_position[0] = 956

		if nuvens2_position[0] <= -100:
			nuvens2_position[0] = 956

		if nuvens3_position[0] <= -100:
			nuvens3_position[0] = 956

		# Movimentos
		background_position[0] += background_movimento['x']
		background2_position[0] += background_movimento['x']

		nuvens_position[0] += nuvens_movimento['x']
		nuvens2_position[0] += nuvens_movimento['x']
		nuvens3_position[0] += nuvens_movimento['x']

		carro_position[1] += carro_movimento['y']

		estrada_position[0] += background_movimento['x']
		estrada2_position[0] += background_movimento['x']
		
		# Plotar na tela
		screen.blit(background, background_position)
		screen.blit(background2, background2_position)
		#screen.blit(sol, sol_position))
		screen.blit(nuvens, nuvens_position)
		screen.blit(nuvens2, nuvens2_position)
		screen.blit(nuvens3, nuvens3_position)
		screen.blit(estrada, estrada_position)
		screen.blit(estrada2, estrada2_position)
		screen.blit(carro, carro_position)
		screen.blit(barra_limite, barra_limite_position)

		if largura <= 496:
			largura += 1
		if largura >= 496:
			break

		barra = pygame.draw.rect(screen, (225, 0, 0), [253, 503, largura, 46])
		
		if flag == 300:
		    if ev < 50: 
		    	testeInterface.ema(jog)
		    elif ev < 75:
		    	# vou add lobo guará
		    	pass

		    elif ev < 85:
		    	# vou add buraco
		    	pass

		flag += 1

		stat1, stat3, stat8, stat9 = getStatusGO(jog, i)
		
		screen.fill((0,0,0),recta)
		i += 1

		screen.blit(stat1, (150,py+250+1*esp))
		screen.blit(stat3, (150,py+300+1*esp))
		screen.blit(stat8, (600,py+250+1*esp))
		screen.blit(stat9, (600,py+300+1*esp))
		#screen.fill( True)
		pygame.display.update()
		print(flag)
		# relógio
		time.tick(30)
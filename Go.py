import pygame
from pygame.locals import *
from random import randint
from eventos import *

def randY():
	return randint(-100, 50)


def getStatusGO(jog, i):
	fonte = pygame.font.Font(None, 30)

	stat1 = "Gasolina: " + str(jog.gas - int(0.06*i)) 
	stat3 = "Durabilidade: " + str(jog.durab - int(0.06*i))
	stat8 = "Distancia restante: " + str(jog.distancia - int(0.6*i))
	stat9 = "Tempo restante: " + str(jog.temporestante - int(0.006*i))

	stat_gas = fonte.render(stat1, 1, (255,255,255))
	stat_dur = fonte.render(stat3, 1, (255,255,255))
	stat_dist = fonte.render(stat8, 1, (255,255,255))
	stat_temp = fonte.render(stat9, 1, (255,255,255))

	return stat_gas, stat_dur, stat_dist, stat_temp

def TelaGo(jog, screen, display, game_over):
	#pygame.init() # Iniciar pygame

	# Configurações gerais da tela
	#screen = pygame.display.set_mode((956,560), 0, 32) # Tamanho da tela
	#pygame.display.set_caption("StarWars Trail") # Título

	# Carregar imagens
	background = pygame.image.load("background1.1.png").convert()
	background2 = pygame.image.load("background1.1.png").convert()

	nuvens = pygame.image.load("nuvem3.png")
	nuvens1 = pygame.image.load("nuvem2.png")
	nuvens2 = pygame.image.load("nuvem1.png")

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

	nuvens = pygame.transform.scale(nuvens, (956,300))
	nuvens2 = pygame.transform.scale(nuvens, (956,300))
	nuvens3 = pygame.transform.scale(nuvens, (956,300))

	# Posições
	barra_limite_position = [250,500]

	background_position = [0,0]
	background2_position = [956,0]

	rand_nuvem = randY()
	rand_nuvem2 = randY()
	rand_nuvem3 = randY()

	nuvens_position = [0, rand_nuvem]
	nuvens2_position = [600, rand_nuvem2]
	nuvens3_position = [300, rand_nuvem3]

	estrada_position = [0,230]
	estrada2_position =[956,230]

	carro_position = [0,280]

	#sol_position = [0,0]

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


	ev = randint(0,100)
	lugar = randint(1,495)


	recta = pygame.Rect((150,350), (800,120))

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
			if tecla[K_w] or tecla[K_UP]:
				carro_position[1] -= 1.5
			elif tecla[K_s] or tecla[K_DOWN]:
				carro_position[1] += 1.5
		elif carro_position[1] <= 260:
			if tecla[K_s] or tecla[K_UP]:
				carro_position[1] += 1.5
		elif carro_position[1] >= 290:
			if tecla[K_w] or tecla[K_DOWN]:
				carro_position[1] -= 1.5

		if carro_position[0] >= 0 and carro_position[0] <= 956:
			if tecla[K_a]or tecla[K_LEFT]:
				carro_position[0] -= 1.5
			elif tecla[K_d] or tecla[K_RIGHT]:
				carro_position[0] += 1.5
		
		if carro_position[0] == -1.5:
			if tecla[K_a]:
				carro_position[0] += 1.5

		if nuvens_position[0] <= -650:
			nuvens_position[0] = 456
			rand_nuvem = randY()

		if nuvens2_position[0] <= -650:
			nuvens2_position[0] = 456
			rand_nuvem2 = randY()

		if nuvens3_position[0] <= -650:
			nuvens3_position[0] = 456
			rand_nuvem3 = randY()

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
		
		if i == lugar:
		    if ev < 50: 
		    	ema2(jog, screen, display)

		    elif ev < 75:
		    	lobo2(jog,screen, display)

		    elif ev < 85:
		    	buraco2(jog, screen, display)
        
		if jog.durab<=0:
		    jog.durab = 0 
		    quebrou2(jog, game_over, screen, display)
            
		if game_over[0]==True:
		    break

		stat1, stat3, stat8, stat9 = getStatusGO(jog, i)
		
		pygame.draw.rect(screen,(255, 255, 255), [0, 332, 956, 228], 5)
		screen.fill((0,0,0),recta)
		i += 1

		screen.blit(stat1, (150,py+250+1*esp))
		screen.blit(stat3, (150,py+300+1*esp))
		screen.blit(stat8, (600,py+250+1*esp))
		screen.blit(stat9, (600,py+300+1*esp))
		
		pygame.display.update()

		# relógio
		time.tick(30)
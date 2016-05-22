import pygame
from pygame.locals import *
from random import randint
from eventos import *
from math import *

def randY():
	return randint(-100, 50)


def getStatusGO(jog, i, game_over):
	fonte = pygame.font.Font(None, 30)

	stat1 = "Gasolina: " + str(jog.gas - int(0.06*i)) 
	stat3 = "Durabilidade: " + str(jog.durab - int(0.06*i))
	stat8 = "Distancia restante: " + str(jog.distancia - int(0.6*i))
	stat9 = "Tempo restante: " + str(jog.temporestante - int(0.006*i))
 
	if (jog.gas - int(0.06*i)) <= 0 or (jog.temporestante - int(0.006*i)) <= 0:
         game_over[0]=True

	stat_gas = fonte.render(stat1, 1, (255,255,255))
	stat_dur = fonte.render(stat3, 1, (255,255,255))
	stat_dist = fonte.render(stat8, 1, (255,255,255))
	stat_temp = fonte.render(stat9, 1, (255,255,255))

	return stat_gas, stat_dur, stat_dist, stat_temp

def TelaGo(jog, screen, display, game_over):
    
	semCactus = False 

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

	carro = pygame.transform.scale(carro, (50,50))

	background = pygame.transform.scale(background, (956,300))
	background2 = pygame.transform.scale(background, (956,300))

	estrada = pygame.transform.scale(estrada, (956,200))
	estrada2 = pygame.transform.scale(estrada, (956,200))

	nuvens = pygame.transform.scale(nuvens, (956,300))
	nuvens2 = pygame.transform.scale(nuvens, (956,300))
	nuvens3 = pygame.transform.scale(nuvens, (956,300))

	cactus = pygame.image.load("Cactus.png")
	cactus = pygame.transform.scale(cactus, (35,40))

	cactus2 = pygame.image.load("Cactus.png")
	cactus2 = pygame.transform.scale(cactus, (35,40))

	cactus3 = pygame.image.load("Cactus.png")
	cactus3 = pygame.transform.scale(cactus, (35,40))

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

	carro_position = [0,270]

	cactus_position = [956, 0]
	
	cactus_y = [285,265]

	# Movimentos
	background_movimento = {'x': -2, 'y': 0}
	nuvens_movimento = {'x': -3, 'y': 0}
	carro_movimento = {'x': 0, 'y': 2}
	cactus_movimento = {'x': 10, 'y': 0}

	# Relógio

	time = pygame.time.Clock()

	#Algumas variáveis
	
	largura = 0
	py = 100 # 1o y da tela 
	esp = 35
	i = 0
	cactus_flag = 0

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
			if tecla[K_d] or tecla[K_RIGHT]:
				carro_position[0] += 1.5

		if carro_position[0] == +957.5:
			if tecla[K_a] or tecla[K_LEFT]:
				carro_position[0] -= 1.5

		if carro_position[1] == -261.5:
			if tecla[K_s] or tecla[K_DOWN]:
				carro_position[1] += 1.5

		if carro_position[1] == -291.5:
			if tecla[K_w] or tecla[K_UP]:
				carro_position[1] -= 1.5



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

		cactus_position[0] -= cactus_movimento['x']

		
		# Plotar na tela
		screen.blit(background, background_position)
		screen.blit(background2, background2_position)
		screen.blit(nuvens, nuvens_position)
		screen.blit(nuvens2, nuvens2_position)
		screen.blit(nuvens3, nuvens3_position)
		screen.blit(estrada, estrada_position)
		screen.blit(estrada2, estrada2_position)
		screen.blit(carro, carro_position)
		screen.blit(barra_limite, barra_limite_position)
  
		if semCactus == False:
			if cactus_flag <= 150:
				if cactus_flag == 150:
				   cactus_flag = 0
				if cactus_flag == 0:
				   cactus_random = randint(0,1)
				
				   cactus_random2 = randint(0,1)
				
				   cactus_random3= randint(0,1)
				
				   cactus_position[0] = 956

			cactus_position[1] =  cactus_y[cactus_random]
			screen.blit(cactus, cactus_position)

			if (cactus_position[0]-carro_position[0]) < 10:
				if cactus_position[0] > carro_position[0]:
					if carro_position[1] - cactus_position[1] < 40 and carro_position[1] - cactus_position[1] > -20:
						print("Carro: " + str(carro_position[1]))
						print("Cactus: " + str(cactus_position[1]))
						print("Bateu")

			cactus_position[1] =  cactus_y[cactus_random2]
			screen.blit(cactus2, (cactus_position[0]+300,cactus_position[1]))

			if ((cactus_position[0]+300)-carro_position[0]) < 10:
				if (cactus_position[0]+300) > carro_position[0]:
					if carro_position[1] - cactus_position[1] < 40 and carro_position[1] - cactus_position[1] > -20:
						print("Carro: " + str(carro_position[1]))
						print("Cactus2: " + str(cactus_position[1]))
						print("Bateu")

			cactus_position[1] =  cactus_y[cactus_random3]

			screen.blit(cactus3, (cactus_position[0]+600,cactus_position[1]))
			screen.blit(cactus3, (cactus_position[0]+400,cactus_position[1]))
		
  
			# Colisões
			distancia_choqueX = cactus_position[0] - carro_position[0]
			distancia_choqueY = cactus_position[1] - carro_position[1]
			distancia_choqueX2 = (cactus_position[0]+200) - carro_position[0]
			distancia_choqueX3 = (cactus_position[0]+400) - carro_position[0]


			if ((cactus_position[0]+600)-carro_position[0]) < 10:
				if (cactus_position[0]+600) > carro_position[0]:
					if carro_position[1] - cactus_position[1] < 40 and carro_position[1] - cactus_position[1] > -20:
						print("Carro: " + str(carro_position[1]))
						print("Cactus3: " + str(cactus_position[1]))
						print("Bateu")	


		

		if largura <= 496:
			largura += 1
		if largura >= 496:
			break

		barra = pygame.draw.rect(screen, (225, 0, 0), [253, 503, largura, 46])
		
  
		if i == lugar:
		    if ev < 30: 
		    	if jog.comida >= 10:
        		    	ema(jog, screen, display)
		    	else:
        		    	lugar = randint((lugar+1),495)
        		    	ev = randint(0,100)
               

		    elif ev < 50:
		    	lobo(jog,screen, display)

		    elif ev < 80:
		    	if jog.reais >= 30:
        		    	assalto(jog, screen, display)
		    	else:
        		    	lugar = randint((lugar+1),495)  
        		    	ev = randint(0,100)
               
		    elif ev < 90:
		    	buraco(jog, screen, display)             
            
    
		if jog.durab<=0:
		    jog.durab = 0 
		    quebrou(jog, game_over, screen, display)
            
		if jog.temporestante <= 0 or jog.health <= 0 or jog.gas <= 0:
		    game_over[0] = True
		    break

		stat1, stat3, stat8, stat9 = getStatusGO(jog, i, game_over)
            
		if game_over[0]==True:
		    break

		
		pygame.draw.rect(screen,(255, 255, 255), [0, 332, 956, 228], 5)
		screen.fill((0,0,0),recta)

		i += 1
		cactus_flag += 1

		screen.blit(stat1, (150,py+250+1*esp))
		screen.blit(stat3, (150,py+300+1*esp))
		screen.blit(stat8, (600,py+250+1*esp))
		screen.blit(stat9, (600,py+300+1*esp))
		
		pygame.display.update()

		# relógio
		time.tick(30)
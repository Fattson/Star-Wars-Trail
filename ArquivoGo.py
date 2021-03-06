import pygame
from pygame.locals import *
from random import randint
from ArquivoEventos import *
from math import *

def randY(): # Função para gerar valores usados para o blit das nuvens
	return randint(-100, 50)

def getStatusGO(jog, i, game_over): # Função que gera os status do personagem em forma de frases e calcula para o posterior blit
	fonte = pygame.font.Font(None, 30)

	stat1 = "Gasolina: " + str(jog.gas - int(0.1*i))
	stat3 = "Durabilidade: " + str(jog.durab - int(0.06*i))
	stat8 = "Distancia restante: " + str(jog.distancia - int(0.6*i))
	stat9 = "Tempo restante: " + str(jog.temporestante - int(0.006*i))
 
	if (jog.gas - int(0.1*i)) <= 0 or (jog.temporestante - int(0.006*i)) <= 0: # Se o gás ou o tempo for == 0 , GAME OVER
         game_over[0]=True

	stat_gas = fonte.render(stat1, 1, (255,255,255))
	stat_dur = fonte.render(stat3, 1, (255,255,255))
	stat_dist = fonte.render(stat8, 1, (255,255,255))
	stat_temp = fonte.render(stat9, 1, (255,255,255))

	return stat_gas, stat_dur, stat_dist, stat_temp

def rect_cactus(screen, cactus_position, x): # Função que cria Hitbox para os Cactus
	return pygame.draw.rect(screen, (255,255,255),[cactus_position[0]+x, cactus_position[1]+20, 5, 20], 1)	# x = 12 ou 312 ou 612

def rect_carro(screen, carro_position):	# Função que cria Hitbox para o carro
	return pygame.draw.rect(screen, (0,0,0),[carro_position[0]+30, carro_position[1]+20, 5, 10])

def TelaGo(jog, screen, display, game_over): # Função "MASTER" que gera a tela GO
    
	semCactus = False # Teste para os cactus

	# Carregar imagens e dimensioná-las

		# Backgound
	background = pygame.image.load("background1.1.png").convert()
	background2 = pygame.image.load("background1.1.png").convert()

	background = pygame.transform.scale(background, (956,300))
	background2 = pygame.transform.scale(background, (956,300))
		# Nuvens
	nuvens = pygame.image.load("nuvem3.png")
	nuvens1 = pygame.image.load("nuvem2.png")
	nuvens2 = pygame.image.load("nuvem1.png")

	nuvens = pygame.transform.scale(nuvens, (956,300))
	nuvens2 = pygame.transform.scale(nuvens, (956,300))
	nuvens3 = pygame.transform.scale(nuvens, (956,300))
		# Estrada
	estrada = pygame.image.load("estrada.png")
	estrada2 = pygame.image.load("estrada.png")

	estrada = pygame.transform.scale(estrada, (956,200))
	estrada2 = pygame.transform.scale(estrada, (956,200))
		# Carro
	carro = pygame.image.load("carro2.png")

	carro = pygame.transform.scale(carro, (50,50))
		# Barra de progresso
	barra_limite = pygame.image.load("Barra_500x50.png").convert()
		# Cactus
	
	cactus = pygame.image.load("cactus_v2.png")
	cactus = pygame.transform.scale(cactus, (35,40))

	cactus_mov = pygame.image.load("cactus_v2_mov.png")
	cactus_mov = pygame.transform.scale(cactus_mov, (35,40))

	cactus_dead = pygame.image.load("cactus_dead.png")
	cactus_dead = pygame.transform.scale(cactus_dead, (35,40))

	cactus2 = pygame.image.load("cactus_v2.png")
	cactus2 = pygame.transform.scale(cactus, (35,40))

	cactus2_mov = pygame.image.load("cactus_v2_mov.png")
	cactus2_mov = pygame.transform.scale(cactus2_mov, (35,40))

	cactus2_dead = pygame.image.load("cactus_dead.png")
	cactus2_dead = pygame.transform.scale(cactus_dead, (35,40))

	cactus3 = pygame.image.load("cactus_v2.png")
	cactus3 = pygame.transform.scale(cactus, (35,40))

	cactus3_mov = pygame.image.load("cactus_v2_mov.png")
	cactus3_mov = pygame.transform.scale(cactus3_mov, (35,40))

	cactus3_dead = pygame.image.load("cactus_dead.png")
	cactus3_dead = pygame.transform.scale(cactus_dead, (35,40))

	# Posições
		
		# Barra
	barra_limite_position = [250,500]
		# Background
	background_position = [0,0]
	background2_position = [956,0]
		# Nuvens (3) com posição aleatória
	rand_nuvem = randY()
	rand_nuvem2 = randY()
	rand_nuvem3 = randY()

	nuvens_position = [0, rand_nuvem]
	nuvens2_position = [600, rand_nuvem2]
	nuvens3_position = [300, rand_nuvem3]
		# Estrada
	estrada_position = [0,230]
	estrada2_position =[956,230]
	
		# Carro
	carro_position = [0,280]
		
      # Cactus
	cactus_position = [956, 0]
	cactus_y = [285,265] # Posição Y varia

	# Movimentos

	background_movimento = {'x': -2, 'y': 0}
	nuvens_movimento = {'x': -3, 'y': 0}
	carro_movimento = {'x': 0, 'y': 2}
	cactus_movimento = {'x': 10, 'y': 0}

	# Relógio

	time = pygame.time.Clock()

	#Algumas variáveis que serão utilizadas
	
	largura = 0
	py = 100 # 1o y da tela 
	esp = 35
	i = 0
	cactus_flag = 0
	ev = randint(0,100)
	lugar = randint(1,495)
	cactus_movim = 0
	Crash = False
	Crash2 = False
	Crash3 = False

	# Retângulo utilizado para ser a área do FILL

	recta = pygame.Rect((150,350), (800,120))

	# Loop, onde será rodado toda a tela GO

	while True:
		for event in pygame.event.get(): # Se for clicado o X para fechar a tela...
			if event.type == QUIT:
				exit()

		tecla = pygame.key.get_pressed() # Registrar toda tecla pressionada
  
		if tecla[K_SPACE]:
			break

		# Condição para o movimento vertical do carro
		if carro_movimento['y'] == 2:
			carro_movimento['y'] = -2

		elif carro_movimento['y'] == -2:
			carro_movimento['y'] = 2

		# Condição para o movimento do Background
		if background_position[0] == -956:
			background_position[0] = 956
		if background2_position[0] == -956:
			background2_position[0] = 956
		
		# Condição para o movimento da estrada
		if estrada_position[0] == -956:
			estrada_position[0] = 956
		if estrada2_position[0] == -956:
			estrada2_position[0] = 956

		# Condições para movimentar o carro
		if carro_position[1] > 260 and carro_position[1] < 290: # Não sair da estrada
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

		if carro_position[0] >= 0 and carro_position[0] <= 956: # Não sair da esctrada
			if tecla[K_a]or tecla[K_LEFT]:
				carro_position[0] -= 1.5
			elif tecla[K_d] or tecla[K_RIGHT]:
				carro_position[0] += 1.5
		
		if carro_position[0] < 1:
			if tecla[K_d] or tecla[K_RIGHT]:
				carro_position[0] += 1.5

		if carro_position[0] > 955:
			if tecla[K_a] or tecla[K_LEFT]:
				carro_position[0] -= 1.5

		if carro_position[1] < 260:
			if tecla[K_s] or tecla[K_DOWN]:
				carro_position[1] += 1.5

		if carro_position[1] > 290:
			if tecla[K_w] or tecla[K_UP]:
				carro_position[1] -= 1.5

		# Condições de movimentação das nuvens

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

			# Background
		background_position[0] += background_movimento['x']
		background2_position[0] += background_movimento['x']
			# Nuvens
		nuvens_position[0] += nuvens_movimento['x']
		nuvens2_position[0] += nuvens_movimento['x']
		nuvens3_position[0] += nuvens_movimento['x']
			# Carro
		carro_position[1] += carro_movimento['y']
			# Estrada
		estrada_position[0] += background_movimento['x']
		estrada2_position[0] += background_movimento['x']		

			# Cactus
		cactus_position[0] -= cactus_movimento['x']

		# Plotar na tela

		screen.blit(background, background_position)
		screen.blit(background2, background2_position)
		screen.blit(nuvens, nuvens_position)
		screen.blit(nuvens2, nuvens2_position)
		screen.blit(nuvens3, nuvens3_position)
		screen.blit(estrada, estrada_position)
		screen.blit(estrada2, estrada2_position)
		c1 = rect_carro(screen, carro_position)
		screen.blit(carro, carro_position)
		screen.blit(barra_limite, barra_limite_position)
  
		# Colocar os cactus na tela em posição "Aleatória"

		if semCactus == False:
			if cactus_flag <= 160:
				if cactus_flag == 160:
				   cactus_flag = 0
				   
				if cactus_flag == 0:
				   cactus_random = randint(0,1)
				
				   cactus_random2 = randint(0,1)
				
				   cactus_random3= randint(0,1)
				
				   cactus_position[0] = 956

				   Crash = False
				   Crash2 = False
				   Crash3 = False
			
			# Gerar posição Y para Cactus e blit na tela
			cactus_position[1] =  cactus_y[cactus_random]
			x1 = rect_cactus(screen, cactus_position, 12)

			# Mudar de imagem do cacto para dar a sensação de movimento
			#print(Crash, Crash2, Crash3)
			#print(cactus_movim)
			
			if cactus_movim < 5:
				if Crash == False:
					screen.blit(cactus, cactus_position)
			if cactus_movim >= 5 and cactus_movim <= 10:
				if Crash == False:
					screen.blit(cactus_mov, cactus_position)
				if cactus_movim == 10:
					cactus_movim = 0
			if Crash:
				screen.blit(cactus_dead,(cactus_position[0], cactus_position[1]+10))
			
			if cactus_position[1] < carro_position[1]: # Para o carro passar na frente o cactus
				screen.blit(carro, carro_position)
			
			# Gerar posição Y para Cactus2 e blit na tela
			cactus_position[1] =  cactus_y[cactus_random2]
			x2 = rect_cactus(screen, cactus_position, 312)

			# Mudar de imagem do cacto para dar a sensação de movimento
			
			if cactus_movim < 5:
				if Crash2 == False:
					screen.blit(cactus2, (cactus_position[0]+300,cactus_position[1]))
			if cactus_movim >= 5 and cactus_movim <= 10:
				if Crash2 == False:
					screen.blit(cactus2_mov, (cactus_position[0]+300,cactus_position[1]))
				if cactus_movim == 10:
					cactus_movim = 0
			
			if Crash2:
				screen.blit(cactus2_dead, (cactus_position[0]+300, cactus_position[1]+10))

			if cactus_position[1] < carro_position[1]: # Para o carro passar na frente o cactus
				screen.blit(carro, carro_position)

			# Gerar posição Y para Cactus3 e blit na tela
			cactus_position[1] =  cactus_y[cactus_random3]
			x3 = rect_cactus(screen, cactus_position, 612)

			# Mudar de imagem do cacto para dar a sensação de movimento
			
			if cactus_movim < 5:
				if Crash3 == False:
					screen.blit(cactus3, (cactus_position[0]+600,cactus_position[1]))
			if cactus_movim >= 5 and cactus_movim <= 10:
				if Crash3 == False:
					screen.blit(cactus3_mov, (cactus_position[0]+600,cactus_position[1]))
				if cactus_movim == 10:
					cactus_movim = 0

			if Crash3:
				screen.blit(cactus3_dead, (cactus_position[0]+600, cactus_position[1]+10))
			
			if cactus_position[1] < carro_position[1]: # Para o carro passar na frente o cactus
				screen.blit(carro, carro_position)
		
			# Colisões
			
			if c1.colliderect(x1) or c1.colliderect(x2) or c1.colliderect(x3):
				jog.durab -= 10
				if jog.durab <= 0:
						jog.durab = 0 
						quebrou(jog, game_over, screen, display)
				
				if c1.colliderect(x1):
					Crash = True
				if c1.colliderect(x2):
					Crash2 = True
				if c1.colliderect(x3):
					Crash3 = True
		# Quando a barra chegar no final, tela Go acaba

			if cactus_flag <= 170:
				if cactus_flag == 170:
						cactus_flag = 0
				if cactus_flag == 0:
						cactus_random = randint(0,1)
						cactus_random2 = randint(0,1)
						cactus_random3= randint(0,1)
						cactus_position[0] = 956
		

        # Gerar barra de progresso
		barra = pygame.draw.rect(screen, (225, 0, 0), [253, 503, largura, 46])
		if largura <= 496:
			largura += 1
		if largura >= 496:
			break

		# Gerar aleatoriedade dos eventos
		if i == lugar:
		    if ev < 40: 
		    	if jog.comida >= 10:
        		    	ema(jog, screen, display)
		    	else: # se nao tem comida suficiente pra ser roubada, ele troca a variavel ev e lugar 
        		    	lugar = randint((lugar+1),495)
        		    	ev = randint(0,100)
               

		    elif ev < 55:
		    	lobo(jog,screen, display)

		    elif ev < 75: 
		    	if jog.reais >= 30:
        		    	assalto(jog, screen, display)
		    	else:# se nao tem dindin suficiente pra ser roubada, ele troca a variavel ev e lugar 
        		    	lugar = randint((lugar+1),495)  
        		    	ev = randint(0,100)
               
		    elif ev < 90:
		    	buraco(jog, screen, display)             
            
    	# Condições para o jogo terminar
		if jog.durab<=0:
		    jog.durab = 0 
		    quebrou(jog, game_over, screen, display)
            
		if jog.temporestante <= 0 or jog.health <= 0 or jog.gas <= 0:
		    game_over[0] = True
		    break

		if game_over[0]==True:
		    break

		# Chamada de função para dar blit na tela
		stat1, stat3, stat8, stat9 = getStatusGO(jog, i, game_over)
        
        # Gerar barra externa a barra ' kkk '
		pygame.draw.rect(screen,(255, 255, 255), [0, 332, 956, 228], 5)
		screen.fill((0,0,0),recta)

		# Contadores
		i += 1
		cactus_flag += 1
		cactus_movim += 1

		# Blit no status
		screen.blit(stat1, (150,py+250+1*esp))
		screen.blit(stat3, (150,py+300+1*esp))
		screen.blit(stat8, (600,py+250+1*esp))
		screen.blit(stat9, (600,py+300+1*esp))
		
		# Update
		pygame.display.update()

		# relógio
		time.tick(30)

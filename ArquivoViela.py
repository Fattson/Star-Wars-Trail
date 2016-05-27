"""
Esse arquivo contem a funcao "viela", para ser usada no jogo Star Wars Trail
"""

import pygame
from pygame.locals import *


def viela(jog, screen, display):

    # Carregar imagens e dimensioná-las
        	# Background
    background = pygame.image.load("viela.png")
    background = pygame.transform.scale(background, (956,560))
        # Carro
    carro = pygame.image.load("carcomplex2.png")
    carro = pygame.transform.scale(carro, (400,150))


	# Personagens
    if jog.comp:
        personagem = pygame.image.load("comp_dark.png")
        personagem = pygame.transform.scale(personagem, (180,180))	# 160x160 para mecat , resto: 180x180
        
        personagem_head = pygame.image.load("comp_dark_head.png")
        personagem_head = pygame.transform.scale(personagem_head, (160,160))	# 160x160 para mecat , resto: 180x180

    if jog.mecatronica:
        personagem = pygame.image.load("mecat_dark.png")
        personagem = pygame.transform.scale(personagem, (180,180))	# 160x160 para mecat , resto: 180x180
        
        personagem_head = pygame.image.load("mecat_dark_head.png")
        personagem_head = pygame.transform.scale(personagem_head, (180,180))	# 160x160 para mecat , resto: 180x180

    if jog.mecanica:
        personagem = pygame.image.load("mec_dark.png")
        personagem = pygame.transform.scale(personagem, (160,160))	# 160x160 para mecat , resto: 180x180
        
        personagem_head = pygame.image.load("mec_dark_head.png")
        personagem_head = pygame.transform.scale(personagem_head, (160,160))	# 160x160 para mecat , resto: 180x180

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
    speedy_car = 0
    espera = 0
    i = 0
    flag = True
    Loop1 = True
    acabou = False
    
    
    
    while Loop1:
         for event in pygame.event.get(): # Se clicar
            if event.type == QUIT:
                exit()
		
		# Se apertar a tecla espaço "rouba o carro"
         if pygame.key.get_pressed()[K_SPACE]:
                 Loop1 = False

		# Fazer a frase ficar piscando
         if i%5:
                 screen.blit(espaco, (0,0))
                 i += 1

		
         else:
                 screen.blit(background,(0,0))
                 screen.blit(carro,carro_position)
                 i += 1
                 
         #pygame.time.wait(250)
                 
         pygame.display.update()
         clock.tick(10)
		


    # Loop 2
    while not acabou:
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
            while not acabou:
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
                      screen.blit(personagem_head, personagem_position)

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
                      if carro_position[0] == 900: #quando o carro sair da tela, acabou a viela (rimou hihihi)
                          acabou = True
                      
			
                  pygame.display.update()
                  clock.tick(30)
                  espera += 1

        else:	
            screen.blit(personagem, personagem_position)

            screen.blit(carro,carro_position)
	
            pygame.display.update()
            clock.tick(30)


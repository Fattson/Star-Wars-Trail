import pygame
from pygame.locals import *
from ArquivoViela import *
from ArquivoPersonagens import *


def fadeIn(screen,display, background): # Efeito fedeIn
    for i in range(0,20):
        screen.blit(background, (0,0))
        pygame.display.update()
        pygame.time.wait(100)

def intro(jog, screen, display): # Função Geraaaal

    # Carregar imagens e dimensioná-las
        # Background
    background = pygame.image.load("estrelaspequeno.png")
    background = pygame.transform.scale(background, (956,560))

    background2 = pygame.image.load("estrelaspequeno2.png")
    background2 = pygame.transform.scale(background2, (956,560))    
        # Texto principal
    texto = pygame.image.load("text1.png")
    texto = pygame.transform.scale(texto, (956,2000))
        # Outros textos
    azul_forte = pygame.image.load("azul_forte.png")
    azul_forte = pygame.transform.scale(azul_forte, (600,200))

    azul_medio = pygame.image.load("azul_medio.png")
    azul_medio = pygame.transform.scale(azul_medio, (600,200))

    azul_fraco = pygame.image.load("azul_fraco.png")
    azul_fraco = pygame.transform.scale(azul_fraco, (600,200))

    azul_superfraco = pygame.image.load("azul_superfraco.png")
    azul_superfraco = pygame.transform.scale(azul_superfraco, (600,200))

    # Posição inicial do texto principal
    position = {'x': 0, 'y': 400}

    # Time
    clock = pygame.time.Clock()

    # Fazer texto de " Roubar o carro"
    fonte = pygame.font.Font(None, 30)
    espaco = fonte.render("Pressione espaço para roubar o carro!", 1, (255,255,255))

    # Carregar som
    som = pygame.mixer.Sound("musica_abertura.wav")
    
    # Algumas variáveis a usar
    azul = 0
    i = 0
    flag = True
    FadeIn = 0
    # Loop principal
    while flag:
        for event in pygame.event.get(): # Sair do jogo
            if event.type == QUIT:
                exit()
        
        # Efeito FadeIn e FadeOut para o texto inicial
        while azul <= 3:
            screen.blit(azul_fraco, (215,250))
            pygame.display.update()
            pygame.time.wait(300)
            
            azul += 1
            
        while azul <= 6:
            screen.blit(azul_medio, (215,250))
            pygame.display.update()
            pygame.time.wait(300)
            
            azul += 1
            
        while azul <= 9:
            screen.blit(azul_forte, (215,250))
            pygame.display.update()
            pygame.time.wait(1000)
            
            azul += 1

        screen.fill((0,0,0))
        while azul <= 12:
            screen.blit(azul_medio, (215,250))
            pygame.display.update()
            
            azul += 1

        pygame.time.wait(200)
        screen.fill((0,0,0))
        while azul <= 15:
            screen.blit(azul_fraco, (215,250))
            pygame.display.update()
            
            azul += 1

        pygame.time.wait(300)
        screen.fill((0,0,0))
        while azul == 16:
            screen.blit(azul_fraco, (215,250))
            pygame.display.update()

            azul += 1

        pygame.time.wait(400)
        screen.fill((0,0,0))
        while azul <= 19:
            screen.blit(azul_superfraco, (215,250))
            pygame.display.update()

            azul += 1

        pygame.time.wait(100)
        screen.fill((0,0,0))

        # Update
        pygame.display.update()

        # Iniciar som
        som.play()
        
        # Loop que move o texto principal
        while True:
            for event in pygame.event.get(): # Se sair
                if event.type ==  QUIT:
                    exit()
            # Iniciar o FadeIn
            if FadeIn == 0:
                fadeIn(screen,display, background)
                FadeIn = 1

            # Acabar o FadeIn    
            else:
                screen.fill((0,0,0))
                screen.blit(background2, (0,0)) 
            screen.blit(texto, (position['x'],position['y']))
            position['y'] -= 1
            pygame.display.update()

            # Apertar a tecla espaço para pular a introdução
            if pygame.key.get_pressed()[K_SPACE]:
                flag = False
                som.fadeout(1000)
                pygame.time.wait(300)
                screen.fill((0,0,0))
                personagem(jog, screen, display)
                pygame.time.wait(200)
                viela(jog, screen, display)
                break
            if position['y'] <= -1650:
                flag = False
                som.fadeout(1000)
                screen.fill((0,0,0))
                personagem(jog, screen, display)
                pygame.time.wait(200)
                viela(jog, screen, display)
                break
        
        clock.tick(30)
        azul += 1

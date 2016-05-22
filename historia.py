import pygame
from pygame.locals import *


def fadeIn(screen,display, background):
    for i in range(0,20):
        screen.blit(background, (0,0))
        pygame.display.update()
        pygame.time.wait(100)

def intro(screen, display):

    
    background = pygame.image.load("estrelaspequeno.png")
    background = pygame.transform.scale(background, (956,560))

    background2 = pygame.image.load("estrelaspequeno2.png")
    background2 = pygame.transform.scale(background2, (956,560))    

    texto = pygame.image.load("text1.png")
    texto = pygame.transform.scale(texto, (956,2000))

    position = {'x': 0, 'y': 400}

    clock = pygame.time.Clock()

    fonte = pygame.font.Font(None, 30)
    espaco = fonte.render("Pressione espaço para roubar o carro!", 1, (255,255,255))


    som = pygame.mixer.Sound("musica_abertura.wav")
    

    azul_forte = pygame.image.load("azul_forte.png")
    azul_forte = pygame.transform.scale(azul_forte, (600,200))
    azul_medio = pygame.image.load("azul_medio.png")
    azul_medio = pygame.transform.scale(azul_medio, (600,200))
    azul_fraco = pygame.image.load("azul_fraco.png")
    azul_fraco = pygame.transform.scale(azul_fraco, (600,200))

    azul = 0


    i = 0
    
    flag = True

    while flag:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        
        while azul <= 3:
            screen.blit(azul_fraco, (215,250))
            pygame.display.update()
            pygame.time.wait(300)
            
            azul += 1
            
        while azul > 3 and azul <= 6:
            screen.blit(azul_medio, (215,250))
            pygame.display.update()
            pygame.time.wait(300)
            
            azul += 1
            
        while azul > 6 and azul <= 9:
            screen.blit(azul_forte, (215,250))
            pygame.display.update()
            pygame.time.wait(1000)
            
            azul += 1

        screen.fill((0,0,0))
        while azul > 9 and azul <= 12:
            screen.blit(azul_medio, (215,250))
            pygame.display.update()
            
            azul += 1
        pygame.time.wait(300)
        screen.fill((0,0,0))
        while azul > 12 and azul <= 15:
            screen.blit(azul_fraco, (215,250))
            pygame.display.update()
            
            azul += 1

        pygame.time.wait(300)
        screen.fill((0,0,0))

        while azul == 16:
            screen.blit(azul_fraco, (215,250))
            pygame.display.update()

            azul += 1
        screen.fill((0,0,0))
        pygame.display.update()

        a = 0
        if azul >= 20:
            som.play()
            
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
        
               
                if a == 0:
                    fadeIn(screen,display, background)
                    a = 1
                else:
                    screen.fill((0,0,0))
                    screen.blit(background2, (0,0)) 
                screen.blit(texto, (position['x'],position['y']))
                position['y'] -= 1
                pygame.display.update()
                if pygame.key.get_pressed()[K_SPACE]:
                    flag = False
                    break
                if position['y'] <= -1650:
                    break

        
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                        
                if pygame.key.get_pressed()[K_SPACE]:
                    flag = False
                    som.fadeout(3000)
                    break
        
                if i%2:
                    screen.blit(espaco, (300,350))
                    pygame.time.wait(250)
                    i += 1
                    pygame.display.update()
    			
                else:
                    pygame.draw.rect(screen, (0, 0, 0), [2,2,956,560])
                    pygame.time.wait(250)
                    i += 1
                    pygame.display.update()
                   
                clock.tick(30)
        clock.tick(30)
        azul += 1
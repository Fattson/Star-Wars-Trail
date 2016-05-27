import pygame
from pygame.locals import *


def personagem(jog, screen, display):

    mecat = pygame.image.load("mecat.png")
    mecat = pygame.transform.scale(mecat, (300,300))
    
    mec = pygame.image.load("mec.png")
    
    mec = pygame.transform.scale(mec, (300,300))
    
    comp = pygame.image.load("comp.png")
    
    comp = pygame.transform.scale(comp, (300,300))
    
    titulo = pygame.image.load("escolha_titulo.png")
    
    fonte = pygame.font.Font(None, 28)
    
    info = fonte.render("Setas para trocar. SPACE para escolher", 1, (255,255,255))
    
    
    ecomp = pygame.image.load('escolha_computacao.png')
    emec = pygame.image.load('escolha_mecanico.png')
    emecat = pygame.image.load('escolha_mecatronico.png')
    
    clock = pygame.time.Clock()
    
    sel = 1
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        
        
        if pygame.key.get_pressed()[K_RIGHT]:
            if sel == 3:
                sel = 1
            else:
                sel += 1
            screen.fill((0,0,0))
            pygame.time.wait(200)
        
        if pygame.key.get_pressed()[K_LEFT]:
            if sel == 1:
                sel = 3
            else:
                sel -= 1
            screen.fill((0,0,0))
            pygame.time.wait(200)
            
        screen.blit(titulo, (0,0))
        screen.blit(comp, (100,100))
        screen.blit(mec, (350,100))
        screen.blit(mecat, (600,100))
        screen.blit(info, (0, 530))
        pygame.display.update()
                
        if sel == 1:
            pygame.draw.rect(screen, (255,255,255), [99,99, 300, 300], 5)
            screen.blit(ecomp, (99, 410))            
            pygame.display.update()            
            
        if sel == 2:
            pygame.draw.rect(screen, (255,255,255), [420,99, 160, 300], 5)
            screen.blit(emec,(420,410))
            pygame.display.update()
            
        if sel == 3:
            pygame.draw.rect(screen, (255,255,255), [650,99, 200, 300], 5)
            screen.blit(emecat,(650, 410))
            pygame.display.update()
            
            
        if pygame.key.get_pressed()[K_SPACE]:
            if sel == 1:
                jog.comp = True
            if sel == 2:
                jog.mecanica = True
            if sel == 3:
                jog.mecatronica = True
            break
        
        
        pygame.display.update()
        clock.tick(30)
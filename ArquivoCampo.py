# -*- coding: utf-8 -*-
"""
Esse arquivo contem a funcao "campo" para ser usada no jogo Star Wars Trail
"""

from pygame import *
from ArquivoLimpa import *
from ArquivoConserto import *
from ArquivoStatus import *

ticke = 35 #fps
fonte = font.Font(None, 30) # define uma fonte
clock = time.Clock() # cria o reloginho


## DEFINICAO DE TEXTOS PARA SEREM USADOS MAIS PARA FRENTE
camp = fonte.render("ACAMPAMENTO! O que deseja fazer?",1,(255,255,255))
camp_menu0 = fonte.render("0 - Continuar a viagem", 1, (255,255,255))
camp_menu1 = fonte.render("1 - Caçar (-2 horas +10 comidas)",1,(255,255,255))
camp_menu2 = fonte.render("2 - Conserto do carro", 1, (255,255,255))
camp_menu3 = fonte.render("3 - Status", 1, (255,255,255))



stat = fonte.render("===== Status =====", 1, (255,255,255))

voltar = fonte.render("0 - Voltar", 1, (255,255,255))

semGrana = fonte.render("Ta sem grana porra",1,(255,255,255))

semComida = fonte.render("Ta sem comida porra, ta tentando enganar alguem?",1,(255,255,255))


done = fonte.render("Done!",1,(255,255,255))

tanomax = fonte.render("Tá no max já!", 1, (255,255,255))

def fazTextoProx(prox): # faz o texto da distancia pra prox cidade
    text = "Distância para a próxima cidade: " + str(prox)
    return fonte.render(text, 1, (255,255,255))

def campo(jog, prox, game_over, screen, display):
    
    background = image.load("campfire1.png")
    background = transform.scale(background, (956,560))
    carro = image.load("carrofogo.png")
    carro = transform.scale(carro, (260,90))
    rect_transparente = image.load("campfire1_transparente1.png")
    rect_transparente= transform.scale(rect_transparente, (956,200)) 
    
    screen.blit(background, (0,0))
    screen.blit(carro, (190,405))
    display.update()
    
    time.wait(1000)    
    
    draw.rect(screen, (0, 0, 0), [2,3,952,200])
    draw.rect(screen, (255, 255, 255), [2,3,952,200], 5)
    screen.blit(rect_transparente, (0,0))
    screen.blit(camp, (10,20))
    screen.blit(camp_menu0, (10,50))
    screen.blit(camp_menu1, (10,80))
    screen.blit(camp_menu2, (10,110))
    screen.blit(camp_menu3, (10,140))
    proxima = fazTextoProx(prox)
    screen.blit(proxima, (600,50))
    display.update()
    
    while True: # loop camp
        for e in event.get():
            if e.type == QUIT:
                exit()
                
        if jog.temporestante <= 0:
            game_over[0] = True
            break                
        
        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
            screen.fill((0,0,0))
            display.update()
            break
    
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]: #Caçar
            jog.temporestante-=2
            jog.comida+=10
            screen.blit(done, (400,80))
            display.update()
            time.wait(1000)
            limpaCampo(screen, display)    
            screen.blit(camp, (10,20))
            screen.blit(camp_menu0, (10,50))
            screen.blit(camp_menu1, (10,80))
            screen.blit(camp_menu2, (10,110))
            screen.blit(camp_menu3, (10,140))
            proxima = fazTextoProx(prox)
            screen.blit(proxima, (600,50))
            display.update()
    
        if key.get_pressed()[K_2] or key.get_pressed()[K_KP2]: #conserto
            limpaCampo(screen, display)
            time.wait(500)
            conserto(jog,'a', screen, display)
            limpaCampo(screen, display)    
            screen.blit(camp, (10,20))
            screen.blit(camp_menu0, (10,50))
            screen.blit(camp_menu1, (10,80))
            screen.blit(camp_menu2, (10,110))
            screen.blit(camp_menu3, (10,140))
            proxima = fazTextoProx(prox)
            screen.blit(proxima, (600,50))
            display.update()
    
        if key.get_pressed()[K_3] or key.get_pressed()[K_KP3]: #STATUS
            limpaCampo(screen, display)
            stat1, stat2, stat3, stat4, stat5, stat6, stat7, stat8, stat9 = getStatus(jog)
            py = 20 # 1o y da tela 
            esp = 30 # espaco entre eles
            screen.blit(stat, (10,py))
            screen.blit(stat1, (10,py+1*esp))
            screen.blit(stat2, (10,py+2*esp))
            screen.blit(stat3, (10,py+3*esp))
            screen.blit(stat4, (10,py+4*esp))
            screen.blit(stat5, (10,py+5*esp))
            screen.blit(stat6, (250,py+1*esp))
            screen.blit(stat7, (250,py+2*esp))
            screen.blit(stat8, (250,py+3*esp))
            screen.blit(stat9, (250,py+4*esp))
            screen.blit(voltar, (600, 100))
            display.update()                
            
            while True: # loopzinho esperando o cara ler o status e decidir voltar
                for e in event.get():
                    if e.type == QUIT:
                        exit()
                        
                if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
                    limpaCampo(screen, display)
                    screen.blit(camp, (10,20))
                    screen.blit(camp_menu0, (10,50))
                    screen.blit(camp_menu1, (10,80))
                    screen.blit(camp_menu2, (10,110))
                    screen.blit(camp_menu3, (10,140))
                    proxima = fazTextoProx(prox)
                    screen.blit(proxima, (600,50))
                    display.update()
                    time.wait(500) # pra dar tempo de tirar o dedo da tecla 0
                    break
            
            display.update()
            clock.tick(ticke)
        
        
    
    display.update()
    clock.tick(ticke)
    

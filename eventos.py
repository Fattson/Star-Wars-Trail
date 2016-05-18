# -*- coding: utf-8 -*-
"""
Created on Wed May 18 08:14:42 2016

@author: GuilhermeZaborowsky
"""

from pygame import *
from random import randint

tick = 35 #fps
clock = time.Clock() # cria o reloginho

def popup(screen, display):
    rect = ((150, 150),(600, 200))
    screen.fill((255,0,0),rect) 
    display.update()
    
def limpaTelaEv(screen, display):
    screen.fill((0,0,0)) # pinta a tela de preto
    display.update()
    

def ema2(jog,screen, display):
    ema0 = image.load("evento_emma1.png")
    screen.blit(ema0,(150,150))
    display.update()
    
    ema_suc1 = image.load("resposta1_emma1.png")
    ema_fal1 = image.load("resposta2_emma1.png")
    ema_suc2 = image.load("resposta3_emma1.png")
    ema_fal2 = image.load("resposta4_emma1.png")
    
    
    
    
    while True: #loop da ema
        
        for e in event.get():
            if e.type == QUIT:
                exit()
        
        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]: #miar
            jog.comida -=10
            limpaTelaEv(screen, display)
            break
        
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]:#perseguir
            
            jog.temporestante -= 3
            s_n = randint(0,100)
            if s_n < 75:
                screen.blit(ema_suc1,(150,150))
                display.update()
                time.wait(5000)
                limpaTelaEv(screen, display)
                break
            
            else:
                jog.comida -= 10       
                screen.blit(ema_fal1, (150,1500))
                display.update()
                time.wait(5000)
                limpaTelaEv(screen, display)
                break
            
            
        if key.get_pressed()[K_2] or key.get_pressed()[K_KP2]:#jogar pedra    
            
            s_n = randint(0,100)
            if s_n < 15:
                jog.comida += 10
                screen.blit(ema_suc2,(150,150))
                display.update()
                time.wait(7000)
                limpaTelaEv(screen, display)
                break
            
            else:
                jog.comida -= 10       
                screen.blit(ema_fal2, (150,150))
                display.update()
                time.wait(5000)
                limpaTelaEv(screen, display)
                break
                
        
        #display.update()
        clock.tick(tick)


def ema(jog, screen, display):
    fontePeq = font.Font(None, 23)
    ema0 = fontePeq.render("Uma ema roubou 10 das suas comidas, e saiu correndo! O que deseja fazer?",0,(255,255,255))
    ema_menu1 = fontePeq.render("0 - Miar e ir embora (perde a comida)",0,(255,255,255))
    ema_menu2 = fontePeq.render("1 - Perseguir e recuperar (gasta tempo, aproximadamente 3 horas)",0,(255,255,255))
    ema_menu3 = fontePeq.render("2 - Tentar jogar uma pedra nela (osso,-tempo +recompensa)",0,(255,255,255))
    ema_suc1 = fontePeq.render("Parabéns, você conseguiu pegar a ema e recuperar sua comida!",0,(255,255,255))
    ema_suc1_2 = fontePeq.render("Apesar de ter demorado 3 horas...",0,(255,255,255))
    ema_fal1 = fontePeq.render("Fracassado! Nem consegue ir atrás de uma ema. Ainda levou 3 horas...",0,(255,255,255))
    ema_suc2 = fontePeq.render("Parábens, você acertou a ema e ela morreu!",0,(255,255,255))
    ema_suc2_2 = fontePeq.render("Recuperou seus 10 e guardou a carne dela (+10 de comida)!",0,(255,255,255))
    ema_fal2 = fontePeq.render("Errou feio, errou rude!! ;)",0,(255,255,255))
    popup(screen, display)
    screen.blit(ema0,(160,160))
    screen.blit(ema_menu1,(160,200))
    screen.blit(ema_menu2,(160,240))
    screen.blit(ema_menu3,(160,280))
    display.update()
    
    while True: #loop da ema
        
        for e in event.get():
            if e.type == QUIT:
                exit()
        
        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]: #miar
            jog.comida -=10
            limpaTelaEv(screen, display)
            break
        
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]:#perseguir
            popup(screen, display)
            jog.temporestante -= 3
            s_n = randint(0,100)
            if s_n < 75:
                screen.blit(ema_suc1,(160,200))
                screen.blit(ema_suc1_2,(160,220))
                display.update()
                time.wait(5000)
                limpaTelaEv(screen, display)
                break
            
            else:
                jog.comida -= 10       
                screen.blit(ema_fal1, (160,200))
                display.update()
                time.wait(5000)
                limpaTelaEv(screen, display)
                break
            
            
        if key.get_pressed()[K_2] or key.get_pressed()[K_KP2]:#jogar pedra    
            popup(screen, display)
            s_n = randint(0,100)
            if s_n < 15:
                jog.comida += 10
                screen.blit(ema_suc2,(160,200))
                screen.blit(ema_suc2_2,(160,220))
                display.update()
                time.wait(5000)
                limpaTelaEv(screen, display)
                break
            
            else:
                jog.comida -= 10       
                screen.blit(ema_fal2, (160,200))
                display.update()
                time.wait(5000)
                limpaTelaEv(screen, display)
                break
                
        
        #display.update()
        clock.tick(tick)
        
def lobo2(jog, screen, display):
    lobo0 = image.load('evento_lobo.png')
    screen.blit(lobo0,(150,150))
    display.update()
    
    lobo_suc = image.load("resposta1_lobo.png")
    lobo_fal = image.load("resposta2_lobo.png")
    lobo_medio = image.load("resposta3_lobo.png")
    
    while True: #loop do lobo
        
        for e in event.get():
            if e.type == QUIT:
                exit()
        
        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]: #fugir
            jog.comida -=10
            limpaTelaEv(screen, display)
            break
        
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]:#lutar
            s_n = randint(0,100)
            if s_n < 15:
                jog.comida += 20
                screen.blit(lobo_suc,(150,150))
                display.update()
                time.wait(8000)
                limpaTelaEv(screen, display)
                break
            elif s_n < 55: 
                screen.blit(lobo_medio,(150,150))
                display.update()
                time.wait(8000)
                limpaTelaEv(screen, display)
                break
            else:
                jog.comida -= 10
                jog.health -= 10
                screen.blit(lobo_fal,(150,150))
                display.update()
                time.wait(8000)
                limpaTelaEv(screen, display)
                break


        
        #display.update()
        clock.tick(tick)


def lobo(jog, screen, display):
    fontePeq = font.Font(None, 23)
    lobo0 = fontePeq.render("Voce foi atacado por um lobo guara! O que deseja fazer?",0,(255,255,255))
    lobo_menu0 = fontePeq.render("0 - Fugir (abandona 10 de comida pra destrair a fera)",0,(255,255,255))
    lobo_menu1 = fontePeq.render("1 - Se defender (boa sorte)",0,(255,255,255))
    lobo_suc = fontePeq.render("Parabéns, você conseguiu matar o lobo mau! E pegou a carne dele. (+20 de comida)",0,(255,255,255))
    lobo_medio = fontePeq.render("Não derrotou a fera, mas tambem nao teve que distraí-la.",0,(255,255,255))
    lobo_fail = fontePeq.render("Seu fraco! Nem consegue derrotar um lobo guara.",0,(255,255,255))
    lobo_fail2 = fontePeq.render("Ficou ferido (-10 de health) e perdeu 10 de comida...",0,(255,255,255))

    popup(screen, display)
    screen.blit(lobo0,(160,160))
    screen.blit(lobo_menu0,(160,200))
    screen.blit(lobo_menu1,(160,240))
    display.update()
    
    while True: #loop da ema
        
        for e in event.get():
            if e.type == QUIT:
                exit()
        
        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]: #fugir
            jog.comida -=10
            limpaTelaEv(screen, display)
            break
        
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]:#lutar
            popup(screen, display)
            s_n = randint(0,100)
            if s_n < 15:
                jog.comida += 20
                screen.blit(lobo_suc,(160,200))
                display.update()
                time.wait(5000)
                limpaTelaEv(screen, display)
                break
            elif s_n < 55: 
                screen.blit(lobo_medio,(160,200))
                display.update()
                time.wait(5000)
                limpaTelaEv(screen, display)
                break
            else:
                jog.comida -= 10
                jog.health -= 10
                screen.blit(lobo_fail,(160,200))
                screen.blit(lobo_fail2,(160,220))
                display.update()
                time.wait(5000)
                limpaTelaEv(screen, display)
                break


        
        #display.update()
        clock.tick(tick)

def buraco2(jog, screen, display):
    buraco0 = image.load('evento_buraco.png')
    screen.blit(buraco0,(150,150))
    display.update()
    
    jog.durab -= 100
    time.wait(5000)
    limpaTelaEv(screen, display)
        
    
def buraco(jog, screen, display):
    fontePeq = font.Font(None, 23)
    buraco0 = fontePeq.render("Oh shit! Passou rapido num buraco! (-100 durabilidade)",0,(255,255,255))
 
    popup(screen, display)
    screen.blit(buraco0,(160,200))
    display.update()
    jog.durab -= 100
    time.wait(3000)
    limpaTelaEv(screen, display)
    

def quebrou(jog, game_over, screen, display):
    fontePeq = font.Font(None, 23)
    quebrou0 = fontePeq.render("O CARRO QUEBROOOU!!!!",1,(255,255,255))
    consE_noGrana = fontePeq.render("Ta sem peças, sorry...",1,(255,255,255))
    consE = fontePeq.render("CONSERTO EMERGENCIAL DO CARRO (200 durabilidade por 500 peças)",1,(255,255,255))
    consE_menu0 = fontePeq.render("0 - Sair",1,(255,255,255))
    consE_menu1 = fontePeq.render("1 - Consertar",1,(255,255,255))
    popup(screen, display)
    screen.blit(quebrou0,(160,200))
    display.update()
    time.wait(3000)
    popup(screen, display)
    screen.blit(consE,(160,160))
    screen.blit(consE_menu0,(160,200))
    screen.blit(consE_menu1,(160,240))
    display.update()
    
    while True: #loop do conserto emergencial
        for e in event.get():
            if e.type == QUIT:
                exit()
                
        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
            limpaTelaEv(screen, display)
            game_over[0] = True
            break
    
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]: 
            if jog.pecas >= 500:
                jog.durab += 200
                jog.pecas -= 500
                time.wait(300)
                limpaTelaEv(screen, display)
                break
            else:
                popup(screen, display)
                screen.blit(consE_noGrana, (160, 200))
                display.update()
                time.wait(2000)
                popup(screen, display)
                screen.blit(consE,(160,160))
                screen.blit(consE_menu0,(160,200))
                screen.blit(consE_menu1,(160,240))
                display.update()
        
        
        #display.update()
        clock.tick(tick)

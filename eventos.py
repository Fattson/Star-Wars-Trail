# -*- coding: utf-8 -*-
"""
Created on Wed May 18 08:14:42 2016

@author: GuilhermeZaborowsky
"""

from pygame import *
from random import randint

tick = 35 #fps
clock = time.Clock() # cria o reloginho
    
def limpaTelaEv(screen, display):
    rect = ((150, 150),(600, 200))
    screen.fill((0,0,0),rect) 
    display.update()
    

def ema(jog,screen, display):
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
            
            if jog.mecatronica:
                s_n -= 15 # + 15% de chance de conseguir

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
            
            if jog.mecatronica:
                s_n -= 15# + 15% de chance de conseguir

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

def lobo(jog, screen, display):
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
            
            if jog.mecatronica:
                s_n -= 15# + 15% de chance de conseguir
                
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



def buraco(jog, screen, display):
    buraco0 = image.load('evento_buraco.png')
    screen.blit(buraco0,(150,150))
    display.update()
    
    jog.durab -= 100
    time.wait(5000)
    limpaTelaEv(screen, display)
        
    
def quebrou(jog, game_over, screen, display):
    quebrou0 = image.load('evento_carro.png')
    screen.blit(quebrou0,(150,150))
    display.update()
    time.wait(3000)
    
    consE = image.load('evento2_carro.png')
    screen.blit(consE,(150,150))
    display.update()
    
    consE_noGrana = image.load('aviso_carro.png')
    
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
               screen.blit(consE_noGrana, (150, 150))
               display.update()
               time.wait(5000)
               screen.blit(consE,(150,150))
               display.update()
        
        
       #display.update()
       clock.tick(tick)


def assalto(jog, screen, display):
    
    ass = image.load('evento_assalto.png')
    screen.blit(ass,(150,150))
    display.update()
    
    ass_suc1 = image.load('resposta1_assalto.png')
    ass_fal1 = image.load('resposta2_assalto.png')
    ass_suc2 = image.load('resposta3_assalto.png')
    ass_fal2 = image.load('resposta4_assalto.png')
    
    while True: #loop do assalto
        for e in event.get():
            if e.type == QUIT:
                exit()
        
        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]: # entrega a grana
            jog.reais -= 30
            limpaTelaEv(screen, display)
            break
        
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]: # reage
            sn = randint(0,100)
            
            if jog.mecatronica:
                sn -= 10# + 10% de chance de conseguir

            if sn < 20:
               screen.blit(ass_suc1,(150,150))
               display.update()
               time.wait(4000)
               limpaTelaEv(screen, display)
               break
            else:
                jog.reais -= 30
                jog.health -= 25
                screen.blit(ass_fal1,(150,150))
                display.update()
                time.wait(4000)
                limpaTelaEv(screen, display)
                break
                
        if key.get_pressed()[K_2] or key.get_pressed()[K_KP2]: #chama o batman
            sn = randint(0,100)
            if sn < 5:
               screen.blit(ass_suc2,(150,150))
               display.update()
               time.wait(4000)
               limpaTelaEv(screen, display)
               break
            else:
                jog.reais -= 30
                jog.health -= 25
                screen.blit(ass_fal2,(150,150))
                display.update()
                time.wait(4000)
                limpaTelaEv(screen, display)
                break
        
        
        #display.update()
        clock.tick(tick)
    
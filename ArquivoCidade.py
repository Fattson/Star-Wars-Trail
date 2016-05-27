# -*- coding: utf-8 -*-
"""
Esse arquivo contem as funcoes "cidade", "menuCidade", "mercado", "menuMercado", "limpaMercado", "fazTextoGrana"
para serem usadas no jogo Star Wars Trail
"""

from pygame import *
from ArquivoLimpa import *
from ArquivoConserto import *
from ArquivoStatus import *

fonte = font.Font(None, 30) # define uma fonte
clock = time.Clock() # cria o reloginho
ticke = 30 #fps

## DEFINICAO DE TEXTOS PARA SEREM USADOS MAIS PARA FRENTE

cid = fonte.render("CIDADE! O que deseja fazer?", 1, (255,255,255))
cid_menu0 = fonte.render("0 - Continuar a viagem", 1, (255,255,255))
cid_menu1 = fonte.render("1 - Mercado (3 horas)", 1, (255,255,255))
cid_menu2 = fonte.render("2 - SUS (2 horas +20 health)", 1, (255,255,255))
cid_menu3 = fonte.render("3 - Hospital Particular (-20 reais +20 health)", 1, (255,255,255))
cid_menu4 = fonte.render("4 - Conserto do carro", 1, (255,255,255))
cid_menu5 = fonte.render("5 - Status", 1, (255,255,255))

mer = fonte.render("===== MERCADO =====", 1, (255,255,255))
mer_menu0 = fonte.render("0 - Estou Pronto", 1, (255,255,255))
mer_menu1 = fonte.render("1 - Comprar 10 comidas (10 reais)", 1, (255,255,255))
mer_menu2 = fonte.render("2 - Vender 10 comidas (+10 reais)", 1, (255,255,255))
mer_menu3 = fonte.render("3 - Comprar 100 pecas (10 reais)", 1, (255,255,255))
mer_menu4 = fonte.render("4 - Comprar 100 gasosa (10 reais)", 1, (255,255,255))
mer_menu5 = fonte.render("5 - Status", 1, (255,255,255))


merC_menu1 = fonte.render("1 - Comprar 10 comidas (5 reais)", 1, (255,255,255))
merC_menu2 = fonte.render("2 - Vender 10 comidas (+5 reais)", 1, (255,255,255))
merC_menu3 = fonte.render("3 - Comprar 100 pecas (5 reais)", 1, (255,255,255))
merC_menu4 = fonte.render("4 - Comprar 100 gasosa (5 reais)", 1, (255,255,255))

stat = fonte.render("===== Status =====", 1, (255,255,255))

voltar = fonte.render("0 - Voltar", 1, (255,255,255))

semGrana = fonte.render("Ta sem grana porra",1,(255,255,255))

semComida = fonte.render("Ta sem comida porra, ta tentando enganar alguem?",1,(255,255,255))


done = fonte.render("Done!",1,(255,255,255))

tanomax = fonte.render("Tá no max já!", 1, (255,255,255))


def fazTextoProx(prox): # faz o texto da distancia pra prox cidade
    text = "Distância para a próxima cidade: " + str(prox)
    return fonte.render(text, 1, (255,255,255))

def fazTextoGrana(jog): # faz um texto de tela mostrando o dinheiro do jogador
    grana = "Grana: " + str(jog.reais)
    return fonte.render(grana,1,(255,255,255))

def menuMercado(jog, screen, display): # imprime na tela o menu do mercado
    #screen.blit(mer, (10,10))
    screen.blit(mer_menu0, (10,20))
    if jog.comp:
        screen.blit(merC_menu1, (10,50))
        screen.blit(merC_menu2, (10,80))
        screen.blit(merC_menu3, (10,110))
        screen.blit(merC_menu4, (10,140))
    else:
        screen.blit(mer_menu1, (10,50))
        screen.blit(mer_menu2, (10,80))
        screen.blit(mer_menu3, (10,110))
        screen.blit(mer_menu4, (10,140))
    screen.blit(mer_menu5, (10,170))
    grana = fazTextoGrana(jog)
    screen.blit(grana, (500,20))
    
    
def limpaMercado(screen, display): # apaga o menu do mercado
    background = image.load("market.png")
    background = transform.scale(background, (956,560))
    rect = image.load("market_preto.png")
    rect = transform.scale(rect, (956,200))
    rect_transparente = image.load("market_transp.png")
    rect_transparente = transform.scale(rect_transparente, (956,200))
    
    screen.blit(background, (0,0))
    draw.rect(screen, (0, 0, 0), [2,2,952,200])
    screen.blit(rect,(0, 0))
    screen.blit(rect_transparente,(0, 0))
    draw.rect(screen, (255, 255, 255), [2,2,952,200], 5)
    display.update()
    
def mercado(jog, screen, display): # o mercado
    background = image.load("market.png")
    background = transform.scale(background, (956,560))
    rect = image.load("market_preto.png")
    rect = transform.scale(rect, (956,200))
    
    rect_transparente = image.load("market_transp.png")
    rect_transparente = transform.scale(rect_transparente, (956,200))
    
    screen.blit(background, (0,0))
    display.update()

    time.wait(1000)
    
    draw.rect(screen, (0, 0, 0), [2,2,952,200])
    screen.blit(rect,(0, 0))
    screen.blit(rect_transparente,(0, 0))
    draw.rect(screen, (255, 255, 255), [2,2,952,200], 5)
    menuMercado(jog, screen, display)
    display.update()

    while True: #loop mercado 

        for e in event.get():
            if e.type == QUIT:
                exit()

        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
            time.wait(500)            
            screen.fill((0,0,0))
            display.update()            
            break

        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]: # comprar comida
            if jog.comp:
                if jog.reais >= 5:
                    jog.reais-=5
                    jog.comida+=10
                    screen.blit(done, (400,50))
                    display.update()
                    time.wait(1000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                
                else:
                    limpaMercado(screen, display)
                    screen.blit(semGrana, (250,100))
                    display.update()
                    time.wait(2000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
            else:
                if jog.reais >= 10:
                    jog.reais-=10
                    jog.comida+=10
                    screen.blit(done, (400,50))
                    display.update()
                    time.wait(1000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                
                else:
                    limpaMercado(screen, display)
                    screen.blit(semGrana, (250,100))
                    display.update()
                    time.wait(2000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                
                
        if key.get_pressed()[K_2] or key.get_pressed()[K_KP2]: # vender comida
            if jog.comp:
                if jog.comida >= 10:
                    jog.comida-=10
                    jog.reais+=5
                    screen.blit(done, (400,80))
                    display.update()
                    time.wait(1000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                else:
                    limpaMercado(screen, display)
                    screen.blit(semComida, (250,100))
                    display.update()
                    time.wait(3000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
            else:
                if jog.comida >= 10:
                    jog.comida-=10
                    jog.reais+=10
                    screen.blit(done, (400,80))
                    display.update()
                    time.wait(1000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                else:
                    limpaMercado(screen, display)
                    screen.blit(semComida, (250,100))
                    display.update()
                    time.wait(3000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
            
        
        if key.get_pressed()[K_3] or key.get_pressed()[K_KP3]: # comprar peças
            if jog.comp:
                if jog.reais >= 5:
                    jog.reais-=5
                    jog.pecas+=100
                    screen.blit(done, (400,110))
                    display.update()
                    time.wait(1000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                else:
                    limpaMercado(screen, display)
                    screen.blit(semGrana, (250,100))
                    display.update()
                    time.wait(2000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                    
            else:
                if jog.reais >= 10:
                    jog.reais-=10
                    jog.pecas+=100
                    screen.blit(done, (400,110))
                    display.update()
                    time.wait(1000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                else:
                    limpaMercado(screen, display)
                    screen.blit(semGrana, (250,100))
                    display.update()
                    time.wait(2000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                    
        if key.get_pressed()[K_4] or key.get_pressed()[K_KP4]: # vender peças
            if jog.comp:
                if jog.reais >= 5:
                    jog.reais-=5
                    jog.gas+=100
                    screen.blit(done, (400,140))
                    display.update()
                    time.wait(1000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                else:
                    limpaMercado(screen, display)
                    screen.blit(semGrana, (250,100))
                    display.update()
                    time.wait(2000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                    
            else:
                if jog.reais >= 10:
                    jog.reais-=10
                    jog.gas+=100
                    screen.blit(done, (400,140))
                    display.update()
                    time.wait(1000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                else:
                    limpaMercado(screen, display)
                    screen.blit(semGrana, (250,100))
                    display.update()
                    time.wait(2000)
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                    
    
        if key.get_pressed()[K_5] or key.get_pressed()[K_KP5]: # STATUS
            limpaMercado(screen, display)
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
                    limpaMercado(screen, display)
                    menuMercado(jog, screen, display)
                    time.wait(500) # pra dar tempo de tirar o dedo da tecla 0
                    break
                
                display.update()
                clock.tick(ticke)
            
        
        
        
        display.update()
        clock.tick(ticke)

def menuCidade(prox, screen, display):    
    #screen.blit(cid, (100,100))
    screen.blit(cid_menu0, (10,20))
    screen.blit(cid_menu1, (10,50))
    screen.blit(cid_menu2, (10,80))
    screen.blit(cid_menu3, (10,110))
    screen.blit(cid_menu4, (10,140))
    screen.blit(cid_menu5, (10,170))
    proxima = fazTextoProx(prox)
    screen.blit(proxima, (400,20))
    display.update()
    

def cidade(jog, prox, game_over, screen, display): # CIDADE

    background = image.load("cidade2.jpg")
    background = transform.scale(background, (956,560))
    
    
    rect_transparente = image.load("cidade2_transparente.jpg")
    rect_transparente = transform.scale(rect_transparente, (956,200))
    
    screen.blit(background, (0,0))
    display.update()
    
    time.wait(1000)
    draw.rect(screen, (0, 0, 0), [2,2,952,200])
    screen.blit(rect_transparente,(0, 0))
    draw.rect(screen, (255, 255, 255), [2,2,952,200], 5)
    menuCidade(prox, screen, display)
    display.update()
    
    while True: # loop cidade
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
    
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]: #MERCADO
            jog.temporestante -= 3
            limpaCidade(screen, display)            
            time.wait(500) # para a opcao 1 nao valer dentro do mercado
            mercado(jog, screen, display)
            limpaCidade(screen, display)
            menuCidade(prox, screen, display)
    
        if key.get_pressed()[K_2] or key.get_pressed()[K_KP2]:#SUS
            if jog.health<100:
                jog.temporestante-=2
                jog.health+=20
                screen.blit(done, (300,80))
                display.update()
                time.wait(1000)
                limpaCidade(screen, display)
                menuCidade(prox, screen, display)
            else:
                screen.blit(tanomax, (300,80))
                display.update()
                time.wait(1000)
                limpaCidade(screen, display)
                menuCidade(prox, screen, display)
            
            if jog.health<100:
                jog.health = 100
                

        if key.get_pressed()[K_3] or key.get_pressed()[K_KP3]:#HOSP
            if jog.health<100:
                jog.reais-=20
                jog.health+=20
                screen.blit(done, (450,110))
                display.update()
                time.wait(1000)
                limpaCidade(screen, display)
                menuCidade(prox, screen, display)
            else:
                screen.blit(tanomax, (450,110))
                display.update()
                time.wait(1000)
                limpaCidade(screen, display)
                menuCidade(prox, screen, display)
            
            if jog.health<100:
                jog.health = 100
                
    
        if key.get_pressed()[K_4] or key.get_pressed()[K_KP4]:#CONSERTO
            screen.blit(background, (0,0))            
            time.wait(500)
            conserto(jog,'c', screen, display)
            limpaCidade(screen, display)
            menuCidade(prox, screen, display)
    
        if key.get_pressed()[K_5] or key.get_pressed()[K_KP5]:#STATUS
            limpaCidade(screen, display)
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
                    time.wait(500) # pra dar tempo de tirar o dedo da tecla 0
                    limpaCidade(screen, display)
                    menuCidade(prox, screen, display)
                    display.update()
                    break
            
            display.update()
            clock.tick(ticke)
        
           
    
    display.update()
    clock.tick(ticke)
    


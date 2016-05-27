# -*- coding: utf-8 -*-
"""
Esse arquivo contem as funcoes "conserto", "limpaConserto" e "menuConserto0",
para serem usadas no jogo Star Wars Trail.
 
"""

from pygame import *
from ArquivoLimpa import *


clock = time.Clock() # cria o reloginho
ticke = 35 #fps
fonte = font.Font(None, 30) # define uma fonte

# variaveis com texto que podem ser colocados na tela

cons = fonte.render("CONSERTO DO CARRO (durabilidade: >600=200pecas >300=300pecas else 500 pecas)",1,(255,255,255))
cons_menu0 = fonte.render("0 - Sair",1,(255,255,255))
cons_menu1 = fonte.render("1 - Consertar (2 horas)",1,(255,255,255))
consM = fonte.render("CONSERTO DO CARRO (durabilidade: >600=100pecas >300=150pecas else 250 pecas)",1,(255,255,255))
semPecas = fonte.render("Ta sem pecas suficientes, vai comprar!",1,(255,255,255))
done = fonte.render("Done!",1,(255,255,255))
tanomax = fonte.render("Tá no max já!", 1, (255,255,255))



def limpaConserto(onde, screen, display): # apaga o menu do conserto
    if onde == 'c':
        limpaCidade(screen, display)
    else:
        limpaCampo(screen, display)
        
        
def menuConserto(jog,onde, screen, display):
    limpaConserto(onde, screen, display)
    if jog.mecanica:
        screen.blit(consM, (100,50))
    else:
        screen.blit(cons, (100,50))
    screen.blit(cons_menu0, (100,100))
    screen.blit(cons_menu1, (100,150))
    textp="Peças: "+str(jog.pecas)
    pecas = fonte.render(textp,1,(255,255,255))
    textd="Durabilidade: "+str(jog.durab)
    durab = fonte.render(textd,1,(255,255,255))
    screen.blit(pecas, (500,150))
    screen.blit(durab, (700,150))
    display.update()

def conserto(jog,onde, screen, display):
    
    
    menuConserto(jog,onde, screen, display)
    
    while True:
        for e in event.get():
            if e.type == QUIT:
                exit()
        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
            #limpaTela()
            time.wait(500)
            break
    
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]: 
            
            
            if jog.durab == 1000:
                screen.blit(tanomax, (350,150))
                display.update()
                time.wait(1000)
                limpaConserto(onde, screen, display)
                menuConserto(jog,onde, screen, display)
            else:
                jog.temporestante -= 2
                if jog.durab > 600:
                    if not jog.mecanica: 
                        if jog.pecas >= 200:
                            jog.durab += 200
                            jog.pecas -= 200
                            if jog.durab > 1000: # nao deixa passar do max
                                jog.durab = 1000
                            screen.blit(done, (400,150))
                            display.update()
                            time.wait(1000)
                            limpaConserto(onde, screen, display)
                            menuConserto(jog,onde, screen, display)
                        else:
                            limpaConserto(onde, screen, display)
                            screen.blit(semPecas, (250,150))
                            display.update()
                            time.wait(2000)
                            limpaConserto(onde, screen, display)
                            menuConserto(jog,onde, screen, display)
                    else:
                        if jog.pecas >= 100:
                            jog.durab += 200
                            jog.pecas -= 100
                            if jog.durab > 1000: # nao deixa passar do max
                                jog.durab = 1000
                            screen.blit(done, (400,150))
                            display.update()
                            time.wait(1000)
                            limpaConserto(onde, screen, display)
                            menuConserto(jog,onde, screen, display)
                        else:
                            limpaConserto(onde, screen, display)
                            screen.blit(semPecas, (250,150))
                            display.update()
                            time.wait(2000)
                            limpaConserto(onde, screen, display)
                            menuConserto(jog,onde, screen, display)
                elif jog.durab > 300:
                    if not jog.mecanica:
                        if jog.pecas >= 300:
                            jog.durab += 200
                            jog.pecas -= 300
                            if jog.durab > 1000: # nao deixa passar do max
                                jog.durab = 1000
                            screen.blit(done, (400,150))
                            display.update()
                            time.wait(1000)
                            limpaConserto(onde, screen, display)
                            menuConserto(jog,onde, screen, display)
                        else:
                            limpaConserto(onde, screen, display)
                            screen.blit(semPecas, (250,150))
                            display.update()
                            time.wait(2000)
                            limpaConserto(onde, screen, display)
                            menuConserto(jog,onde, screen, display)
                    else:
                        if jog.pecas >= 150:
                            jog.durab += 200
                            jog.pecas -= 150
                            if jog.durab > 1000: # nao deixa passar do max
                                jog.durab = 1000
                            screen.blit(done, (400,150))
                            display.update()
                            time.wait(1000)
                            limpaConserto(onde, screen, display)
                            menuConserto(jog,onde, screen, display)
                        else:
                            limpaConserto(onde, screen, display)
                            screen.blit(semPecas, (250,150))
                            display.update()
                            time.wait(2000)
                            limpaConserto(onde, screen, display)
                            menuConserto(jog,onde, screen, display)
                else:
                    if not jog.mecanica:
                        if jog.pecas >= 500:
                            jog.durab += 200
                            jog.pecas -= 500
                            if jog.durab > 1000: # nao deixa passar do max
                                jog.durab = 1000
                            screen.blit(done, (400,150))
                            display.update()
                            time.wait(1000)
                            limpaConserto(onde, screen, display)
                            menuConserto(jog,onde, screen, display)
                        else:
                            limpaConserto(onde, screen, display)
                            screen.blit(semPecas, (100,150))
                            display.update()
                            time.wait(2000)
                            limpaConserto(onde, screen, display)
                            menuConserto(jog,onde, screen, display)
                    else:
                        if jog.pecas >= 250:
                            jog.durab += 200
                            jog.pecas -= 250
                            if jog.durab > 1000: # nao deixa passar do max
                                jog.durab = 1000
                            screen.blit(done, (400,150))
                            display.update()
                            time.wait(1000)
                            limpaConserto(onde, screen, display)
                            menuConserto(jog,onde, screen, display)
                        else:
                            limpaConserto(onde, screen, display)
                            screen.blit(semPecas, (100,150))
                            display.update()
                            time.wait(2000)
                            limpaConserto(onde, screen, display)
                            menuConserto(jog,onde, screen, display)
            
            
            
            
            
        
        display.update()
        clock.tick(ticke)

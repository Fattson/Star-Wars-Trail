from pygame import *
#import loopJogo.py as lj
import SwTrail as sw
import Go
from random import randint

jog = sw.Jogo()



# 3000 km  5 cidades 5 camps

CC = []
ci = 5 # 1
ca = 5 # 2
p = 50
tick = 35 #fps


for i in range(ci+ca): # monta o vetor CC
    if ci>0 and ca>0:
        x = randint(1,100)

        if x > p:
            CC.append(1)
            ci -= 1
            p += 15
        else:
            CC.append(2)
            ca -= 1
            p -= 15
            
    elif ci>0:
        CC.append(1)
        ci -= 1
    else:
        CC.append(2)      
        ca -= 1
        

def dist_proximaCidade(CCrest): # Recebe o CC restante e retorna a distancia (em rodadas) para a prox cidade
    
    d = -1     
    
    for j in range(1,len(CCrest)):
        if CCrest[j] == 1:
            d = j
            break
    if len(CCrest) == 2 and CCrest[1] == 2:
        d = 2
    if len(CCrest) == 1:
        d = 1   
    return (d)

init()

screen = display.set_mode((956,560), 0, 32) # cria a janela

x,y = (100,100)
#bg = image.load("bg.png").convert() # define uma imagem bg
fonte = font.Font(None, 30) # define uma fonte
fontePeq = font.Font(None, 23)

screen.fill((0,0,0)) # pinta a tela de preto
clock = time.Clock() # cria o reloginho

#screen.blit(bg, (0,0))

#jog = sw.Jogo()

cid = fonte.render("CIDADE! O que deseja fazer?", 1, (255,255,255))
cid_menu0 = fonte.render("0 - Continuar a viagem", 1, (255,255,255))
cid_menu1 = fonte.render("1 - Mercado", 1, (255,255,255))
cid_menu2 = fonte.render("2 - SUS", 1, (255,255,255))
cid_menu3 = fonte.render("3 - Hospital Particular", 1, (255,255,255))
cid_menu4 = fonte.render("4 - Conserto do carro", 1, (255,255,255))
cid_menu5 = fonte.render("5 - Status", 1, (255,255,255))

mer = fonte.render("===== MERCADO =====", 1, (255,255,255))
mer_menu0 = fonte.render("0 - Estou Pronto", 1, (255,255,255))
mer_menu1 = fonte.render("1 - Comprar 10 comidas (10 reais)", 1, (255,255,255))
mer_menu2 = fonte.render("2 - Vender 10 comidas (+10 reais)", 1, (255,255,255))
mer_menu3 = fonte.render("3 - Comprar 100 pecas (10 reais)", 1, (255,255,255))
mer_menu4 = fonte.render("4 - Comprar 100 gasosa (10 reais)", 1, (255,255,255))
mer_menu5 = fonte.render("5 - Status", 1, (255,255,255))

camp = fonte.render("ACAMPAMENTO! O que deseja fazer?",1,(255,255,255))
camp_menu0 = fonte.render("0 - Continuar a viagem", 1, (255,255,255))
camp_menu1 = fonte.render("1 - Caçar",1,(255,255,255))
camp_menu2 = fonte.render("2 - Conserto do carro", 1, (255,255,255))
camp_menu3 = fonte.render("3 - Status", 1, (255,255,255))

cons = fonte.render("CONSERTO DO CARRO (durabilidade: >600=200pecas >300=300pecas else 500 pecas)",1,(255,255,255))
cons_menu0 = fonte.render("0 - Sair",1,(255,255,255))
cons_menu1 = fonte.render("1 - Consertar",1,(255,255,255))

stat = fonte.render("===== Status =====", 1, (255,255,255))

voltar = fonte.render("0 - Voltar", 1, (255,255,255))

semGrana = fonte.render("Ta sem grana porra",1,(255,255,255))

semComida = fonte.render("Ta sem comida porra, ta tentando enganar alguem?",1,(255,255,255))

semPecas = fonte.render("Ta sem pecas suficientes, vai comprar!",1,(255,255,255))

done = fonte.render("Done!",1,(255,255,255))

tanomax = fonte.render("Tá no max já!", 1, (255,255,255))

go = fonte.render("TELA GO",1,(255,255,255))

msg_gameover = fonte.render("GAME OVER",1,(255,255,255))
msg_chegou = fonte.render("CHEGOOOOOU!!!",1,(255,255,255))

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

lobo0 = fontePeq.render("Voce foi atacado por um lobo guara! O que deseja fazer?",0,(255,255,255))
lobo_menu0 = fontePeq.render("0 - Fugir (abandona 10 de comida pra destrair a fera)",0,(255,255,255))
lobo_menu1 = fontePeq.render("1 - Se defender (boa sorte)",0,(255,255,255))
lobo_suc = fontePeq.render("Parabéns, você conseguiu matar o lobo mau! E pegou a carne dele. (+20 de comida)",0,(255,255,255))
lobo_medio = fontePeq.render("Não derrotou a fera, mas tambem nao teve que distraí-la.",0,(255,255,255))
lobo_fail = fontePeq.render("Seu fraco! Nem consegue derrotar um lobo guara.",0,(255,255,255))
lobo_fail2 = fontePeq.render("Ficou ferido (-10 de health) e perdeu 10 de comida...",0,(255,255,255))

buraco0 = fontePeq.render("Oh shit! Passou rapido num buraco! (-100 durabilidade)",0,(255,255,255))
 

def getTempoDist(jog): # retorna o tempo e a distancia restantes (em forma de caixa de texto pygame)
    dist = "Distancia " + str(jog.distancia) + "km/3000km"
    time = "Tempo restante: " + str(jog.temporestante) + " horas"
    textD = fonte.render(dist, 1, (255,255,255))
    textT = fonte.render(time, 1, (255,255,255))
    return textD,textT

def getStatus(jog): # faz as frases do STATUS
    stat1 = "Gasolina: " + str(jog.gas)
    stat2 = "Pecas: " + str(jog.pecas)
    stat3 = "Durabilidade: " + str(jog.durab)
    stat4 = "Comida: " + str(jog.comida)
    stat5 = "Health: " + str(jog.health)
    stat6 = "Dinheiro: " + str(jog.reais)
    stat7 = "Amigos vivos: " + str(jog.numero_jogadores-1)
    stat8 = "Distancia restante: " + str(jog.distancia)
    stat9 = "Tempo restante: " + str(jog.temporestante)

    stat_gas = fonte.render(stat1, 1, (255,255,255))
    stat_pecas = fonte.render(stat2, 1, (255,255,255))
    stat_dur = fonte.render(stat3, 1, (255,255,255))
    stat_com = fonte.render(stat4, 1, (255,255,255))
    stat_health = fonte.render(stat5, 1, (255,255,255))
    stat_din = fonte.render(stat6, 1, (255,255,255))
    stat_amig = fonte.render(stat7, 1, (255,255,255))
    stat_dist = fonte.render(stat8, 1, (255,255,255))
    stat_temp = fonte.render(stat9, 1, (255,255,255))
    
    return stat_gas, stat_pecas, stat_dur, stat_com, stat_health, stat_din, stat_amig, stat_dist, stat_temp

msg_comeco1 = fonte.render("vc e 3 amigos tao no piaui e blablabla roubaram um carro blablabla vai", 1, (255,255,255))
msg_comeco2 = fonte.render("a viagem comeca num mercado, chequem o STATUS e comprem o necessario", 1, (255,255,255))


def limpaTela():
    screen.fill((0,0,0)) # pinta a tela de preto
    display.update()
    




def menuMercado(jog): # imprime na tela o menu do mercado
    screen.blit(mer, (100,100))
    screen.blit(mer_menu0, (100,150))
    screen.blit(mer_menu1, (100,200))
    screen.blit(mer_menu2, (100,250))
    screen.blit(mer_menu3, (100,300))
    screen.blit(mer_menu4, (100,350))
    screen.blit(mer_menu5, (100,400))
    grana = fazTextoGrana(jog)
    screen.blit(grana, (500,100))
    
def fazTextoProx(prox): # faz o texto da distancia pra prox cidade
    text = "Distância para a próxima cidade: " + str(prox)
    return fonte.render(text, 1, (255,255,255))
    
def fazTextoGrana(jog):
    grana = "Grana: " + str(jog.reais)
    return fonte.render(grana,1,(255,255,255))
    
def mercado(jog):
    menuMercado(jog)

    while True: #loop mercado 

        for e in event.get():
            if e.type == QUIT:
                exit()

        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
            limpaTela()
            time.wait(500)
            break

        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]:
            if jog.reais >= 10:
                jog.reais-=10
                jog.comida+=10
                screen.blit(done, (500,200))
                display.update()
                time.wait(1000)
                limpaTela()
                menuMercado(jog)
            
            else:
                limpaTela()
                screen.blit(semGrana, (250,200))
                display.update()
                time.wait(2000)
                limpaTela()
                menuMercado(jog)
                
                
        if key.get_pressed()[K_2] or key.get_pressed()[K_KP2]:
            if jog.comida >= 10:
                jog.comida-=10
                jog.reais+=10
                screen.blit(done, (500,250))
                display.update()
                time.wait(1000)
                limpaTela()
                menuMercado(jog)
            else:
                limpaTela()
                screen.blit(semComida, (250,200))
                display.update()
                time.wait(3000)
                limpaTela()
                menuMercado(jog)
        
        
        if key.get_pressed()[K_3] or key.get_pressed()[K_KP3]:
            if jog.reais >= 10:
                jog.reais-=10
                jog.pecas+=100
                screen.blit(done, (500,300))
                display.update()
                time.wait(1000)
                limpaTela()
                menuMercado(jog)
            else:
                limpaTela()
                screen.blit(semGrana, (250,200))
                display.update()
                time.wait(2000)
                limpaTela()
                menuMercado(jog)
                
        if key.get_pressed()[K_4] or key.get_pressed()[K_KP4]:
            if jog.reais >= 10:
                jog.reais-=10
                jog.gas+=100
                screen.blit(done, (500,350))
                display.update()
                time.wait(1000)
                limpaTela()
                menuMercado(jog)
            else:
                limpaTela()
                screen.blit(semGrana, (250,200))
                display.update()
                time.wait(2000)
                limpaTela()
                menuMercado(jog)
                
    
        if key.get_pressed()[K_5] or key.get_pressed()[K_KP5]:
            limpaTela()
            stat1, stat2, stat3, stat4, stat5, stat6, stat7, stat8, stat9 = getStatus(jog)
            py = 100 # 1o y da tela 
            esp = 35 # espaco entre eles
            screen.blit(stat, (100,py))
            screen.blit(stat1, (100,py+1*esp))
            screen.blit(stat2, (100,py+2*esp))
            screen.blit(stat3, (100,py+3*esp))
            screen.blit(stat4, (100,py+4*esp))
            screen.blit(stat5, (100,py+5*esp))
            screen.blit(stat6, (100,py+6*esp))
            screen.blit(stat7, (100,py+7*esp))
            screen.blit(stat8, (100,py+8*esp))
            screen.blit(stat9, (100,py+9*esp))
            screen.blit(voltar, (100, 500))
            display.update()
            
            while True: # loopzinho esperando o cara ler o status e decidir voltar
                for e in event.get():
                    if e.type == QUIT:
                        exit()
            
                if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
                    limpaTela()
                    menuMercado(jog)
                    time.wait(500) # pra dar tempo de tirar o dedo da tecla 0
                    break
                
                display.update()
                clock.tick(tick)
            
        
        
        
        display.update()
        clock.tick(tick)

def menuCidade(prox):
    limpaTela()    
    screen.blit(cid, (100,100))
    screen.blit(cid_menu0, (100,150))
    screen.blit(cid_menu1, (100,200))
    screen.blit(cid_menu2, (100,250))
    screen.blit(cid_menu3, (100,300))
    screen.blit(cid_menu4, (100,350))
    screen.blit(cid_menu5, (100,400))
    proxima = fazTextoProx(prox)
    screen.blit(proxima, (100,500))
    display.update()
    

    
def menuConserto(jog):
    limpaTela()    
    screen.blit(cons, (100,100))
    screen.blit(cons_menu0, (100,150))
    screen.blit(cons_menu1, (100,200))
    textp="Peças: "+str(jog.pecas)
    pecas = fonte.render(textp,1,(255,255,255))
    textd="Durabilidade: "+str(jog.durab)
    durab = fonte.render(textd,1,(255,255,255))
    screen.blit(pecas, (500,200))
    screen.blit(durab, (700,200))
    display.update()

def conserto(jog):
    menuConserto(jog)
    
    while True:
        for e in event.get():
            if e.type == QUIT:
                exit()
        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
            limpaTela()
            time.wait(500)
            break
    
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]: 
            
            if jog.durab == 1000:
                screen.blit(tanomax, (300,200))
                display.update()
                time.wait(1000)
                limpaTela()
                menuConserto(jog)
            else:
                if jog.durab > 600:
                    if jog.pecas >= 200:
                        jog.durab += 200
                        jog.pecas -= 200
                        if jog.durab > 1000: # nao deixa passar do max
                            jog.durab = 1000
                        screen.blit(done, (300,200))
                        display.update()
                        time.wait(1000)
                        limpaTela()
                        menuConserto(jog)
                    else:
                        limpaTela()
                        screen.blit(semPecas, (250,200))
                        display.update()
                        time.wait(2000)
                        limpaTela()
                        menuConserto(jog)
                elif jog.durab > 300:
                    if jog.pecas >= 300:
                        jog.durab += 200
                        jog.pecas -= 300
                        if jog.durab > 1000: # nao deixa passar do max
                            jog.durab = 1000
                        screen.blit(done, (300,200))
                        display.update()
                        time.wait(1000)
                        limpaTela()
                        menuConserto(jog)
                    else:
                        limpaTela()
                        screen.blit(semPecas, (250,200))
                        display.update()
                        time.wait(2000)
                        limpaTela()
                        menuConserto(jog)
                else:
                    if jog.pecas >= 500:
                        jog.durab += 200
                        jog.pecas -= 500
                        if jog.durab > 1000: # nao deixa passar do max
                            jog.durab = 1000
                        screen.blit(done, (300,200))
                        display.update()
                        time.wait(1000)
                        limpaTela()
                        menuConserto(jog)
                    else:
                        limpaTela()
                        screen.blit(semPecas, (250,200))
                        display.update()
                        time.wait(2000)
                        limpaTela()
                        menuConserto(jog)
            
            
            
            
            
        
        display.update()
        clock.tick(tick)
    
    
def cidade(jog, prox, game_over): # CIDADE
    
    menuCidade(prox)
    
    while True: # loop cidade
        for e in event.get():
            if e.type == QUIT:
                exit()
                
        if jog.temporestante <= 0:
            game_over[0] = True
            break       
    
        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
            limpaTela()
            break
    
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]: #MERCADO
            limpaTela()            
            time.wait(500) # para a opcao 1 nao valer dentro do mercado
            mercado(jog)
            menuCidade(prox)
    
        if key.get_pressed()[K_2] or key.get_pressed()[K_KP2]:#SUS
            if jog.health<100:
                jog.temporestante-=2
                jog.health+=20
                screen.blit(done, (500,250))
                display.update()
                time.wait(1000)
                limpaTela()
                menuCidade(prox)
            else:
                screen.blit(tanomax, (500,250))
                display.update()
                time.wait(1000)
                limpaTela()
                menuCidade(prox)
            
            if jog.health<100:
                jog.health = 100
                

        if key.get_pressed()[K_3] or key.get_pressed()[K_KP3]:#HOSP
            if jog.health<100:
                jog.reais-=20
                jog.health+=20
                screen.blit(done, (500,300))
                display.update()
                time.wait(1000)
                limpaTela()
                menuCidade(prox)
            else:
                screen.blit(tanomax, (500,300))
                display.update()
                time.wait(1000)
                limpaTela()
                menuCidade(prox)
            
            if jog.health<100:
                jog.health = 100
                
    
        if key.get_pressed()[K_4] or key.get_pressed()[K_KP4]:#CONSERTO
            limpaTela()            
            time.wait(500)
            conserto(jog)
            menuCidade(prox)
    
        if key.get_pressed()[K_5] or key.get_pressed()[K_KP5]:#STATUS
            limpaTela()
            stat1, stat2, stat3, stat4, stat5, stat6, stat7, stat8, stat9 = getStatus(jog)
            py = 100 # 1o y da tela 
            esp = 35 # espaco entre eles
            screen.blit(stat, (100,py))
            screen.blit(stat1, (100,py+1*esp))
            screen.blit(stat2, (100,py+2*esp))
            screen.blit(stat3, (100,py+3*esp))
            screen.blit(stat4, (100,py+4*esp))
            screen.blit(stat5, (100,py+5*esp))
            screen.blit(stat6, (100,py+6*esp))
            screen.blit(stat7, (100,py+7*esp))
            screen.blit(stat8, (100,py+8*esp))
            screen.blit(stat9, (100,py+9*esp))
            screen.blit(voltar, (100, 500))
            display.update()            
            
            while True: # loopzinho esperando o cara ler o status e decidir voltar
                for e in event.get():
                    if e.type == QUIT:
                        exit()
                        
                if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
                    limpaTela()
                    screen.blit(cid, (100,100))
                    screen.blit(cid_menu0, (100,150))
                    screen.blit(cid_menu1, (100,200))
                    screen.blit(cid_menu2, (100,250))
                    screen.blit(cid_menu3, (100,300))
                    screen.blit(cid_menu4, (100,350))
                    screen.blit(cid_menu5, (100,400))
                    proxima = fazTextoProx(prox)
                    screen.blit(proxima, (100,500))
                    display.update()
                    time.wait(500) # pra dar tempo de tirar o dedo da tecla 0
                    break
            
            display.update()
            clock.tick(tick)
        
           
    
    display.update()
    clock.tick(tick)
    

def campo(jog, prox, game_over):
    limpaTela()    
    screen.blit(camp, (100,100))
    screen.blit(camp_menu0, (100,150))
    screen.blit(camp_menu1, (100,200))
    screen.blit(camp_menu2, (100,250))
    screen.blit(camp_menu3, (100,300))
    proxima = fazTextoProx(prox)
    screen.blit(proxima, (100,500))
    display.update()
    
    while True: # loop camp
        for e in event.get():
            if e.type == QUIT:
                exit()
                
        if jog.temporestante <= 0:
            game_over[0] = True
            break                
        
        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
            limpaTela()
            break
    
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]: #Caçar
            jog.temporestante-=2
            jog.comida+=10
            screen.blit(done, (500,200))
            display.update()
            time.wait(1000)
            limpaTela()    
            screen.blit(camp, (100,100))
            screen.blit(camp_menu0, (100,150))
            screen.blit(camp_menu1, (100,200))
            screen.blit(camp_menu2, (100,250))
            screen.blit(camp_menu3, (100,300))
            proxima = fazTextoProx(prox)
            screen.blit(proxima, (100,500))
            display.update()
    
        if key.get_pressed()[K_2] or key.get_pressed()[K_KP2]: #conserto
            limpaTela()
            time.wait(500)
            conserto(jog)
            limpaTela()    
            screen.blit(camp, (100,100))
            screen.blit(camp_menu0, (100,150))
            screen.blit(camp_menu1, (100,200))
            screen.blit(camp_menu2, (100,250))
            screen.blit(camp_menu3, (100,300))
            proxima = fazTextoProx(prox)
            screen.blit(proxima, (100,500))
            display.update()
    
        if key.get_pressed()[K_3] or key.get_pressed()[K_KP3]: #STATUS
            limpaTela()
            stat1, stat2, stat3, stat4, stat5, stat6, stat7, stat8, stat9 = getStatus(jog)
            py = 100 # 1o y da tela 
            esp = 35 # espaco entre eles
            screen.blit(stat, (100,py))
            screen.blit(stat1, (100,py+1*esp))
            screen.blit(stat2, (100,py+2*esp))
            screen.blit(stat3, (100,py+3*esp))
            screen.blit(stat4, (100,py+4*esp))
            screen.blit(stat5, (100,py+5*esp))
            screen.blit(stat6, (100,py+6*esp))
            screen.blit(stat7, (100,py+7*esp))
            screen.blit(stat8, (100,py+8*esp))
            screen.blit(stat9, (100,py+9*esp))
            screen.blit(voltar, (100, 500))
            display.update()            
            
            while True: # loopzinho esperando o cara ler o status e decidir voltar
                for e in event.get():
                    if e.type == QUIT:
                        exit()
                        
                if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
                    limpaTela()
                    screen.blit(camp, (100,100))
                    screen.blit(camp_menu0, (100,150))
                    screen.blit(camp_menu1, (100,200))
                    screen.blit(camp_menu2, (100,250))
                    screen.blit(camp_menu3, (100,300))
                    proxima = fazTextoProx(prox)
                    screen.blit(proxima, (100,500))
                    display.update()
                    time.wait(500) # pra dar tempo de tirar o dedo da tecla 0
                    break
            
            display.update()
            clock.tick(tick)
        
        
    
    display.update()
    clock.tick(tick)
    
 
def popup():
    rect = ((150, 150),(600, 200))
    screen.fill((255,0,0),rect) 
    display.update()
    


def ema(jog):
    popup()
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
            limpaTela()
            break
        
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]:#perseguir
            popup()
            jog.temporestante -= 3
            s_n = randint(0,100)
            if s_n < 75:
                screen.blit(ema_suc1,(160,200))
                screen.blit(ema_suc1_2,(160,220))
                display.update()
                time.wait(5000)
                limpaTela()
                break
            
            else:
                jog.comida -= 10       
                screen.blit(ema_fal1, (160,200))
                display.update()
                time.wait(5000)
                limpaTela()
                break
            
            
        if key.get_pressed()[K_2] or key.get_pressed()[K_KP2]:#jogar pedra    
            popup()
            s_n = randint(0,100)
            if s_n < 15:
                jog.comida += 10
                screen.blit(ema_suc2,(160,200))
                screen.blit(ema_suc2_2,(160,220))
                display.update()
                time.wait(5000)
                limpaTela()
                break
            
            else:
                jog.comida -= 10       
                screen.blit(ema_fal2, (160,200))
                display.update()
                time.wait(5000)
                limpaTela()
                break
                
        
        #display.update()
        clock.tick(tick)

def lobo(jog):
    popup()
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
            limpaTela()
            break
        
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]:#lutar
            popup()
            s_n = randint(0,100)
            if s_n < 15:
                jog.comida += 20
                screen.blit(lobo_suc,(160,200))
                display.update()
                time.wait(5000)
                limpaTela()
                break
            elif s_n < 55: 
                screen.blit(lobo_medio,(160,200))
                display.update()
                time.wait(5000)
                limpaTela()
                break
            else:
                jog.comida -= 10
                jog.health -= 10
                screen.blit(lobo_fail,(160,200))
                screen.blit(lobo_fail2,(160,220))
                display.update()
                time.wait(5000)
                limpaTela()
                break


        
        #display.update()
        clock.tick(tick)


def buraco(jog):
    popup()
    screen.blit(buraco0,(160,200))
    display.update()
    jog.durab -= 100
    time.wait(3000)
    limpaTela()
    



screen.blit(msg_comeco1, (100,100)) # escreve a intro na tela
screen.blit(msg_comeco2, (100, 150))
display.update() #da um update pra aparecer o escrito na tela

time.wait(3000) # espera, em milisegundos
limpaTela()

menuMercado(jog)
while True: #loop mercado inicial

    for e in event.get():
        if e.type == QUIT:
            exit()

    if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
        limpaTela()
        break

    if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]:
        if jog.reais >= 10:
            jog.reais-=10
            jog.comida+=10
            screen.blit(done, (500,200))
            display.update()
            time.wait(1000)
            limpaTela()
            menuMercado(jog)
            
        else:
            limpaTela()
            screen.blit(semGrana, (250,200))
            display.update()
            time.wait(2000)
            limpaTela()
            menuMercado(jog)
        
        
    if key.get_pressed()[K_2] or key.get_pressed()[K_KP2]:
        if jog.comida >= 10:
            jog.comida-=10
            jog.reais+=10
            screen.blit(done, (500,250))
            display.update()
            time.wait(1000)
            limpaTela()
            menuMercado(jog)
        else:
            limpaTela()
            screen.blit(semComida, (250,200))
            display.update()
            time.wait(3000)
            limpaTela()
            menuMercado(jog)
        
        
    if key.get_pressed()[K_3] or key.get_pressed()[K_KP3]:
        if jog.reais >= 10:
            jog.reais-=10
            jog.pecas+=100
            screen.blit(done, (500,300))
            display.update()
            time.wait(1000)
            limpaTela()
            menuMercado(jog)
        else:
            limpaTela()
            screen.blit(semGrana, (250,200))
            display.update()
            time.wait(2000)
            limpaTela()
            menuMercado(jog)
    
    if key.get_pressed()[K_4] or key.get_pressed()[K_KP4]:
        if jog.reais >= 10:
            jog.reais-=10
            jog.gas+=100
            screen.blit(done, (500,350))
            display.update()
            time.wait(1000)
            limpaTela()
            menuMercado(jog)
        else:
            limpaTela()
            screen.blit(semGrana, (250,200))
            display.update()
            time.wait(2000)
            limpaTela()
            menuMercado(jog)
    
    
    if key.get_pressed()[K_5] or key.get_pressed()[K_KP5]:
        limpaTela()
        stat1, stat2, stat3, stat4, stat5, stat6, stat7, stat8, stat9 = getStatus(jog)
        py = 100 # 1o y da tela 
        esp = 35 # espaco entre eles
        screen.blit(stat, (100,py))
        screen.blit(stat1, (100,py+1*esp))
        screen.blit(stat2, (100,py+2*esp))
        screen.blit(stat3, (100,py+3*esp))
        screen.blit(stat4, (100,py+4*esp))
        screen.blit(stat5, (100,py+5*esp))
        screen.blit(stat6, (100,py+6*esp))
        screen.blit(stat7, (100,py+7*esp))
        screen.blit(stat8, (100,py+8*esp))
        screen.blit(stat9, (100,py+9*esp))
        screen.blit(voltar, (100, 500))
        display.update()
        
        while True: # loopzinho esperando o cara ler o status e decidir voltar
            for e in event.get():
                if e.type == QUIT:
                    exit()
            
            if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
                limpaTela()
                menuMercado(jog)
                time.wait(500) # pra dar tempo de tirar o dedo da tecla 0
                break
            
            display.update()
            clock.tick(tick)
            
        
        
        
    display.update()
    clock.tick(tick)

game_over = [False]
chegou = False

i = 0

###  LOOP PRINCIPAL DO JOGO  ###

while game_over[0]==False and chegou==False: 
    
    
    for e in event.get():
        if e.type == QUIT:
            exit()

    
    
    proxCidade = dist_proximaCidade(CC[i:])

    dist, temp = getTempoDist(jog)
    #screen.blit(go, (100,100))
    #screen.blit(dist,(100,500))
    #screen.blit(temp,(500,500))

    display.update()####### COMEÇA A TELA GO

    Go.TelaGo(jog)
    
    time.wait(2000) ####### TERMINA A TELA GO
    
    if jog.temporestante <= 0 or jog.health <= 0:
        game_over[0] = True
        break
    
    
    jog.varia_comida()
    if jog.comida < 0:
        jog.comida = 0
    
    
    jog.varia_gas()

    jog.varia_distancia()

    jog.varia_durabilidade(jog.tempodeviagem)
    if jog.durab < 0:
        jog.durab = 0

    jog.varia_health()
            

    jog.varia_tempo()
    
    if jog.distancia <= 0:
        chegou = True
        break
    elif jog.temporestante <= 0 or jog.health <= 0:
        game_over[0] = True
        break
    
    if CC[i] == 1:
        cidade(jog, proxCidade, game_over) 
    else:
        campo(jog, proxCidade, game_over) 
    
    i += 1
    
    if jog.temporestante <= 0 or jog.health <= 0:
        game_over[0] = True
        break
    
        
    display.update()
    clock.tick(tick)


limpaTela()



if game_over[0] == True:
    screen.blit(msg_gameover, (250,200))
    display.update()
    
if chegou == True:
    screen.blit(msg_chegou, (250,200))
    display.update()

while True:
    
    for e in event.get():
        if e.type == QUIT:
            exit() 
    
    display.update()
    clock.tick(tick)
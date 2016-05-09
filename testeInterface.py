from pygame import *
#import loopJogo.py as lj
import SwTrail as sw
import random as rd

jog = sw.Jogo()

# 3000 km  5 cidades 5 camps

CC = []
ci = 5 # 1
ca = 5 # 2
p = 50

for i in range(ci+ca): # monta o vetor CC
    if ci>0 and ca>0:
        x = rd.randint(1,100)

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
bg = image.load("bg.png").convert() # define uma imagem bg
fonte = font.Font(None, 30) # define uma fonte

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

stat = fonte.render("===== Status =====", 1, (255,255,255))

voltar = fonte.render("0 - Voltar", 1, (255,255,255))

semGrana = fonte.render("Ta sem grana porra",1,(255,255,255))

semComida = fonte.render("Ta sem comida porra, ta tentando enganar alguem?",1,(255,255,255))

done = fonte.render("Done!",1,(255,255,255))

def getStatus(jogador): # faz as frases do STATUS
    stat1 = "Gasolina: " + str(jogador.gas)
    stat2 = "Pecas: " + str(jogador.pecas)
    stat3 = "Durabilidade: " + str(jogador.durab)
    stat4 = "Comida: " + str(jogador.comida)
    stat5 = "Health: " + str(jogador.health)
    stat6 = "Dinheiro: " + str(jogador.reais)
    stat7 = "Amigos vivos: " + str(jogador.numero_jogadores-1)
    stat8 = "Distancia restante: " + str(jogador.distancia)
    stat9 = "Tempo restante: " + str(jogador.temporestante)

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
    


screen.blit(msg_comeco1, (100,100)) # escreve a intro na tela
screen.blit(msg_comeco2, (100, 150))
display.update() #da um update pra aparecer o escrito na tela

time.wait(3000) # espera, em milisegundos
limpaTela()

def menuMercado():
    screen.blit(mer, (100,100))
    screen.blit(mer_menu0, (100,150))
    screen.blit(mer_menu1, (100,200))
    screen.blit(mer_menu2, (100,250))
    screen.blit(mer_menu3, (100,300))
    screen.blit(mer_menu4, (100,350))
    screen.blit(mer_menu5, (100,400))
    
menuMercado()
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
            menuMercado()
            
        else:
            limpaTela()
            screen.blit(semGrana, (250,200))
            display.update()
            time.wait(2000)
            limpaTela()
            menuMercado()
        
        
    if key.get_pressed()[K_2] or key.get_pressed()[K_KP2]:
        if jog.comida >= 10:
            jog.comida-=10
            jog.reais+=10
            screen.blit(done, (500,250))
            display.update()
            time.wait(1000)
            limpaTela()
            menuMercado()
        else:
            limpaTela()
            screen.blit(semComida, (250,200))
            display.update()
            time.wait(3000)
            limpaTela()
            menuMercado()
        
        
    if key.get_pressed()[K_3] or key.get_pressed()[K_KP3]:
        if jog.reais >= 10:
            jog.reais-=10
            jog.pecas+=100
            screen.blit(done, (500,250))
            display.update()
            time.wait(1000)
            limpaTela()
            menuMercado()
        else:
            limpaTela()
            screen.blit(semGrana, (250,200))
            display.update()
            time.wait(2000)
            limpaTela()
            menuMercado()
    
    if key.get_pressed()[K_4] or key.get_pressed()[K_KP4]:
        if jog.reais >= 10:
            jog.reais-=10
            jog.gas+=100
            screen.blit(done, (500,250))
            display.update()
            time.wait(1000)
            limpaTela()
            menuMercado()
        else:
            limpaTela()
            screen.blit(semGrana, (250,200))
            display.update()
            time.wait(2000)
            limpaTela()
            menuMercado()
    
    
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
        
        while True: # loopzinho esperando o cara ler o status e decidir voltar
            for e in event.get():
                if e.type == QUIT:
                    exit()
            
            if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
                limpaTela()
                menuMercado()
                break
            
            display.update()
            clock.tick(30)
            
        time.wait(500) # pra dar tempo de tirar o dedo da tecla 0
        
        
    display.update()
    clock.tick(30)

game_over = False
chegou = False

while game_over==False and chegou==False: #loop do jogo
    
    for e in event.get():
        if e.type == QUIT:
            exit()

    
    
    
    
    
    
    if key.get_pressed()[K_e] or key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
        limpaTela()
    
    if key.get_pressed()[K_c]: #teste bobo
        screen.blit(cid, (100,100))
        screen.blit(cid_menu0, (100,150))
        screen.blit(cid_menu1, (100,200))
        screen.blit(cid_menu2, (100,250))
        screen.blit(cid_menu3, (100,300))
        screen.blit(cid_menu4, (100,350))
        screen.blit(cid_menu5, (100,400))
        
    display.update()
    clock.tick(30)


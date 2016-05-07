from pygame import *
#import loopJogo.py as lj
import SwTrail as sw
import random as rd

meuJogador = sw.Jogo()

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

#meuJogador = sw.Jogo()

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

msg_comeco1 = fonte.render("vc e 3 amigos tao no piaui e blablabla roubaram um carro blablabla vai", 1, (255,255,255))
msg_comeco2 = fonte.render("a viagem comeca num mercado, chequem o STATUS e comprem o necessario", 1, (255,255,255))

screen.blit(msg_comeco1, (100,100)) # escreve a intro na tela
screen.blit(msg_comeco2, (100, 150))
display.update() #da um update pra aparecer o escrito na tela

time.wait(5000)
screen.fill((0,0,0)) # pinta a tela de preto
display.update()

screen.blit(mer, (100,100))
screen.blit(mer_menu0, (100,150))
screen.blit(mer_menu1, (100,200))
screen.blit(mer_menu2, (100,250))
screen.blit(mer_menu3, (100,300))
screen.blit(mer_menu4, (100,350))
screen.blit(mer_menu5, (100,400))
    
while True: #loop mercado inicial

    for e in event.get():
        if e.type == QUIT:
            exit()

    if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
        screen.fill((0,0,0))
        break
    
    display.update()
    clock.tick(20)

game_over = False
chegou = False

while game_over==False and chegou==False:
    
    for e in event.get():
        if e.type == QUIT:
            exit()

    
    if key.get_pressed()[K_e] or key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
        screen.fill((0,0,0))
    
    if key.get_pressed()[K_c]: 
        screen.blit(cid, (100,100))
        screen.blit(cid_menu0, (100,150))
        screen.blit(cid_menu1, (100,200))
        screen.blit(cid_menu2, (100,250))
        screen.blit(cid_menu3, (100,300))
        screen.blit(cid_menu4, (100,350))
        screen.blit(cid_menu5, (100,400))
        
    display.update()
    clock.tick(20)


from pygame import *
from random import randint

init()

from ArquivoJogador import *
from ArquivoGo import *
from ArquivoCidade import *
from ArquivoCampo import *
from ArquivoHistoria import *


mixer.init()
jog = Jogador()                                       

# 3000 km  5 cidades 5 camps

CC = []
ci = 5 # numero de cidades
ca = 5 # numero de camps
p = 50
ticke = 35 #fps


for i in range(ci+ca): # monta o vetor CC (composto de 1s e 2s, 1= cidade 2= campo)
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



screen = display.set_mode((956,560), 0, 32) # cria a janela

x,y = (100,100)
fonte = font.Font(None, 30) # define uma fonte
fontePeq = font.Font(None, 23) # define uma fonte de tamanho menor

screen.fill((0,0,0)) # pinta a tela de preto
clock = time.Clock() # cria o reloginho

# define as musicas
m1 = mixer.Sound('musica_1.wav')
m2 = mixer.Sound('musica_2.wav')
m3 = mixer.Sound('musica_3.wav')
m4 = mixer.Sound('musica_4.wav')
m5 = mixer.Sound('musica_5.wav')
m6 = mixer.Sound('musica_6.wav')
m7 = mixer.Sound('musica_7.wav')

musicas = [m1,m2,m3,m4,m5,m6,m7]

# INTROOOOOOO
intro(jog, screen,display)


# ACABA A INTROOOOO

game_over = [False]
chegou = False


mercado(jog, screen, display) # mercado inicial

###  LOOP PRINCIPAL DO JOGO  ###
i = 0
n_anterior = -1
n = -1
while game_over[0]==False and chegou==False: 
    
    
    for e in event.get():
        if e.type == QUIT:
            exit()

    
    
    proxCidade = dist_proximaCidade(CC[i:]) # calcula a distancia pra proxima cidade, em rodadas

    #display.update()
    
    ####### COMEÇA A TELA GO
    
    while n == n_anterior: # pra nao comecar a msma musica d nv
        n = randint(0,6) # numero aleatorio de 0 a 6 (sim, eu testei e o 6 ta incluso qndo faz assim)
        
    n_anterior = n
    ma = musicas[n] # pega uma musica aleatoriamente
    ma.set_volume(1.0) # volta pro volume alto
    ma.play()
 
    TelaGo(jog, screen,display, game_over)

    ma.set_volume(0.2) # abaixa o volume, pro jogador pensar
    ####### TERMINA A TELA GO
    
    if game_over[0]==True:
        break
    
    if jog.temporestante <= 0 or jog.health <= 0 or jog.gas <= 0:
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
    
    if jog.reais <= 0:
        jog.reais =0
    
    if jog.comida <=0:
        jog.comida =0
    
    if jog.distancia <= 0:
        chegou = True
        break
    elif jog.temporestante <= 0 or jog.health <= 0 or jog.gas <= 0:
        game_over[0] = True
        break
    
    if CC[i] == 1:
        cidade(jog, proxCidade, game_over, screen, display) 
    else:
        campo(jog, proxCidade, game_over, screen, display)
        
    
    i += 1
    
    if jog.temporestante <= 0 or jog.health <= 0:
        game_over[0] = True
        break
    
    ma.stop() # para a musica, para trocar
        
    display.update()
    clock.tick(ticke)

## Saiu do loop principal do jogo
## ou seja, ou deu game_over ou chegou

ma.stop() # para a musica do jogo

black = image.load('afeeeeeee.png') # uma tela preta, para fazer o fadeout

for i in range(50): #FADE OUT PORRAAAAA :D
    screen.blit(black,(0,0))
    display.update()
    time.wait(10)
    
if game_over[0] == True: # se deu game_over
    
    musica_gameover = mixer.Sound('musicagame_over.wav') # toca Imperial March
    musica_gameover.play()
    
    if jog.health <= 0: # se ele morreu
        gameover1 = image.load('game_over2.png')
        screen.blit(gameover1, (0,0))
        display.update()
    else: # se foi outro motivo (gasolina, quebrou o carro, etc)
        gameover2 = image.load('game_over1.png')
        screen.blit(gameover2, (0,0))
        display.update()
    
if chegou == True: # se ele chegou no destino final
    vitoria = image.load('tela_preta_chupragraicer_vitoria.png')
    fracasso = image.load('tela_preta_chupragraicer_fracasso.png')
    chegada = image.load('chegada.png')
    chegada_aviso = image.load('chegada_aviso.png')
    
    screen.blit(chegada, (0,0)) # imagem dele no cinema, menu para comprar o ingresso ou sair
    display.update()
    
    while True:
    
        for e in event.get():
            if e.type == QUIT:
                exit() 
        
        if key.get_pressed()[K_1] or key.get_pressed()[K_KP1]: # SAIR, game over
            screen.blit(fracasso,(0,0))
            musica_gameover = mixer.Sound('musicagame_over.wav')
            musica_gameover.play()
            break

        if key.get_pressed()[K_0] or key.get_pressed()[K_KP0]: # Tentar comprar, se nao tem grana suficiente volta pro menu
            if jog.reais >= 100:
                screen.blit(vitoria,(0,0))
                m1.play()
                break
            else:
                screen.blit(chegada_aviso,(0,0))
                display.update()
                time.wait(5000)
                screen.blit(chegada,(0,0))
                
    
        display.update()
        clock.tick(ticke)


while True: # mini loop de final de jogo, ate a pessoa fechar a janela
    
    for e in event.get():
        if e.type == QUIT:
            exit() 
    
    
    display.update()
    clock.tick(ticke)
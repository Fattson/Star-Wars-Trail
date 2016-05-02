# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 08:16:01 2016

@author: GuilhermeZaborowsky
"""

import SwTrail as sw
import random as rd

meuJogador = sw.Jogo()

# 3000 km  5 cidades 5 camps

CC = []
ci = 5 # 1
ca = 5 # 2
p = 50

for i in range(ci+ca):
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
        
def dist_proximaCidade(CCrestante):
    for d in len(CCrestante):
        if CCrestante[d] == 1:
            break
    
    return d+1

def status(jogador):
    
    print("Comida: ", jogador.comida)
    print("Gasolina: ", jogador.gas)
    print("Pecas: ", jogador.pecas)
    print("Health: ", jogador.health)
    print("DinDin: ", jogador.reais)
    print("Amigos vivos: ", jogador.numero_jogadores-1)
    print("Distancia faltante: ", jogador.distancia)
    print("Tempo restante: ", jogador.temporestante)
    
def mercado(jogador):# criar
    
def conserto(jogador):# criar
    
def camp(jogador, prox):# criar
    


def cidade(jogador, prox):
    print("Vc esta numa cidade, oq deseja fazer?")
    print("Rodadas p prox cidade (ou destino final): ", prox)
    x = -1
    while x != 0:
        x = int(input("0 - continuar viagem (0 horas) /n1 - mercado (3 horas) /n2 - SUS (2 horas) /n3 - hospotal particular (0 horas/20 reais) /n4 - conserto do carro (2 horas) /n5 - Status"))
        if x == 1: # mercado
            mercado(jogador)
        if x == 2: # sus
            print("foi ao sus, gastou 2 horas re recuperou 20 de vida")
            jogador.temporestante -= 2
            jogador.health += 20
        if x == 3:
            if jogador.reais >= 20:
                print("foi ao hospital, gastou 20 reais e recuperou 20 health")
            else:
                print("nao deu, vc ta sem grana")
        if x == 4:
            conserto(jogador)
        if x == 5:
            status(jogador)
        

chegou = False
game_over = False

print("vc e 3 amigos tao no piaui e blablabla roubaram um carro blablabla vai")
print("a viagem comeca na cidade que vcs estavam com a escola")
proxCidade = dist_proximaCidade(CC)
cidade(meuJogador, proxCidade)

i = 0 #iterador de rodadas

while chegou == False and game_over == False:
    
    ev = rd.randint(1,100)
    
    proxCidade = dist_proximaCidade(CC[i:])
    
    if ev < 50:
        #acontece ema
    elif ev < 75:
        #acontece lobo guara
    elif ev < 85:
        #acontece buraco
    
    if meuJogador.temporestante <= 0:
        game_over = True
        break
    
    meuJogador.varia_comida()
    meuJogador.varia_gas()
    meuJogador.varia_distancia()
    meuJogador.varia_durabilidade()
    meuJogador.varia_health()
    meuJogador.varia_tempo()
    
    if meuJogador.distancia <= 0:
        chegou = True
        break
    elif meuJogador.temporestante <= 0:
        game_over = True
        break
    
    if CC[i] == 1:
        cidade(meuJogador, proxCidade) #continuar criando
    else:
        camp(meuJogador, proxCidade) # criar
        
    if meuJogador.distancia <= 0:
        chegou = True
    elif meuJogador.temporestante <= 0:
        game_over = True
    
    i += 1
    


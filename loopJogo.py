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
        
def cidade(jogador):
    print("Vc esta numa cidade, oq deseja fazer?")
    x = -1
    while x != 0:
        x = int(input("0 - continuar viagem /n 1 - mercado /n 2 - SUS /n 3 - hospotal particular /n 4 - mecanico"))
        #CONTINUAR
        

chegou = False
game_over = False

print("vc e 3 amigos tao no piaui e blablabla roubaram um carro blablabla vai")
cidade(meuJogador)

while chegou == False and game_over == False:
    
    ev = rd.randint(1,100)
    
    if ev < 50:
        #acontece ema
    elif ev < 65:
        #acontece buraco
    
    meuJogador.varia_comida()
    meuJogador.
    


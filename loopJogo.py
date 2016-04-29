# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 08:16:01 2016

@author: GuilhermeZaborowsky
"""

#import SwTrail as sw
import random as rd

#meuCarro = sw.Carro()
#meuJogador = sw.Jogo()

# 3000 km  5 cidades 5 camps

CC = []
ci = 5 # 1
ca = 5 # 2
p = 50

for i in range(ci+ca):
    print(p)
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
        
print(CC)


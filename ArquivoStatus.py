# -*- coding: utf-8 -*-
"""
Esse arquivo tem a funcao getStatus, para ser usada no jogo Star Wars Trail

"""
from pygame import *

fonte = font.Font(None, 30) # define uma fonte


def getStatus(jog): # faz as frases do STATUS
    stat1 = "Gasolina: " + str(jog.gas)
    stat2 = "Pecas: " + str(jog.pecas)
    stat3 = "Durabilidade: " + str(jog.durab)
    stat4 = "Comida: " + str(jog.comida)
    stat5 = "Health: " + str(jog.health)
    stat6 = "Dinheiro: " + str(jog.reais)
    stat7 = "Amigos vivos: " + str(jog.numero_personagens-1)
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

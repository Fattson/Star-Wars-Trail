# -*- coding: utf-8 -*-
"""
Esse arqivo contem 2 funcoes: limpaCidade e limpaCamp,  para serem usadas no jogo Star Wars Trail



"""

from pygame import *

def limpaCidade(screen, display): #limpa a parte escrita na cidade

    background = image.load("cidade2.jpg")
    background = transform.scale(background, (956,560))

    rect_transparente = image.load("cidade2_transparente.jpg")
    rect_transparente = transform.scale(rect_transparente, (956,200))   
    
    screen.blit(background, (0,0))
    draw.rect(screen, (0, 0, 0), [2,2,952,200])
    screen.blit(rect_transparente,(0, 0))
    draw.rect(screen, (255, 255, 255), [2,2,952,200], 5)
    display.update()
    
    
def limpaCampo(screen, display): # limpa a parte escrita no camp
    
    background = image.load("campfire1.png")
    background = transform.scale(background, (956,560))
    carro = image.load("carrofogo.png")
    carro = transform.scale(carro, (260,90))
    rect_transparente = image.load("campfire1_transparente1.png")
    rect_transparente= transform.scale(rect_transparente, (956,200)) 
    
    screen.blit(background, (0,0))
    screen.blit(carro, (190,405))
    draw.rect(screen, (0, 0, 0), [2,3,952,200])
    draw.rect(screen, (255, 255, 255), [2,3,952,200], 5)
    display.update()
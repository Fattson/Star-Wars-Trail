# -*- coding: utf-8 -*-
"""
Created on Wed May  4 08:54:55 2016

@author: bvbit
"""

import pygame

pygame.init ()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Star Wars Trail')

pygame.display.update()

#pygame.display.updade(#sem nada aqui dentro) = pygame.display.flip()

gameExit = False

while not gameExit :
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True
pygame.quit()

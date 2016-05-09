# -*- coding: utf-8 -*-
"""
Created on Wed May  4 08:54:55 2016

@author: bvbit
"""

import pygame

pygame.init ()

white = (255, 255, 255)
black = (0,0,0)
red = (255, 0 ,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Star Wars Trail')

pygame.display.update()

#pygame.display.updade(#sem nada aqui dentro) = pygame.display.flip()

gameExit = False

lead_x = 300
lead_y = 300


while not gameExit :
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
            if event.key == pygame.K_RIGHT:
                lead_x += 10
                
pygame.quit()

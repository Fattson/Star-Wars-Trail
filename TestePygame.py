import pygame

pygame.init()

screen = pygame.display.set_mode((956,560), 0, 32)
#sur = pygame.Surface((30,30), flags=0, depth=)
#circulo = pygame.draw.circle(screen, (0,0), (100,100), 5, width=0)

x,y = (100,100)
imagem = pygame.image.load("oi.png").convert_alpha()
bg = pygame.image.load("bg.png").convert()


while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	tecla = pygame.key.get_pressed()
	if tecla[pygame.K_w]:
		screen.blit(imagem, (-10,-10))

	screen.fill((0,0,0))
	screen.blit(bg, (0,0))
	screen.blit(imagem, (0,0))
	pygame.display.update()


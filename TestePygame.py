from pygame import *
#import loopJogo.py as lj
import SwTrail.py as sw

init()

screen = display.set_mode((956,560), 0, 32)
#sur = pygame.Surface((30,30), flags=0, depth=)
#circulo = pygame.draw.circle(screen, (0,0), (100,100), 5, width=0)

x,y = (100,100)
#imagem = pygame.image.load("oi.png").convert_alpha()
bg = image.load("bg.png").convert()
fonte = font.Font(None, 30)

screen.fill((0,0,0))
clock = time.Clock()

#screen.blit(bg, (0,0))

#meuJogador = sw.Jogo()

cid = fonte.render("CIDADE! O que deseja fazer?", 1, (255,255,255))
cid_menu0 = fonte.render("0 - Continuar a viagem", 1, (255,255,255))
cid_menu1 = fonte.render("1 - Mercado", 1, (255,255,255))
cid_menu2 = fonte.render("2 - SUS", 1, (255,255,255))
cid_menu3 = fonte.render("3 - Hospital Particular", 1, (255,255,255))
cid_menu4 = fonte.render("4 - Conserto do carro", 1, (255,255,255))
cid_menu5 = fonte.render("5 - Status", 1, (255,255,255))

msg_comeco1 = fonte.render("vc e 3 amigos tao no piaui e blablabla roubaram um carro blablabla vai", 1, (255,255,255))
msg_comeco2 = fonte.render("a viagem comeca na cidade que vcs estavam com a escola", 1, (255,255,255))

screen.blit(msg_comeco1, (100,100))
screen.blit(msg_comeco2, (100, 150))

clock.tick(200)
screen.fill((0,0,0))

game_over = False
chegou = False

while game_over==False and chegou==False:
    
    for e in event.get():
        if e.type == QUIT:
            exit()

    if key.get_pressed()[K_a]:
        hw = fonte.render("Hello World!", 1, (255,255,255))
        screen.blit(hw, (100,100))
    if key.get_pressed()[K_e] or key.get_pressed()[K_0] or key.get_pressed()[K_KP0]:
        screen.fill((0,0,0))
    
    if key.get_pressed()[K_c]: 
        #cidade(meuJogador)
        screen.blit(cid, (100,100))
        screen.blit(cid_menu0, (100,150))
        screen.blit(cid_menu1, (100,200))
        screen.blit(cid_menu2, (100,250))
        screen.blit(cid_menu3, (100,300))
        screen.blit(cid_menu4, (100,350))
        screen.blit(cid_menu5, (100,400))
        
    #screen.fill((0,0,0))
    #screen.blit(bg, (0,0))
    #screen.blit(imagem, (0,0))
    display.update()
    clock.tick(20)


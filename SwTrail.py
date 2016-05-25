# Star Wars Trail

from random import randint


class Jogo:
	def __init__(self):
		# Estoque não variáveis com a classe do jogador
		self.tipo = 0 # 1 = Computação (melhor de todas obvioooo) 2 = Mecatronica 3 = Mecanica
		self.comida = 100
		self.gas = 250
		self.pecas = 1000
		self.health = 100
		self.reais = 100
		self.temporestante = 100    # Tempo restante
		self.tempodeviagem = 3    # Tempo de viagem, não conta o tempo gasto em cidade ou camp, apenas na tela go
		self.numero_jogadores = 3
		self.distancia = 300
		self.velocidade = 100
		self.durab = 1000 # durabilidade

	def varia_durabilidade(self, tempo):
		self.durab -= tempo*10

	def varia_gas(self):
		if 0 < self.velocidade < 50:
			self.gas -= int((self.velocidade*self.tempodeviagem) / 8)
		elif 50 < self.velocidade < 110:
			self.gas -= int((self.velocidade*self.tempodeviagem) / 10)

	def varia_comida(self):
		tx = 2
		self.comida -= self.numero_jogadores*tx

	def varia_distancia(self):
		self.distancia -= self.velocidade*self.tempodeviagem


	def varia_health(self):
		# Varia conforme os eventos e com:
		if self.comida == 0:
			if 50 <= self.health <= 100:
				self.health -= 4*self.tempodeviagem
			elif 0 < self.health < 50:
				self.health -= 7*self.tempodeviagem


	def varia_tempo(self):
		self.temporestante -= self.tempodeviagem
		# E tambem na cidade e pá

#class Eventos:
	"""def __init__(self):
		prob = randint(1,2)
		if prob == 1: 
			self.ema()"""
def ema(jogador):
    animais = ["ema", "hiena", "alpaca"]
    i = randint(0,2)
    print()
    print("Uma {0} roubou 10 das suas comidas, e saiu correndo! O que deseja fazer? ".format(animais[i]))
    print("1 - Perseguir e recuperar (gasta tempo, aproximadamente 3 horas)")
    print("2 - Miar e ir embora (perde a comida)")
    print("3 - Tentar jogar uma pedra nela (osso, mas instantaneo e mata o bixo, dando mais comida)")
    escolha = int(input("==>")) 
    
    if escolha == 1:
        jogador.temporestante -= 3
        s_n = randint(0,100)
        if s_n < 75:
            print("Parabéns, você conseguiu pegar a {0} e recuperar sua comida! Apesar de ter demorado 3 horas".format(animais[i]))
            
        else:
            print("Fracassado! Nem consegue ir atrás de uma {0}. Ainda levou 3 horas --' ".format(animais[i]))
            jogador.comida -= 10            
            
    elif escolha == 2:
            print("Você é um miao!")
            jogador.comida -= 10

    elif escolha == 3:
        s_n = randint(0,100)
        if s_n < 15:
            print("Parábens, você acertou a {0} e ela morreu, recuperou seus 10 e guardou a carne dela (+10 de comida)!".format(animais[i]))
            jogador.comida += 10
        else:
            print("Errou feio, errou rude!")
            jogador.comida -= 10

def lobo_guara(jogador):
    animais = ["lobo guara", "urso", "esquilo do mau"]
    i = randint(0,2)
    print()
    print("Voce foi atacado por um {0}! O que deseja fazer?".format(animais[i]))
    print("1 - Se defender (boa sorte)")
    print("2 - Fugir (abandona 10 de comida pra destrair a fera)")
    escolha = int(input("==>"))
    
    if escolha == 1:
        s_n = randint(0,100)
        if s_n < 15:
            print("Parabéns, você conseguiu matar o {0}! E pegou a carne dele. (+20 de comida)".format(animais[i]))
            jogador.comida += 20
        elif s_n < 55: 
            print("Não derrotou a fera, mas tambem nao teve que distraí-la")
        else:
            print("Seu fraco! Nem consegue derrotar um {0}. Ficou ferido (-10 de health) e perdeu 10 de comida ".format(animais[i]))
            jogador.comida -= 10
            jogador.health -= 10
    elif escolha == 2:
        print("Você é um miao!")
        jogador.comida -= 10
 	

            
def buraco(jogador):
    print()
    print("Se distraíu e atingiu um grande buraco na estrada!")
    print("(-100 de durabilidade do carro)")
    jogador.durab -= 100
    if jogador.durab < 0:
        jogador.durab = 0
    
def lampiao(jogador):
    escolha = input("Caralho, Lampião acabou de te desafiar para um fight, aceita? Se aceitar e perder, morreu! 'Sim/Não' ")
    if escolha == "Sim":
        s_n = randint(1,2)
        if s_n == 1:
            print("Palmas, tu é foda! matou o lampião, e com isso conseguiu 100 reais.")
            jogador.reais += 100
        else:
            print("Haha, Se fodeu!")
            jogador.health = 0
    elif escolha == "Não":
        s_n = randint(1,4)
        if s_n == 4:	
            print("Bom, tentou fugir mas morreu")
        else:
            print("Conseguiu fugir")




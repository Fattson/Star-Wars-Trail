# Star Wars Trail

from random import randint


"""class Carro:     # Victor, o que você acha de abolirmos a classe Carro, e deixarmos todas as variaveis em Jogo? Fiz isso por enquanto mas qq coisa mudamos de volta. GG

	def __init__(self):
		self.velocidade = 10
	
	def returnVelocidade(self):
		return self.velocidade 
"""

class Jogo:
	def __init__(self):
		# Estoque não variáveis com a classe do jogador
		self.comida = 100
		self.gas = 10
		self.pecas = 1000
		self.health = 100
		self.reais = 0
		self.temporestantante = 100    # Tempo restante
		self.tempodeviagem = 2    # Tempo de viagem, não conta o tempo gasto em cidade ou camp, apenas na tela go
		self.numero_jogadores = 3
		self.distancia = 3000
		self.velocidade = 10
		self.durab = 1000 # durabilidade

	def varia_gas(self):
		if 0 < self.velocidade < 50:
			self.gas -= (self.velocidade*self.tempodeviagem) / 8
		elif 50 < self.velocidade < 110:
			self.gas -= (self.velocidade*self.tempodeviagem) / 10

	def varia_comida(self):
		tx = 1
		self.comida -= self.numero_jogadores*tx
		print(self.comida)

	def varia_distancia(self):
		self.distancia -= self.velocidade*self.tempodeviagem
		print(self.distancia)

	def varia_pecas(self):
		# Varia conforme há o conserto do carro
		besteira = besteira

	def varia_health(self):
		# Varia conforme os eventos e com:
		if self.comida == 0:
			if 50 <= self.health <= 100:
				self.health -= 4*self.tempodeviagem
			elif 0 < self.health < 50:
				self.health -= 7*self.tempodeviagem

	def varia_reais(self):
		# Varia com as compras ou eventos
		besteira = besteira

	def varia_tempo(self):
		self.temporestantante -= self.tempodeviagem
		# E tambem na cidade e pá

class Eventos:
	"""def __init__(self):
		prob = randint(1,2)
		if prob == 1: 
			self.ema()"""
	def ema(self):
		animais = ["ema, hiena, alpaca"]
		i = randint(0,2)
		self.escolha = input("Voce foi atacado por uma {0}! O que deseja fazer? ".format(animais[i]))
		if self.escolha == "Perseguir":
			s_n = randint(1,2)
			print(s_n)
			if s_n == 1:
				print("Parabéns, você conseguiu pegar a {0} e recuperar 10 de comida! Apesar de ter demorado ".format(animais[i]))
				self.comida += 10

			else:
				print("Fracassado! Nem consegue ir atrás de uma {0}. ".format(animais[i]))

		elif self.escolha == "Miar":
			print("Você é um miao!")

		elif self.escolha == "Tentar jogar pedra":
			s_n == randint(1,2)
			if s_n == 1:
				print("Parábens, você acertou a {0} e ela morreu, ganhou 20 de comida!".format(animais[i]))
				self.comida += 20
			else:
				print("Errou de longe, vesgo!")

	def lobo_guara(self):
		animais = ["lobo guara", "urso", "esquilo"]
		i = randint(0,2)
		self.escolha = input("Voce foi atacado por um {0}! O que deseja fazer? \n === Escolhas === \n Se esconder \n Fugir ".format(animais[i]))

		if self.escolha == "Se esconder":
			s_n = randint(1,2)
			if s_n == 1:
				print("Parabéns, você conseguiu pegar o {0} e recuperar 10 de comida! Apesar de ter demorado ".format(animais[i]))
				self.comida += 10

			else:
				print("Fracassado! Nem consegue ir atrás de um {0}. ".format(animais[i]))

		elif self.escolha == "Fugir":
			print("Você é um miao!")

	def lampiao(self):
		self.escolha = input("Caralho, Lampião acabou de te desafiar para um fight, aceita? Se aceitar e perder, morreu! 'Sim/Não' ")
		if self.escolha == "Sim":
			s_n = randint(1,2)
			if s_n == 1:
				print("Palmas, tu é foda! matou o lampião, e com isso conseguiu 100 reais.")
				self.reais += 100
			else:
				print("Haha, Se fodeu!")
				self.health = 0
		elif self.escolha == "Não":
			s_n = randint(1,4)
			if s_n == 4:	
				print("Bom, tentou fugir mas morreu")
			else:
				print("Conseguiu fugir")

"""Sw = Jogo()
Sw.varia_comida()
Sw.varia_distancia()"""
Eventos()


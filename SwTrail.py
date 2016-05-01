# Star Wars Trail

from random import randint


class Carro:

	def __init__(self):
		self.velocidade = 10
	
	def returnVelocidade(self):
		return self.velocidade

class Jogo:
	def __init__(self):
		car = Carro()
		# Estoque não variáveis com a classe do jogador
		self.comida = 100
		self.gas = 10
		self.pecas = 0
		self.health = 100
		self.reais = 0
		self.temporestantante = 100    # Tempo restante
		self.tempodeviagem = 2    # Tempo de viagem, não conta o tempo gasto em cidade ou camp, apenas na tela go
		self.numero_jogadores = 3
		self.distancia = 3000
		self.velocidade = car.returnVelocidade()

	def varia_gas(self):
		if 0 < self.velocidade < 50:
			self.gas -= (self.velocidade*self.tempodeviagem) / 8
		elif 50 < self.velocidade < 110:
			self.gas -= (self.velocidade*self.tempodeviagem) / 10

	def varia_comida(self):
		tx = 1
		self.comida -= self.numero_jogadores*tx
		print(self.velocidade)

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
	def __init__(self):
		#prob = randint(1,2)
		#if prob == 1: 
		#	self.ema()
	def ema(self):
		self.escolha = input("Voce foi atacado por uma Ema! O que deseja fazer? ")
		print(self.escolha)
		if self.escolha == "Perseguir":
			s_n = randint(1,2)
			print(s_n)
			if s_n == 1:
				print("Parabéns, você conseguiu pegar a ema e recuperar 10 de comida! Apesar de ter demorado ")

			else:
				print("Fracassado! Nem consegue ir atrás de uma Ema.")

		elif self.escolha == "Miar":
			print("Você é um miao!")

		elif self.escolha == "Tentar jogar pedra":
			s_n == randint(1,2)
			if s_n == 1:
				print("Parábens, você acertou a Ema e ela morreu, ganhou 20 de comida!")
			else:
				print("Errou de longe, vesgo!")

		def lobo_guara(self):
			self.escolha = input("Voce foi atacado por uma lobo guará! O que deseja fazer? ")
			if self.escolha == "Se esconder":
				s_n = randint(1,2)
				print(s_n)
				if s_n == 1:
					print("Parabéns, você conseguiu pegar a ema e recuperar 10 de comida! Apesar de ter demorado ")

				else:
					print("Fracassado! Nem consegue ir atrás de uma Ema.")

			elif self.escolha == "Fugir":
				print("Você é um miao!")


"""Sw = Jogo()
Sw.varia_comida()
Sw.varia_distancia()"""
Eventos()


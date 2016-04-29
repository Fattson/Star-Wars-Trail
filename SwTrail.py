# Star Wars Trail

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
		self.temporestantante = 100
		self.tempodeviagem = 2
		self.numero_jogadores = 3
		self.distancia = 3000
		self.velocidade = car.returnVelocidade()
	
	def varia_comida(self):
		tx = 1
		self.comida -= self.numero_jogadores*tx
		print(self.velocidade)

	def varia_distancia(self):
		self.distancia -= self.velocidade*self.tempodeviagem
		print(self.distancia)

	def varia_pecas(self):
		# Varia conforme há o conserto do carro

	def varia_saude(self):
		# Varia conforme os eventos e com:
		if self.comida == 0:
			if 50 <= self.health <= 100:
				self.health -= 4*self.tempodeviagem
			elif 0 < self.health < 50:
				self.health -= 7*self.tempodeviagem
		

Sw = Jogo()
Sw.varia_comida()
Sw.varia_distancia()


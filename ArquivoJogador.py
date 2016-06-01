from random import randint

"""
Esse arquivo contem uma classe, Jogador, 
que é responsavel pelo objeto principal do jogo Star Wars Trail.

"""
class Jogador:
	"""
    Essa classe representa um jogador de Star Wars Trail.
    
    Ele tem como atributos:
     - 3 de "tipo", sao booleanos para saber o tipo do jogador
     - 6 estoques para ser manejados durante o jogo
     - e 3 de informacoes do andamento do jogo
     
    Além disso, possui 6 métodos, responsáveis pela variação dos estoques ao longo do jogo.
    
	"""
	def __init__(self):
		 #Ele é do tipo que for True, sempre 2 delas serao False
		self.mecatronica = False
		self.mecanica = False
		self.comp = False		
          
          # Estoques para ser manejados durante o jogo

		self.comida = 0
		self.gas = 100
		self.pecas = 100
		self.health = 100
		self.reais = 500
		self.durab = 500 # durabilidade
  
  
          # Infos sobre o andamento do jogo
		self.temporestante = 50    # Tempo restante
		self.tempodeviagem = 3    # Tempo de viagem, não conta o tempo gasto em cidade ou camp, apenas na tela go
		self.numero_personagens = 3
		self.distancia = 300

		self.comida = 50
		self.gas = 90
		self.pecas = 100
		self.health = 150
		self.reais = 100
		self.durab = 700 # durabilidade
  
  
          # Infos sobre o andamento do jogo
		self.temporestante = 40  # Tempo restante
		self.tempodeviagem = 3    # Tempo de viagem, não conta o tempo gasto em cidade ou camp, apenas na tela go
		self.numero_personagens = 3
		self.distancia = 300
		self.velocidade = 100


	def varia_durabilidade(self, tempo):
		self.durab -= tempo*10 

	def varia_gas(self):
		if 0 < self.velocidade < 50:
			self.gas -= int((self.velocidade*self.tempodeviagem) / 8)
		elif 50 < self.velocidade < 110:
			self.gas -= int((self.velocidade*self.tempodeviagem) / 10)

	def varia_comida(self):
		tx = 2
		self.comida -= self.numero_personagens*tx

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
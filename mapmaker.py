"""
Class Responsável pela criação de um mapa em Texto.
Tem que ser capaz de admitir o número de blocos, finais, treasures, e size (n x n)
Tem que ser capaz de guardar monstros e players nos seus blocos
Cada bloco tem que ter uma dificuldade para saber q monstros spawnar
Dificuldade pode ser ajustada 
"""

import random
from unit import Unit

class Mapmaker:

	def __init__(self, size, n_blocos, finais, treasures, inic, dificuldade, jogadores, criaturas):
		self.size = size
		self.n_blocos = n_blocos
		self.finais = finais
		self.treasures = treasures
		self.dificuldade = dificuldade
		self.jogadores = jogadores

		self.map = []
		self.inic = inic
		spot = [inic[0],inic[1]]

		self.casas = {}

		for i in range(size):
			self.map.append([])
			for j in range(size):
				self.map[i].append(0)

		self.map[self.inic[0]][self.inic[1]] = "I"
		self.casas[(self.inic[0],self.inic[1])] = ["I", "Loja",0,[]] # TIPO DE CASA | Special Interactions | Dificuldade | Ocupações por Players/Monstros

		while self.n_blocos - 1 > 0:
			
			if self.map[spot[0]][spot[1]] == 0:
				self.map[spot[0]][spot[1]] = "X"
				self.casas[(spot[0],spot[1])] = ["X","-",dificuldade*((inic[0] - spot[0])**2 + (inic[1] - spot[1])**2),[Unit("Nome", 100,10)]]
				self.n_blocos += -1
			else:
				r = random.randint(1, 4)

				if r == 1: # Andar para cima
					if spot[0] - 1 >= 0:
						spot[0] += -1

				elif r == 2: # Andar para baixo
					if spot[0] + 1 <= size-1:
						spot[0] += 1

				elif r == 3: # Andar para esquerda
					if spot[1] - 1 >= 0:
						spot[1] += -1

				elif r == 4: # andar para direita
					if spot[1] + 1 <= size-1:
						spot[1] += 1


	def show_map(self):
		for i in self.map:
			print(i)

	def show_casas(self):
		print(self.casas)

	def finished(self):
		if self.casas["end"][3] == []: 
			return True
		else:
			return False 

mapa = Mapmaker(10,20,1,1,(1,1),1,[], {})
mapa.show_map()
mapa.show_casas()
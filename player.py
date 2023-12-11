"""
Classe para criar os players para o jogo
"""
from mapmaker import Mapmaker

class Player:

	def __init__(self, nome, hp, dmg, cod):
		self.nome = nome
		self.hp = hp
		self.dmg = dmg
		self.code = code

	def show_hp(self):
		return self.hp

	def show_name(self):
		return self.nome

	def do(self, act, Map):
		if act == "MU":
			pass
		if act == "MD":
			pass
		if act == "ML":
			pass
		if act == "MR":
			pass
		if act == "B":
			pass
		if act == "RP":
			pass
		if act == "A":
			pass
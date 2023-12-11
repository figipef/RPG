"""
Class Unidade, nomeadamente adversários que serão colocados no mapa
"""
class Unit:
	def __init__(self, name, health, damage):

		self.health = health
		self.damage = damage
		self.name = name
		#self.code = code

	def update_health(self,hp_dif):
		self.health += hp_dif

	def update_damage(self,dmg_dif):
		self.damage += dmg_dif

	def show_damage(self):
		return self.damage

	def show_name(self):
		return self.nome

	def show_hp(self):
		return self.health
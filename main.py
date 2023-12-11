from unit import Unit
from mapmaker import Mapmaker
from player import Player
from game import game

if __name__ == "__main__":

	resposta = 0
	players = []
	cod = 0
	while resposta != 1:
		resposta = input("Que deseja fazer (N - criar personagem, 0 - começar o jogo)): \n")

		if respota == "N":
			Nome = input("Nome do Personagem: \n")
			players.append(Player(Nome, 100, 10,cod))
			cod += 1

	creaturas = { #Nome, hp, dmg, dificuldade normalizada
	1 : ["Slime", 10, 2, 0.1],
	2 : [""]
	}

"""
Programa para fazer com que o jogo ande para a frente
"""

def game(Map,Players):
	while not Map.finished():
		for i in Players:

			act = input(f"Jogada do {i.show_name()}: \n")
			i.do(act, Map)



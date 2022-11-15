FILE = 'solucion4.txt'

def generate_solution(solucion):
	with open(FILE, "w+") as sol:
		for numero_lavado, prendas in solucion.items():
			for prenda in prendas:
				sol.write(prenda + " " + str(numero_lavado) + "\n")

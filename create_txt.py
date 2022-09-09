def generate_solution(solucion):
	with open("solucion2.txt", "w+") as sol:
		for numero_lavado, prendas in solucion.items():
			for prenda in prendas:
				sol.write(prenda + " " + str(numero_lavado) + "\n")

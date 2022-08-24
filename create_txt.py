def generar_archivo_solucion(solucion):
	with open("solucion.txt", "w+") as sol:
		for numero_lavado, prendas in solucion.items():
			for prenda in prendas:
				sol.write(prenda + " " + str(numero_lavado) + "\n")

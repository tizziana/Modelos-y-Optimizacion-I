from grafo_lavanderia import Lavanderia

def mannage_line(lavanderia, line):
	type = line[0]

	if (type == "e"):
		lavanderia.agregar_prendas_incompatibles(line[1], line[2])
	
	elif (type == "n"):
		lavanderia.agregar_prenda(line[1], line[2])


def creacion_grafo():
	try:
		lavanderia = Lavanderia()
		with open("Primer_Problema.txt", 'r') as file:
			
			for line in file:
				mannage_line(lavanderia, line.split())		

		return lavanderia	

	except Exception as e:
		print("[ERROR] No se pudo abrir el archivo de lavanderia.")


def solucion_lavados(lavanderia):
	lavados = {}
	prendas_ordenadas = dict(sorted(lavanderia.obtener_prendas().items(), key=lambda item: -item[1]))

	numero_lavado = 1
	for prenda in prendas_ordenadas:
		for lavado in range(1, numero_lavado + 1):
			if lavanderia.es_compatible(prenda, lavados.setdefault(lavado, [])):
				lavados[lavado].append(prenda)
				break

		numero_lavado += 1

	print("LAVADOS: ")
	print(lavados)
	return lavados
		

def generar_archivo_solucion(solucion):
	with open("solucion.txt", "w+") as sol:
		for numero_lavado, prendas in solucion.items():
			for prenda in prendas:
				sol.write(prenda + " " + str(numero_lavado) + "\n")


def main():
	lavanderia = creacion_grafo()
	generar_archivo_solucion(solucion_lavados(lavanderia))


main()
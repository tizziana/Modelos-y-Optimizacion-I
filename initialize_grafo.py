from grafo_lavanderia import Lavanderia
PROBLEM_FILE = 'Cuarto_Problema.txt'

def mannage_line(lavanderia, line):
	type = line[0]

	if (type == "e"):
		lavanderia.agregar_prendas_incompatibles(line[1], line[2])
	
	elif (type == "n"):
		lavanderia.agregar_prenda(line[1], line[2])


def create_grafo():

	try:
		lavanderia = Lavanderia()
		with open(PROBLEM_FILE, 'r') as file:
			for line in file:
				mannage_line(lavanderia, line.split())		

		return lavanderia	

	except Exception as e:
		print("[ERROR] No se pudo abrir el archivo de lavanderia.")


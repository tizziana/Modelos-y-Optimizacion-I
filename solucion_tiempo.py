
def tiempo_total_lavados(lavanderia, archivo_solucion):
	
	tiempo_total = {}
	with open(archivo_solucion, 'r') as file:
		lines = file.readlines()

		# prenda, lavado
		for line in lines:
			linea = line.strip('\n').split(' ')
			numero_prenda = linea[0]
			numero_lavado = linea[1]
			
			tiempo_prenda_lavado = lavanderia.obtener_datos_prenda(numero_prenda)

			if not numero_lavado in tiempo_total:
				tiempo_total[numero_lavado] = tiempo_prenda_lavado

			elif tiempo_total[numero_lavado] < tiempo_prenda_lavado: 
				tiempo_total[numero_lavado] = tiempo_prenda_lavado

	return sum(tiempo_total.values()), len(tiempo_total.keys())
class Lavanderia:

	def __init__(self):
		self.prendas = []
		self.prendas_incompatibles = {}
		self.prendas_tiempo_lavado = {}
		self.cantidad_vertices = 0
		self.cantidad_aristas = 0


	def agregar_prenda(self, prenda, tiempo_lavado_prenda):
		if self.prendas(prenda):
			return False

		self.prendas_tiempo_lavado[prenda] = tiempo_lavado_prenda
		self.cantidad_vertices += 1
		return True


	def obtener_datos_prenda(self, prenda):
		return self.prendas_tiempo_lavado[prenda]


	def agregar_prendas_incompatibles(self, prenda1, prenda2):
		#rari porque tengo las incompatibilidades antes que la ropa sooo esto no se chequearia
		# if not self.prendas_incompatibles(prenda1) or not self.prendas_incompatibles(prenda2):
		#	return False

		self.prendas_incompatibles[prenda1] = [prenda2]
		self.prendas_incompatibles[prenda2] = [prenda1]
		self.cantidad_aristas += 1
		return True

	def vertice_pertenece(self, prenda):
		return prenda in self.prendas_tiempo_lavado.keys()


	
	# leer el archivo
	# por cada e -> agregar al dicc de incompatib
	# por cada n -> agregar al dicc de tiempo_lavado
	# chequear que haya la misma cant de vertices y aristas que dice p edge 20 210
class Lavanderia:

	def __init__(self):
		self.prendas_incompatibles = {}
		self.prendas_tiempo_lavado = {}
		self.cantidad_vertices = 0
		self.cantidad_aristas = 0

	def agregar_prenda(self, prenda, tiempo_lavado_prenda):
		self.prendas_tiempo_lavado[prenda] = int(tiempo_lavado_prenda)
		self.cantidad_vertices += 1

	def obtener_datos_prenda(self, prenda):
		return self.prendas_tiempo_lavado[prenda]

	def agregar_prendas_incompatibles(self, prenda1, prenda2):
		self.prendas_incompatibles.setdefault(prenda1, []).append(prenda2)
		self.cantidad_aristas += 1
		
	def obtener_incompatibilidades(self, prenda):
		return self.prendas_incompatibles[prenda]

	def obtener_prendas(self):
		return self.prendas_tiempo_lavado

	def es_compatible(self, prenda1, lista_prendas):
		compatible = True
		
		for prenda in lista_prendas:
			if prenda in self.prendas_incompatibles[prenda1]:
				compatible = False

		return compatible

	def obtener_cant_prendas(self):
		return self.cantidad_vertices

	def obtener_cant_incompatibilidades(self):
		return self.cantidad_aristas
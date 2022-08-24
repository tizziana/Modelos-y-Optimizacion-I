from initialize_grafo import creacion_grafo
from create_txt import generar_archivo_solucion

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

	return lavados


def main():
	lavanderia = creacion_grafo()
	generar_archivo_solucion(solucion_lavados(lavanderia))


main()
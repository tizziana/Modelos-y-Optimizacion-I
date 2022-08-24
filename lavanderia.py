from initialize_grafo import create_grafo
from create_txt import generate_solution

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
	lavanderia = create_grafo()
	generate_solution(solucion_lavados(lavanderia))


main()
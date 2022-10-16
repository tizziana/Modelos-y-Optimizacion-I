# Tercera entrega
## Modelos y Optimización 

### Objetivos
   Determinar en qué lavado poner cada prenda para minimizar el tiempo total de lavados, cumpliendo con la condicion de que el tiempo total de un lavado se da por el tiempo que lleva lavar la prenda mas sucia en el mismo, es decir, por la prenda que lleva mas tiempo.

### Hipótesis y supuestos 
 - No se descompone ninguna maquinaria mientras se lava
 - El tiempo de lavado tiene en cuenta sacar y poner la ropa
 - No se tiene en cuenta el tiempo entre un lavado y otro
 

### Variables
[Siendo n el total de prendas]

i = 0,..,n

j= 0,..,n


- Ti: Tiempo de lavado de la prenda i 

Para saber en qué lavado va cada prenda:
- Yij = 1,  si la prenda i entra en el lavado j
- Yij = 0, sino


Por ahora contamos con que hay n lavados, y eso sería cierto en el peor de los casos, o sea cuando hay una prenda por cada lavado. Pero si tenemos mas de una prenda por lavado hay, entonces, menos lavados que numero de prendas. Por lo tanto tenemos la siguiente variable bivalente:

- Wj = 1, si el lavado se realiza 
- Wj = 0, sino


Ahora tenemos que agregar el tema de las incompatibilidades entre prendas, es decir, que las prendas que son incompatibles no pueden ir en el mismo lavado, por lo que necesitamos otra variable para asegurarnos de que esto no suceda:

- Euv = 0, si las prendas u y v son incompatibles
- Euv = 1, si las prendas u y v son compatibles


Por último, tenemos : 
Xij: tiempo de lavado de la prenda i en el lavado j

- Xj: tiempo del lavado j

### Modelo:
 min Z =  Σj Xj , j=1,..,n

- Si Wj está en cero (o sea, que ese lavado no se va a realizar) => Yij debe ser cero ∀i:

Yij ≤  Wj, si el lavado ∄ => ninguna prenda puede ir a ese lavado

- Una prenda sólo puede ir a un lavado:
 Σj  Yij = 1, j=1,..,n, ∀i:

- Las prendas u y v incompatibles no pueden encontrarse en el mismo lavado:

Yuj + Yvj ≤ Euv + 1

, y las prendas compatibles pueden, o no, ir en el mismo lavado


- Necesitamos que cada lavado tenga el valor de la prenda que lleva mas tiempo de lavado

Xij = Ti*Yij

Xij ≤ Xj ≤ Xij + M(1 - Max_ij),


siendo Max_ij = 1 si la prenda i en el lavado j  es la que tiene max tiempo de lavado,
y 0 sino:

Entonces:    Σi Max_ij = 1, i = 1,..,n 

Con esto último estamos diciendo que sólo puede haber un maximo dentro de las prendas del lavado j.

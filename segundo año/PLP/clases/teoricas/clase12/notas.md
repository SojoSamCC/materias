# Introducción

En un fórmula solo puede hacer símbolos de función, símbolos de predicado. El resto es sintaxis estándard de la lófica de primer orden.

La evaluación de una fórmula se mapea a un elemento del dominio.

Un predicado se define como un conjunto de n uplas.

Ejemplo:

```
    P := y + x = 10 
    (y, x) pertenece I(P)

    Luego (9, 1) pertenece a I(P)
```

Hasta cierto punto se puede pensar que la estructura es la implementación.

Demostrar que algo es invalido o satisfactible significa encontrar un ejemplo donde se cumpla la definición de inválido o satisfactible según corresponda.

Para demostrar que sea válido usamos el método de resolución!

Con resolución demostrabamos que ¬sigma es insatisfactible y por lo tanto sigma es válida.

Los métodos que sabemos para probar si una fórmula es válida son: deducción natural y resolución.

# Resolución SLD

EL proceso de elegir las dos cláusulas se le llama 'búsqueda'.

Un literal es una fórmula atómica.

La lógica proposicional es totalmente decidible, o sea, simpre podemos saber si una fórmula es o no válida.

Pasos principales en resolución:
- busqueda: encontrar dos cláusulas que puedan generar una nueva cláusula que no tenía antes en el conjunto de cláusulas.
- selección: seleccionar al conjunto de pares de literales que van a poder unificar entre sí.
- unificación: aplicar la unificación entre los pares de literales que elegí.

La resolución SLD es más óptima que la general PERO a cambio solo puede demostrar cierto conjunto de clásulas, es decir pierde generalidad en lo que puede demostrar.

Una cláusula de Horn es básicamente un cláusula que tiene cualquier cantidad de literales negativos y a lo sumo un literal positivo.

[meter las diapos]

Las azules son de definción y las negras son objetivo.

Con esto bajamos la complejidad temporal del método de resolución general. Es lineal en la búsqueda, lineal en la selección y lineal en la unificación.

La idea para demmostrar algo a partir de alguna hipótesis es:
metor entre $\land$ a nuestras hipótesis y decimos que eso implica lo que queremos demostrar.

Ejemplo:
```
Dado 1 y 2 y queremos demostrar 3. 
Entonces eso se nota como (1 ∧ 2) => 3.
Eso es equivalente a probar ¬((1 ∧ 2) => 3) ≡

≡ ¬(¬(1 ∧ 2) V 3) ≡
≡ ¬¬(1 ∧ 2) ∧ ¬3 ≡
≡ 1 ∧ 2 ∧ ¬3
```

En el ejemplo de la diapo: a es predicado, s es función y 0 es función también.

La interpretación es:

a es un predicado ternario donde el primer elemento de la tupla sumado con el segundo elemento de la tupla es igual al tercer elemento de la tupla.

```
S = MGU({a(s(0), X3, s(s(s(0)))) ?= a(s(X2), Y2, s(Z2))}) = 
{a(s(0), X3, s(s(s(0)))) ?= a(s(X2), Y2, s(Z2))} ~> Decompose
{s(0) ?= s(X2), X3 ?= Y2, s(s(s(0))) ?= s(Z2)}   ~> Decompose
{0 ?= X2, X3 ?= Y2, s(s(s(0))) ?= s(Z2)}         ~> Swap
{X2 ?=0, X3 ?= Y2, s(s(s(0))) ?= s(Z2)}          ~> Elim {X2 := 0}
{X3 ?= Y2, s(s(s(0))) ?= s(Z2)}                  ~> Elim {X3 := Y2}
{s(s(s(0))) ?= s(Z2)}                            ~> Decompose
{s(s(0)) ?= Z2}                               ~> Swap
{Z2 ?= s(s(0))}.
```

Ese Y4 está ahí porque tenemos que recordar que cada cláusula tiene un cuantificador universal y las variables pueden ser diferentes entre las cláusulas del conjunto de cláusulas. Entonces lo mejor es renombrarlo para evitar confusiones luego.

Para que sea SLD **SÍ O SÍ** tuvimos que haber hecho todos pasos de resolución SLD, con que haya hecho un paso o no se cumpliera algun requerimiento de la misma, entonces ya no es SLD.

# Semántica de Prolog

> Dato que puede ser útil: el ';' en prolog es una macro, que toma dos clásulas y las reescribe como una sola, investigar eso.

El orden de las cláusulas importa, fuertemente.

```
En prolog esto: P(a) => Q(X). Se escribe así Q(X) :- P(a).
```

IMPORTANTE:

A prolof no le importa el occurs-check. Con que prolog pueda unificar, ya lo toma como true.

> En Haskell las variables pueden aparecer una sola vez del lado izquierdo. Sí, Haskell.

[meter las diapos de semántica de prolog]

# Aspectos extra lógicos

El uso del cut (!) está prohibido en la guía porque generalmente se termina usando para evitar soluciones repetidas y eso no es una buena práctica de programación pues significa que teníamos errores lógicos en alguna definición de algún predicado.

No es que el cut (!) corta la ejecución apenas se llegue a él. Lo que sucede es que se termina de evaluar toda la definición de la cláusula y luego si en algún momento cuando se volvió a revisar esa cláusula, entonces se ignora y se sigue adelante. 

Revisar el patrón de instanciación es explicar qué pasa si voy instanciando o no cada argumento del predicado en la query.

El not está interesante en su definición porque si encuentra que una definición de un predicado falla entonces falla la primera cláusula del not y cuando cae en la segunda obtiene éxito. Caso contrario entonces pasa por el cut (!), devuelve la falla -completar-.

> Importante: el not NO instancia variables, es importante el orden en donde pongamos al not durante la definición de una cláusula.
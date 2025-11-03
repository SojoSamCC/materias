# Programación Lógica parte 1

# Mini intro

En la programación lógica no indicamos los pasos para ejecutar algo y tampoco funciones matemáticas.

Esto es darle reglas de razonamiento a la compu y dejar que la compu infiera el valor de verdad de un input con ese razonamiento.

# Bases de conocimiento

[meter diapo de bases de conocimiento]

Es el set de predicados, reglas y hechos que tomamos de base para luego resolver el ejercicio.

Todo lo que no sea una definición es un axioma. O sea:

```prolog
zombie(juan)
zombie(Valeria)

tomo_mate_despues(juan, carlos)
tomo_mate_despues(carla, juan)

infectade(ernesto)
```

```
La query ?- tomo_mate_despues(juan, X) NO es una función porque dado un input no nos devuelve siempre el mismo output. Porque precisamente, si fuera una función tomo_mate_despues(juan, X) entonces siempre devolvería UN X particular, en este caso si existiera una línea como tomo_mate_despues(juan, pepe) entonces el output de tomo_mate_despues(juan, X) sería carlos y pepe, y eso ya no es función.
```

Esto es lógica clásica porque si algo NO es verdadero entonces podemos decir que es Falso, ejemplo infectade(clara) porque no existe zombie(clara) o tomo_mate_despues(clara, alguien que era zombie).

¿En intuicionista vale eso?

El orden de las respuestas depende siempre del orden de la declaración de nuestras cláusulas en nuestra base de conocimiento.

# Sintaxis de prolog

[meter la diapo de la sintaxis]

si algo está en minúscula entonces es una constante.

# Ejercicios

[meter diapo]

```prolog
natual(cero)
natural(suc(X)) :- natural(X)
```
```
mayorA2(suc(suc(suc(X)))) :- natural(X)

es así porque se piensa como que: Te doy un X natural y eso implica que es mayor 3. O sea, me fijo si es mayor a 3.

Si hacemos 

?- mayorA2(suc(suc(suc(X)))).

Eso nos devuelve TODOS los X para que esto valga, prolog se fija un valor de X para que eso valga, simple. el primer valor válido sería X = cero porque suc(suc(suc(cero))) es válido. Si hicieramos

?- mayorA2(X).

Entonces nos devuelve a partir del suc(suc(suc(X))) porque prolog empieza a mostrar desde el primer valor de X para que esto mayorA2 sea válido, por definición eso es suc(suc(suc(X)))
```
```
Si hacemos trace en la consola podemos ver más o menos el flujo de cómo prolog va unificando.
```

```prolog
menor(cero, suc(X)) :- natural(X).
menor(suc(X), suc(Y)) :- natural(X), natural(X), menor(X, Y). 
```
Si queremos que algo sea False, entonces mejor que no exista una manera de que prolog unifique con eso que queremos.
```
amaALosGatos(Z).
    |{Z := John, Y := odie} ~> tieneMascota(John, odie)
    |   | gato(odie) ~> False
    |
    |{Z := John, Y := garfield} ~> tieneMascota(John, garfiel)
    |   | gato(odie) ~> True
```

# Reversibilidad

[meter diapo]

Esto tiene que ver cómo hacer el aproach con el pasaje de argumentos, la instanciación.

Estar instanciado es que le ponemos un valor al argumento del predicado.
No estar instanciado es que le ponemos una variable al argumento del predicado.

```
+X debe estar instanciado
-X no debe estar instanciado
?X puede o no estar instanciado
```

Ejemplo: el predicado natural es reversible en X.

¿Que sea reversible entonces es que pueda estar o no instanciado? ¿No reversible es que sí o sí deba estar instanciado o no estar instanciado pero no las dos a la vez?

# Aritmética

[meter diapo]

> Importante: E TIENE que ser una expresión aritmética y no cualquier otra cosa. O sea, el X is E es decir que X unifica con la reducción aritmética de E.

> Nota: el is básicamente lo vamos a usar con el único propósito de instanciar a lo de la izquierda con lo de la derecha.

```prolog
mi solución:

entre(X, Y, Y) :- X =< Y.
entre(X,Y,Z) :-
    Z >= X, % esto no anda porque Z no va a estar instanciada :O.
    Z =< Y,
    N is Y-1,
    entre(X,N,Z).
```
```prolog
La de la clase:

entre(X, Y, X) :- X =< Y.
entre(X, Y, Z) :-
    X < Y,
    N is X+1,
    entre(N, Y, Z)

esto es como que tengo [X, ..., Z, ..., Y] y vamos moviendo la X hasta llegar a Z. Cuando llegamos a Z nos fijamos si Z <= Y!!!
```

# Listas

[meter diapo]

```prolog
Mi solución:

long([], N) :- 0.
long([H | T], N) :- N is (1 + long(T, N-1)). % no se puede porque long es un predicado y no una función que devuelve algo, el predicado devuelve un valor de verdad.
```
```prolog
Solución de la clase:

long([], 0). % esto es lo mismo que lo que hice yo pero más lindo.
long([_ | T], N) :- long(T, M), N is M+1.
```

> predicado/numero se refiere a que el predicado toma numero argumentos.

Es reversible en N porque en la segunda línea no estamos usando ninguna instanciación de N. 

```prolog
mi solución:

no_esta(X, []).
no_esta(X, [H | T]) :- X \= H, esta(X, T).

sacar(_, [], YS).
sacar(X, L, YS) :- no_esta(X, L), YS is L. % No vale porque L no es una expresión aritmética.
```
```prolog
sacar(_, [], []).
sacar(X, [X | T], L) :- sacar(X, L).
sacar(X, [H | T], [H | L]) :- X \= H, sacar(X, T, L)
```
```
Mi solución:

sacar_uno(_, [], []).
sacar_uno(X, [X | T], T).
sacar_uno(X, [H | T], [H | L]) :- X \= H, sacar_uno(X, T, L)

sinConsecRep([], []).
sinConsecRep([H | T], YS) :- sacar_uno(H, T, YS), sinConsecRep(T, YS).
```
```
Solución de alguien en la clase:

sinConsecRep([], []).
sinConsecRep([H], [H]).
sinConsecRep([H, H | T], [H | T]) :-
    sinConsecRep(T, T) :-
sinConsecRep([H, X | T], [H, X | T]) :-
    sinConsecRep([X | T], [X | T]). 
% falla con sinConsecRep([1,1,1])

otra:
sinConsecRep([], []).
sinConsecRep([H], [H]).
sinConsecRep([H, H | T], L) :-
    sinConsecRep([H | T], L) :-
sinConsecRep([H, X | T], [H, X | T]) :-
    sinConsecRep([X | T], [X | T]). 
% falta ver que sean diferentes y hay otro error pero no sé cuál es.


Solución de la clase:

sinConsecRep([], []).
sinConsecRep([H], [H]).
sinConsecRep([H, H | T], L) :-
    sinConsecRep([H | T], L).
sinConsecRep([H, X | T], [H, X | L]) :-
    H \= X, sinConsecRep([X | T], [X | L]). 
```

> Que le pongamos nombres distintos a las variables no significa que no puedan ser iguales.

```prolog
% append es reversible en todos sus argumentos.

Solución de la clase:

prefijo(XS, PS) :- append(PS, _, XS).
```

# append está piola

```
Hacer append(L1, L2, [1,2,3]) me da todas las maneras de armarme la lista [1,2,3].
```

# capicua

[poner diapo y estudiarla bien].

# estudiar member también.


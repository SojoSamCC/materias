# Programación lógica 2

[meter diapos introductorias]

que estpe semi instanciado siginifica que está la estructura pero que no todos los elementos de la estructura están instanciados.

los predicados var, nonvar, y ground son útiles.

ground se usa para las estructuras que están seminstanciadas.

> Función de predicado = Predicado.

# Ejercicio: iésimo

```prolog
% iesimo(+I, +L, -X)
iesimo(0, [X | _], X).
iesimo(I, [_ | T], X) :- 
    I > 0, 
    N is I-1, 
    iesimo(N, T, X).

Si el I es negativo entonces no hay problema porque en algun momento la lista se va a acabar y vamos a obtener false.
```

importante: que algo sea reversible en un parámetro significa. 
    perimero hay que decir qeu el predicado funciona con ese paramatero con una isntanciación disrinta a la pedida.
    la pregunta es ¿Funciona el predicado para la variable con una instanciación diferente? Hay que explicar que funciona en la instanciación pedida y en la contraria.

    Lo importante: justificar que el predicado es reversible en una varaible:
        1. no hay error.
        2. que el predicado hace efectivamente lo que debería de hacer con ese instanciado.

    Que todos los predicados internos sean reversibles, no significa que el predicado original es reversible.

    1. No falla.
    2. Funcione correctamente.
    3. Funcione con la instanciación pedida.

    La reversibilidad SIEMPRE se evalúa mirando de a 1.

En este caso el I debería de darme el índice de todos los elementos con la I sin instanciar.

1. Mirar el código con la I sin instanciar y ver que no falle. En este caso falla por el I > 0 y con J is I-1.
2.

Para que sea reversible podemos hacer:

```prolog
iesimo_reversible(0, [X | _], X).
iesimo_reversible(I', [_ | T], X) :-
    iesimo_reversible(J, T, X'),
    I' is J + 1
```

Funciona porque en cada pasa el iseimo me lo instancia el resultado recursivo, veamos el arbol.

```
iesimo_reversible(I, [1, 2, 3], X)
    iesimo_reversible(0, [2, 3], [])                            ~> True. {I := 0, X := 1}
    iesimo_reversible(0, [1, 2, 3], 1)                          {I := I', X := X', T := [2, 3]}
        iesimo_reversible(J, [2, 3], X'), I' is J+1
            I' is 0 + 1                                         {J := 0, X := 2}
                1 is 0 + 1                                      {I' := 1}

Tengo una foto, subirla.

Esto no sirve para justificar reversibilidad, hay que hacerlo con palabras y brevemente.
```

# Ejercicio: predicado desde.

da todos los números desde un número X en adelante.

el primero (la X) sí o sí debe venir instanciado porque tengo que hacer una operación aritmética.

El Y no debe estar instanciado porque se cuelga (creo). EDIT: correcto porque durante la ejecución se llama a desde(X, Y) con X > Y y eso se cuelga porque cada vez llama a un X con un X mayor.

Para justificar que Y no es reversible:

No es reversible porque no tiene condición de corte y una vez que el primero argumento sea mayor que el segundo entonces comienza una recursión infinita.

> Si en algún momento se cuelga la ejecución entonces se dice que "el predicado se cuelga".

```
% desde_reversible(+X, ?Y).

desde_reversible(X, Y) :- var(Y), desde(X, Y).
desde_reversible(X, Y) :- nonvar(Y), Y >= X.

```

En general cuando una reversibilidad se cuelga, un tip para manejar con los predicados infinitos para que sean reversibles conviene usar var, nonvar; mas que nada para dividir en casos de: si es variable: hago algo, sino otra cosa.

# Ejercicio pmq: pares menores que.

```

% pmq(+X, -Y).

pmq(X, Y) :- between(0, X, Y), mod(Y, 2) =:= 0.

Está cheta esta definición está cheta porque es como decir: Y está entre 0 y X, y luego fijate que Y es par.

mod es parte del motor aritmético, no es un predicado sino una función.
```

Esta técnica se usa en prolog, se llama Generate & Test: generamos todos los números en un rango y luego filtramos por los que cumplen con lo que queremos.

# Ejercicio: coprimos.

```
% coprimos(-X, -Y)

coprimos(X, Y) :- armarPares(X, Y), gcd(X, Y) =:= 1.

armarPares(X, Y) :- desde(0, S), between(0, S, X), Y is S-X.

El desde me instancia todos los numeros infinitamente, obtengo todos los valores entre 0 y S y luego me fijo la resta entre Y y ese numero entre 0 y S.
```

> Importante: Leer las leyes de generación infinita.

No es reversible en X e Y porque si les pasamos instanciados entonces: ok, vamos a encontra una generación que tenga esa instanciación PERO, luego el predicado va a ponerse a buscar infinitamente por otro par que cumpla eso y eso nunca va a ocurrir.

La justificación: no es reversible porque si yo le paso instanciadas X e Y en algun momento sesatisface la suma, pero el predicado desde genera infinitamente, con lo cual nunca va encontrar una suma que cumpla al par X e Y instanciado con lo cual la recursión sería infinita.

# Soluciones repetidas

[Meter slide de esto]

> Importante: El único metapredicado que podemos usar en la guía y en el parcial es not.

> Recuerdo: el not NO instancia. Solo devuelve True o False. No genera ninguna instanciación.

> OJO: Prolog SIEMPRE va a entrar por donde pueda entrar a menos que se le diga lo contrario.

> Nunca trabajar con un predicado pensando en: "me quedo con las primeras soluciones" o similar.

No sirve la versión dada vuelta porque ese not mete una falla porque existe una instanciación de abuela que da True, entonces el not falla y nunca vemos los progenitores.

En la versión de arriba las X e Y están instanciadas por el progenitos.

Esta es una solución, puede haber más ¿Funcionará haciendo un swap entre las definciones de pariente y sacando el not?.

---

# Negación por falla

> IMPORTANTE: el not no es la negación lógica de un predicado, sino que funciona como un no existe instanciación tal que se cumple lo de adentro.

> hacer not((P(X), Q(X))) (sí, con doble paréntesis), lo que hace es fijarse que no exista una instanciación de X que cumpla P(X) y Q(X).

```
% corteMasParejo(+L, -L1, -L2)
corteMasParejo([], [], []).
corteMasParejo(L, L1, L2) :- sumlist(L1, SL1), sumlist(L2, SL2), no sé, veo la clase
```
```
% unCorte(+L, -L1, -L2, -D) Hacer esto se le llama patrón de isntanciación y siempre hay que ponerlo en nuestras funciones auxiliares y explicar cómo las vamos a usar.

unCorte(L, L1, L2, D) :- 
    append(L1, L2, L), 
    sumlist(L1, S1), 
    sumlist(L2, S2),
    D is abs(S1-S2).

corteMasParejo(L, L1, L2) :- unCorte(L, L1, L2, D), not( (unCorte(L, _, _, D2), D2 < D) ).

Es reversible en L1 y L2 porque en nuestras definiciones siempre terminamos instanciando sin problema a las variables.
```

# proximo primo:

```
divisores(X, D) :- between(1, X, D'), X mod D' =:= 0.

esPrimo(2).
esPrimo(X) :- divisores(X, D), D is 1. 

% proximoPrimo(+X, -P)
proximoPrimo(X, P) :- esPrimo(P), P > X, no sé como meter el literal del not.
```
```
siguientePrimo(+N)
siguientePrimo(N, P) :-  

primo(N) :- 
    N > 1,
    N1 is N-1,
    not((between(2, N1, V), N mod V =:= 0)).

proximoPrimo(N, P) :- N1 is N+1, siguietePrimo(N1, P).

```

> El not sirve como un forall. Es útil! pensarlo y masterizarlo.

se me acaba la batería. Luego completo.

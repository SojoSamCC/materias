# Clase práctica de cálculo Lambda $\lambda$ --- Cálculo $(\lambda x. \ Lxmbdx) \ a$

utils
$$
\lambda
\vdash
\tau
\sigma
$$

# Sintaxis

[slide3]

fv es una función que toma el conjunto de todos los terminos y que me devuelve el conjunto de partes de las variables en los términos.

## Ejercicios de variables libres y ligadas

FV(x) = {x}

FV(true) = $\empty$

FV(false) = $\empty$

FV(if M then N else P) = FV(M) U FV(N) U FV(P)

FV(M N) = FV(M) U FV (N)

FV($\lambda\ x:\ \sigma.\ M$) = FV(M) - {x}

Un término es cerrado si no tiene variables libres, o sea FV(M) = $\empty$

## Ejercicios
[slide 4]

a)
$\lambda\ x:$ Bool->Bool.x true

FV($\lambda\ x:$ Bool->Bool.x true) = {true}

Las varaibles ligadas son {x}

Árbol sintáctico:

```
                            λ x: Bool->Bool.x true
                                    |  abs --- todo lo que es sintaxis lo borro. Me quedo con el cuerpo
                                    |           de la lambda.
                                    x true
                                    | app
                                    |
                            ___________________
                            |                 |
                            x                true
```


b)

x y $\lambda\ x:$ Bool->Bool.x y

alfa renombre: z y $\lambda\ x:$ Bool->Bool.x y

FV(z y $\lambda\ x:$ Bool->Bool.x y) = {z, y} --- La y es la misma porque es una variables libre
                                                  Toda variable libre es la misma en todo el contexto.

Las varaibles ligadas son {x}

Árbol sintáctico:

```
                        z y λ x: Bool-> Bool.x y 
                         |    app   |   
                        z y         λ x: Bool->Bool. x y
                        | | app               |
                        z y                   | abs
                                              |
                                             x y
                                             | | app
                                             x y
```

c)

($\lambda\ x:$ Bool->Bool.x y) ($\lambda$ y:Bool. x)
           |              | |             |        |
           ________________  libre      ligada     libre
           ligadas esas x's

FV(($\lambda\ x:$ Bool->Bool.x y) ($\lambda$ y:Bool. x)) = {x, y}

```
                    (λx: Bool->Bool. x y) (λy: Bool. x)
                    |               app               |
                λx: Bool-> Bool. x y                λy:Bool.x
                   | abs                               | abs
                   |                                   x
                  x y
                  | | app
                  x y
```


d) no se puede, está incompleto.

e) está mal porque le falta el tipo.

f) 

if x then y else (λz: Bool. z)

FV(if x then y else (λz: Bool. z)) = {x, y}

La variable z está ligada.

```
                    if x then y else (λz: Bool. z)
                    |            |               | if
                    x            y          (λz: Bool. z)
                                                 | abs
                                                 z
```

g) λy: $\sigma$. y |||| No se puede porque $\sigma$ es una meta variable de tipos y no existe en nuestro universo actual.

h) true false |||| no tipa pero es un término sintácticamente bien formado porque es una aplicación.

i) x M |||| M no es un término, no anda.

j) if x then (λx: Bool. x) |||| no es correcto sintácticamente.


# Tipado

[slide 5 y 6]

$\Gamma \vdash M:\tau$ "Bajo el contexto Gamma, M es de tipo tau".

## Ejercicios

a)
```
    ___________T-VAR ______________T-TRUE          ____________T-VAR
    R ⊢ x: Bool      R ⊢ true: bool                R ⊢ y: bool
    ______________________________________________________________T-IF
    R = {x:Bool, λy:Bool} ⊢ (if x then true else y): Bool
    ______________________________________________________________T-ABS
    x:Bool ⊢ (λy:Bool. if x then true else y): Bool-> Bool
    _________________________________________________________T_ABS      ______________________T-FALSE
    ⊢ (λx: Bool. λy:Bool. if x then true else y): Bool-> Bool -> Bool   ⊢ false: Bool -> Bool
    __________________________________________________________________________________________T-APP
        ⊢ (λx: Bool. λy:Bool. if x then true else y) false: Bool -> Bool
```

b) 

```
        __________________________T-TRUE
            x: bool ⊢ true: bool
```

c) no hay información en el contexto y tengo variables libres, entonces no voy a poder afirmar que x es de tipo Bool cuando la logre "aislar" del resto del término. Esto pasa porque el término no es cerrado.

d) Los tipos de lo que lo devuelve porque necesito que x: Bool -> Bool y al mismo tiempo que x: Bool. Para poder demostrar que esto no tipa se puede hacer el árbolde tipado y demostrar el momento en que no tipa.


Hay que hacer los ejercicios de la slide 8. 

b)

$(\tau \rightarrow \rho) \rightarrow (\sigma \rightarrow \tau) \rightarrow (\sigma \rightarrow \rho)$

--- Se puede pensar como en haskell que es un una función que recibe un f y un g y devuelve algo de tipo $(\sigma \rightarrow \rho)$

Respuesta:

$\lambda f:\tau \rightarrow \rho. \ \lambda g:\sigma \rightarrow \tau. \ \lambda x:\sigma$. f (g x)

Es la función composición (.).

c) 

$\sigma \rightarrow \tau$ --- es una función porque tiene una flecha.

Busquemos alguna función que cumpla eso.

$\sigma: Bool. \ \tau:Bool. \ \lambda x:Bool. x : Bool \rightarrow Bool$

$\sigma: Bool. \ \tau:Bool->Bool. \lambda x:Bool. \ \lambda y:Bool. y: \ Bool \rightarrow Bool \rightarrow Bool$

No hay manera de encontrar una función que esté habitada porque sigma y tau no tienen ninguna relación.

Lo de arriba no fue una demostración.

# Semántica

En el call by name siempre nos va interesar reducir a un valor antes de pasarlo a una lambda.

# Semántica operacional

Los valores son términos que no se pueden reducir y que son cosas que nos interesan que nuestro programa devuelva.

Las reglas de congruencia sonlas que me reducen a valores. Las reglas de cómputo son las que me resuelven los valores. O sea, la regla d econgruencia es la que me permite decidir por cuál rama ir y la de cómputo es la que me resuelve una rama.


f) es un valor. Si el f tuviera parentesis desde el principio hasta antes del false, entonces sería aplicación y no sería valor.
g) es un valor.

## Ejercicio reducciones

a)
```
((λx: B. λy: B. if x then true else y) false) true
______________________________________ ______ _____
                M                       N       O
```

Tiene forma ((λ M') V1) V2

```
((λx: B. λy: B. if x then true else y) false) true    ---> E-App1, E-AppAbs --> 
(λy: B. if false then true else y) true               ---> E-AppAbs         -->
if false then true else true                          ---> E-IfFalse        -->
true                                                  ---> es valor.
```

b) 
```
(λx: B. λy: B-> B. y (y x)) ((λz: B. true) false) (λw: B. w)
___________________________ _____________________ __________
            M                           N               O


Tiene forma ((M N) O)

Con O = Valor
Con N = λ V1
Con M = Valor
```

```
(λx: B. λy: B-> B. y (y x)) ((λz: B. true) false) (λw: B. w) ---> E-App1, E-App2, β -->
(λx: B. λy: B-> B. y (y x)) (true) (λw: B. w)                ---> E-App1, β         -->
(λy: B-> B. y (y true)) (λw: B. w)                           ---> β                 -->
(λw: B. w) ((λw: B. w) true)                                 ---> E-App2, β  *nota* -->
(λw: B. w) true                                              ---> β                 -->
true                                                         ---> es valor.

*nota* Porque lo de la izquierda es valor y la derecha no es valor. Notar que si aplicabamos β sin E-App2 llegabamos al mismo resultado pero estaba mal hecho el pasaje.
```


## Ejercicio determinismo

La idea es usar lemas de generación en cada regla que tenemos y lo que tenemos que hacer es por ejemplo elegir una regla, luego plantear que tenemos M -> M1 y M -> M2 y ver que si tenemos esa regla entonces M tiene que tener una forma en particular y evaluar que ambos lados de la -> no se pueden reducir con ninguna otra regla y que por lo tanto M -> M2 tiene que ser igual sí o sí a M -> M1


# Extensión con números naturales

Dentro de los valores tenemos Succ(V) y V solo puede ser zero o Succ(V') con V: Nat, inclusive si es una lambda con tipo Nat no cuadra porque va a ser de tipo Nat -> algo y no matchearía.

Los números son valores, no reducen a nada.

--- Se saltearon los ejercicios de juicio de tipado ---

```
isZero(Succ(Pred(Succ(zero))))                      ---> E-IsZero, E-Succ, E-PredSucc -->
isZero(Succ(zero))                                  ---> E-IsZero_n                   -->
false    
```

```
isZero(pred(succ(pred(zero))))                      ---> E-IsZero, E-Pred, E-Succ     -->
No reduce, es una forma normal.
```

```
isZero(pred(succ(pred(x))))                         ---> E-IsZero, E-Pred, E-Succ     -->
No tipa en el contexto vacío porque tiene una variable libre, entonces ni siquiera lo vamos a considerar un programa, entonces no podemos hacer más nada con él.
```

**Las Macros**

Es tomar un término que ya existe y le ponemos un nombre para luego hacer reemplazo sintáctico.

Ejemplo:

$id_{\tau} = \lambda x: \tau. \ x$

$and = \lambda x: \ Bool. \ \lambda y:\ Bool.$ if x then y else false

**Reducir el cuerpo de la lambda**: 

Si $M \rightarrow N$, entonces: $\lambda x: \ \tau.\ M \rightarrow \lambda x: \tau. N$ ($\zeta$)
```
lambda x: nat. pred(succ(0)) -> e-app1, zeta -> (lambda x: N. 0) 0 
pero también podiamos hacer lambda x: nat. pred(succ(0)) -> beta -> pred(succ(0))
```

```
λz: N-> N. ((λx:N->N. x 23) λz:N. 0) -> ζ, β 
λz: N-> N. (λz:N->N. 0) 23 -> ζ, β 
λz:N->N. 0
```



# Notas
- Usar letras mayúsculas para términos y minúsculas para variables.
- M N se dice: M se aplica a N
- Solo se pueden renombrar a las variables libres.
- En el juicio hay un término, en el término las variables pueden estar libres o ligadas.
- Si me llega a pasar que caigo en la regla de tipado T-VAR y la variable no tiene tipo en el contexto, entonces es porque o hice algo mal o porque la variable era libre y nunca voy a poder sacarmela de encima (eso significa que le término orignal no era cerrado y entonces no se podía hacer un juicio sobre él).
- "Las lambdas tiene tipo flecha".
- Para demostrar que un tipo está habitado significa que para cualquier tipo que se me da de sigma o tau o rho o el que sea, entonces la función siempre tipa correctamente si se les reemplaza en la función.
- Valor es una forma normal. Particularmente un termino que no reduce más.
- Una forma normal que no es valor puede ser una variable libre o algo que tenga una variable libre.
- El determinismo es sumamente importante en la materia.
- Si un término se puede reducir entonces automáticamente no es un valor. Para que sea un valor entonces tiene que ser cerrado, bien tipado y tiene que estar definido en nuestra gramática de valores.
- La cantidad de reglas de cómputo debe ser igual a la cantidad de valores posibles, las reglas de congruencia pueden haber todas las que uno necesite. 
- El "progreso" es la idea de que: si tengo un término que es una forma normal y no es valor entonces debería poder reducirlo (no interesa el caso en que no es valor y no es cerrado porque queremos que siempre tipe todo).
- El determinismo es => Solo puedo agregar una regla en todo momento!
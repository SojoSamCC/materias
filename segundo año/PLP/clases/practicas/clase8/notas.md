# Clase inferencia de tipos

[meter diapos iniciales]

Si no hay variables libres entonces no necesitamos contexto.
```
{y: Nat} ⊢ λx: X1. succ(y) : X1 -> Nat
```

El más general es el último porque es la identidad, queremos que reciba algo y devuelva lo mismo, independientemente de su tipo.

Cuando decimos que un juicio es el más general, decimos que tenemos una instancia de lo que está en la diapo y podemos hacer cualquier sustitución y eso siempre va a tipar.

# Ejercicio inferir a ojo

```
λx. y
{y: X2} ⊢ λx: X1. y : X1 -> X2
```
```
{f: Bool -> X1} ⊢ f true: X1
```
```
{x: Nat} ⊢ isZero(x) : Bool 
```

# MGU

```
MGU {X2 -> X1 -> Bool = X2 -> X3} =     
    {X2 -> (X1 -> Bool) = X2 -> X3}     -> Decompose
    {X2 ?= X2, X1 -> Bool ?= X3}        -> Delete
    {X1 -> Bool ?= X3}                  -> Swap
    {X3 ?= X1 -> Bool}                                

    S = {X2 -> x1 -> Bool} = S (X2 -> X3) 
```
```
MGU = {(X2->X1) -> Nat ?= X2 -> X3}      -> Decompose
MGU = {X2 ->X1 ?= X2,  Nat ?= X3}        -> Swap
MGU = {X2 ?= X2 ->X1,  Nat ?= X3}        -> Occurs-Check
MGU = Falla
```
```
MGU = {X1 -> Bool ?= Nat -> Bool, X2 ?= X1 -> X1}   -> Elim S1 = {X2 := X1 -> X1}
    {X1 -> Bool ?= Nat -> Bool}                     -> Decompose      
    {X1 ?= Nat, Bool ?= Bool}                       -> Decompose      
    {X1 ?= Nat}                                     -> Elim S2 = {X1 := Nat}
    {}


    (S2 ° S1) (X) = S2 (S1 (X))
    
    S = S2 ° S1 = {X1 := Nat} ° {X2 := X1 -> X1} =

    ||| Esto se puede hacer S2 (S1 (Xi)) = S2 (Xi) = Xi, con i != 2 y i != 1 |||

    = {X1 := Nat, X2 := Nat -> Nat} = S
```

> Delete es SOLO para variables, decompose nos saca los constructores igualados.

# Notas

- El MGU es único salvo renomrbe de variables.
- EL orden en el MGU no importa mucho porque es un conjunto.

# Algoritmo de Inferencia de tipos

[Meter las diapos de los pasos]

1. Siempre podemos rectificar gracias a alfarenombre

    ```
    Rectificar:

    (λf. λx. f (f x)) (λf. f) ~> FV = {}

    (λf. λx. f (f x)) (λg. g)
    ```
    ```
    Rectificar:
    x (λx. Succ(x)) ~> FV = {x de la lambda}

    x (λy. Succ(y))
    ```

2. .
    ```
    M0 = λf: X1. λx: X2. f (f x)
    R0 = {}
    ```
    ```
    M0 = x (λy: X2. Succ(y))
    R0 = {X: X1}
    ```

3. [Meter la diapo con las reglas]

4. [Meter la diapo del paso 4 de MGU], ese tau que aparece es el tipo que generamos en el paso 3.

# Ejemplo

```
λf. λx. f (f x)

1. Rectificar: Listo

2. Anotación: 
    M0 = λf: Xf. λx: Xx. f (f x)
    R0 = {}
                                                        ***
                                                   ______________
3. I( {} | λf: Xf. λx: Xx. f (f x))             = (Xf -> Xx -> X2 | E)
        I({f: Xf} | λx: Xx. f (f x))            = (Xx -> X2 | Xf ?= X1 -> X2, Xf ?= (Xx -> X1))
            I({f: Xf, x: Xx} | f (f x))         = (X2 | Xf ?= X1 -> X2, Xf ?= (Xx -> X1))
                I({f: Xf, x: Xx} | f )          = (Xf | {}) 
                I({f: Xf, x: Xx} | f x )        = (X1 | Xf ?= (Xx -> X1))
                    I({f: Xf, x: Xx} | f )      = (Xf | {})
                    I({f: Xf, x: Xx} | x )      = (Xx | {})

4. MGU = {Xf ?= X1 -> X2, Xf ?= (Xx -> X1)}      -> Elim {Xf := X1 -> X2}
        {X1 -> X2 ?= (Xx -> X1)}                 -> Decompose
        = {X1 ?= Xx,  X2 ?= X1}                  -> Elim {X1 := Xx}
        = {X2 ?= Xx}                             -> Elim {X2 := Xx}
        = {}

    S = {X2 := Xx} ° {X1 := Xx} ° {Xf := X1 -> X2} 
      = {X2 := Xx, X1 :=Xx, Xf := Xx -> Xx}
    
    Juicio de tipado más general es:

        S(R0) |- S(M0) : S(Xf -> Xx -> X2) = 
                           _______________
                           Este cacho es ***

        = S(R0) |- S(M0) : (Xx -> Xx) -> Xx -> Xx
        
        = {} |- λf: Xx -> Xx. λx: Xx. f (f x) : (Xx -> Xx) -> Xx -> Xx
```
```
λx. x y x

1. Rectificado: sí

2. Anotación: 
    M0 = λx: X1. x y x
    R0 = {y: X2}

3. I({y: X2} | λx: X1. x y x)             = (X1 -> X4 | X3 := X1 -> X4, X1 ?= X2 -> X3)
    I({y: X2, x: X1} | x y x)             = (X4 | X3 := X1 -> X4, X1 ?= X2 -> X3)
        I({y: X2, x: X1} | x y)           = (X3 | X1 := X2 -> X3)
            I({y: X2, x: X1} | x)         = (X1 | {})
            I({y: X2, x: X1} | y)         = (X2 | {})
        I({y: X2, x: X1} | x)             = (X1 | {})

4. MGU = {X3 := X1 -> X4, X1 ?= X2 -> X3}       -> Elim {X3 := X1 -> X4}
    {X1 ?= X2 -> X1 -> X4}                      -> Occurs-Check
    Falla

    Finalmente el término λx. x y x no tiene tipo.
```

# Notas
- Hay que estar muy pendiente de qué está ligando una variable y qué no
- No se pueden renombrar las variables libres, solo las ligadas.

# Extensiones de I con  extensiones del cálculo lambda

El ejercicio de la diapo tiene mayor dificultad de un parcial. Se tomó en una cursada de verano de PLP.

El ejercicio está en la diapo.

Siempre que instanciemos variables deben ser de tipo frescas. Si metiamos sigma o tau entonces hubiesemos metido metavariables y estaría mal.

Decompose es para cualquier constructor.

Hay que juntar todo de modo tal que del lado derecho de la sustitución no me quede nada que ya reemplacé.

# Otro

```
Case Succ(0) :: x of [] ~> x ; x :: y ~> succ(x) :: []
```
1. Rectificar: 
    ```
    Case Succ(0) :: x of [] ~> x ; h :: t ~> Succ(h) :: []
            ||| Notar que la y no era libre porque el :: es un ligador!!! |||
    ```
2. Anotación:
    ```
    R0 = {x = X0}
    M0 = Case Succ(0) :: x of [] ~> x ; h :: t ~> Succ(h) :: []_{x1}
        ||| No se hace con la otra [] porque es notación del case!!! |||
    ```
3. Inferencia:
    ```
    Lo comprimo un poco para que entre más cómodo

                                                                                E
                                                                   ______________________________
    I({x: X0}|Case Succ(0)::x of []~>x; h::t~>Succ(h)::[]x1) = (X0|X0?=[Xh],X0?=[X1],Xt?=X0,E1,E3)

                                                                        E1
                                                                    ___________________
        I({x: X0}|Succ(0)::x)                                = (X0|{X0?=[Nat], Nat?=Nat})
            I({x: X0}|Succ(0))                               = (Nat|0 ?= Nat)
                I({x: X0}|0)                                 = (Nat| {})
            I({x: X0}|x)                                     = (X0 | {})

        I({x: X0}|x)                                         = (X0 | {})

                                                                                E3
                                                                        ___________________
        I({x: X0, h:Xh, t:Xt}|Succ(h)::[]X1)                 = ([X1] | [X1]?=[Nat], Xh?=Nat)
            I({x: X0, h:Xh, t:Xt}|Succ(h))                   = (Nat  | Xh?=Nat)
                I({x: X0, h:Xh, t:Xt}|h)                     = (Xh   | {})
            I({x: X0, h:Xh, t:Xt}|[]X1)                      = ([X1] | {})
    ```

4. MGU:
    ```
    S = MGU(E) = {X0?=[Xh],X0?=[X1],Xt?=X0, X0?=[Nat], Nat?=Nat, [X1]?=[Nat], Xh?=Nat} =
        {X0?=[Xh],X0?=[X1],Xt?=X0, X0?=[Nat], Nat?=Nat, [X1]?=[Nat], Xh?=Nat}  -> 
            .
            . En el parcial no es necesario hacer el paso por paso, pero hay que saber aplicar al
            . algoritmo igualmente
            .
        = {X1 := Nat, Xh := Nat, X0 := [Nat], Xt := [Nat]}

    El juicio de tipado más general es:

        S(R0) |- S(M0) : S(X0)
        {x:[Nat]} |- Case Succ(0)::x of []~>x; h::t~>Succ(h)::[]_{Nat} : [Nat]
    ```

# Otro más

```
Un ejemplito:
    [Succ(x) | x <- 0::1::[]_{Nat}, isZero(x)]
```
```
La x SOLO puede aparecer libre en M1 y M3, el contexto de los tipos de I me lo dice!!!!!!!!!!!!
x solo puede aparecer ligada en M1 y M3

[if c then 0 else 1 | x <- false :: isZero(x) :: [], True]
```
1. Rectificación: 
    ```
    [if y then 0 else 1 | y <- false :: isZero(x) :: [], true]
    ```
2. Anotación de tipos:
    ```
    R0 = {x:X1}
    M0 = [if y then 0 else 1 | y <- false :: isZero(x) :: []_{x2}, true]
    ```
3. Inferencia:
    ```
    Lo comprimo para que entre todo comodamente

    I({x:X1}|[if y then 0 else 1|y<-false::isZero(x)::[]X2, true]) = (t2)

        I({x:X1, y:X0}|if y then 0 else 1)                         = (Nat | X0?=Bool, Nat ?= Nat)
            I({x:X1, y:X0}|y)                                      = (X0  | {})
            I({x:X1, y:X0}|0)                                      = (Nat | {})
            I({x:X1, y:X0}|Succ(0))                                = (Nat | Nat ?= Nat)
                I({x:X1, y:X0}|0)                                  = (Nat | {})

        I({x:X1}|false::isZero(x)::[]X2)                           = ([X2] | [x2]?=[Bool],X1 ?= Nat)
            I({x:X1}|false)                                        = (Bool | {})
            I({x:X1}|isZero(x)::[]X2)                              = ([X2] | [X2]?=[Bool],X1 ?= Nat)
                I({x:X1}|isZero(x))                                = (Bool | X1 ?= Nat)
                    I({x:X1} | x)                                  = (X1   | {})
                I({x:X1}|[]X2)                                     = ([X2] | {})

        I({X,X1} | True)                                           = (Bool | {})


                                        E
                 ___________________________________________________________________
    t2: ([Nat] | [X2]?=[X0], Bool ?= Bool, X0?=Bool, Nat?=Nat, [X2]?=[Bool], X1?=Nat)
    ```
4. MGU:
    ```
    S = MGU(E) = 
        {[X2]?=[X0], Bool ?= Bool, X0?=Bool, Nat?=Nat, [X2]?=[Bool], X1?=Nat} ~>
        .
        .
        .
        .
        {X0 := Bool, X1 := Nat, X2 := Bool}
    
    El juicio de tipado más general es:
        S(R0) |- S(M0) : S([Nat]) =

            Nat |- [if y then 0 else 1|y<-false::isZero(x)::[]Bool, true] : [Nat]
    ```

# Notas
- A nosotros iempre nos van a dar las extensiones dle algoritmo I
- Ojo que es muy importante NO renombrar variables libres.
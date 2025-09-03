# Programación funcional (parte 2)

- foldr1 y foldr1 sirven para hacer recursión estructural sobre listas cuando no tenemos un caso base lo suficientemente claro.

```haskell
maximo :: Ord a => [a]->a
maximo = foldr1 (\x rec -> if x > rec then x else rec)

-- equivalente
maximo :: Ord a => [a]->a
maximo = foldr1 max
```
```haskell
mejorSegun :: (a->a->Bool) -> [a] -> a
mejorSegun f = foldr1 (\x rec -> if f x rec then x else rec)

-- equivalente
mejorSegun :: (a->a->Bool) -> [a] -> a
mejorSegun f = foldl1 (\x rec -> if f x rec then x else rec)
```
Ahora recursión sobre listas
```haskell
elem :: Eq a => a->[a]-> Bool
elem e = foldr (\x rec -> x==e || rec) False

take' :: Int -> [a] -> [a]
take' _ [] = []
take n (x:xs) = if n== 0 then [] else x:take (n-1) xs

-- equivalente, pero más lindo
take' :: Int -> [a] -> [a]
take' _ [] = const []
take n (x:xs) = \n -> if n== 0 then [] else x:take (n-1) xs


-- es muy molesto el n porque no puedo restarle uno así no más en el foldr.

-- Esta es la manera en la que se hace
take :: Int -> [a] -> [a]
take n = foldr (\x rec -> \n -> if n == 0 then [] else x: flip rec (n-1)) []
```
rec es el resultado de la recursión, o sea, en este caso es rec = take xs

hacer recr con foldr se usa inversión de parámetros. Usar una tupla.

foldl no sirve para hacer recursión sobre lsitas infinitas porque no hay manera de poder impedir que el llamado recursivo se haga, o sea, no hay manera de cortar la recursión en algún caso en particular, como sí lo hace foldr o recr.

foldl es la función principal en la recursión.
foldr no es la función principal en la recursión.

```haskell
listasQueSuman :: Int -> [[Int]]
listasQueSuman 0 = [[]]
listasQueSuman n | n>0 = [x:xs | x <- [1..n], xs <- listasQueSuman (n-x)]
```
En la función listasQueSuman se usa recursión global porque se usan los resultados recursivos de todos los valores de n posibles.
```haskell
fact :: Int -> Int
fact 0 = 1
fact n | n>0 = n* fact (n-1)
```
es primitiva porque estamos usando el argumento recursivo en otro lugar que no es la recursión.
```haskell
fibonacci :: Int -> Int
fibonacci 0 = 1
fibonacci 1 = 1
fibonacci n | n>1 = fibonacci (n-1) + fibonacci (n-2)
```
Es global porque no solo accedo al resultado anterior en la recursión, sino que también llamo a la recursión anterior a la recursión anterior.

La recursión estructural SOLO puede usar la recursión del paso anterior.

```haskell
pares :: [(Int, Int)]
pares = [(x,y) | x <- [1..y], y <- [1..]]

pares :: [(Int, Int)]
pares = [(x,y) | suma <- [1..], x <- x[1..s], y <- [1..s], x+y == s] --este anda

pares :: [(Int, Int)]
pares = [(x,s-x) | suma <- [1..], x <- x[1..s-1]] --este anda
```
Cuando estamos con listas infinitas nos conviene inventarnos un parámetro que nos asegure que me cumple la condición que debo cumplir y automaticamente definir los parámetros necesarios para que se genere el parámetro principal (ejemplo: suma)

```haskell
listas :: [[Int]]
listas = [xs | n<.[1..], xs <- listasQueSuman n]
```
Notar que de esa manera hizo sacó las sublistas de las listas
```haskell
listas :: [[Int]]
listas = concatMap listasQueSuman [1..]
```

# Folds sobre otras estructuras de datos

## AEB
Los constructores de data [a] son:
data lista a = [] | a: lista a
```haskell
-- Por ejemplo
data AEB a = Hoja a | Bin (AEB a) a (AEB a)
```
### ¿Cómo sería el tipo del fold de esa estructura?
```haskell
foldAEB :: (Hoja a-> b)->(AEB a-> a -> AEB a -> b) -> AEB a ->b -- Nein
foldAEB :: (Hoja a-> b)->(Bin (AEB a) a (AEB a) -> ) -> AEB a ->  b -- Nein
foldAEB :: (a-> b)->(b-> a -> b -> b) -> AEB a ->  b -- YES
```
Por cada constructor hay que tener una función o una constante para el tipo!!!

### ¿Cómo sería la definición del fold de esa estructura?
```haskell
foldAEB :: (a-> b)->(b-> a -> b -> b) -> AEB a ->  b 
foldAEB fHoja fBin arbol = 
    case arbol of
        Hoja x -> fHoja x
        Bin izq r der -> fBin (recu izq) r (recu der)
            where recu = 
                foldAEB fHoja fBin
```
```haskell
altura :: AEB a -> Int
altura = foldAEB (Const 1) (\rizq r rder -> 1 + max rizq rder) (Hoja a)

espejo :: AEB a -> AEB a
espejo = foldAEB (flip Const _) (\rizq r rder -> Bin der r izq)

espejo :: AEB a -> AEB a
espejo = foldAEB Hoja (\rizq r rder -> Bin der r izq) -- Los constructores también son funciones!!!
```

## AB
```haskell
data AB a = Nil | bin (AB a) a (AB a)
```
insertarABB es primitiva porque no estoy llamando a la recursión con i y con d en simultáneo.
truncar es estructural porque no estamos usando los argumentos recursivos como algo que no es recursivo. No usa ni i ni a d con nada que no sea la recursión y por otro lado no llama a la recursión con nada que no sea i o d.

```haskell
data Polinomio a = X | Cte a | Suma (Polinomio a) (Polinomio a) | Prod (Polinomio a) (Polinomio a)

-- f(x) = x^2+1
f x = Suma (Prod x x) (Cte 1) 
```
```haskell
evaluar :: Num a => a -> Polinomio a -> a
evaluar v poli = 
    case poli of
        X -> v
        Cte x -> x
        Suma pi pd -> (+) (evaluar v pi) (evaluar v pd)
        Prod pi pd -> (*) (evaluar v pi) (evaluar v pd)
```
```haskell
foldPoli :: b -> (a->b) -> (b->b->b) -> (b->b->b) -> Polinomio a-> b
foldPoli fX fCte fSuma fProd poli =
    case poli of
        X -> fX
        Cte c -> fCte c
        Suma pi pd -> fSuma (recu pi) (recu pd)
        Prod pi pd -> fSuma (recu pi) (recu pd)
            where recu =
                foldPoli fX fCte fSuma fProd
```
```haskell
evaluar :: Num a => a -> Polinomio a -> a
evaluar e = foldPoli e id (+) (*)
```
## RoseTree
```haskell
data RoseTree a = Rose a [RoseTree a]
```
```haskell
foldRose :: (a-> [b] ->b) -> RoseTree a -> b
foldRose fRose (Rose x lista)= fRose x (map recu lista) 
    where recu =  
        recu :: RoseTree a -> b 
        foldRose fRose 
```
```haskell
ramas :: RoseTree a -> [[a]]
ramas = foldRose (\x lista -> x: lista) -- ?                                

ramas :: RoseTree a -> [[a]]
ramas = foldRose (\x lista -> if null xs 
                                then [[x]]
                                else map (x:) (concat lista) -- analizar fuertemente
                                )                     
```

## Conjunto
```haskell
type Conj a = (a->Bool)
```
```haskell
vacio :: Conj a
vacio = const False
```
```haskell
insertar :: Eq a => a -> Conj a -> Conj a
insertar e conj = (\x -> e == x || conj e)

pertence :: Eq a => a -> Conj a -> Bool
pertenece e conj = conj e

eliminar :: Eq a => a -> Conj a -> Conj a
eliminar e conj = (\x -> e/=x && conj e)

-- Ejemplos: 
-- pertence 2 (eliminar 2 (insertar 2 vacio))
-- pertence 2 (eliminar 3 (insertar 2 vacio))
```
Escribir las funciones interseccion, union y diferencia.
```haskell

```
```haskell
```

# Nota
- Ojo eh! Que la recursión estructural SOLO pueda usar la recursión del paso anterior no siginifica que no la pueda usar una sola vez.
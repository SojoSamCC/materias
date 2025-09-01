# Programación funcional

## Ejercicio 1
1. 
```haskell
    max2 :: (Int, Int) -> Int
    max2 (x, y) | x >= y = x
                | otherwise = y
        
    normavectorial :: (Int, Int) -> Int
    normaVectorial (x, y) = sqrt (x^2 + y^2)

    subtract :: Num a=> a->a->a
    subtract = flip (-)
    
    predecesor :: Num a=> a->a
    predecesor = subtract 1

    evaluarEnCero :: Num a => (a -> b) -> b
    evaluarEnCero = \f-> f 0

    dosVeces :: (a->a)->a->a
    dosVeces = \f-> f . f

    flipAll :: [(a->b->c)]->[(b->a->c)]
    flipAll = map flip

    flipRaro :: b -> (a->b->c) -> (a->c) -- notar que es esto porque flip flip /= flip . flip
    flipRaro = flip flip
```
2.
```haskell
    max2 :: Int -> Int -> Int
    max2 = (\x y -> if x>=y then x else y)

    normavectorial :: Int -> Int -> Int
    normaVectorial = \x y -> sqrt (x^2 + y^2)
```
## Ejercicio 2
1.
```haskell
    curry :: ((a, b) -> c) -> (a->b->c)
    curry f = \x y -> f (x y)
```
2.
```haskell
    uncurry :: (a->b->c) -> ((a,b)->c) 
    uncurry f = \(x, y) -> f x y
```
3.
---

## Ejercicio 3
1.
```haskell
    foldr :: (a->b->b) -> b -> [a] -> b
    foldr _ z [] = z
    foldr f z (x:xs) = f x (foldr f z xs)
```

```haskell
    sum :: Num a => [a] -> a
    sum = foldr (+) 0

    elem :: Eq a => a -> [a] -> Bool
    elem x = foldr (\y rec -> x == y || rec) False

    (++) :: [a]->[a]->[a]
    (++) l1 l2 = foldr (:) l2 l1

    filter :: (a->Bool) -> [a] -> [a]
    filter f = foldr (\x rec -> if f x then x:rec else rec) []

    map :: (a->b)->[a]->[b]
    map f = foldr (\x rec -> f x: rec) []
```
2.
```haskell
mejorSegun :: (a -> a -> Bool) -> [a] -> a
mejorSegun f = foldr1 (\x rec -> if f x rec then x else rec)
```
3.
```haskell
sumasParciales :: Num a => [a] -> [a]
sumasParciales lista = foldr (\x rec -> sum (take ((length lista) - (length rec)) lista) : rec) [] lista
```
4.
```haskell
sumaAlt :: [Int] ->Int
sumaAlt = foldr (\x rec -> x + ((*(-1)) rec)) 0
```
5.
```haskell
sumaAlt :: [Int] ->Int
sumaAlt = (foldr (\x rec -> x + ((*(-1)) rec)) 0) . reverse 
```
## Ejercicio 4
> No tengo ni la menor idea de como hacer ninguno de estos ejercicios
1.
```haskell
permutaciones :: [a] -> [[a]]
permutaciones lista = concatMap (foldr (\x rec -> take 1 rec : [x] : rec) lista) lista
```
No sé cómo hacerlo

2.
```haskell
partes :: [a]->[[a]]
partes = foldr ()
```
## Ejercicio 5
La recursión es estructural unicamente en elementosEnPosicionesPares porque el llamado recursivo solo depende de una lista, que la cola.

```haskell
elementosEnPosicionesPares :: [a] -> [a]
elementosEnPosicionesPares lista = fst (foldr (\x (rec,par) -> if par then (x:rec, not par) else (rec, not par)) ([], True) lista)
```
## Ejercicio 6
a.
```haskell
sacarUna :: Eq a => a -> [a] -> [a]
sacarUna e = recr (\x xs rec -> if x == e then xs else x:rec) []
```
b. Porque con foldrno me puedo guardar la cola de la lista. 
```haskell
insertarOrdenado :: Ord a => a -> [a] -> [a]
insertarOrdenado e = recr (\x xs rec -> if x>e then e:x:xs else x:rec) []
```
## Ejercicio 7
1.
```haskell
mapPares :: ((a,b)->(c,d)) -> [(a,b)] -> [(c,d)]
mapPares f = foldr (\par rec -> (f (fst par), f (snd par)):rec) []
```
2.
> No se me ocurre como armarla con foldr
```haskell
armarPares :: [a]->[b]->[(a,b)]
```
3.
> no se me ocurre como hacerla.
```haskell
mapDoble :: (a->b) -> [a] -> [a] -> [b] -- ???? Si no entendí mal el enunciado es esto
mapDoble f l1 = foldr (\l2 rec -> ) [] - -no sé
```
## Ejercicio 8


## Ejercicio 9
1.
> Está bien????
```haskell
data Nat = Zero | Succ Nat

foldNat :: b -> (a->b->b) -> a -> b
foldNat cZero cNat x = 
    case x of
        Zero -> cZero
        (Succ n) -> cNat (Succ n) (foldNat cZero cNat n)
```
2.
```haskell
potencia :: Nat -> Nat
potencia = foldNat Zero (\nat rec -> ) -- ni idea
```

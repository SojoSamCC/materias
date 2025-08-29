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
```haskell
```
```haskell
```
```haskell
```


# Currificación y aplicación parcial

- Las funciones en haskell siempre se aplican a un argumento.
## Currficación
Una función currificada es una función que toma un argumento y devuelve otra función que espera más argumentos.

```haskell
prod :: (Int,Int)-> Int
prod (x,y) = x*y

prod' :: Int->Int-> Int
prod' x y = x * y
```
prod' es una función que toma una un entero y devuelve una función que toma otro entero y lo multiplica por el número original antes de ser currificada, o sea x.

currificada se refiere a una función que toma un parametro y devuelve otra función que es la aplicación parcial de una función.

Definamos curry, toma una función no currificada y la currifica
```haskell
curry :: ((a,b)->c)->(a->b->c)
curry f x y = f (x,y)

-- equivalente
curry :: ((a,b)->c)->(a->b->c)
curry f = \x y -> f (x, y) 
```

Definamos uncurry, toma una función currificada y la descurrifica

```haskell
uncurry :: (a->b->c) -> ((a->b)->c)
uncurry f (x y) = f x y

-- equivalente 
uncurry :: (a->b->c) -> ((a->b)->c)
uncurry f = \(x,y) -> f x y
```
```haskell
uncurry :: (a->b->c) -> ((a->b)->c)
uncurry f (x y) = f x y

-- equivalente 
uncurry :: (a->b->c) -> ((a->b)->c)
uncurry f = \(x,y) -> f x y
```


## Aplicación parcial
```haskell
prod :: (Int,Int)-> Int
prod (x,y) = x*y

doble :: Int->Int
doble = prod 2

triple :: Int -> Int
triple = (*3)

triple :: Int -> Int
triple = (3*)

-- (*3) == triple n 3
-- (3*) == triple 3 n

sumarUno :: Int->Int
sumarUno = (+) 1

esMayorDeEdad :: Int -> Bool
esMayorDeEdad = (<=) 18 
-- esMayorDeEdad 20 --> (<=) 18 20 --> 18 <= 20
```

## Funciones muy útiles

```haskell
-- (.)
restar_3_y_multiplicar_por_4 :: Int
restar_3_y_multiplicar_por_4 = ((\x -> x*4).(\y->y-3)) 


-- 1.
(.) :: (b->c)->(a->b)->(a->c) -- ojo que devuelve una función que va de (a->c) y no un c directamente.
(.) f g = \x -> f (g x)

-- equivalente
(.) :: (b->c)->(a->b)->(a->c) -- ojo que devuelve una función que va de (a->c) y no un c directamente.
f (.) g = \x -> f (g x)

-- equivalente
(.) :: (b->c)->(a->b)->(a->c) -- ojo que devuelve una función que va de (a->c) y no un c directamente.
(.) f g x = f (g x)s


-- 2.
flip :: (a->b->c) -> (b->a->c)
flip f = \x y -> f y x

-- equivalente
flip :: (a->b->c) -> (b->a->c)
flip f x y = f y x

-- notar que flip NO llama a la función. Entonces esto lo que tiene es que no se me indefine la función si yo le paso los parámetros al revés aunque tengan diferentes tipos porque cuando yo llamo a flip f YO ya le estoy pasando los argumentos al revés a propósito, entonces cuando la función pasa por el flip se acomodan al orden en que van. El truco es ese, le paso los argumentos al revés ADREDE a la función f para que luego el flip me los acomode a como

-- 3.
($) ::(a->b)->a->b -- aplica una funcion a un argumento 
($) f = \x -> f x

($) ::(a->b)->(a->b) -- aplica una funcion a un argumento 
($) f = f 

-- esta función es útil en casos como este
-- f (g (h (j (k x)))) == f $ g $ h $ j $ k x



-- 4.
const :: (a -> b) -> a
const = \x _ -> x

-- equivalente
const :: (a -> b) -> a
const x _ = x
```

```haskell
-- flip $ 0
-- hace esto
-- flip $ 0 f -> ($) f 0 == f 0

-- (==0) . (flip mod 2)
-- hace esto
--- (==0) . (flip mod 2) 8 --> (==0) . (mod 8 2) --> 0 == 0  
```

## Listas
Sabemos que en el lenguaje haskell tenemos variables, constructores, aplicaciones y no mucho más.

Hay macors para definir listas.
- Por extensión
- Secuencias
- Por comprensión:
    ```haskell
    -- [expresion | selectores, condiciones]
    -- por ejemplo [(x,y) | x<-[0..5], y<-[0..3], x+y==4]

    Esto primero evalua en el primer valor de x e itera por todos los de y, es como un 
    ```
    ```python
    lista=[]
    for x in range([0..5]):
        for y in range([0..3]):
            if x+y == 4:
                lista.append((x,y,))
    ```
    ```haskell
    -- las listas no tienen que tener el mismo tipo exactamente.
    ```
    ```haskell
    -- podemos usar listas infinitas

    naturales = [1..]
    multiplos_de_3 = [0,3,..]

    hola_infinito = repeat 'hola'

    primos = [n | n<-[2..], esPrimo n]

    -- esta es una definición recursiva de una lista
    inifitosUnos = 1: infinitosUnos
    ```

Como Haskell tiene evaluación lazy, entonces podemos trabajar con listas infinitas sin problema.

```haskell
take :: Int -> [a] -> [a]
take 0 _ = []
take _ [] = []
take n (x:xs) = x : take (n-1) xs

inifitosUnos :: [Int]
inifitosUnos = 1: infinitosUnos

nUnos :: Int -> [Int] -- toma un n y devuelve una lista de tamaño n donde todas sus posiciones son unos.
nUnos n = take n infinitosUnos
```

```haskell
fibs = 0:1:fibsApartir 0 1
    where
        fibsApartir a b = a + b : fibsApartir b (a+b)

fibs = 0:1:zipWith (+) fibs (drop 1 fibs)

zip hace esto: zip [1,2,3] [4,5,6] = [(1,4),(2,5),(1,6)]

zipWith hace lo mismo que zip pero solo arma una lista aplicando la función que le pases.

-- obtener el n-esimo fibonacci
fib n = head (drop n fibs)
```
# Funciones totales vs parciales
## Pregunta
¿Cuales de las siguientes funciones pueden ser totales?
```haskel
- null :: [a] -> Bool
- tail :: [a] -> [a]
- head :: [a] -> a
- safeHead :: [a] -> Maybe a 
```
- null es total.
- tail no es total
- head no es total.
- safeHead si es total.

Basicamente el Maybe me hace total una función porque me salva en caso de que se indefina.

```haskell
dobleHeadA lista = if null lista
                        then Nothing
                        else Just (2 * head lista)
dobleHeadB lista = case lista of
                    [] -> Nothing
                    (x:_) -> Just (2 * x)
```

el 
```haskell 
case
```
está bueno porque me salva de tener que poner las ecuaciones en orden.

# Funciones de alto orden
```haskell
maximo :: Ord a => [a]->a
maximo (x:xs) = case xs of
                    [] = x
                    (y:ys) =  if x > maximo (y:ys) then x else maximo (y:ys)

minimo :: Ord a => [a] -> a
minimo (x:xs) = case xs of
                    [] = x
                    (y:ys) = if x < minimo (y:ys) then x else minimo (y:ys)

listaMasCorta :: [[a]] -> [a]
listaMAsCorta (x:xs) = case xs of
                        [] = x
                        (y:ys) = if length x < lenth (listaMAsCorta (y:ys)) then x else listaMAsCorta (y:ys)

mejorSegun :: (a->a->Bool)->[a]->a
mejorSegun f (x:xs) = case xs of
                        [] = []
                        (y:ys) = if f x (mejorSegun (y:ys)) then x else mejorSegun (y:ys)


maximo = mejorSegun (>) 
minimo = (<)
listaMAsCorta = mejorSegun (\(x:xs) length x < length xs) -- xs puede ser r, r de recursión.

maximo = foldr (\lista -> mejorSegun (>) lista) []  
minimo = foldr (\lista -> (<) lista) []  
listaMAsCorta = foldr (\lista -> mejorSegun (length) lista) []  
```
```haskell
filter :: (a->Bool) -> [a] -> [a]
filter _ [] = []
filter p (x:xs) = 
    if p x 
        then x: filter xs
        else filter xs

deLongitudN :: Int -> [[a]] -> [[a]]
deLongitudN n = filter (\lista -> length lista == n)

-- equivalente
deLongitudN :: Int -> [[a]] -> [[a]]
deLongitudN n = filter ((==n) . length) -- esta es la forma cheta en la que a los profes les gusta que escribamos.

soloPuntosFijosEnN :: Int -> [Int->Int]
soloPuntosFijosEnN n = filter (\f -> f n == n)

-- equivalente
soloPuntosFijosEnN :: Int -> [Int->Int]
soloPuntosFijosEnN n = filter (((==n) . f) n)
```
```haskell
map :: (a->b) ->[a]->[b]
map _ [] = []
map f (x:xs) = f x : map  f xs

reverseAnidado :: [[Char]] -> [[Char]]
reverseAnidado xs = reverse (map reverse xs)

reverseAnidado :: [[Char]] -> [[Char]]
reverseAnidado = reverse . (map reverse)

paresCuadrados :: [Int] -> [Int]
paresCuadrados = map (\n -> if even n then n*n else n)
```
Notar que filter y map hacen una cosa cuando tenemos la lista vacía y otra cuando la lista es no vacía... Podemos generalizar!
```haskell
-- Es como una cosa así no?
f _ z [] = []
f g z (x:xs) = g x (f g x)
```
```haskell
-- LLegó foldr
foldr :: (a->b->b)->b->[a]->b
foldr _ z [] = z
foldr f z (x:xs) = f x (foldr f z xs)

filter p = foldr (\x r -> if p x then x:r else r) []
```
```haskell
-- Definir una expresión equivalente a la siguiente utilizando map y filter
listaComp :: (a->Bool) -> (a->b) -> [a] -> [b]
listaComp p f xs = [f x | x<-xs, p x]

listaComp :: (a->Bool) -> (a->b) -> [a] -> [b]
listaComp p f = map f . filter p
```


# Notas
- curry permite hacer la aplicación parcial pero NO es la aplicación parcial.
- Casi siempre vamos a trabajar con funciones currificadas.
- Haskell siempre reduce la expresión más externa si la necesita.
- Cuando tenemos una función que recibe el resultado de aplicar una función a un parámetro, entonces ahí conviene usar la composición.

# Aprender Erlang, ta bueno.
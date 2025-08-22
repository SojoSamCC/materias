# Notas
- Un paradigma de programación se puede ver como una forma de pensar y ver el mundo, es más arraigado a una forma de programar. Cada paradigma tienes sus primitivas. En la programación funcional las primitivas son las funciones.
- programación es: el avión está hecho, lo uso. 
implemtación: es como se construye el avión.
semantica: Lo que explica que el avión vuela.
- Una función de orden superior indica que una función puede recibir como parametros datos que son funciones en sí y no datos primitivos como str, int, float, etc.
- Compilación es la traducción de un lenguaje de programación a otro.
- Las diapos no son buena fuente de referencia o de estudio. Ya lo sabes, por eso estás recursando.

# Tipos basicos y secuencias
Esto es más que nada ejercicios.

## Factorial

    factorial :: Int -> Int 
    factorial 0 = 1
    factorial n = n * factorial (n-1) 
- Es una función parcial porque no está definida en todo el conjunto de numeros a los que pertenecen

# sumaN
    sumaN :: Int -> [Int] -> [Int]
    sumaN _ [] = [] 
    sumaN n (x:xs) = (n+x) : sumaN n xs

# aparece
    aparece :: Char -> String -> Bool
    aparece c "" = False
    aparece char (c:cs) = char == c || aparece char cs

- Notar que también puede ser
    -
        aparece :: Eq a=> a -> [a] -> Bool
        aparece c [] = False
        aparece elem (c:cs) = elem == c || aparece elem cs

# ordenar
    -- Hace uso de insertion sort. Implementar con Selection
    ordenar :: [Float] -> [Float]
    ordenar []     = []
    ordenar (x:xs) = insertar_ordenadamente x (ordenar xs)

    -- pre: la lista de entrada está ordenada de menor a mayor
    insertar_ordenadamente :: Float -> [Float] -> [Float]
    insertar_ordenadamente f [] = [f]
    insertar_ordenadamente f (y:ys) = if f<y then f:y:ys else y : insertar_ordenadamente f ys

- Notar que también puede ser
    -
        -- Hace uso de insertion sort. Implementar con Selection
        ordenar :: Ord a => [a] -> [a]
        ordenar []     = []
        ordenar (x:xs) = insertar_ordenadamente x (ordenar xs)

        -- pre: la lista de entrada está ordenada de menor a mayor
        insertar_ordenadamente :: Ord a => a -> [a] -> [a]
        insertar_ordenadamente f [] = [f]
        insertar_ordenadamente f (y:ys) = if f<y then f:y:ys else y : insertar_ordenadamente f ys

# Notas
- programación
- implementación: como hace la compu para ejecutar sus programas.
- semántica: explicar lo que hace un programa de forma matematicamente precisa. Darle significado matematicamente preciso a los programas. Un ejemplo son los TADS (acuerdate la tripla de Hoare).
- La aplicación tiene mayor precedencia que el cons.
- (:) se le llama 'cons'
- Eq se refiere a que lo que le sigue es que se puede comparar. Es una restricción de Type class.

# Tipos de datos inductivos
- Aclaración: hoy solo vamos a ver como se trabaja con ellos.

# Direccion

## Opuesta
    data Direccion = Norte | Este | Sur | Oeste
        deriving Show -- esta linea es para que se muestre en pantalla de la forma más literal posible

    instance Eq Direccion where
        Norte == Norte = True
        Sur == Sur     = True
        Este == Este   = True
        Oeste == Oeste = True
        _ == _         = False

    opuesta :: Direccion -> Direccion
    opuesta dir = 
        case dir of
            Norte = Sur
            Este = Oeste
            Sur = Norte
            Oeste = Este

## ultimo_indice_de

    ultimo_indice_de :: Eq a => a -> [a] -> Int
    ultimo_indice_de e []     = -1
    ultimo_indice_de x (y:ys) = 
        if x /= y || elem x ys
            then 1 + ultimo_indice_de x ys
            else 0
    
- es parcial porque se indefine en el caso de que se le de una lista vacia.

## Hagamos ultimo_indice_de total

    Maybe a = Nothing | Just a

    ultimo_indice_de :: Eq a => a -> [a] -> Int
    ultimo_indice_de e []     = Nothing
    ultimo_indice_de x (y:ys) = 
        if x /= y || elem x ys
            then 1 + ultimo_indice_de x ys
            else 0

## Notas
- Para crear el propio tipo de dato inductivo se debe indicar con el data. 
- un constructor es una forma de decir de qué manera se construyen las estructuras de datos.
- un tipo de dato inductivo.
- Maybe Int: lo que hace es agregarme un nuevo tipo de dato para Int. Ver anotación en papel.

# Arbol binario
    data AB a = Nil | Bin (AB a) a (AB a)
    -- Bin :: AB a -> a -> AB a -> AB a ||| Este es el tipo que tiene Bin, Haskell lo infiere.
    -- Nil :: AB a
- ¿Cómo se ve esto?
    -
        1
       / \      ---->  Bin(Bin Nil 2 Nil) 1 (Bin Nil 3 Nil)
      2   3

## preorder
    
    -- comienza por la raíz, revisa un nodo y luedo hace lo mismo para todo el hijo izquierdo.

    preorder :: AB a -> [a]
    preorder Nil  = []
    preoder (Bin izq r der) = r: (preorder izq ++ preorder der)
    -- Pensamiento clave: asumir que preorder izq y preorder der ya funcionan bien y son una lista.

## inorder y postorder TAREA

    --revisa un 

# Tipos abstractos de datos
## Queremos implementar un conjunto

    Necesitamos
        vacio :: Conj a
        insertar :: Eq a => a -> Conj a -> Conj a
        pertenece :: Eq a => a -> Conj a -> Bool
        eliminar :: Eq a => a -> Conj a -> Conj a

    data Conj a = CConj [a]
    -- invariante: la lista no tiene repetidos.
    -- CConj :: [a] -> Conj a

    vacio :: Conj a
    vacio = CConj []

    insertar :: Eq a => a -> Conj a -> Conj a
    insertar x (CConj ys) = 
        if elem x ys
            then CConj ys
            else CConj (x:ys)

    pertenece :: Eq a => a -> Conj a -> Bool
    pertenece x (CConj ys) = elem x ys                

    eliminar :: Eq a => a -> Conj a -> Conj a
    eliminar x (CConj ys) = 
        if elem x ys
            then funcion para eliminar un elemento de una lista de modo CConj (func c ys)
            else CConj ys

    # TAREA IMPLEMENTAR iguales (dice si dos Conj son iguales)

# Queremos implementar un diccionario

    Necesitamos
        vacio :: Dict k v
        definir :: Ord k => k->v->Dict k v -> Dict k v
        buscar :: Ord k => k->Dict k v -> Maybe k v

    -- Usamos estructura de arbol binario de busqueda como estructura de representación.
    Maybe a = Nothing | Just a
    data AB a = Nil | Bin (AB a) a (AB a)
    data Dict k v = CDict (AB (k, v))
    -- CDict :: AB (k, v) -> Dict k v

    vacio :: Dict k v
    vacio = CDict (Nil)

    definir :: Ord k => k->v->Dict k v -> Dict k v
    definir clave valor (CDict arbol) = CDict (insertar_en_ABB clave valor arbol)
        where
            --insertar_en_ABB :: Ord k => AB (k, v) -> AB (k, v)
            insertar_en_ABB Nil = Bin Nil (clave, valor) Nil 
            insertar_en_ABB (Bin izq (clave', valor') der) 
                | clave == clave' = Bin izq (clave, valor) der
                | clave < clave' = Bin (insertar_en_ABB izq) (clave', valor') der
                | otherwise = Bin izq (clave', valor') (insertar_en_ABB der)

    buscar :: Ord k => k->Dict k v -> Maybe k v
    buscar clave (CDict abb) = buscar_en_ABB abb
        where 
            buscar_en_ABB Nil = Nothing
            buscar_en_ABB (Bin izq (clave', valor') der) 
                | clave == clave' = Just valor'
                | clave < clave' = buscar_en_ABB izq
                | otherwise = buscar_en_ABB der

## Nota:
- Usamos Maybe a para que las funciones sean totales y que no se indefinan en algún valor.

# Enumeraciones combinatorias
    Idea: Queremos funciones que nos den todas las posibilidades segun algún criterio.

## subsecuencias
    subsecuencias :: [a] -> [[a]]
    subsecuencias [] = [[]]
    subsecuencias (x:xs) = duplicar_con_y_sin_x (subsecuencias xs)
        where
            duplicar_con_y_sin_x :: a -> [[a]] -> [[a]]
            duplicar_con_y_sin_x x [] = []
            duplicar_con_y_sin_x x (l:ls) = (l:((x:l): duplicar_con_y_sin_x x ls))

## hay un ejercicio más, es tarea.

# Avisos


# foldr
## def
    foldr :: (a->b->b)->b->[a]->[b]
    foldr _ z [] = [z]
    foldr f z (x:xs) = f x : foldr f z xs
    
## sumaN
    sumaN :: Int -> [Int] -> [Int]
    sumaN n = foldr ((+) n) [] 

## aparece (CHEQUEAR PORQUE ESTÁ MAL)
    aparece :: Char -> String -> Bool
    aparece c = foldr (\c (s:ss) -> c == s || rec) ""

# Notas extra
- La materia está buena.
- POO lo vamos a ver mejor en Ingenieria de software.
- No interesan muchos las definiciones de libro. Importa más la parte semántica.
- A la materia le importa mucho el lado semántico.
- Una interfaz son un conjunto de operaciones que me permiten interactuar con un tipo abstracto de dato.
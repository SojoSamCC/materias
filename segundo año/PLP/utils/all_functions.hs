-- Funciones dadas en las clase teoricas
-- Clase teorica 1
factorial :: Int -> Int 
factorial 0 = 1
factorial n = n * factorial (n-1)

sumaN :: Int -> [Int] -> [Int]
sumaN _ [] = [] 
sumaN n (x:xs) = (n+x) : sumaN n xs

aparece :: Eq a=> a -> [a] -> Bool
aparece c [] = False
aparece elem (c:cs) = elem == c || aparece elem cs

-- Hace uso de insertion sort. Implementar con Selection
ordenar :: Ord a => [a] -> [a]
ordenar [] = []
ordenar (x:xs) = insertar_ordenadamente x (ordenar xs)
-- no es de la clase 1 pero notar que se puede hacer 
-- ordenar = foldr insertar_ordenadamente [] xs

-- pre: la lista de entrada está ordenada de menor a mayor
insertar_ordenadamente :: Ord a => a -> [a] -> [a]
insertar_ordenadamente f [] = [f]
insertar_ordenadamente f (y:ys) = if f<y then f:y:ys else y : insertar_ordenadamente f ys

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
        Norte -> Sur
        Este -> Oeste
        Sur -> Norte
        Oeste -> Este

data Maybe a = Nothing | Just a

-- ultimo_indice_de :: Eq a => a -> [a] -> Maybe Int
-- ultimo_indice_de e []     = Nothing
-- ultimo_indice_de x (y:ys) = 
--     if x /= y || elem x ys
--         then 1 + ultimo_indice_de x ys
--         else 0

data AB a = Nil | Bin (AB a) a (AB a)
-- comienza por la raíz, revisa un nodo y luedo hace lo mismo para todo el hijo izquierdo.
preorder :: AB a -> [a]
preorder Nil  = []
preoder (Bin izq r der) = r: (preorder izq ++ preorder der)
-- Pensamiento clave: asumir que preorder izq y preorder der ya funcionan bien y son una lista.

data Conj a = CConj [a]
-- invariante: la lista no tiene repetidos.
-- CConj :: [a] -> Conj a

insertar_en_conj :: Eq a => a -> Conj a -> Conj a
insertar_en_conj x (CConj ys) = 
    if elem x ys
        then CConj ys
        else CConj (x:ys)

pertenece_en_conj :: Eq a => a -> Conj a -> Bool
pertenece_en_conj x (CConj ys) = elem x ys                

-- eliminar_en_conj :: Eq a => a -> Conj a -> Conj a
-- eliminar_en_conj x (CConj ys) = 
--     if elem x ys
--         then funcion para eliminar un elemento de una lista de modo CConj (func c ys)
--         else CConj ys

-- data Maybe a = Nothing | Just a 
-- data AB a = Nil | Bin (AB a) a (AB a) 
data Dict k v = CDict (AB (k, v))
-- CDict :: AB (k, v) -> Dict k v
-- definir :: Ord k => k->v->Dict k v -> Dict k v
-- definir clave valor (CDict arbol) = CDict (insertar_en_ABB clave valor arbol)
--     where
--         --insertar_en_ABB :: Ord k => AB (k, v) -> AB (k, v)
--         insertar_en_ABB Nil = Bin Nil (clave, valor) Nil 
--         insertar_en_ABB (Bin izq (clave', valor') der) 
--             | clave == clave' = Bin izq (clave, valor) der
--             | clave < clave' = Bin (insertar_en_ABB izq) (clave', valor') der
--             | otherwise = Bin izq (clave', valor') (insertar_en_ABB der)

-- buscar :: Ord k => k->Dict k v -> Maybe k v
-- buscar clave (CDict abb) = buscar_en_ABB abb
--     where 
--         buscar_en_ABB Nil = Nothing
--         buscar_en_ABB (Bin izq (clave', valor') der) 
--             | clave == clave' = Just valor'
--             | clave < clave' = buscar_en_ABB izq
--             | otherwise = buscar_en_ABB der

-- subsecuencias :: [a] -> [[a]]
-- subsecuencias [] = [[]]
-- subsecuencias (x:xs) = duplicar_con_y_sin_x (subsecuencias xs)
--     where
--         duplicar_con_y_sin_x :: a -> [[a]] -> [[a]]
--         duplicar_con_y_sin_x x [] = []
--         duplicar_con_y_sin_x x (l:ls) = (l:((x:l): duplicar_con_y_sin_x x ls))

foldr_ :: (a->b->b)->b->[a]->b
foldr_ _ z [] = z
foldr_ f z (x:xs) = f x (foldr_ f z xs)

# Fuerza bruta
## Def
Easy, es verificar todas las soluciones posibles y tomar la que cumpla nuestras necesidades.
Literalmente, probar todas las soluciones posibles, o sea todas las combinaciones posibles.

# Backtracking
## Def
Easy, es hacer fuerza bruta pero si veo que el camino que estoy tomando no llega a una solución válida entonces me detengo ahí y empiezo a volver atrás sobre mis pasos y así hasta llegar a una solución válida.
En este caso tengo que verificar constantemente que mi solución parcial me puede llevar a una solución total.

## Podas por factibilidad y podas por optimalidad
### factibilidad
Son podas que lo que hacen eliminar ramas completas del arbol sí y solo sí el estado o solución parcial que tengo en realidad no me lleva a ninguna solución.

### Optimalidad
Lo que hace es estar chequeando todo el tiempo si el camino por el que voy me lleva a una solución mejor que la que ya tenía.

# Ejercicios
## Ejercicio 1
```python
def palabrasEnCadena(cadena:str, se_podia:bool = False)->bool:

    # Debo terminar.

    largo=len(cadena)
    if largo == 1:
        return 

    if se_podia:
        return True


    medio = largo // 2

    izquierda = cadena[:medio]
    derecha = cadena[medio:]
    parte_del_medio= 

    cond = palabra(izquierda) or palabra(derecha) or palabra(parte_del_medio)

    return cond
```
### ¿Qué complejidad tiene?
T(n) = 
$$
\begin{cases}
O(1) , si n=0. \\ \\
\sum_{k=0}^{n-1}{T(k)+O(n)}, cc
\end{cases}
$$
> T(k) es la complejidad de llamar a la función desde el índice donde me quedé.

No puedo hacer teo. maestro porque no estoy haciendo particiones balanceadas.

Para demostrar la complejidad hay que usar inducción.

Notemos que si $n>1$ entonces $T(n-1)=s\sum_{k=0}^{n-2}{T(k)+C*(n-1)}$
Notemos que $T(n)-T(n-1)=T(n-1)+c == T(n)=2T(n-1)+C$
Notar que acotamos la O(n) por una constante C que viene de la definición de orden de una función. Luego O(n) la acotamos por $C*n$ y entonces al hacer la resta me queda $C*n - C*(n-1) = C$

Entonces cuando vemos el árbol de recursión me queda que por cada llamado recursivo abro en dos cada subllamado y la altura es $2^n$ porque es un árbol completo porque todo el tiempo bajo a n en 1. **ver dibujito que hice en papel**.

$$
\text{Finalmente} \\
.\\
T(n) \in O(2^{n}) \\ 

\text{} \\
\text{El arbol tiene altura n y por cada nivel se me duplica la cantidad de casos a evaluar.}
$$

Demostremos por otro camino diferente al árbol de recursión. Inducción.

Notemos que $T(n) \in O(2^{n}) \implies T(n) \leq C'\times 2^{n}$

$$
\text{Inducción} \\
\text{} \\
T(n)=2T(n-1)+C \\
T(n) \leq 2(C'2^{n-1}+C) \\
T(n) \leq C'2^{n}+C \\

\text{} \\
\text{Esto está mal, ver porque me quedó el factor C dando vueltas, entonces esto implica que } T(n) \text{ no sea necesariamente menor o igual que } C'2^{n}\\
$$

$$
\text{Inducción} \\
T(n)=2T(n-1)+C \\
HI \ = \ T(n) \leq 2(C'2^{n-1}+C) = 2(C'2^{n-1}+C) - d \\
= 2(C'2^{n-1}-d)+C = C'2^{n}- 2d +C = C'2^{n}- d - (d - C) \ d \geq C \\
T(n) \leq C'2^{n}-d
$$
Este sí vale porque como el d es negativo y es general, entonces sí vale el menor o igual.

Ahora veamos la demo incorrecta en la diapo.


## Ejercicio 2

El problema en sí es encontrar la raíz más óptima. Lo que conviene hacer es iterar por todos los elementos armando un ABB y al mismo calcular la sumatoria de la cantidad de accesos, me debo quedar con el ABB que me dé la menor cantidad de accesos, en principio lo mejor que puedo hacer es guardarme la sumatoria más chica y si mientras me armo un arbol me queda una sumatoria más grande (aún si no la terminé) entonces corto la ejecución y retorno hasta el proximo elemento en f.

1.
$$
costo(A,f,i,j) =
\begin{cases}
0 \ , \text{si } A = \empty \text{ y } i \gt j\\
\sum_{k=i}^{j}{f(k) + costo(A_{izq}, f, i, A_{raiz} - 1) + costo(A_{der}, f, A_{raiz}+1, j)} \text{ , si } i \leq j\\
\end{cases}
$$

Esto lo que hace es sumar UNA vez todos los valores que se encuentran por en un nivel y todos los que están en sus subniveles.

2.
CASI le pego a la solución. La cosa es meto una raíz y hago recursión a izquierda y a derecha, me fijo  cual es la raíz que minimiza el árbol, eso recursivamente y me voy guardando el mejor costo y voy comparando.

3.

$$
T(n) = \sum_{k=1}^{n}{[T(k-1) + T(n-k)] + O(n)} \text{ notar que esto suma dos veces lo mismo porque uno sube en el parámetro y el otro baja!!!} \\
T(n) = 2*\sum_{k=0}^{n-1}{[T(k)] + O(n)} \\
T(n) \in O(3^n) \\
$$
Van a subir la demostración de esto al campus.
```python
```
# Notas
- Hacer todas las combinaciones posibles en el problema de las n-reinas tiene complejidad $O(2^{n^{2}})$
- Si tengo un for es probable que me quede una sumatoria en la función recursiva.
- Cuando hagamos inducción nos importan las constantes, entonces no está bueno olvidarselas uasndo la notación asintótica.
- En el Cormen cuando demuestran por inducción se llama el método de la sustitución.
- Leer el capítulo 4 del Cormen. 4.3, 4.4 principalmente.
- Cuando no tengo un n trivial entonces lo que me fijo es poner a n como el tamaño de mi instancia para cada instancia.
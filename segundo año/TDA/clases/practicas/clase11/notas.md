# Clase ejercicios de flujo parte 2

# Ejercicio: Hospitales

![alt text](image.png)

![alt text](image-1.png)

Esto es lo clásico que piden en un problema de flujo máximo.

La parte de la complejidad casi siempre es decir: uso EK y esta es la complejidad.

![alt text](image-2.png)

![alt text](image-3.png)

![alt text](image-4.png)

![alt text](image-5.png)

![alt text](image-6.png)

azul y rojo son D1 y D2.

Está buena esa idea! Para cada médico le asignamos un período y a cada período le asignamos los días del período. Para otro médico GENERAMOS un nodo por cad período en el que puede trabajar (aún si se repite con otro médico) y lestooo.

![alt text](image-7.png)

![alt text](image-8.png)

![alt text](image-9.png)

![alt text](image-10.png)

![alt text](image-11.png)

es C para evitar que un médico trabaje más de C días.

![alt text](image-12.png)

es 1 la capacidad porque en cada día solo puede trabajar un solo médico.

En las aristas que no tienen capacidad podemos tener capacidad mayor o igual que 1, lo más restrictivo es 1, pero si es infinito sigue estando bien.

# Nota:
- Nos puede pasar que pusimos todas las restricciones del problema sobre el grafo, entonces la capacidad no nos va a importar. Podemos argumentar de esa manera que esa capacidad puede ser infinito porque no nos importa.

![alt text](image-13.png)

![alt text](image-14.png)

![alt text](image-15.png)

> IMPORTANTE: siempre que modelemos una red de flujo tenemos que pensar en esto: ¿Qué siginifica una unidad de flujo? Esto es lo que nos sirve para argumentar que nuestro modelo modela al problema.

![alt text](image-16.png)

Quiero mostrar que una solución candidata a mi problema del mundo real implica que hay un flujo en mi modelo y que ese flujo implica a una solución al problema del mundo real.

![alt text](image-17.png)

![alt text](image-18.png)

![alt text](image-19.png)

![alt text](image-20.png)

![alt text](image-21.png)

Usamos ese teorema porque sí o sí el flujo tiene que ser un número entero, entonces conviene usar este teorema. Hay muchas propiedades útiles cuando el flujo es entero.

La vuelta es: dado un flujo ¿Cómo reconstruirías tu asignación?

![alt text](image-22.png)

![alt text](image-23.png)

Para esto queremos tener acotado lo más posible los valores de cada complejidad del algoritmo que resuelva al problema.

![alt text](image-24.png)

![alt text](image-25.png)

![alt text](image-26.png)

![alt text](image-27.png)

# Nota:
- Generalmente estas justificaciones son medio constructivas.
- Siempre tenemos que justificar que todo el flujo que entra es el mismo flujo que sale.
- En general las formas de argumentar al flujo máximo: casi siempre va a ser viendo un corte.
- Usamos el mínimo entre mf y nm^2 porque el primero es FF y el otro e EK, FF es un método más que un algoritmo porque puede implementarse la búsqueda con diferentes algorimos.
- La U es el flujo.

# Moraleja del ejercicio:
### A veces nos conviene esto ee repetir nodos para poder manejar por capas.


# Ejercicio Titanic

![alt text](image-28.png)

![alt text](image-29.png)

![alt text](image-30.png)

A este tipo de problemas se les llama problemas de transporte: tenemos algo que queremos mover a otro lugar según algunas condiciones.

![alt text](image-31.png)

No metemos al agua ninguna solución factible porque se muere.

![alt text](image-32.png)

![alt text](image-33.png)

![alt text](image-34.png)

![alt text](image-35.png)

![alt text](image-36.png)

![alt text](image-37.png)

![alt text](image-38.png)

![alt text](image-39.png)

![alt text](image-40.png)

![alt text](image-41.png)

![alt text](image-42.png)

Para el problema no es relevante el tema de que puede haber una sola en el iceberg a la vez pues en el caso implementativo lo que podemos hacer asignarle un turno a cada una y listo señores ;).

![alt text](image-43.png)

![alt text](image-44.png)

![alt text](image-45.png)

![alt text](image-46.png)

![alt text](image-47.png)

![alt text](image-48.png)

![alt text](image-49.png)

![alt text](image-50.png)

![alt text](image-51.png)

![alt text](image-52.png)

![alt text](image-53.png)

![alt text](image-54.png)

![alt text](image-55.png)

![alt text](image-56.png)

![alt text](image-57.png)

![alt text](image-58.png)

![alt text](image-59.png)

![alt text](image-60.png)

El tema del orden es solo una interpretación que le damos al flujo, porque el flujo lo que va a hacer es darme todos los caminos, nosotros tenemos que que asignar el orden para que puedan salvarse todas las personas que el flujo me dio.

![alt text](image-61.png)

![alt text](image-62.png)

![alt text](image-63.png)

![alt text](image-64.png)

![alt text](image-65.png)

![alt text](image-66.png)

![alt text](image-67.png)

![alt text](image-68.png)

# Notas:
- Lo de duplicar al nodo es un buen truco si queremos agregarle una "capacidad a un nodo", en realidad es agregar capacidades y restricciones.
- argumentar la conexión del grafo con el problema puede ser trivial pero es muy importante.

Necesitamos los sensores, la tierra y las ventanas de tiempo como nodos.

fuente a receptores, una cola por cada ventana de tiempo (Q1,1; Q1,2; Q2,1, ...) (se conectan con capacidades art), las colas tienen capacidades de datos que pueden almacenar (hacemos lo de asignarle una capacidad a los nodos) o guardarse en el tiempo (mandarlos a las colas de tiempo t +1), y las colas se conectan con su ventana asociada.    

idea importante:

nosotros queremos modelas las colas que vamos modelando en el tiempo, entonces bamos a tener que resgtringirlas por cada bentana tenemos que tener las colas en tiempo 1, 2, ,3 y 4 y tiene qiet haber iuna retroalimentación de en tiempo 1 me ghuardo el datro o lo mando a las dempas colas.

Una unidad de flujo es un megabyte. 

La semántica es un receptor le manda todos los datos a la cola, si la cola no pudo entonces la manda a otra ventana de tiempo y la cola le manda todo lo que puede a la ventana.

# Notas parcial:
- El parcial va a tener el mismo formato que el anterior. Van a ser de 3 de desarrollo.
- Escribir todo lo que sepamos, aun si no nos acordamos de algo.
- Los ejercicios de la guía que son avanzados son como los del parcial, echarles un ojo.
- Los choices van a ser más teóricos.
- Los de desarrollo van a ser más parecidos a lso que hicimos en las prácticas.
- Nos van a pedir seguramente que justifiquemos, no que demostremos. Más que nada porque el problema puede estar en lenguaje natural.
- En el parcial nos van a decir (MUY PROBABLE) algo como: dada una matriz dime cómo creas el grafo.

# Notas:
- Corte mínimo y capacidades y flujo.
- Repasar las propiedades de cada algoritmo.
- Prim vs kruskal.
- Complejidades y cuando conviene cada una.


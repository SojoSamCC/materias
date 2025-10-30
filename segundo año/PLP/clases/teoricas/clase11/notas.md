# Resolución lógica

# Idea:

Hacer un programa que dada una proposición me diga si es verdadera o no. 

ES imposible lograr hacer un programa capaz de eso, sin embargo lo que se puede hacer es un algoritmo que: dada una proposición, me dice si es verdadera o no, si no me dice eso es porque puede seguir indefinidamente o que sea falsa.

![alt text](image.png)

> Rojo es predicado.

> Azul son constantes.

# Notas:
- Uno lo que hace en prolog es tener una base de conocimiento.

![alt text](image-1.png)

Mayúsculas son variables.

En prolog uno no escribe suma(1, 2) = 3 sino suma(1, 2, 3). Es un predicado. O sea esto es como decir la suma de X + Y es Z: suma(X, Y, Z)

![alt text](image-2.png)

Las variables son todas las letras mayúsculas que aparezcan libres. El ejemplo se lee como

para todo X, Y, Z. padre(X, Z) y padre(Z, Y) => abuelo(X, Y)

![alt text](image-3.png)

Prolog trabaja asumiendo la lógica clásica.

# Notas:
- Un termino puede ser una variable o un símbolo de función de aridad n aplicado a n términos.

# Resolución para lógica proposicional

![alt text](image-4.png)

![alt text](image-5.png)

Luego de aplicar el paso 1 y 2 repetidas veces al final nos queda solo negaciones o no de fórmulas atómicas o la conjunción y disyunción entre ellas.

> En lógica intuicionista no valen ni el paso 1 ni el 2, pero com oestamos en lógica clásica entonces sí se vale.


![alt text](image-6.png)

Una CNF puede tener una sola clásula, no necesariamente tiene que tener el and.

- Un literal es un fórmula atómica negada o no.
- Una cláusula es una disyunción entre literales.
- Una CNF es una conjunción entre cláusulas.

![alt text](image-7.png)

Podemos escribirla como conjunto porque la conjunción es conmutativa y no nos importa el orden, y también como es idempotente no nos importan los repetidos, y como es asociativa tampoco nos importa cómo asociamos los valores del conjunto. Gracias a esas 3 propiedades se comporta como un conjunto.

AL final del día tendríamos un conjunto de conjuntos.

Cada valor del conjunto de conjuntos representa un fórmula.

```
Ejemplo:

{{P, Q}, {¬P, R}} representa a la fórmula (P V Q) ∧ (¬P V R)

{} como CNF es True porque representa a todas las fórmulas

{{}} como CNF es Bottom porque representa a la conjunción de Falso con todas las demás fórmulas.
```

![alt text](image-8.png)

![alt text](image-9.png)

Una CNF es basicamente: ningún V tiene adentro un ∧ y solo hay ¬ en fórmulas atómicas.

![alt text](image-10.png)

```
La regla de resolución se resume o se puede reescribir a esto.


|- P V Q            |- ¬P V R
_______________________________________
|- Q V R

Tomando en cuenta que Q y R pueden ser muchas más fórmulas. 
```

O sea, lo que se hace es como identifcar un P que se ve en una sección de nuestro conjunto de cláusulas, y separalo con un ¬P que aparezca en otra sección de ese mismo conjunto y separarlos.

```
Ejemplo

{P, Q, ¬R} {R, S, Q, ¬P} Si tomamos como P a R, entonces tiene como resolvente {P, Q, S, Q, ¬P}
```

Es como "enchufar" dos cláusulas.

![alt text](image-11.png)

La idea es ir enchufando dos cláusulas para que me aparezcan cláusulas que no tengo en el C actual. Si llego a que no tengo dos cláusulas que se puedan enchufar entonces es que originalmente C es Satisfacible (Devolver SAT), si llego a {} devolver Insatisfacible porque probé que negandola entonces llegué al bottom.

![alt text](image-12.png)

![alt text](image-13.png)

![alt text](image-14.png)

# Resolución para lógica de primer orden

![alt text](image-15.png)

Si quiero ver si una fórmula es válida y la fórmula tiene variables libres, entonces meto un para todo por cada variable libre diferente.

![alt text](image-16.png)

Lo que está en gris es lo que no es nuevo con respecto a lo de antes.

![alt text](image-17.png)

![alt text](image-18.png)

Que sea satisfactible quiere decir que hay una interpretación tal que a cada elemento del universo existe una interpretación que haga verdadera la fórmula.

Que dos fórmulas sean equivalentes significa que toda interpretación de una haga verdadera a la otra. El lema ese dice que si existe una interpretación que haga verdadera a una, entonces también hace verdadera a la otra.

Lo que hacemos es tomamos un símbolo de función nuevo y extendemos al lenguaje con ese nuevo símbolo de función. No puede ser un símbolo de función que ya esté en uso.

![alt text](image-19.png)

![alt text](image-20.png)

![alt text](image-21.png)

![alt text](image-22.png)

{{P(X), Q(X, Y)}, {¬P(X), R(Y,Y)}} La X que está en el primer conjunto es la misma para todo lo que está adentro de ese conjunto, PERO no es la misma que la del otro conjunto.

![alt text](image-23.png)

![alt text](image-24.png)

El existencial lo sacamos poniendole a f las variables que aparecen en P que no sean Y.

![alt text](image-25.png)

![alt text](image-26.png)

![alt text](image-27.png)

O sea, esto es: divido en dos conjuntos: por un lado los que no están negados junto con todo lo que le quedaba "asociado", y por el otro lado los no negados junto con todo lo que le había quedado "asociado".

sí o sí hay que elegir al menos una cosa de cada lado. No puedo tener variables en común entre cada conjunto, hay que hacer renombre si llegamos a tener conjuntos diferentes con variables con el mismo nombre.

![alt text](image-28.png)

![alt text](image-29.png)

![alt text](image-30.png)

![alt text](image-31.png)

![alt text](image-32.png)

![alt text](image-33.png)


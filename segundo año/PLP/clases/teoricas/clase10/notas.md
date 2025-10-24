# Lógica de primer orden

![alt text](image.png)

Las proposiciones atómicas son indivisibles.

![alt text](image-1.png)

Que algo se pueda 'computar' es algo que se pueda calcular automáticamente usando alguna máquina.

![alt text](image-2.png)

# Sintaxis de la lógica de primer orden.

![alt text](image-3.png)

> Un lenguaje es un conjunto de símbolos, informalmente.

> La aridad es el conjunto de argumento que toma cada función, acá la función es un símbolo, no exactamante una función como uno lo piensa normalmente (aunque más adelante sí se comporta como una).

![alt text](image-4.png)

Siempre deben coincidir la aridad de la f con la cantidad de argumentos que le damos. 

> t es una variable o una función de aridad n que toma n términos.

![alt text](image-5.png)

El igual es un símbolo de aridad 2.

Hasta este punto los símbolos que vemos no significan nada porque no le hemos dado una semántica formalmente en este lenguaje L.

![alt text](image-6.png)
![alt text](image-7.png)

Los símbolos de predicado (en rojo) deben recibir dos términos, no puede pasar que reciba otro predicado porque no está definido en este lenguaje.

Los "para todo" y "existe" son un constructor de fórmulas.

> Hasta este punto la noción de si una fórmula es "verdadera" no existe.

![alt text](image-8.png)

![alt text](image-9.png)

```
No podíamos hacer

σ{X := Z ∗ Z} ≡ succ(Z ∗ Z) = Y =⇒ ∃Z.(Z ∗ Z) + Z = Y porque estaríamos ligando una variable que originalmente era libre.
```


# Notas
- La lógica es el fundamento de la programación lógica, y desde otro punto de vista también de la programación funcional.

# Deducción natural para lógica de primer orden

![alt text](image-10.png)

### Cuantificación universal

![alt text](image-11.png)

Para todo E
Lo que quiere decir es que para toda aparición libre de X entonces sí vale que esa X la podemos reemplazar por cualquier cosa y aún así vale sigma, entonces vale el el para todo.

Para todo i
```
No podíamos escribir R0 |- sigam{X:=t} porque eso significa que reemplazamos en sigma por UN tau particular.
```
Un definición equivalente era
```
Γ ⊢ σ X{X:=Z} Z fresca
_______________________
Γ ⊢ ∀X. σ
```

![alt text](image-12.png)

```
                                              | Acá se hizo σ{X:=cos(X)} no hay problema con
                                              |  ese reemplazo. Es como decir: el cos de cualquier
∀X.(P(X) ∧ Q(X)) ⊢ ∀X.(P(X) ∧ Q(X))     <~~~ | cosa puede valer -particularmente-, cualquier cosa
________________________________________
                            σ
                    ____________________ 
∀X.(P(X) ∧ Q(X)) ⊢ P(cos(X)) ∧ Q(cos(X))
```

![alt text](image-13.png)

si hay dos para todos, entonces sus variables ligadas son totalmente diferentes.
```
∀X. P(X). ∀X. Q(X) Por más que las X's sean las mismas (a nivel símbolos) esa expresión es totalmente equivalente a ∀X. P(X). ∀Y. Q(Y)
```

> Dos fórmulas que difieren únicamente en el nombre de las variables ligadas, son equivalentes entre sí.

![alt text](image-14.png)

### Cuantificación existencial

![alt text](image-15.png)

![alt text](image-16.png)

No podíamos hacer Ei en el segundo paso porque nos lleva a un callejón sin salida.

![alt text](image-17.png)

![alt text](image-18.png)

Buscar un caso patológico donde no valga eso.

# Semántica de la lógica de primer orden

![alt text](image-19.png)

![alt text](image-20.png)

![alt text](image-21.png)

![alt text](image-22.png)

![alt text](image-23.png)

![alt text](image-24.png)

![alt text](image-25.png)

Un modelo es que existe un universo y una función de interpretación que hace que una fórmula sigma sea verdadera BAJO esa estructura.

![alt text](image-26.png)

![alt text](image-27.png)

El primero es inválido porque el = no tiene la interpretación que uno se espera necesariamente. Puede ser como que el = tiene la interpretación que lo de la izquierda sea true y la derecha false.

![alt text](image-28.png)

# Unificación de términos

![alt text](image-29.png)

A partir de esta diapo no dieron más clase. Supongo que hay que leer lo que sigue.

# Notas personales
- Investigar acerca de sistemas distribuidos.

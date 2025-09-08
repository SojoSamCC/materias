package main

import (
	"bufio"
	"fmt"
	"os"
)

var energia []int
var palabras []string
var cant_palabras int
var memo = make(map[string]int)

const infinito = int(1e18)

func obtener_entrada() {
	in := bufio.NewReader(os.Stdin)

	// Leer primera linea
	var n int
	fmt.Fscan(in, &n)

	cant_palabras = n

	// Inicializo tamaño de array energía
	energia = make([]int, n)

	// Leer cantidad de energía
	for i := 0; i < n; i++ {
		fmt.Fscan(in, &energia[i])
	}

	// Leer palabras pero solo guardar primera y última letra
	palabras = make([]string, n)
	for i := 0; i < n; i++ {
		var palabra string
		fmt.Fscan(in, &palabra)

		if len(palabra) == 1 {
			// palabra de un solo carácter → primera = última
			palabras[i] = string(palabra[0])
		} else {
			primera := palabra[0]
			ultima := palabra[len(palabra)-1]
			palabras[i] = string(primera) + string(ultima)
		}
	}
}
func ordenar(pos_palabra int, pos_char int, ultima_letra byte, acc int) int {

	clave := fmt.Sprintf("%d-%d-%c", pos_palabra, pos_char, ultima_letra)

	if valor, existe := memo[clave]; existe {
		return valor
	}

	if pos_palabra == cant_palabras {
		return acc
	}

	palabra_actual := palabras[pos_palabra]
	largo := len(palabra_actual)

	// m := "palabra_actual [0]: " + string(palabra_actual[0]) + " | palabra_actual [1]: " + string(palabra_actual[1]) + " | Ultima letra: " + string(ultima_letra)
	// fmt.Println(m)

	if largo > 1 {
		// fmt.Println("palabra_actual[0] < ultima_letra: ", palabra_actual[0] < ultima_letra)
		if palabra_actual[0] < ultima_letra {
			if palabra_actual[1] < ultima_letra {
				clave = fmt.Sprintf("%d-%d-%c", pos_palabra, palabra_actual[0], ultima_letra)
				acc = infinito
			} else {
				clave = fmt.Sprintf("%d-%d-%c", pos_palabra, palabra_actual[1], ultima_letra)
				acc = ordenar(pos_palabra+1, 0, palabra_actual[1], acc+energia[pos_palabra])
			}
		} else if palabra_actual[1] < ultima_letra {
			clave = fmt.Sprintf("%d-%d-%c", pos_palabra, palabra_actual[0], ultima_letra)
			acc = ordenar(pos_palabra+1, 0, palabra_actual[0], acc)
		} else {
			acc = min(ordenar(pos_palabra+1, 0, palabra_actual[0], acc), ordenar(pos_palabra+1, 0, palabra_actual[1], acc+energia[pos_palabra]))
		}
	} else {
		if palabra_actual[0] < ultima_letra {
			clave = fmt.Sprintf("%d-%d-%c", pos_palabra, palabra_actual[0], ultima_letra)
			acc = infinito
		} else {
			acc = ordenar(pos_palabra+1, 0, palabra_actual[0], acc)
		}
	}

	memo[clave] = acc

	return acc
}
func main() {

	obtener_entrada()

	res := ordenar(0, 0, ' ', 0)

	if res == infinito {
		fmt.Println(-1)
	} else {
		fmt.Println(res)
	}
}

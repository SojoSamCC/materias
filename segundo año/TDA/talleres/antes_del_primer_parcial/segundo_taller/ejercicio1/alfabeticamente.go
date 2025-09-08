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

	// Leer palabras completas
	palabras = make([]string, n)
	for i := 0; i < n; i++ {
		var palabra string
		fmt.Fscan(in, &palabra)
		palabras[i] = palabra
	}
}

func reverse(palabra string) string {
	runes := []rune(palabra)
	n := len(runes)
	// invierto las runes del string
	for i := 0; i < n/2; i++ {
		runes[i], runes[n-1-i] = runes[n-1-i], runes[i]
	}
	return string(runes) // vuelve a string
}
func ordenar(pos_palabra int, acc int) int {

	clave := fmt.Sprintf("%d-%d", pos_palabra, pos_palabra-1)

	if valor, existe := memo[clave]; existe {
		return valor
	}

	if pos_palabra+1 == cant_palabras {
		return acc
	}

	palabra_actual := palabras[pos_palabra]
	palabra_siguiente := palabras[pos_palabra+1]

	if palabra_actual > palabra_siguiente {
		if reverse(palabra_actual) > palabra_siguiente {
			acc = infinito
		} else {
			acc = ordenar(pos_palabra+1, acc+energia[pos_palabra])
		} // no sé cómo manejar el caso donde le hago reverse a una palabra y eso me modifica tod0o lo anterior.
	} else {
		acc = ordenar(pos_palabra+1, acc)
	}

	memo[clave] = acc

	return acc
}
func main() {

	obtener_entrada()

	res := ordenar(1, 0)

	if res == infinito {
		fmt.Println(-1)
	} else {
		fmt.Println(res)
	}

}

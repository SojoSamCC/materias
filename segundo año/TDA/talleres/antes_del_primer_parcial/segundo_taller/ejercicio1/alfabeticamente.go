package main

import (
	"bufio"
	"fmt"
	"os"
)

var energia []int
var memo [][2]int
var palabras []string
var cant_palabras int
var palabras_reverse []string

const infinito = int(1e18)

func reverse(palabra string) string {
	runes := []rune(palabra)
	n := len(runes)
	// invierto las runes del string
	for i := 0; i < n/2; i++ {
		runes[i], runes[n-1-i] = runes[n-1-i], runes[i]
	}
	return string(runes) // vuelve a string
}
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
	palabras_reverse = make([]string, n)
	for i := 0; i < n; i++ {
		var palabra string
		fmt.Fscan(in, &palabra)
		palabras[i] = palabra
		palabras_reverse[i] = reverse(palabra)
	}

	memo = make([][2]int, cant_palabras)
	for i := 0; i < cant_palabras; i++ {
		memo[i][0] = infinito - 1
		memo[i][1] = infinito - 1
	}
}
func ordenar(era_reverse int, pos_palabra int) int {

	if pos_palabra == cant_palabras {
		return 0
	}

	if memo[pos_palabra][era_reverse] != infinito-1 {
		return memo[pos_palabra][era_reverse]
	}

	palabra_actual := palabras[pos_palabra]

	var palabra_anterior string
	if era_reverse == 1 {
		palabra_anterior = palabras_reverse[pos_palabra-1]
	} else {
		palabra_anterior = palabras[pos_palabra-1]
	}

	acc := infinito

	if palabra_anterior <= palabra_actual {
		acc_temp := ordenar(0, pos_palabra+1)
		if acc_temp <= acc {
			acc = acc_temp
		}
	}

	if palabras_reverse[pos_palabra] >= palabra_anterior {
		acc_temp := ordenar(1, pos_palabra+1)

		acc_temp += energia[pos_palabra]
		if acc_temp <= acc {
			acc = acc_temp
		}
	}

	memo[pos_palabra][era_reverse] = acc

	return acc
}
func main() {

	obtener_entrada()

	res := min(ordenar(0, 1), ordenar(1, 1)+energia[0])

	if res == infinito {
		fmt.Println(-1)
	} else {
		fmt.Println(res)
	}

}

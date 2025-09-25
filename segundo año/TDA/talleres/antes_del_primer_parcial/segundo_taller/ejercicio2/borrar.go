package main

import (
	"bufio"
	"fmt"
	"os"
)

var memo [][]int // variable global
var palabra []byte
var largo_string int

const infinito = int(1e9)

func obtener_entrada() {
	in := bufio.NewReader(os.Stdin)

	// Leer la primera línea (largo_string)
	fmt.Fscanln(in, &largo_string)

	// Leer la segunda línea (la palabra)
	linea, _ := in.ReadString('\n')
	linea = linea[:len(linea)-1] // eliminar el salto de línea
	palabra = []byte(linea)      // convertir string a slice de bytes
	// hago eso para poder acceder a los Char de la palabra como si fueran una lista de Char
}

func borrar() int {
	// hasta este punto puedo asumir que memo[i][i] siempre va a ser 1 porque eso es la minima cantidad de pasos que hay que hacer para borrar una letra consimo misma.

	for largo_string_parcial := 2; largo_string_parcial <= largo_string; largo_string_parcial++ {

		desde := 0
		hasta := largo_string_parcial + desde - 1
		for hasta < largo_string {

			memo[desde][hasta] = 1 + memo[desde+1][hasta]

			desde_intermedio := desde + 1
			for desde_intermedio <= hasta {

				if palabra[desde_intermedio] == palabra[desde] {

					acc := 0

					if desde_intermedio+1 <= hasta {
						acc = memo[desde_intermedio+1][hasta]
					}

					memo[desde][hasta] = min(memo[desde][hasta], memo[desde+1][desde_intermedio]+acc)
				}

				desde_intermedio += 1
			}

			desde += 1
			hasta = largo_string_parcial + desde - 1
		}
	}

	return memo[0][largo_string-1]
}

func main() {
	obtener_entrada()

	// Aprovecho e inicializo la matriz para memorizar.
	memo = make([][]int, largo_string)
	for i := 0; i < largo_string; i++ {
		memo[i] = make([]int, largo_string)
		for j := 0; j < largo_string; j++ {
			if i == j {
				memo[i][j] = 1
			} else {
				memo[i][j] = infinito
			}
		}
	}

	res := borrar()

	fmt.Println(res)
}

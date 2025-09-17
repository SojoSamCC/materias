package main

import (
	"bufio"
	"fmt"
	"os"
)

var palabra []byte
var largo_string int
var memo [][]int // variable global

const infinito = int(1e18)

func obtener_entrada() {
	in := bufio.NewReader(os.Stdin)

	// Leer la primera línea (largo_string)
	fmt.Fscanln(in, &largo_string)

	// Leer la segunda línea (la palabra)
	linea, _ := in.ReadString('\n')
	linea = linea[:len(linea)-1] // eliminar el salto de línea
	palabra = []byte(linea)      // convertir string a slice de bytes

	// // Inicializar la matriz global memo de tamaño largo_string x largo_string
	// memo = make([][]int, largo_string)
	// for i := range memo {
	// 	memo[i] = make([]int, largo_string)
	// 	for j := range memo[i] {
	// 		memo[i][j] = -1 // asignar -1 a cada posición
	// 	}
	// }
}

//	func borrar(pos_cambio int, acc int) int {
//		if memo[pos_cambio] != infinito {
//			return memo[pos_cambio]
//		}
//		if acc >= minimo {
//			return infinito
//		}
//	}
// func borrar(pos_inicio int, pos_fin int, pos_fin_por_caso int, era_por_caso bool) int {

// 	if era_por_caso {
// 		if pos_inicio > pos_fin_por_caso {
// 			return 0
// 		}
// 		if palabra[pos_inicio] != palabra[pos_fin] {
// 			return borrar(pos_inicio, pos_fin+1, pos_fin_por_caso, true)
// 		}
// 		// if pos_inicio-pos_fin > 0 {
// 		// 	acc := borrar(pos_inicio+1, pos_inicio+1, pos_fin_por_caso, true)
// 		// } else {
// 		// 	return borrar(pos_inicio, pos_fin+1, pos_fin_por_caso, true)
// 		// }
// 	}

// 	if pos_fin > largo_string {
// 		return 0
// 	}
// 	if palabra[pos_inicio] != palabra[pos_fin] {
// 		return borrar(pos_inicio, pos_fin+1, pos_fin_por_caso+1, false)
// 	}
// 	if pos_fin-pos_inicio > 0 {
// 		acc := borrar(pos_inicio+1, pos_inicio+1, pos_fin_por_caso, true)
// 		return 1 + acc + borrar(pos_fin+1, pos_fin+1, pos_fin+1, false)
// 	} else {
// 		return borrar(pos_inicio, pos_fin+1, pos_fin_por_caso+1, false)
// 	}

// }
func borrar() int {
	// hasta este punto puedo asumir que memo[i][i] siempre va a ser 1 porque eso es la minima cantidad de pasos que hay que hacer para borrar una letra consimo misma.
	for i := range largo_string {
		for j := i; j < largo_string; j++ {
			for k := i + 1; k < j; k++ {
				// no sé cómo comparar esto. La idea que el se compare cuanto me costó lo del medio.
			}
		}
	}
}
func main() {
	obtener_entrada()
	memo = make([][]int, largo_string)
	for i := range largo_string {
		memo[i] = make([]int, largo_string)
	}
	for i := range largo_string {
		memo[i][i] = 1
	}
	borrar()

	// if largo_string == 1 {
	// 	fmt.Println(1)
	// }

	// pos_inicio := 0
	// posciones_cambio = make([][]int, 0)
	// largo_posiciones_cambio := 0
	// for i := 1; i < largo_string; i++ {
	// 	if palabra[i] != palabra[i-1] {
	// 		posciones_cambio = append(posciones_cambio, []int{pos_inicio, i - 1})
	// 		pos_inicio -= pos_inicio
	// 		pos_inicio += i
	// 		largo_posiciones_cambio += 1
	// 	}
	// }

	// // Agregar el último segmento
	// posciones_cambio = append(posciones_cambio, []int{pos_inicio, largo_string - 1})

	// memo = make([]int, largo_posiciones_cambio)
	// for i := 0; i < largo_posiciones_cambio; i++ {
	// 	memo[i] = infinito
	// }

	// for i := 0; i < largo_posiciones_cambio; i++ {
	// 	memo[i] = borrar(i)
	// }
}

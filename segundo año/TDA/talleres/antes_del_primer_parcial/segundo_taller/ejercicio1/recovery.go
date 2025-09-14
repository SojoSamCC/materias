// package main

// import (
// 	"bufio"
// 	"fmt"
// 	"os"
// 	"time"
// )

// var energia []int
// var palabras []string
// var cant_palabras int
// var memo = make(map[string]int)

// const infinito = int(1e18)

// func obtener_entrada() {
// 	in := bufio.NewReader(os.Stdin)

// 	// Leer primera linea
// 	var n int
// 	fmt.Fscan(in, &n)

// 	cant_palabras = n

// 	// Inicializo tamaño de array energía
// 	energia = make([]int, n)

// 	// Leer cantidad de energía
// 	for i := 0; i < n; i++ {
// 		fmt.Fscan(in, &energia[i])
// 	}

// 	// Leer palabras completas
// 	palabras = make([]string, n)
// 	for i := 0; i < n; i++ {
// 		var palabra string
// 		fmt.Fscan(in, &palabra)
// 		palabras[i] = palabra
// 	}
// }

// func reverse(palabra string) string {
// 	runes := []rune(palabra)
// 	n := len(runes)
// 	// invierto las runes del string
// 	for i := 0; i < n/2; i++ {
// 		runes[i], runes[n-1-i] = runes[n-1-i], runes[i]
// 	}
// 	return string(runes) // vuelve a string
// }
// func ordenar(era_reverse bool, pos_palabra int, acc int) int {

// 	// clave := fmt.Sprintf("%t-%d-%d", era_reverse, pos_palabra, acc)

// 	// if valor, existe := memo[clave]; existe {
// 	// 	return valor
// 	// }

// 	mensaje := fmt.Sprintf("Posicion: %d, acc: %d", pos_palabra, acc)
// 	println(mensaje)
// 	if pos_palabra == cant_palabras {
// 		// memo[clave] = acc
// 		return acc
// 	}

// 	palabra_actual := palabras[pos_palabra]

// 	var palabra_anterior string
// 	if era_reverse {
// 		palabra_anterior = reverse(palabras[pos_palabra-1])
// 	} else {
// 		palabra_anterior = palabras[pos_palabra-1]
// 	}

// 	if palabra_anterior <= palabra_actual {
// 		if palabra_anterior <= reverse(palabra_actual) {
// 			return min(ordenar(false, pos_palabra+1, acc), ordenar(true, pos_palabra+1, acc+energia[pos_palabra]))
// 		} else {
// 			return ordenar(false, pos_palabra+1, acc)
// 		}
// 	} else if palabra_anterior <= reverse(palabra_actual) {
// 		return ordenar(true, pos_palabra+1, acc+energia[pos_palabra])
// 	} else {
// 		// if pos_palabra-1 == 0 {
// 		// 	if reverse(palabra_anterior) <= palabra_actual {
// 		// 		if reverse(palabra_anterior) <= reverse(palabra_actual) {
// 		// 			mensaje := fmt.Sprintf("Posicion: %d, acc: %d, energia[pos_palabra-1]: %d", pos_palabra, acc, energia[pos_palabra-1])
// 		// 			println(mensaje)
// 		// 			return min(ordenar(pos_palabra+1, acc+energia[pos_palabra-1]+energia[pos_palabra]), ordenar(pos_palabra+1, acc+energia[pos_palabra-1]))
// 		// 		} else {
// 		// 			return ordenar(pos_palabra+1, acc+energia[pos_palabra-1])
// 		// 		}
// 		// 	} else {
// 		// 		return infinito
// 		// 	}
// 		// } else {
// 		// 	println("\ntoy aca")
// 		// 	mensaje := fmt.Sprintf("Posicion: %d, acc: %d", pos_palabra, acc)
// 		// 	println(mensaje)
// 		return infinito
// 		// }
// 	}
// }
// func ordenar_memo(era_reverse bool, pos_palabra int, acc int) int {

// 	clave := fmt.Sprintf("%t-%d-%d", era_reverse, pos_palabra, acc)

// 	if valor, existe := memo[clave]; existe {
// 		return valor
// 	}

// 	mensaje := fmt.Sprintf("Posicion: %d, acc: %d", pos_palabra, acc)
// 	println(mensaje)
// 	if pos_palabra == cant_palabras {
// 		memo[clave] = acc
// 		return acc
// 	}

// 	palabra_actual := palabras[pos_palabra]

// 	var palabra_anterior string
// 	if era_reverse {
// 		palabra_anterior = reverse(palabras[pos_palabra-1])
// 	} else {
// 		palabra_anterior = palabras[pos_palabra-1]
// 	}

// 	if palabra_anterior <= palabra_actual {
// 		if palabra_anterior <= reverse(palabra_actual) {
// 			return min(ordenar(false, pos_palabra+1, acc), ordenar(true, pos_palabra+1, acc+energia[pos_palabra]))
// 		} else {
// 			return ordenar(false, pos_palabra+1, acc)
// 		}
// 	} else if palabra_anterior <= reverse(palabra_actual) {
// 		return ordenar(true, pos_palabra+1, acc+energia[pos_palabra])
// 	} else {
// 		// if pos_palabra-1 == 0 {
// 		// 	if reverse(palabra_anterior) <= palabra_actual {
// 		// 		if reverse(palabra_anterior) <= reverse(palabra_actual) {
// 		// 			mensaje := fmt.Sprintf("Posicion: %d, acc: %d, energia[pos_palabra-1]: %d", pos_palabra, acc, energia[pos_palabra-1])
// 		// 			println(mensaje)
// 		// 			return min(ordenar(pos_palabra+1, acc+energia[pos_palabra-1]+energia[pos_palabra]), ordenar(pos_palabra+1, acc+energia[pos_palabra-1]))
// 		// 		} else {
// 		// 			return ordenar(pos_palabra+1, acc+energia[pos_palabra-1])
// 		// 		}
// 		// 	} else {
// 		// 		return infinito
// 		// 	}
// 		// } else {
// 		// 	println("\ntoy aca")
// 		// 	mensaje := fmt.Sprintf("Posicion: %d, acc: %d", pos_palabra, acc)
// 		// 	println(mensaje)
// 		return infinito
// 		// }
// 	}
// }
// func main() {

// 	obtener_entrada()

// 	start := time.Now()
// 	res := min(ordenar(false, 1, 0), ordenar(true, 1, energia[0]))
// 	tiempo_transcurrido := time.Since(start)

// 	start = time.Now()
// 	res_memo := min(ordenar(false, 1, 0), ordenar(true, 1, energia[0]))
// 	tiempo_transcurrido_memo := time.Since(start)

// 	if res == infinito {
// 		fmt.Println(-1)
// 	} else {
// 		fmt.Println(res)
// 	}

// 	// Muestra el tiempo exacto en varias unidades
// 	// fmt.Printf("Tiempo de ejecución: %v\n", tiempo_transcurrido)
// 	// fmt.Printf("En nanosegundos: %d ns\n", tiempo_transcurrido.Nanoseconds())
// 	// fmt.Printf("En microsegundos: %.3f µs\n", float64(tiempo_transcurrido.Nanoseconds())/1000)
// 	fmt.Printf("res en milisegundos: %.3f ms\n", float64(tiempo_transcurrido.Nanoseconds())/1e6)
// 	fmt.Printf("res_memo en milisegundos: %.3f ms\n", float64(tiempo_transcurrido_memo.Nanoseconds())/1e6)

// 	if float64(tiempo_transcurrido.Nanoseconds())/1e6 <= float64(tiempo_transcurrido_memo.Nanoseconds())/1e6 {
// 		fmt.Printf("res")
// 	} else {
// 		if res_memo == infinito {
// 			fmt.Println(-1)
// 		} else {
// 			fmt.Println(res_memo)
// 		}
// 		fmt.Printf("res_memo")
// 	}
// }

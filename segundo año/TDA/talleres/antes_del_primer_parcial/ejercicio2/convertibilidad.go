package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func obtener_entrada() (int, int) {
	os_stdin := os.Stdin
	entrada := bufio.NewScanner(os_stdin)
	entrada.Split(bufio.ScanWords)

	siguiente_linea := func() int {
		entrada.Scan()
		var k int
		fmt.Sscan(entrada.Text(), &k)
		return k
	}
	n_carlos := siguiente_linea()
	n_que_quiere := siguiente_linea()

	return n_carlos, n_que_quiere
}

func n_por_dos(n int) int {
	return n * 2
}
func por_10_mas_1(n int) int {
	return n*10 + 1
}

func buscar_solucion(n_carlos int, n_que_quiere int, array_pasos []int) string {

	// Conquer
	if n_carlos == n_que_quiere {
		array_en_formato_de_salida := fmt.Sprint(array_pasos)
		array_en_formato_de_salida = strings.Trim(array_en_formato_de_salida, "[]")
		resultado := fmt.Sprintf("YES\n%d\n%s", len(array_pasos), array_en_formato_de_salida)
		return resultado
	}

	if n_carlos > n_que_quiere {
		return "NO"
	}

	// Divide
	n_carlos_por_2 := n_por_dos(n_carlos)
	multiplicar_por_10_mas_1 := por_10_mas_1(n_carlos)

	array_pasos_por_dos := append([]int{}, array_pasos...)
	array_pasos_por_dos = append(array_pasos_por_dos, n_carlos_por_2)

	array_pasos_por_10_mas_1 := append([]int{}, array_pasos...)
	array_pasos_por_10_mas_1 = append(array_pasos_por_10_mas_1, multiplicar_por_10_mas_1)

	ver_si_salia_con_multiplicar_por_2 := buscar_solucion(n_carlos_por_2, n_que_quiere, array_pasos_por_dos)
	ver_si_salia_con_multiplicar_por_10_mas_1 := buscar_solucion(multiplicar_por_10_mas_1, n_que_quiere, array_pasos_por_10_mas_1)

	// Combine
	if ver_si_salia_con_multiplicar_por_2 != "NO" {
		return ver_si_salia_con_multiplicar_por_2
	} else if ver_si_salia_con_multiplicar_por_10_mas_1 != "NO" {
		return ver_si_salia_con_multiplicar_por_10_mas_1
	} else {
		return "NO"
	}
}
func main() {
	n_carlos, n_que_quiere := obtener_entrada()

	resultado := buscar_solucion(n_carlos, n_que_quiere, []int{n_carlos})

	fmt.Println(resultado)
}

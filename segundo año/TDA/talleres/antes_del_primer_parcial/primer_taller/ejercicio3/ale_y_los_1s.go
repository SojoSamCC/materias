package main

import (
	"bufio"
	"fmt"
	"math/bits"
	"os"
)

func obtener_entrada() (int, int, int) {
	entrada := bufio.NewReader(os.Stdin)
	var n_inicial_ale, l, r int
	fmt.Fscan(entrada, &n_inicial_ale, &l, &r)
	return n_inicial_ale, l, r
}
func buscar_solucion(n_inicial_ale int, l int, r int, altura_del_arbol_de_recursion int) int {

	// Conquer
	if n_inicial_ale == 0 {
		return 0
	} else if n_inicial_ale == 1 {
		return 1
	} else if n_inicial_ale == 2 {
		if r != l {
			return r - l
		} else {
			return r % 2
		}
	} else if n_inicial_ale == 3 {
		return r - l + 1
	}

	// Divide
	cociente_n_inicial_ale_entre_2 := n_inicial_ale / 2
	n_inicial_ale_modulo_2 := n_inicial_ale % 2

	cant_elemetos_de_los_lados := (1 << (altura_del_arbol_de_recursion - 1)) - 1 // 2^(altura_del_arbol_de_recursion-1) - 1

	pos_medio := cant_elemetos_de_los_lados + 1

	// Combine
	if l < pos_medio && r < pos_medio { // comienza en la izquierda y termina en la izquierda
		return buscar_solucion(cociente_n_inicial_ale_entre_2, l, r, altura_del_arbol_de_recursion-1)
	} else if l > pos_medio && r > pos_medio { // comienza en la derecha y termina en la derecha
		return buscar_solucion(cociente_n_inicial_ale_entre_2, l-pos_medio, r-pos_medio, altura_del_arbol_de_recursion-1)
	} else if l < pos_medio && r > pos_medio { // comienza en la izquierda y termina en la derecha
		parte_izquierda := buscar_solucion(cociente_n_inicial_ale_entre_2, l, pos_medio-1, altura_del_arbol_de_recursion-1)
		parte_derecha := buscar_solucion(cociente_n_inicial_ale_entre_2, 1, r-pos_medio, altura_del_arbol_de_recursion-1)
		return parte_izquierda + n_inicial_ale_modulo_2 + parte_derecha
	} else if l < pos_medio && r == pos_medio { // comienza en la izquierda y termina en el medio
		parte_izquierda := buscar_solucion(cociente_n_inicial_ale_entre_2, l, pos_medio-1, altura_del_arbol_de_recursion-1)
		return parte_izquierda + n_inicial_ale_modulo_2
	} else {
		parte_derecha := buscar_solucion(cociente_n_inicial_ale_entre_2, 1, r-cant_elemetos_de_los_lados-1, altura_del_arbol_de_recursion-1)
		return n_inicial_ale_modulo_2 + parte_derecha // comienza en el medio y termina en la derecha
	}
}
func main() {
	n_inicial_ale, l, r := obtener_entrada()

	fmt.Println(buscar_solucion(n_inicial_ale, l, r, bits.Len(uint(n_inicial_ale)))) // bits.Len(uint(n_inicial_ale)) == floor(log2(n_inicial_ale)) + 1)

}

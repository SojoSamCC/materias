package main

import (
	"bufio"
	"fmt"
	"os"
)

var largo_string int
var palabra string

func obtener_entrada() {
	in := bufio.NewReader(os.Stdin)

	// Leer primera linea
	fmt.Fscan(in, &largo_string)

	// Leer segunda linea
	fmt.Fscan(in, &palabra)
}
func hallar_contiguos(pos_string int, palabra string) int {

	inicial := palabra[pos_string]
	final := pos_string + 1
	for final < len(palabra) && palabra[final] == inicial {
		final += 1
	}
	return final
}
func borrar(palabra string) int {
	for i := 0; i < len(palabra); i++ {
		// no sé
	}
}
func main() {
	obtener_entrada()
}

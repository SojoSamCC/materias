package main

import (
	"bufio"
	"fmt"
	"os"
)

var numCasos int
var casos []Caso
var palabra_actual string

type Caso struct {
	largo   int
	palabra string
}

func obtenerEntrada() {
	entrada := bufio.NewReader(os.Stdin)

	fmt.Fscan(entrada, &numCasos)
	casos = make([]Caso, numCasos)

	for i := 0; i < numCasos; i++ {
		var largo int
		var palabra string
		fmt.Fscan(entrada, &largo, &palabra)
		casos[i] = Caso{largo: largo, palabra: palabra}
	}
}

func contarCambios(l byte, i int, j int) int {
	cambios := 0
	for k := i; k < j; k++ {
		if palabra_actual[k] != l {
			cambios += 1
		}
	}

	return cambios
}

func l_lindo(i int, j int, l byte) int {
	// mi idea es partir de contar la cantidad de cambios que tendría que hacer si lo de la izquierda no es l-lindo en comparación si lo de la derecha no es l-lindo.
	// lo que noto es que sí o sí termino dividiendo al problema en dos strings pero se cumple esto de la propiedad de que todo de un lado debe ser un caracter.
	// si me pasa algo como que tengo 'bb' entonces no problem porque en la recursión busco el minimo entre irme por ir por una rama o la otra.
	// es mucho más eficiente si en vez de reconstruir el string todo el tiempo uso dos indices para ubicarme dentro de la palabra y de paso defino a la palabra con la que estoy trabajando como variable global!!!

	if i >= j {
		return 0
	}

	largo := j - i
	if largo == 1 {
		if palabra_actual[i] == l {
			return 0
		}
		return 1
	}

	mitad := (j + i) / 2

	siguiente := l + 1

	if l == 'z' {
		siguiente = 'a'
	}

	l_lindo_izq := contarCambios(l, i, mitad) + l_lindo(mitad, j, siguiente)
	l_lindo_der := contarCambios(l, mitad, j) + l_lindo(i, mitad, siguiente)

	if l_lindo_izq <= l_lindo_der {
		return l_lindo_izq
	} else {
		return l_lindo_der
	}
}

func main() {
	obtenerEntrada()
	for i := 0; i < numCasos; i++ {
		caso := casos[i]
		palabra_actual = caso.palabra

		res := l_lindo(0, caso.largo, 'a')

		fmt.Println(res)
	}
}

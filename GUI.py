import time
from InquirerPy import inquirer

class RAN:
    
    @staticmethod
    def barra_RAN(largo=50, delay=0.01):
        """
        Imprime una barra con texto centrado y un degradado suave (rojo a amarillo)
        con el texto: RAN SECURITY
        """
        print()
        texto = "RAN SECURITY"
        relleno_total = largo - len(texto)
        izquierda = relleno_total // 2
        derecha = relleno_total - izquierda
        contenido = ' ' * izquierda + texto + ' ' * derecha

        rgb_inicio = (255, 0, 0)     # rojo
        rgb_fin = (255, 255, 0)      # amarillo

        gradiente = []
        for i in range(len(contenido)):
            r = int(rgb_inicio[0] + (rgb_fin[0] - rgb_inicio[0]) * i / (len(contenido) - 1))
            g = int(rgb_inicio[1] + (rgb_fin[1] - rgb_inicio[1]) * i / (len(contenido) - 1))
            b = int(rgb_inicio[2] + (rgb_fin[2] - rgb_inicio[2]) * i / (len(contenido) - 1))
            gradiente.append((r, g, b))

        for char, (r, g, b) in zip(contenido, gradiente):
            color = f"\033[48;2;{r};{g};{b}m\033[38;2;255;255;255m"  # fondo RGB, texto blanco
            print(f"{color}{char}\033[0m", end='', flush=True)
            time.sleep(delay)
        print("\n")

class general:
    @staticmethod
    def barra_rgb(texto, rgb_inicio:tuple[int,int,int], rgb_fin:tuple[int,int,int],largo=50, delay=0.01):
        """
        Imprime una barra con texto centrado y un degradado suave entre rgb_inicio a rgb_fin
        con el texto dado
        """
        print()
        relleno_total = largo - len(texto)
        izquierda = relleno_total // 2
        derecha = relleno_total - izquierda
        contenido = ' ' * izquierda + texto + ' ' * derecha

        gradiente = []
        for i in range(len(contenido)):
            r = int(rgb_inicio[0] + (rgb_fin[0] - rgb_inicio[0]) * i / (len(contenido) - 1))
            g = int(rgb_inicio[1] + (rgb_fin[1] - rgb_inicio[1]) * i / (len(contenido) - 1))
            b = int(rgb_inicio[2] + (rgb_fin[2] - rgb_inicio[2]) * i / (len(contenido) - 1))
            gradiente.append((r, g, b))

        for char, (r, g, b) in zip(contenido, gradiente):
            color = f"\033[48;2;{r};{g};{b}m\033[38;2;255;255;255m"  # fondo RGB, texto blanco
            print(f"{color}{char}\033[0m", end='', flush=True)
            time.sleep(delay)
        print("\n")

class selectores:
    def elegir_opciones(self,lista_opciones,texto="--- Selección de opciones/s ---"):
        seleccionadas=[]
        cond=True
        lista_opciones.append('Listo/Salir')
        print(texto)
        while cond:
            select=inquirer.select(
                message=f"\nSelecciona una opción por favor\n",
                choices=lista_opciones
            ).execute()
            if "Listo/Salir" not in select:
                seleccionadas.append(str(select))
                lista_opciones = [x for x in lista_opciones if x not in set(seleccionadas)]
            else:
                cond=False
        return seleccionadas
    
    def elegir_opciones_single(self,lista_opciones,texto='--- Elegir opción ---'):
        print(texto)
        select=inquirer.select(
            message=f"\nSelecciona una opción por favor\n",
            choices=lista_opciones
        ).execute()
        return select
import sys
from pathlib import Path
ruta_base=Path(__file__).resolve().parent
sys.path.append(str(ruta_base))
import os
import re
from GUI import selectores as selectores_
directorios=os.listdir(ruta_base)

directorios=[directorio for directorio in directorios if os.path.isdir(os.path.join(ruta_base, directorio))]

directorios.remove(".git")
directorios.remove("env")
directorios.remove("__pycache__")
selectores=selectores_()

anios=selectores.elegir_opciones(directorios,texto='Elija el año que le interese')

for anio in anios:
    materias=os.path.join(ruta_base,anio)
    materias=os.listdir(materias)
    materias=[directorio for directorio in materias if os.path.isdir(os.path.join(ruta_base, anio))]
    materias=selectores.elegir_opciones(lista_opciones=materias,texto='Elija materias')
    for materia in materias:
        clases=os.path.join(ruta_base,anio,materia)
        clases=os.listdir(clases)
        clases=[directorio for directorio in clases if os.path.isdir(os.path.join(ruta_base, anio,materia))]
        clases=selectores.elegir_opciones(clases,texto='Elija clases')
        for clase in clases:
            notas=os.path.join(ruta_base,anio,materia,clase,'notas.md')
            
            lineas=[]
            with open(notas,"r",encoding="utf-8",newline="") as f:
                lineas+=f.readlines().copy()
            
            new_lines=[]
            for linea in lineas:
                linea = linea.replace("\\in", "∈")
                linea = re.sub(r"\._(.*?)_\.", r"<sub>\1</sub>", linea)
                linea = re.sub(r"\.\^(.*?)\^\.", r"<sup>\1</sup>", linea)
                new_lines.append(linea)
            
            with open(notas,"w",encoding="utf-8",newline="") as f:
                f.writelines(new_lines)
            
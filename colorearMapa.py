"""---- COLOREO DE MAPAS CON CUATRO COLORES------

PRÁCTICA REALIZADA POR JOSÉ TORDECILLA Y JULIÁN MEJIA
"""

import random

adyacencias = {
    "Argentina": ["Chile", "Bolivia", "Paraguay", "Uruguay", "Brasil"],
    "Bolivia": ["Peru", "Brasil", "Chile", "Argentina", "Paraguay"],
    "Brasil": ["Guyana Francesa", "Suriname", "Guayana", "Venezuela", "Colombia", "Peru", "Bolivia", "Paraguay", "Uruguay", "Argentina"],
    "Colombia": ["Ecuador", "Peru", "Brasil", "Venezuela"],
    "Chile": ["Peru", "Bolivia", "Argentina"],
    "Ecuador": ["Colombia", "Peru"],
    "Guayana": ["Venezuela", "Suriname", "Brasil"],
    "Guyana Francesa": ["Suriname", "Brasil"],
    "Paraguay": ["Bolivia", "Brasil", "Argentina"],
    "Peru": ["Ecuador", "Colombia", "Brasil", "Bolivia", "Chile"],
    "Suriname": ["Guayana", "Guyana Francesa", "Brasil"] ,
    "Uruguay": ["Argentina", "Brasil"],
    "Venezuela": ["Colombia", "Guayana", "Brasil"]
}

paises = ["Argentina","Bolivia", "Brasil", "Chile", "Colombia","Ecuador", "Guayana","Guyana Francesa", "Paraguay","Peru","Suriname","Uruguay","Venezuela"]

colores = ["Rojo", "Amarillo", "Azul", "Verde"]

mapaColoreado={}

def recorrerPaises(paises):
    #Recorriendo un pais y asignando un primer color
    for paisActual in paises:
            asignarColores(paisActual, color= 0, vacio=True)

def asignarColores(pais, color, vacio):
    #En caso de colorear por primera vez
    if vacio:
        mapaColoreado[pais] = colores[0]
    #reescribiendo el pais con otro color
    else:
        posColor = colores.index(color)
        colorR = random.randint(0, 3)

        for i in adyacencias[pais]:
            v.append(mapaColoreado[i])

        while v.__contains__(colores[colorR]):
            colorR = random.randint(0, 3)

        if colorR == 0:
            mapaColoreado[pais] = colores[colorR]
        elif colorR == 1:
            mapaColoreado[pais] = colores[colorR]
        elif colorR == 2:
            mapaColoreado[pais] = colores[colorR]
        elif colorR == 3:
            mapaColoreado[pais] = colores[colorR]

def compararColores(paises, adyacencias):
    #Verificando que los colores de las adyacencias y el país actual no sea el mismo
    for paisActual in paises:
            for paisAdy in adyacencias[paisActual]:
                if mapaColoreado[paisActual] == mapaColoreado[paisAdy]:
                    asignarColores(paisActual, mapaColoreado[paisAdy],vacio=False)
def imprimir():
    rojo = "\033[0;31m"
    amarillo = "\033[0;33m"
    azul ="\033[0;34m"  
    verde = "\033[0;32m" 


    for i in mapaColoreado:
        color = ""
        if mapaColoreado[i] == "Rojo":
            color = rojo
        elif mapaColoreado[i] == "Amarillo":
            color = amarillo
        elif mapaColoreado[i] == "Verde":
            color = verde
        elif mapaColoreado[i] == "Azul":
            color = azul 

        print(color, i , "---->" ,mapaColoreado[i])


def main():
    recorrerPaises(paises)
    compararColores(paises, adyacencias)

    imprimir()

main()


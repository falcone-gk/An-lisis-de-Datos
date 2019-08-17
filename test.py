"""
Creado para realizar las respectivas pruebas al la librería data_analysis.
"""

import numpy as np
import data_analysis as das

def main():
    """Función para generar los test."""
    x_val = list(np.random.randn(50)*100)
    y_val = list(np.random.randn(50)*100)
    z_val = list(np.random.randn(50)*100)
    index = list(range(0, 50))

    data = {
        "Indice": index,
        "Valores de x" : x_val,
        "Valores de y" : y_val,
        "Valores de z" : z_val
    }

    my_class = das.Data(data)

    #Muestra todas las variables.
    print(my_class)

    #Muestra los datos de la variable deseada.
    print(my_class["Valores de x"])

    #Muestras Los estadísticos básicos de una variable (media, quartiles, desviación estándar, etc.)
    print(my_class.describe(["Valores de x", "Valores de y", "Valores de z"]))

    #Grafica las variables.
    figura = my_class.plot("Indice", "Valores de x", title="Prueba de gráfico 1")
    figura.savefig("images/test1.png")

    #Realiza un gráfico de puntos.
    figura = my_class.scatter_plot("Valores de y", "Valores de x", title="Prueba de gráfico 2")
    figura.savefig("images/test2.png")

    #Realiza gráficos de puntos comparando entre las variables deseadas.
    figura = my_class.relation(["Valores de x", "Valores de y", "Valores de z"])
    figura.savefig("images/test3.png")

    #Realización de varios gráficos.
    figura = my_class.mult_plot("Indice", ["Valores de x", "Valores de y", "Valores de z"])
    figura.savefig("images/test4.png")

    #Realización de varios gráficos por separado.
    figura = my_class.mult_plot("Indice", ["Valores de x", "Valores de y", "Valores de z"],
                                separate=True)
    figura.savefig("images/test5.png")

if __name__ == "__main__":
    main()

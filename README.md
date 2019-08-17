# Data-Analysis
Este código se encarga de obtener todas las características estadísticas básicas que se pueden obtener de una base de datos, desde la media hasta la desviación estándar o incluso más, según se vaya desarrollando. Además se irá agregando más métodos para la realización de gráficos de datos para su respectivo análisis.

## Prerrequisitos
- El código corre en **Python 3**.
- Es necesario la instalación de la librería **Matplotlib**.

## Corriendo el Test
Para correr el test es necesario tener instalada la librería **numpy** (usada para generar datos aleatorios) y tener en una misma carpeta los archivos **data_analysis.py** y **test.py** en un mismo folder.

Lo que realiza el test es mostrar todas los métodos disponibles y cómo se usan.

En la primera parte del test simplemente se importa la librería, se generan datos aleatorios, el índice a usar y se crea el objeto Data.
```python

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
```

A continuación se muestran los resultados de todas las pruebas.
```python
    #Muestra todas las variables.
    print(my_class)
```
![Imagen de la base de datos](/images/show_data.png)

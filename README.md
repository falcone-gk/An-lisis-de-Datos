# Data-Analysis
Este código se encarga de obtener todas las características estadísticas básicas que se pueden obtener de una base de datos, desde la media hasta la desviación estándar o incluso más, según se vaya desarrollando. Además se irá agregando más métodos para la realización de gráficos de datos para su respectivo análisis.

## Prerrequisitos
- El código corre en **Python 3**.
- Es necesario la instalación de la librería **Matplotlib**.

## Corriendo el Test
Para correr el test es necesario tener instalada la librería **numpy** (usada para generar datos aleatorios) y tener en una misma carpeta los archivos **data_analysis.py** y **test.py** en un mismo folder.

Lo que realiza el test es mostrar todas los métodos disponibles y cómo se usan.

### Generación de datos
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

### Obtención de estadísticos básicos
A continuación se muestran los resultados de todas las pruebas.
```python
    #Muestra todas las variables.
    print(my_class)
```
![Imagen de la base de datos](/images/show_data.png)

Debido a espacio solo se muestra una parte de la data, pero lo que se propone es a mostrar todos los datos.

La siguiente parte de código solo muestra los valores de la variable que se desea:
```python
    #Muestra los datos de la variable deseada.
    print(my_class["Valores de x"])
```
![Imágen de la variable deseada](/images/show_var.png)

Para obtener los estadísticos principales de cada variable lo puedes hacer llamando uno por uno, los siguientes métodos están disponibles:

- [max_val](https://github.com/falcone-gk/Data-Analysis/blob/fdbd76dd7aef114880526064586ba0f542ba1f79/data_analysis.py#L159)
- [min_val](https://github.com/falcone-gk/Data-Analysis/blob/fdbd76dd7aef114880526064586ba0f542ba1f79/data_analysis.py#L167)
- [mean](https://github.com/falcone-gk/Data-Analysis/blob/fdbd76dd7aef114880526064586ba0f542ba1f79/data_analysis.py#L193)
- [q_one](https://github.com/falcone-gk/Data-Analysis/blob/fdbd76dd7aef114880526064586ba0f542ba1f79/data_analysis.py#L209)
- [median](https://github.com/falcone-gk/Data-Analysis/blob/fdbd76dd7aef114880526064586ba0f542ba1f79/data_analysis.py#L200)
- [q_third](https://github.com/falcone-gk/Data-Analysis/blob/fdbd76dd7aef114880526064586ba0f542ba1f79/data_analysis.py#L221)
- [q_range](https://github.com/falcone-gk/Data-Analysis/blob/fdbd76dd7aef114880526064586ba0f542ba1f79/data_analysis.py#L235)
- [std_dev](https://github.com/falcone-gk/Data-Analysis/blob/fdbd76dd7aef114880526064586ba0f542ba1f79/data_analysis.py#L251)
- [variance](https://github.com/falcone-gk/Data-Analysis/blob/fdbd76dd7aef114880526064586ba0f542ba1f79/data_analysis.py#L241)

Sin embargo, si se quiere un resumen de de las variables que uno quiere con sus estadísticos principales, entonces aquí se muestra el código que lo realiza:
```python
    #Muestras Los estadísticos básicos de una variable (media, quartiles, desviación estándar, etc.)
    print(my_class.describe(["Valores de x", "Valores de y", "Valores de z"]))
```
![imagen de la descripción de las variables](/images/description.png)

### Gráfico de variables
En esta sección se mostrarán los tipos de gráficos que se pueden obtener del objeto Data.

```python
    figura = my_class.plot("Indice", "Valores de x", title="Prueba de gráfico 1")
    figura.savefig("images/test1.png")
```
![Imagen de los valores de x](/images/test1.png)

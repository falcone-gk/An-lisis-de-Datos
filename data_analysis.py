"""
Este código se encarga de obtener todas las características estadísticas
básicas que se pueden obtener de una base de datos, desde la media hasta
la desviación estándar o incluso más, según se vaya desarrollando. Además
se irá agregando más métodos para la realización de gráficos de datos
para su respectivo análisis.
"""

from math import floor, ceil, sqrt
import matplotlib.pyplot as plt
import matplotlib.style as style

style.use("seaborn")

class Data:
    """Estructura de dos dimensiones que tiene como base a un diccionario de
    Python, en el que se podrá obtener los distintos estadísticos, para cada
    variable y se podrán realizar distintos gráficos para un mejor análisis.

    Keyword arguments:

    data: Variable de tipo dictionario que esté estructurado de la siguiente
    manera

        {string: list}

        El valor key debe ser de tipo 'str' y los valores deben ser del tipo
        'list' en el que deben estar los valores de cada variable ya sea de
        tipo 'int' o 'float'.
    """

    def __new__(cls, data=None):
        items = list(data.values())
        keys = list(data.keys())
        for col in keys:
            if not isinstance(col, str):
                raise ValueError("Los nombres de las columnas deben ser de tipo 'str'.")

        for arr in items:
            for value in arr:
                if isinstance(value, (int, float)):
                    pass
                else:
                    raise ValueError("Los nombres de cada columna deben ser 'int' o 'float'.")

        sizes = set(map(len, items))
        if not len(sizes) == 1:
            raise IndexError("Las columnas no tienen la misma cantidad de valores.")

        return object.__new__(cls)

    def __init__(self, data):
        self.__data = data
        self._columns = data.keys()
        self.index = len(list(data.values())[0])

    @property
    def columns(self):
        """
        Propiedad para retornar los nombres de las columnas en una lista y aplicar un setter
        para que estos nombres no sean facilmente cambiados.
        """
        return self._columns

    @columns.setter
    def columns(self, value):
        raise ValueError("No puedes asignar nuevos nombres para las columnas de este manera.")

    def __repr__(self):
        msg = ""
        panel = [[0 for i in self.columns] for j in range(self.index+1)]
        for i, col in enumerate(self.columns):
            panel[0][i] = col

        sizers = []
        i = 0
        for key, val in self.__data.items():
            rows = []
            rows.append(key)
            for j, item in enumerate(val):
                rows.append(str(round(item, 2)))
                panel[j+1][i] = str(round(item, 2))
            i += 1
            sizers.append(max(list(map(len, rows))))

        for row in panel:
            for j, val in enumerate(row):
                msg += val.rjust(sizers[j]) + "  "
            msg += "\n"

        return msg

    def __getitem__(self, col):
        msg = ""
        values = []
        sizer = [len(col)]

        for val in self.__data[col]:
            values.append(str(round(val, 2)))
            sizer.append(len(str(round(val, 2))))

        size = max(sizer)
        msg += col.rjust(size, " ") + "\n"

        for val in values:
            msg += val.rjust(size, " ") + "\n"

        return msg

    def describe(self, columns):
        """
        Muestra la descripción básica de una serie de datos.
        Tienes que insertar en una lista los nombres de las columnas de las cuales quieres
        su descripción.

        columns: Lista con los nombres de las columnas que se desean sus descripciones.
        """

        _char = [
            ('mean', self.mean),
            ('min', self.min_val),
            ('25%', self.q_one),
            ('50%', self.median),
            ('75%', self.q_third),
            ('max', self.max_val),
            ('std', self.std_dev)
        ]

        panel_char = []
        cols = ['     ']

        for col in columns:
            cols.append(col)
        panel_char.append(cols)

        for func in _char:
            values = []
            values.append(func[0])
            for col in columns:
                values.append(str(round(func[1](col), 2)))
            panel_char.append(values)

        trans_panel = [[0 for i in range(len(panel_char))] for j in range(len(columns)+1)]
        for i, val in enumerate(panel_char):
            for j in range(len(columns)+1):
                trans_panel[j][i] = len(val[j])
        sizers = list(map(max, trans_panel))

        description = ''
        for row in panel_char:
            for i, val in enumerate(row):
                if i == 0 and val != '     ':
                    description += "{:5s}".format(val) + ": "
                else:
                    description += val.rjust(sizers[i], " ") + "  "
            description += "\n"
        return description

    def max_val(self, name):
        """
        Retorna el máximo valor de la columna de nombre 'name'.

        name: Nombre de la columna de la cual queremos el máximo valor.
        """
        return max(self.__data[name])

    def min_val(self, name):
        """
        Retorna el mínimos valor de la columna de nombre 'name'.

        name: Nombre de la columna de la cual queremos el mínimo valor.
        """
        return min(self.__data[name])

    def __get_ind(self, name):
        """
        Si la cantidad de datos de una lista de valores de una variable
        es impar, se toma un solo valor índice (el central) para obtener
        la mediana de un conjunto de valores, en el caso de valor par
        se genera una lista.
        """
        ind = (len(self.__data[name])+1) / 2

        if int(ind) == float(ind):
            ind = int(ind) - 1
        else:
            ind1 = floor(ind)
            ind2 = ceil(ind)
            ind = [ind1 - 1, ind2 - 1]

        return ind

    def mean(self, name):
        """Retorna la suma de todos los valores de la variable"""
        t_sum = 0
        for num in self.__data[name]:
            t_sum += num
        return t_sum/len(self.__data[name])

    def median(self, name):
        """Retorna la media de un conjunto de valores."""

        sort_data = sorted(self.__data[name])
        ind = self.__get_ind(name)
        if isinstance(ind, list):
            return (sort_data[ind[0]] + sort_data[ind[1]]) / 2
        return float(sort_data[ind])

    def q_one(self, name):
        """Retorna el primer cuartil del conjunto de valores"""

        ind = self.__get_ind(name)
        if isinstance(ind, list):
            sub_arr = self.__data[name][:ind[0]+1]
        else:
            sub_arr = self.__data[name][:ind]
        sub_data = Data({name: sub_arr})

        return sub_data.median(name)

    def q_third(self, name):
        """Retorna el tercer cuartil del conjunto de valores"""

        sorted_data = sorted(self.__data[name])
        ind = self.__get_ind(name)

        if isinstance(ind, list):
            sub_arr = sorted_data[ind[1]:]
        else:
            sub_arr = sorted_data[ind + 1:]
        sub_data = Data({name: sub_arr})

        return sub_data.median(name)

    def q_range(self, name):
        """Retorna la diferencia entre el primer cuartil y el tercero."""

        res = self.q_third(name) - self.q_one(name)
        return res

    def variance(self, name):
        """Retorna la varianza de la columna deseada"""

        mean_vals = self.mean(name)
        _sum = 0
        for val in self.__data[name]:
            _sum += (val - mean_vals)**2
        _var = _sum/len(self.__data[name])
        return _var

    def std_dev(self, name):
        """Retorna la desviación estándar de la columna deseada"""

        var = self.variance(name)
        return sqrt(var)

    def plot(self, axis_x, axis_y, title=None):
        """
        Realiza un gráfico lineal entre en axis_x e axis_y.

        Keyword arguments:

        axis_x: Nombre de la columna que se desee que esté en el eje x.

        axis_y: Nombre de la columna que se desee que esté en el eje y.

        title: Título para el gráfico (opcional).
        """
        fig, axs = plt.subplots()
        axs.plot(self.__data[axis_x], self.__data[axis_y])
        axs.set_ylabel(axis_y)
        axs.set_xlabel(axis_x)
        axs.set_title(title)
        plt.show()
        return fig

    def scatter_plot(self, axis_x, axis_y, title=None):
        """
        Realiza un gráfico de puntos entre axis_x e axis_y.

        Keyword arguments:

        axis_x: Nombre de la columna que se desee que esté en el eje x.

        axis_y: Nombre de la columna que se desee que esté en el eje y.

        title: Título para el gráfico (opcional).
        """
        fig, axs = plt.subplots()
        axs.scatter(self.__data[axis_x], self.__data[axis_y])
        axs.set_ylabel(axis_y)
        axs.set_xlabel(axis_x)
        axs.set_title(title)
        plt.show()
        return fig

    def relation(self, variables):
        """
        Muestra gráficos de puntos entre las columnas deseadas.

        Keyword arguments:

        variables: Lista con los nombres de las columnas que se desean comparar.
        """
        nvar = len(variables)
        axis = 0
        fig = plt.figure()
        for i in range(nvar):
            for j in range(nvar):
                axis += 1
                axs = fig.add_subplot(nvar, nvar, axis)

                if i == j:
                    plt.text(0.5, 0.5, variables[i], horizontalalignment='center')
                    axs.set_xticks([])
                    axs.set_yticks([])

                else:
                    plt.plot(self.__data[variables[j]], self.__data[variables[i]], 'bo')
                    plt.subplots_adjust(hspace=0.7, wspace=0.5)
        plt.show()
        return fig

    def mult_plot(self, axis_x, axis_y, separate=False):
        """Realiza gráficos de más de una variable.

        Keyword arguments:

        axis_x: Es la variable (índice) que irá en el eje x.

        axis_y: Lista con los nombres de las columnas de las variables.

        separate: Variable de tipo bool, se encarga de verificar si se desea que las
        variables se grafican en un mismo cuadro (separate=False) o se observen en
        diferentes recuadros (separate=True).
        """

        if separate:
            fig, axs = plt.subplots(len(axis_y), 1, sharex=separate)
            for i, _ax in enumerate(axs):
                _ax.plot(self.__data[axis_x], self.__data[axis_y[i]])
                _ax.set_title(axis_y[i])
            plt.xlabel(axis_x)
        else:
            fig = plt.figure()
            axs = fig.add_subplot(111)
            for col in axis_y:
                axs.plot(self.__data[axis_x], self.__data[col], label=col)
            axs.legend()
            axs.set_xlabel(axis_x)
        plt.show()
        return fig

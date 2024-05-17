# Scatter plots con plotly

Los graficos de dispersión o nubes de puntos, se utilizan para mostrar la relación entre dos variables numéricas. Cada punto de datos se presenta como un punto en un plano cartesian, donde la posición del punto en el eje X corresponde al valor de una variables y la posición en el eje Y corresponde al valor de la otra variables.

## Características de los gráficos de dispoersión:

* Explorar relaciones entre variables
* Identificar correlaciones
* Encontrar valores atípicos
* Visualizar tendencias
* Comparar grupos

## Referencia del código
En el script scatter_plots.py vemos la creación de un scatter plot con plotly utilizando numpy y pandas.

go.Scatter se usa para crear el grafico, se utilizan 2 arrays o iterables para los parametros X e Y. El modo (parametro "mode") está seteado en "markers", que significa que los puntos de datos se presentan como marcadores. El parametro "marker" recibe un diccionario con las propiedades de los marcadores, es decir, los estilos.

go.Layout es una función que se utiliza para crear la diseño del grafico. Es decir las etiquetas como el titulo o las leyenda de los ejes. El parametro mode define el modo de desplazamiento, que esta seteado en "colsets" (el mas cercano) lo que significa que la información sobre herramientas se mostrará el punto de datos más cercano.


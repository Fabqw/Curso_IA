## Desarrollo de curso de inteligencia artificial, klab

### Clase 8 de junio
- Búsqueda de deep research en modelos de inteligencia artificial
- Ayuda en la búsqueda integrada en la web, junto con los enlaces de la información requerida

- **¿Qué es Google Colab?**
    - [Google Colab](https://colab.research.google.com/) es una plataforma gratuita de Google que permite escribir y ejecutar código Python en la nube a través de notebooks Jupyter.
    - Es ampliamente utilizada para aprendizaje automático, análisis de datos y experimentación, ya que ofrece acceso a recursos como GPUs y TPUs sin necesidad de configuración local.

- **¿Qué es TensorFlow?**
    - [TensorFlow](https://www.tensorflow.org/) es una biblioteca de código abierto desarrollada por Google para el aprendizaje automático y el aprendizaje profundo.
    - Permite construir y entrenar modelos de redes neuronales de manera eficiente, utilizando tanto CPUs como GPUs.
    - Es ampliamente utilizada en investigación y producción para tareas como clasificación de imágenes, procesamiento de lenguaje natural y más.

- **Procesamiento de datos**
    - Fuente de datos
    - Procesamiento
    - Datos objetivos
    - Modelos
    - Datos transformados
    - Evaluación

- **Modelo Iris**  
> Los datos del modelo Iris pueden obtenerse desde plataformas como [Kaggle](https://www.kaggle.com/), que ofrece el dataset para su descarga y análisis.

#### Descripción del modelo Iris

- El modelo Iris es un clásico en el aprendizaje automático, utilizado para la clasificación de especies de flores Iris a partir de medidas de sus partes.
- **Características del dataset:**
    - Largo de sépalo 
    - Ancho de sépalo
    - Largo de pétalo
    - Ancho de pétalo
- **Variable objetivo:**
    - Especies (Iris setosa, Iris versicolor, Iris virginica)
- Este dataset es ampliamente utilizado para practicar técnicas de clasificación y visualización de datos.

> El dataset Iris también está disponible en el [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris), una de las fuentes más reconocidas para conjuntos de datos de aprendizaje automático. Desde allí se puede descargar el archivo en formato CSV y utilizarlo para experimentos y análisis en diferentes plataformas.

#### Dataset Iris: columna por columna

| Columna           | Descripción                        | Ejemplo de valor |
|-------------------|------------------------------------|------------------|
| sepal_length      | Largo del sépalo (cm)              | 5.1              |
| sepal_width       | Ancho del sépalo (cm)              | 3.5              |
| petal_length      | Largo del pétalo (cm)              | 1.4              |
| petal_width       | Ancho del pétalo (cm)              | 0.2              |
| species           | Especie de la flor                 | Iris-setosa      |

- **Significado de cada valor:**
    - *sepal_length*: Medida del largo del sépalo en centímetros.
    - *sepal_width*: Medida del ancho del sépalo en centímetros.
    - *petal_length*: Medida del largo del pétalo en centímetros.
    - *petal_width*: Medida del ancho del pétalo en centímetros.
    - *species*: Clase o especie de la flor (variable objetivo).

---

### Clase 9 de junio

La existencia de variables dependientes e independientes, con el tipo de aprendizaje según las funciones.

#### Aprendizaje supervisado

- **Definición:** El modelo aprende a partir de datos etiquetados, donde se conoce la respuesta correcta (variable dependiente).
- **Variables:**
    - *Independientes*: Características de entrada (ejemplo: largo y ancho de sépalo y pétalo).
    - *Dependiente*: Variable objetivo o etiqueta (ejemplo: especie de la flor).
- **Ejemplo:** Clasificación de especies de Iris usando las medidas de la flor.
- **Técnicas comunes:** Regresión, clasificación.

- **Visualización:**  
    ![Ejemplo de aprendizaje supervisado: clasificación de flores Iris](https://upload.wikimedia.org/wikipedia/commons/5/56/Iris_dataset_scatterplot.svg)  
    *En la imagen se observa cómo los datos etiquetados permiten al modelo aprender a clasificar las especies de Iris según sus características.*

#### Aprendizaje no supervisado

- **Definición:** El modelo aprende a partir de datos no etiquetados, buscando patrones o agrupaciones en los datos.
- **Variables:** Solo se utilizan variables independientes, no hay una variable objetivo explícita.
- **Ejemplo:** Agrupar flores Iris en clústeres según sus características, sin conocer la especie.
- **Técnicas comunes:** Clustering (agrupamiento), reducción de dimensionalidad.

La clase tiene que ser finita, para el uso de los modelos de regresion

#### scikit-learn

tarea como importar los datos de kaggle de iris

---
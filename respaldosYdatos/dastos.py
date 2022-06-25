# Cargamos las librerías típicas de python
import matplotlib.pyplot as plt # para plotear
import numpy as np              # numpy para los arrays


# Cargamos un módulo de la librería de Tensorflow que contiene el dataset fashion-mnist
from keras.datasets import mnist,fashion_mnist

(X_train_raw, y_train), (X_test_raw, y_test) = fashion_mnist.load_data()  # cargo los dataset de entrenamiento y testeo

# defino un vector de categorías donde el índice de cada elemento corresponde a la categoría asociada
categories = ['T-shirt/top', 'Trouser','Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


# Ploteo 25 imagenes al azar del set de entrenamiento con sus respectivas clases
fig = plt.figure(figsize = (8,8)) # seteo el tamano de la figura
for i in range(25):
    j = np.random.randint(0, len(X_train_raw)) # en cada iteracion elijo un numero random entre 0 y la longitud de X_train_raw que es 60000 (el numero de imagenes) para usar de indice
    plt.subplot(5,5,i+1) # Voy a tener una matriz de 5x5 subplots y voy llenando en la iteracion i-esima el subplot i+1
    plt.imshow(X_train_raw[j], interpolation='none', cmap="gray") # plotea una imagen random, pues es la imagen j-esima del set de entrenamiento, en formato (28,28) para imagenes en escala de grises
    plt.title("clase: {}".format(categories[y_train[j]]), fontsize = 10) # pongo el titulo a los plots con el nombre de la clase a la que pertenece la imagen y seteo el tamano de letra
    plt.xticks([]) # le saco los ticks en el eje X
    plt.yticks([]) # le saco los ticks en el eje Y
plt.show()
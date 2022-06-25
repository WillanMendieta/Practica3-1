from cgitb import small
import numpy as np
import matplotlib.pyplot as pp
import pandas as pd
tabla=pd.read_csv("datos.csv",sep=",")
def autolabel(rects):    
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(30, 2),  textcoords="offset points", arrowprops=dict(arrowstyle="->", color='black'))
fig, ax = pp.subplots()
x=np.arange(4)
ancho=0.50
reactsAbrigo=ax.bar(x - ancho/2, tabla['abrigo'], ancho/2, label='abrigo')
reactsBotin=ax.bar(x - ancho/2, tabla['botin'], ancho/2, label='botin')
reactsZapatillas=ax.bar(x - ancho/2, tabla['zapatillas'], ancho/2, label='zapatillas')
reactsPantalon=ax.bar(x - ancho/2, tabla['pantalon'], ancho/2, label='pantalon')
autolabel(reactsAbrigo)
autolabel(reactsBotin)
autolabel(reactsZapatillas)
autolabel(reactsPantalon)
ax.set_ylabel('Cantidad')
ax.set_title('Matriz de confusion')
ax.set_xticks(x)
ax.set_xticklabels(['abrigo','botin','zapatillas','pantalon'])
fig.tight_layout()
ax.legend()
pp.savefig("Matriz_Confusion.png")
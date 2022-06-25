from cgitb import small
import numpy as np
import matplotlib.pyplot as pp
import pandas as pd
tabla=pd.read_csv("datos.csv",sep=",")
pp.figure(figsize=(50,50))
nombres = ["Abrigo","Abrigo/Botin","Abrigo/Zapatillas", "Abrigo/Pantalon"]
pp.subplot(2,2,1)

pp.rc('font',size = 55)
pp.pie(tabla.iloc[0], labels=nombres,autopct="%0.2f %%")
pp.title("Prediccion de Abrigo" , bbox={"facecolor":"0.8", "pad":0.5})

pp.subplot(2,2,2)
nombres = ["Botin/Abrigo","Botin","Botin/Zapatillas","Botin/Pantalon"]
pp.pie(tabla.iloc[1],labels=nombres,autopct="%0.2f %%")
pp.title("Prediccion de Botin" , bbox={"facecolor":"0.8", "pad":0.5})

pp.subplot(2,2,3)
nombres = ["Zapatillas/Abrigo","Zapatillas/Botin","Zapatillas", "Zapatillas/Pantalon"]
pp.pie(tabla.iloc[2],labels=nombres,autopct="%0.2f %%")
pp.title("Prediccion de Zapatillas" , bbox={"facecolor":"0.8", "pad":0.5})

pp.subplot(2,2,4)
nombres = ["Pantalon/Abrigo","Pantalon/Botin","Pantalon/Zapatillas","Pantalon"]
pp.pie(tabla.iloc[3],labels=nombres,autopct="%0.2f %%")
pp.title("Prediccion de Pantalon", bbox={"facecolor":"0.8", "pad":0.5})

pp.savefig("Prediccion.png")


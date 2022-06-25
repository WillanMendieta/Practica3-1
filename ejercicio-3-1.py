import mahotas
import numpy as np
import matplotlib.pyplot as pp
import os
import csv
def calcular_momentos(train, test):
    imagenesTrain = mahotas.imread(train)
    imagenesTest = mahotas.imread(test)
    momentosZ = mahotas.features.zernike_moments(imagenesTrain[:, :], 28)
    momentosZR = mahotas.features.zernike_moments(imagenesTest[:, :], 28)        
    return np.linalg.norm(momentosZ-momentosZR)
#Carpeta abrigo
train_abrigo=os.listdir("Abrigo/train")
test_abrigo=os.listdir("Abrigo/test")

#Carpeta botin
train_botin=os.listdir("Botin/train")
test_botin=os.listdir("Botin/test")

#Carpeta zapatillasD
train_zapatillas=os.listdir("Zapatillas/train")
test_zapatillas=os.listdir("Zapatillas/test")

#Carpeta pantalon
train_Pantalon=os.listdir("Pantalon/train")
test_Pantalon=os.listdir("Pantalon/test")

matrizConfusion=np.zeros((4,4))
for abrigo in test_abrigo:
    listaAbrigo=[]
    listaBotin=[]
    listaZapatillas=[]
    listaPantalon=[]
    for tstabrigo in train_abrigo:        
        dist_ecucli=calcular_momentos(train="Abrigo/train/"+tstabrigo,test="Abrigo/test/"+abrigo)
        listaAbrigo.append(dist_ecucli)
    for tstbotin in train_botin:        
        dist_ecucli=calcular_momentos(train="Botin/train/"+tstbotin,test="Abrigo/test/"+abrigo)
        listaBotin.append(dist_ecucli)
    for tstzapatillas in train_zapatillas:        
        dist_ecucli=calcular_momentos(train="Zapatillas/train/"+tstzapatillas,test="Abrigo/test/"+abrigo)
        listaZapatillas.append(dist_ecucli) 


    for tstPantalon in train_Pantalon:        
        dist_ecucli=calcular_momentos(train="Pantalon/train/"+tstPantalon,test="Abrigo/test/"+abrigo)
        listaPantalon.append(dist_ecucli) 

    #If de cada lista Abrigo
    if(np.min(listaAbrigo)<np.min(listaBotin) and np.min(listaAbrigo)<np.min(listaZapatillas) and np.min(listaAbrigo)<np.min(listaPantalon)):
        matrizConfusion[0,0]+=1

    #If de cada lista Botin
    if(np.min(listaBotin)<np.min(listaAbrigo) and np.min(listaBotin)<np.min(listaZapatillas) and np.min(listaBotin)<np.min(listaPantalon)):
        matrizConfusion[0,1]+=1

    #If de cada lista Zapatillas
    if(np.min(listaZapatillas)<np.min(listaBotin) and np.min(listaZapatillas)<np.min(listaAbrigo) and np.min(listaZapatillas)<np.min(listaPantalon)):
        matrizConfusion[0,2]+=1

    #If de cada lista Pantalon
    if(np.min(listaPantalon)<np.min(listaAbrigo) and np.min(listaPantalon)<np.min(listaBotin) and np.min(listaPantalon)<np.min(listaZapatillas)):
        matrizConfusion[0,3]+=1

for botin in test_botin:
    listaAbrigo=[]
    listaBotin=[]
    listaZapatillas=[]
    listaPantalon=[]

    for tstabrigo in train_abrigo:        
        dist_ecucli=calcular_momentos(train="Abrigo/train/"+tstabrigo,test="Botin/test/"+botin)
        listaAbrigo.append(dist_ecucli)

    for tstbotin in train_botin:        
        dist_ecucli=calcular_momentos(train="Botin/train/"+tstbotin,test="Botin/test/"+botin)
        listaBotin.append(dist_ecucli)

    for tstzapatillas in train_zapatillas:        
        dist_ecucli=calcular_momentos(train="Zapatillas/train/"+tstzapatillas,test="Botin/test/"+botin)
        listaZapatillas.append(dist_ecucli)

    for tstPantalon in train_Pantalon:        
        dist_ecucli=calcular_momentos(train="Pantalon/train/"+tstPantalon,test="Botin/test/"+botin)
        listaPantalon.append(dist_ecucli) 

    #If de cada lista Abrigo
    if(np.min(listaAbrigo)<np.min(listaBotin) and np.min(listaAbrigo)<np.min(listaZapatillas) and np.min(listaAbrigo)<np.min(listaPantalon)):
        matrizConfusion[1,0]+=1

    #If de cada lista Botin
    if(np.min(listaBotin)<np.min(listaAbrigo) and np.min(listaBotin)<np.min(listaZapatillas) and np.min(listaBotin)<np.min(listaPantalon)):
        matrizConfusion[1,1]+=1

    #If de cada lista Zapatillas
    if(np.min(listaZapatillas)<np.min(listaBotin) and np.min(listaZapatillas)<np.min(listaAbrigo) and np.min(listaZapatillas)<np.min(listaPantalon)):
        matrizConfusion[1,2]+=1

    #If de cada lista Pantalon
    if(np.min(listaPantalon)<np.min(listaAbrigo) and np.min(listaPantalon)<np.min(listaBotin) and np.min(listaPantalon)<np.min(listaZapatillas)):
        matrizConfusion[1,3]+=1

for zapatillas in test_zapatillas:
    listaAbrigo=[]
    listaBotin=[]
    listaZapatillas=[]
    listaPantalon=[]
    for tstabrigo in train_abrigo:        
        dist_ecucli=calcular_momentos(train="Abrigo/train/"+tstabrigo,test="Zapatillas/test/"+zapatillas)
        listaAbrigo.append(dist_ecucli)
    for tstbotin in train_botin:        
        dist_ecucli=calcular_momentos(train="Botin/train/"+tstbotin,test="Zapatillas/test/"+zapatillas)
        listaBotin.append(dist_ecucli)
    for tstzapatillas in train_zapatillas:        
        dist_ecucli=calcular_momentos(train="Zapatillas/train/"+tstzapatillas,test="Zapatillas/test/"+zapatillas)
        listaZapatillas.append(dist_ecucli)
    for tstPantalon in train_Pantalon:        
        dist_ecucli=calcular_momentos(train="Pantalon/train/"+tstPantalon,test="Zapatillas/test/"+zapatillas)
        listaPantalon.append(dist_ecucli) 

    #If de cada lista Abrigo
    if(np.min(listaAbrigo)<np.min(listaBotin) and np.min(listaAbrigo)<np.min(listaZapatillas) and np.min(listaAbrigo)<np.min(listaPantalon)):
        matrizConfusion[2,0]+=1

    #If de cada lista Botin
    if(np.min(listaBotin)<np.min(listaAbrigo) and np.min(listaBotin)<np.min(listaZapatillas) and np.min(listaBotin)<np.min(listaPantalon)):
        matrizConfusion[2,1]+=1

    #If de cada lista Zapatillas
    if(np.min(listaZapatillas)<np.min(listaBotin) and np.min(listaZapatillas)<np.min(listaAbrigo) and np.min(listaZapatillas)<np.min(listaPantalon)):
        matrizConfusion[2,2]+=1

    #If de cada lista Pantalon
    if(np.min(listaPantalon)<np.min(listaAbrigo) and np.min(listaPantalon)<np.min(listaBotin) and np.min(listaPantalon)<np.min(listaZapatillas)):
        matrizConfusion[2,3]+=1

for pantalon in test_Pantalon:
    listaAbrigo=[]
    listaBotin=[]
    listaZapatillas=[]
    listaPantalon=[]
    for tstabrigo in train_abrigo:        
        dist_ecucli=calcular_momentos(train="Abrigo/train/"+tstabrigo,test="Pantalon/test/"+pantalon)
        listaAbrigo.append(dist_ecucli)
    for tstbotin in train_botin:        
        dist_ecucli=calcular_momentos(train="Botin/train/"+tstbotin,test="Pantalon/test/"+pantalon)
        listaBotin.append(dist_ecucli)
    for tstzapatillas in train_zapatillas:        
        dist_ecucli=calcular_momentos(train="Zapatillas/train/"+tstzapatillas,test="Pantalon/test/"+pantalon)
        listaZapatillas.append(dist_ecucli)
    for tstPantalon in train_Pantalon:        
        dist_ecucli=calcular_momentos(train="Pantalon/train/"+tstPantalon,test="Pantalon/test/"+pantalon)
        listaPantalon.append(dist_ecucli) 

    #If de cada lista Abrigo
    if(np.min(listaAbrigo)<np.min(listaBotin) and np.min(listaAbrigo)<np.min(listaZapatillas) and np.min(listaAbrigo)<np.min(listaPantalon)):
        matrizConfusion[3,0]+=1

    #If de cada lista Botin
    if(np.min(listaBotin)<np.min(listaAbrigo) and np.min(listaBotin)<np.min(listaZapatillas) and np.min(listaBotin)<np.min(listaPantalon)):
        matrizConfusion[3,1]+=1

    #If de cada lista Zapatillas
    if(np.min(listaZapatillas)<np.min(listaBotin) and np.min(listaZapatillas)<np.min(listaAbrigo) and np.min(listaZapatillas)<np.min(listaPantalon)):
        matrizConfusion[3,2]+=1

    #If de cada lista Pantalon
    if(np.min(listaPantalon)<np.min(listaAbrigo) and np.min(listaPantalon)<np.min(listaBotin) and np.min(listaPantalon)<np.min(listaZapatillas)):
        matrizConfusion[3,3]+=1



    headers = ('abrigo', 'botin', 'zapatillas', 'pantalon')
with open('datos.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(matrizConfusion)
#Carpeta pantalon
train_Pantalon=os.listdir("Pantalon/train")
test_Pantalon=os.listdir("Pantalon/test")

matrizConf=np.zeros((3,3))
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
    if(np.min(listaAbrigo)<np.min(listaBotin) and np.min(listaAbrigo)<np.min(listaZapatillas)):
        matrizConf[0,0]+=1
    if(np.min(listaBotin)<np.min(listaAbrigo) and np.min(listaBotin)<np.min(listaZapatillas)):
        matrizConf[0,1]+=1
    if(np.min(listaZapatillas)<np.min(listaBotin) and np.min(listaZapatillas)<np.min(listaAbrigo)):
        matrizConf[0,2]+=1

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
    if(np.min(listaAbrigo)<np.min(listaBotin) and np.min(listaAbrigo)<np.min(listaZapatillas)):
        matrizConf[1,0]+=1
    if(np.min(listaBotin)<np.min(listaAbrigo) and np.min(listaBotin)<np.min(listaZapatillas)):
        matrizConf[1,1]+=1
    if(np.min(listaZapatillas)<np.min(listaBotin) and np.min(listaZapatillas)<np.min(listaAbrigo)):
        matrizConf[1,2]+=1

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
    if(np.min(listaAbrigo)<np.min(listaBotin) and np.min(listaAbrigo)<np.min(listaZapatillas)):
        matrizConf[2,0]+=1
    if(np.min(listaBotin)<np.min(listaAbrigo) and np.min(listaBotin)<np.min(listaZapatillas)):
        matrizConf[2,1]+=1
    if(np.min(listaZapatillas)<np.min(listaBotin) and np.min(listaZapatillas)<np.min(listaAbrigo)):
        matrizConf[2,2]+=1

    headers = ('abrigo', 'botin', 'zapatillas')
with open('datos.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(matrizConf)
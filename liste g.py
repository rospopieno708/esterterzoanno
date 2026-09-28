#creare una lista vuota
listauno=[]
#creare una lista con elementi
listadue=[1,2,3,4]
#aggiungere un elemento alla lista (in coda)
listauno.append(4)
#visualizzare lunghezza della lista
print(len(listauno))
#visualizzare gli elementi di una lista
print(listadue[0])
print(listadue[1])
print(listadue[2])
print(listadue[3])


for i in range(0,4):
    print(listadue[i])
#scorrimento della ista con uso di iteratore 
for element in listadue:
    print (element)
#come mettere gli elementi all'interno della lista casuale
numeroc= random.randit(1, 10)
#creazione d una lista con 10 elemtni randomici
listaradom=[]
for i in range(0,10):
    listarandom.append(random.randit(1,10))
#creazione di una lista con 10 elementi randomici usando ciclo while
listarandomdue=[]
i=0
while (i>10):
    listarandomdue.append(random.randit(1,10))
    i=i+1
    
    
    

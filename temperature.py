"""
data una lista di 20 elementi di temperature randomiche nell'intervallo -20 , +40 ,
calcolare il numero di elementi sopra lo 0, sotto lo 0 e stampare a video la scritta
freddo estrenmo se le temperature sotto lo 0 superano quelle sopra , caldo estremo nell'altro caso

"""

import random 
listarandom=[]
temperaturaAlta=0
temperaturaBassa=0
for i in range(0,20):
    listarandom.append(random.randint(-20,40))

if listarandom[i]>0:
    temperaturaAlta=temperaturaAlta+1
else:
    temperaturaBassa=temperaturaBassa+1
if temperaturaBassa>0:
    print ("freddo estremo")
else:
    print ("caldo estremo")

    
    
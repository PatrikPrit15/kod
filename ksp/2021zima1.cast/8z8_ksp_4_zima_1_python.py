import sys
import array
import numpy as np
import math
vys = 0
dvys=0
vysledok = 999999999999999999999999999999
pocetpolicn, dlzkapolices =[int (x) for x in input ().split ()]
knihapos =[int (x) for x in input ().split ()]
for i in range (1):
    for i2 in range (pocetpolicn):
        if knihapos[i2]>i:
            if knihapos[i2] - i > dlzkapolices / 2:
                vys = vys + dlzkapolices - (knihapos[i2] - i)
            else:
                vys = vys + knihapos[i2] - i
        if knihapos[i2]<i:
            if i - knihapos[i2] > dlzkapolices / 2:
                vys = vys + dlzkapolices - (i - knihapos[i2])
            else:
                vys = vys + i - knihapos[i2]
        if vys>=vysledok:
            break
    if (vys < vysledok):
        vysledok = vys 
    dvys=vys
    vys = 0
zmena=0
for i in range(pocetpolicn):
    if (knihapos[i]!=(dlzkapolices+1)/2):
        if(knihapos[i]<dlzkapolices/2+1 and knihapos[i]>0):
            zmena-=1
        else:
            zmena+=1
if (dlzkapolices%2==0):
    pole=-10*np.ones((pocetpolicn*2+1,2))
    for i in range (pocetpolicn):
        pole[i,0]=knihapos[i]
        pole[i,1]=2
        if(knihapos[i]<(dlzkapolices/2)):
            pole[i+pocetpolicn,0]=(dlzkapolices/2)+knihapos[i]
        if(knihapos[i]>=(dlzkapolices/2)):
            pole[i+pocetpolicn,0]=int(knihapos[i]-(dlzkapolices/2))
        pole[i+pocetpolicn,1]=-2
else:
    pole=-10*np.ones((pocetpolicn*3+1,2))
    for i in range (pocetpolicn):
        pole[i,0]=knihapos[i]
        pole[i,1]=2
        if(knihapos[i]<math.floor(dlzkapolices/2)):
            pole[i+pocetpolicn,0]=math.ceil(dlzkapolices/2)+knihapos[i]
        else:
            pole[i+pocetpolicn,0]=int(knihapos[i]-math.floor(dlzkapolices/2))
        pole[i+pocetpolicn,1]=-1
        
        if(knihapos[i]<math.ceil(dlzkapolices/2)):
            pole[i+2*pocetpolicn,0]=math.floor(dlzkapolices/2)+knihapos[i]
        else:
            pole[i+2*pocetpolicn,0]=int(knihapos[i]-math.ceil(dlzkapolices/2))
        pole[i+(2*pocetpolicn),1]=-1
pole = pole[pole[:,0].argsort()]
pole[0,0]=0
pole[0,1]=0
for i in range(len(pole)):
    if (pole[i,0]>0 and i>0):
        dvys+=zmena*(pole[i,0]-pole[i-1,0])
        zmena+=pole[i,1]
    if(dvys<vysledok):
        vysledok=int(dvys)
print (vysledok)
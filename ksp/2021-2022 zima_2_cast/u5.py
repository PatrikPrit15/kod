from collections import deque 
v,e,s,f=map(int,input().split(" "))#vstup
h=[0]*v #vytvorenie pola na vstup
for i in range(v):
    h[i]=int(input()) #zapisovanie vstupu do pola
vstup=[[0 for i in range(3)] for j in range(e)] #vytvorenie pola na vstup
for i in range(e):
    vstup[i][0],vstup[i][1],vstup[i][2]=map(float,input().split(" "))#zapisovanie vstupu
    vstup[i][2]=float(abs(h[int(vstup[i][0])]-h[int(vstup[i][1])]))/vstup[i][2]#počítanie strmosti
vstup = sorted(vstup, key=lambda x: x[2])#zoradenie pola podla strmosti
pole = [[] for i in range(v+1)]#vytvorenie pola do kt. sa budú pridávať svahy

for i in range(0,e):#testovanie 
    pole[int(vstup[i][0])].append(int(vstup[i][1])) #pridanie cesty do pola
    pole[int(vstup[i][1])].append(int(vstup[i][0])) #pridanie otocenej cesty do pola
    if i<e-1:#keď toto nieje posledny element
        if vstup[i][2]==vstup[i+1][2]:#ked je hodnota strmosti 2 vstupov rovnaka tak to nepocita 2x
            continue
    pq = deque() #vytvorenie priority queue
    pq.append(s) #pridanie zaciatku do priority queue
    bol = [False for i in range(v)] #vytvorenie pola s hodnotami kde som uz bol
    bol[s] = True #nastavenie zaciatku na true
    while len(pq)>0:#keď je v deque nejaký prvok
        z = pq.popleft() #vymazanie elementu zlava a ulozenie do z
        for el in pole[z]: #testovanie ciest od z
            if (el == f):#testovanie či sme v cieli
                print("{:.2f}".format(vstup[i][2])) #vypísanie odpovede
                exit() #koniec programu
            if bol[el]==False:#ked sme v novom bode tak sa nastaví na true a prida sa do pq
                pq.append(el)
                bol[el] = True
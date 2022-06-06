n,k,t =map(int, input().split(" "))    #vstup hodnot
c=list(map(int, input().split(" ")))   #vstup časov kváskov
pole = [0]*(t+11)     #tvorba pola
vysledok=0            #vytvorenie premennej vysledok kt. bude obsahovat pocet kvaskov v dany den
for x in c:           #pridanie casu rozmnozenia do pola
    pole[x+1]+=1      #index je den rozmnozenia a hodnota je pocet kvaskov kt. sa vtedy rozmnozia
for x in range(t+1):  #iterovanie cez pole
    if pole[x]!=0:    #podmienka ked sa v tento den rozdelia nejake kvásky
        pole[x+7]+=pole[x]     #pridanie noveho dna rozmnozenia starych kvaskov
        pole[x+9]+=pole[x]*k   #pridanie noveho dna rozmnozenia novych kvaskov (tych co prave vznikli)
        pole[x]=0              #vymazanie hodnoty lebo tieto kvasky sa uz rozmnozili
for x in range(t,t+10):  #spocitavanie poctu kvaskov v zadany den 
    vysledok+=pole[x]    #priratanie poctu kvaskov ktore by sa rozdelili v den x 
print(vysledok)     #vypisanie poctu kvaskov v zadany den
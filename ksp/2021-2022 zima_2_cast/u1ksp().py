smer=input() #nacitanie str z vstupom
if smer.count("<")>smer.count(">"):#zisty ktorym smerom je trasa a vsetky sipky vodorovne sa daju proti tomuto smeru
    smer=smer.replace("<",">") #vymienanie sipok kt. idu "spravnym smerom"
else: #ked je smer cesty opacny alebo sa ciel nachadza na rovnakej vodorovnej pozicii(x ciela =0) tak sa vymenia opacne sipky
    smer=smer.replace(">","<")#vymienanie sipok kt. idu "spravnym smerom"
if smer.count("^")>smer.count("v"):#zisty ktorym smerom je trasa a vsetky sipky zvysle sa daju proti tomuto smeru
    smer=smer.replace("^","v")#vymienanie sipok kt. idu "spravnym smerom"
else:#ked je smer cesty opacny alebo sa ciel nachadza na zvyslej pozicii(y ciela =0) tak sa vymenia opacne sipky
    smer=smer.replace("v","^")#vymienanie sipok kt. idu "spravnym smerom"
print(smer) #vypisanie trasy
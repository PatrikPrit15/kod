n, fma = map(int, input().split(" "))  # nacitanie vstupu
pole = list(map(int, input().split(" ")))  # nacianie vstupu z silami
# pole v ktorom budu hodnoty max dlzky postupnosti po tuto hodnotu = dlzka postupnosti potialto
po = [0 for _ in range(n)]
# pole v ktorom budu hodnoty dlzky postupnosti po koniec=od tialto sa da spravit postupnost takejto dlzky
po_otocene = [0 for _ in range(n)]
di = {}  # slovnik s poslednym vyskytom cisla

# vytvaranie pola s dlzkami postupnosti od i po koniec, algoritmus postupuje od zadu
for i in range(n - 1, -1, -1):
    po_otocene[i] = 1 + po_otocene[di[pole[i] + 1]] if pole[i] + 1 in di else 1  # ==v
    # if pole[i] + 1 in di: #ked sa nachadza vacsie cislo v slovniku
    #     po_otocene[i] = 1 + po_otocene[di[pole[i] + 1]]#pridanie hodnoty o 1 vacsej ako hodnota cisla o 1 vacsieho
    # else:
    #     po_otocene[i] = 1 #koniec postupnosti, uz nieje o 1 vacsie cislo, ! ideme od zadu !
    di[pole[i]] = i  # nastavenie posledneho vyskytu cisla pole[i] na i

di = {}  # resetovanie slovniku
# vytvorenie nového slovniku kde kluc=cislo v poli-sila (pole) a pod nim je list indexov tohto cisla=pozicie tochto cisla, potom nebude musiet algoritmus hladat v celom poli
d = {}
ma = 0  # premenna s max dlzkov radu
for i in range(n):  # vytvorenie slovnika s poziciami
    if pole[i] in d:  # ak uz bol clovek s rovnakou silou
        d[pole[i]].append(i)  # prida sa jeho index do pola pod kluc=sile
    else:  # ked je tento clovek prvy s silou pole[i]
        d[pole[i]] = [i]  # nastavi sa jeho index pod kluc jeho hodnoty

# hlavny cyklus skusa pridavat adama na kazdu poziciu, i= pozicia adama, popri tom tvori pole po s dlzkami postupnosti po cislo na indexe i (pole[i])
for i in range(n):
    po[i] = 1 + po[di[pole[i] - 1]] if pole[i] - 1 in di else 1
    di[pole[i]] = i  # do slovnika sa da posledny vyskyt hodnoty pole[i]
    if (
        pole[i] + 2 in d
    ):  # ked existuje hodnota kt. je o 2 vacsia teda adam spoji 2 postupnosti
        a2 = next((index for index in d[pole[i] + 2] if index >= i), -1)
        # ked je este v slovniku pod rovnakym klucom nejaka hodnota
        while len(d[pole[i] + 2]) > 0 and d[pole[i] + 2][0] <= i:
            # ked je tato hodnota(index) mensia ako i tak ju vymazeme lebo ju uz nebude treba a zbytocne by sa cez nu iterovalo
            d[pole[i] + 2].pop(0)  # vymazanie prvej hodnoty z pola v slovniku
        ma = max(ma, po[i] + 1) if a2 == -1 else max(ma, po[i] + 1 + po_otocene[a2])
    else:  # ked nie
        # ma sa nastavi na max z ma a dlzku postupnosti po pole[i]+1(jedna je adam)
        ma = max(ma, po[i] + 1)
print(ma)  # vypise sa dlzka najdlhsej postupnosti

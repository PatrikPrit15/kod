import math,time
v=0
# ulohy na https://projecteuler.net/archives




#u1 ctrl k +ctrl c; ctrl k + ctrl u
#  for i in range(1,1000):
#     if i%3==0 or i%5==0:
#         v+=i
# print(v)

#u2
# f1,f2,d=1,1,0
# v=0
# while 1:
#     if f2>4000000:
#         break
#     d=f2
#     f2+=f1
#     f1=d
#     if f2%2==0:
#         v+=f2
# print(v)

#u3
# c=600
# i=2
# while i<=c:
#     if c%i==0:
#         print(i)
#         c/=i
#     else:
#         i+=1

#u4
# for i in range(100,1000):
#     for y in range(i,1000):
#         x=i*y
#         if str(x)==str(x)[::-1]:
#             v=max(v,x)
# print(v)

#u5
# while 1:
#     v+=9699690 #sucin prvocisel po 20
#     zle=0
#     for i in range(1,21):
#         if (v/i)%1!=0:
#             zle=1
#             break
#     if zle==0:
#         print(v)
#         break

#u6
# sum2=0
# _2sum=0
# for i in range(1,101):
#     sum2+=i**2
#     _2sum+=i
# _2sum=_2sum**2
# print(_2sum-sum2)

#u7
# primes=[2]
# i=3
# while len(primes)<10001:
#     je=1
#     for p in primes:
#         if (i/p)%1==0:
#             je=0
#             break
#     if je==1:
#         primes.append(i)
#     i+=2
# print(primes[-1])

#u8
# c="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
# ms=0
# for i in range(988):
#     ams=1
#     for x in range(13):
#         ams*=int(c[x+i])
#     ms=max(ms,ams)
# print(ms)

#u9
# from math import sqrt
# import math
# for a in range(1,1001):
#     for b in range(a,1001):
#         if float(math.sqrt(a**2+b**2))%1==0:
#             if(a+b+math.sqrt(a**2+b**2))==1000:
#                 print(a*b*math.sqrt(a**2+b**2))

#u10  15sekund
# prvocisla=[2] #list prvocisel
# aktualne_cislo=3
# while aktualne_cislo<2*10**6:#generator prvocisel do
# 	je_prvocislo=True

# 	for prvocislo in prvocisla:
# 		if prvocislo**2>aktualne_cislo:
# 			break
# 		if (aktualne_cislo/prvocislo)%1==0:
# 			je_prvocislo=False
# 			break

# 	if je_prvocislo:#pridanie prvocisla
# 		prvocisla.append(aktualne_cislo)
# 	aktualne_cislo+=2

# print(sum(prvocisla))


start=time.perf_counter() #0,3 sekundy
n=2*10**6
primes = set([2,3]+list(range(5,n+1,6))+list(range(7,n+1,6)))
p = 5
state=1
while p ** 2 < n:
    if p in primes:
        for number in range(p**2, n+1, p*2):
            primes.discard(number)
    if state:
        p += 2
        state=0
    else:
        p+=4
        state=1
print(sum(primes))
print(time.perf_counter()-start)




#u11
# pole=[[1 for i in range(40)] for x in range(40)]
# for i in range(20):
# 	pole[i+3][3:24]=map(int,input().split(" "))
# for y in range(20):
# 	for x in range(20):
# 		h=pole[y+3][x+3]*pole[y+3][x+4]*pole[y+3][x+5]*pole[y+3][x+6]
# 		ve=pole[y+3][x+3]*pole[y+4][x+3]*pole[y+5][x+3]*pole[y+6][x+3]
# 		dvp=pole[y+3][x+3]*pole[y+4][x+4]*pole[y+5][x+5]*pole[y+6][x+6]
# 		dvl=pole[y+3][x+3]*pole[y+4][x+2]*pole[y+5][x+1]*pole[y+6][x]
# 		v=max(v,h,ve,dvp,dvl)
# print(v)

#u12
# v=1
# pc=1
# while 1:
# 	v+=pc+1
# 	pc+=1
# 	d=0
# 	for i in range(1,math.ceil(math.sqrt(v))):
# 		if (v/i)%1==0:
# 			d+=2
# 	if math.ceil(math.sqrt(v))==math.sqrt(v):
# 		d-=1
# 	if d>500:
# 		print("d={}, cislo={}".format(d,v))
# 		break

#u13
# for i in range(100):
#     v+=int(input())
# print(str(v)[:10:])

#u14
# p=0
# ma=0
# pole=[0]
# for i in range(1,10**6):
#     di=i
#     p=0
#     while di!=1:
#         if di<i:
#             p+=int(pole[int(di)])
#             break
#         p+=1
#         if di%2==0:
#             di/=2
#         else:
#             di=3*di+1
#     pole.append(p)
#     if p>ma:
#         ma=p
#         v=i
# print(v)

#u15
# vel=20
# vel+=1#kvoli tomu ze hrana ma o 1 viac vrcholov ako stvorcekov
# pole=[[0 for i in range(vel)] for i in range(vel)]
# for i in range(vel):
#     pole[i][0]=1
#     pole[0][i]=1
# for y in range(1,vel):
#     for x in range(1,vel):
#         pole[x][y]=pole[x-1][y]+pole[x][y-1]
# print(pole[-1][-1])

#u16
# cislo=str(2**1000)
# sum=0
# for i in cislo:
# 	sum+=int(i)
# print(sum)

#u17
# import inflect 
# dosl=inflect.engine()
# for x in range(1,100001):
# 	jc=dosl.number_to_words(x)
# 	for y in jc:
# 		if y in "abcdefghijklmnopqrstuvwxyz":
# 			v+=1
# print(v)
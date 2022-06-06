# Logistická rovnica
# Bifurkačný diagram:
# 1<r<3 – asympt. stabilný
# 3<r<1+√6 – dvojcykly
# r=3.544090...– štvorcykly
# r>3.57 – chaotický
import time
import matplotlib.pyplot as plt
from PIL import Image
import time
start = time.perf_counter()
w, h, zoom = 19200, 10800, 1
bitmap = Image.new("1", (w, h), "white")
pix = bitmap.load()

print(f"start:{time.perf_counter()-start}")


def get_x(x, r):
    return r*x*(1-x)


for g in range(w):
    x = 0.5
    r = g/w*4  # od 3 po 4
    for i in range(int(100+1000*r)):
        x = get_x(x, r)
        pix[int(w/4*r-1), int(h*(-x)-1)] = 0
    # for i in l:
    #     #plt.plot(r,i, marker="o", markersize=1, markeredgecolor="black", markerfacecolor="black")
    #     bitmap[int(w/4*r-1), int(h*(-i)-1)]= False
    #     p+=1
print(f"celkovy cas bol: {time.perf_counter()-start} sekund")
# plt.show()
bitmap.show()
# n=input("file name:")
# bitmap.save(f"{n}.png")

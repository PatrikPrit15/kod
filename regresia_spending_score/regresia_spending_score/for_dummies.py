def normalize(x, xmin, xmax):
    nx = x
    nx = (nx-xmin)/(xmax-xmin)
    return nx


def rescale(x, x_min, x_max):
    sx = x
    sx = sx*(x_max-x_min)+x_min
    return sx


def use_model(i, m):
    w1, w2, b = m
    return i[0]*w1+i[1]*w2+b


model = (-0.2766, -0.0656, 0.6363)
inputs = (int(input("zadaj vek:")), int(input("zadaj vysku platu v 1000usd:")))
inputs = (normalize(inputs[0], 18, 70), normalize(inputs[1], 15, 137))
pred = use_model(inputs, model)
pred = rescale(pred, 1, 97)
print(f'Skore podla modelu je: {pred:.2f}')

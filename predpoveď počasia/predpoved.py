import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

import os

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data_BA_2016-2022_1.csv")
data = np.zeros(1987 * 232)
data = np.reshape(data, (1987, 232))
df["datetime"] = pd.DatetimeIndex(df["datetime"]).month
import seaborn as sns

# f, ax = plt.subplots(figsize=(10, 8))
# corr = df.corr()
# sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
#             square=True, ax=ax)
# plt.show()
for dni in range(1950):
    data[dni][0] = df["datetime"][dni + 21]
    data[dni][1:] = df[
        [
            "tempmax",
            "tempmin",
            "dew",
            "humidity",
            "precip",
            "windspeed",
            "winddir",
            "sealevelpressure",
            "cloudcover",
            "visibility",
            "solarenergy",
        ]
    ][dni : dni + 21].values.flatten()
X, y = data[:, :-77], data[:, -77:]
import seaborn as sns

# print(X)
# sns.pairplot(df[["datetime","tempmax","tempmin","precip"]], diag_kind='kde')
# print(df.describe())
# plt.show()
def build_and_compile_model():
    model = keras.Sequential(
        [
            keras.Input(shape=(155,)),
            layers.Dense(150, activation="relu"),
            layers.Dense(130, activation="relu"),
            layers.Dense(100, activation="relu"),
            layers.Dense(85, activation="relu"),
            layers.Dense(77),
        ]
    )

    model.compile(
        loss="mean_absolute_error", optimizer=tf.keras.optimizers.Adam(0.0002)
    )
    return model


model = build_and_compile_model()
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
history = model.fit(
    X_train,
    y_train,
    batch_size=1,
    epochs=10,
    # We pass some validation for
    # monitoring validation loss and metrics
    # at the end of each epoch
    validation_data=(X_test, y_test),
)
plt.plot(history.history["val_loss"])
plt.show()
# print(X.shape)
# model.summary()
import pandas as pd
import numpy as np

df2 = pd.read_csv("30d.csv")
features = [
    "tempmax",
    "tempmin",
    "dew",
    "humidity",
    "precip",
    "windspeed",
    "winddir",
    "sealevelpressure",
    "cloudcover",
    "visibility",
    "solarenergy",
]
df2_ = df2[features]
df2 = pd.DatetimeIndex(df2["datetime"]).month
# print(df2)
datap = np.ones((1, 155))
datap[0][0] = df2[-1]
datap[0][1:] = df2_[-14:].values.flatten()
# print(datap)
preds = model.predict(datap)
for den in range(7):
    for i, feature in enumerate(features):
        print(den, feature, preds[0][i + den*11])
    abc = input("enter")
print(model.summary())

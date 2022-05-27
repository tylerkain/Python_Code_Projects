import pandas as pd
import numpy as np
import tensorflow as tf
from keras import layers
# Make numpy values easier to read.
np.set_printoptions(precision=3, suppress=True)



abalone_train = pd.read_csv(
    "https://storage.googleapis.com/download.tensorflow.org/data/abalone_train.csv",
    names=["Length", "Diameter", "Height", "Whole weight", "Shucked weight",
           "Viscera weight", "Shell weight", "Age"])

print(abalone_train.head())

# abalone_train.to_csv("Datasets/Shell_Data.csv")

abalone_features = abalone_train.copy()
abalone_labels = abalone_features.pop('Age')

abalone_features = np.array(abalone_features)

abalone_model = tf.keras.Sequential([
    layers.Dense(64),
    layers.Dense(1)
])

abalone_model.compile(loss=tf.keras.losses.MeanSquaredError(),
                      optimizer=tf.optimizers.Adam())

normalize = layers.Normalization()

norm_abalone_model = tf.keras.Sequential([
    normalize,
    layers.Dense(64),
    layers.Dense(1)
])

norm_abalone_model.compile(loss=tf.losses.MeanSquaredError(),
                           optimizer=tf.optimizers.Adam())

norm_abalone_model.fit(abalone_features, abalone_labels, epochs=10)

predict = np.array([[0.435, .45, 0.1, 0.33, .30, .077, 0.096]])

age_predict = norm_abalone_model.predict(predict)
print(age_predict)
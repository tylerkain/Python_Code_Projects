import pandas as pd
import numpy as np
import tensorflow as tf
from keras import layers

# Importing Data

file = "Datasets/Car_Purchasing_Data.csv"
car_data = pd.read_csv(file)
print(car_data)

# Transform Data

car_data_features = car_data.copy()
car_data_labels = car_data_features.pop('Car Purchase Amount')

car_data_features = np.array(car_data_features)

normalize = layers.Normalization()
normalize.adapt(car_data_features)

# # Create Model
car_data_model = tf.keras.Sequential([normalize, layers.Dense(64), layers.Dense(64), layers.Dense(1)])
car_data_model.compile(optimizer='adam', loss='mean_squared_error')

car_data_model.fit(car_data_features, car_data_labels, epochs=40)

predict = np.array([[1, 50, 50000, 10000, 600000]])

y_predict = car_data_model.predict(predict)
print(y_predict)



from sklearn.datasets import load_boston
import pandas as pd
import DataFunctions as data_func




boston_data = load_boston()

# boston_data_df = pd.DataFrame(data=boston_data.data, columns=boston_data.feature_names)
# # print(boston_data_df)

# file = "../Datasets/boston_data_df.csv"
# boston_data_df.to_csv(file)

file = "../Datasets/boston_data_df.csv"
boston_data_df = pd.read_csv(file)

boston_data_df["Price"] = boston_data.target

# print(boston_data_df)
#
# data_func.Check_missing_values(boston_data_df)
# data_func.plot_hist(boston_data_df["RAD"], num_bins=5)
# data_func.distplot(boston_data_df["Price"])
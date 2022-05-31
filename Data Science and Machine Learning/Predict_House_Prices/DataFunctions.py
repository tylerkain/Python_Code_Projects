import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def Check_missing_values(file):
    data = pd.isnull(file).any()
    print(data)


def plot_hist(data, num_bins=0):
    plt.hist(data, bins=num_bins)
    plt.show()


def distplot(data):
    sns.distplot(data, hist=False)
    plt.show()
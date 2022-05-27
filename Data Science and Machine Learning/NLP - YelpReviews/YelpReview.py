# Import Libraries
import string

import nltk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


def clean_text(file):
    file = file
    yelp_review_text = pd.read_csv(file)
    stopwords = nltk.corpus.stopwords.words('english')
    yelp_review_text["clean_text"] = yelp_review_text['text'].str.lower().apply(
        lambda x: ' '.join([word for word in x.split() if word not in
                            stopwords]))
    save_file = "../Datasets/yelp_review_clean.csv"
    yelp_review_text.to_csv(save_file)


vectorizer = CountVectorizer()
NB_classifier = MultinomialNB()


# Load Data

# file = "../Datasets/yelp.csv"
# clean_text(file)

file = "../Datasets/yelp_review_clean.csv"
# remove_stop_words(file)
yelp_df = pd.read_csv(file)

# Visualize Data

# yelp_df["length"] = yelp_df["text"].apply(len)
# # print(yelp_df["length"])
# # yelp_df["length"].plot(bins=100, kind="hist")
# # plt.show()
#
# # g= sns.FacetGrid(data=yelp_df, col='stars', col_wrap=3)
# # g.map(plt.hist, 'length', bins=20)
# # plt.show()
#
yelp_df_review_stars_1 = yelp_df[yelp_df["stars"] == 1]
yelp_df_review_stars_5 = yelp_df[yelp_df["stars"] == 5]
yelp_df_review = pd.concat([yelp_df_review_stars_1, yelp_df_review_stars_5])

yelp_vectorizer = vectorizer.fit_transform(yelp_df_review['clean_text'])
# print(yelp_vectorizer)
# print(vectorizer.get_feature_names())

label = yelp_df_review['stars'].values
# print(label)

# NB_classifier.fit(yelp_vectorizer, label)
#
# test_text_1 = ["amazing food! best ever, highly recommend "]
# test_text_2 = ["Shit Place, food awful made me sick"]
#
# test_countvectorizer = vectorizer.transform(test_text_1)
# test_predict = NB_classifier.predict(test_countvectorizer)
# print(test_predict)

x = yelp_vectorizer
y = label
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

NB_classifier.fit(x_train, y_train)
# y_predict_train = NB_classifier.predict(x_train)
# print(y_predict_train)
#
# cm = confusion_matrix(y_train, y_predict_train)
# sns.heatmap(cm, annot=True)
# plt.show()


y_predict_test = NB_classifier.predict(x_test)

print(classification_report(y_test, y_predict_test))

cm = confusion_matrix(y_test, y_predict_test)
sns.heatmap(cm, annot=True)
plt.show()

# TF-DIF METHOD

yelp_tfidf = TfidfTransformer().fit_transform(yelp_vectorizer)
print(yelp_tfidf)

x = yelp_tfidf
y = label

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
NB_classifier.fit(x_train, y_train)

cm = confusion_matrix(y_test, y_predict_test)
sns.heatmap(cm, annot=True)
plt.show()

y_predict_test = NB_classifier.predict(x_test)
print(classification_report(y_test, y_predict_test))
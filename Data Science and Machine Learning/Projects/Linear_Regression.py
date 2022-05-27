import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

movie_budget = "cost_revenue_dirty.csv"
movie_budget_data = pd.read_csv(movie_budget)

X = DataFrame(movie_budget_data, columns=['Production Budget ($)'])
y = DataFrame(movie_budget_data, columns=['Worldwide Gross ($)'])

regression = LinearRegression()
regression.fit(X, y)
prediction = regression.predict(X)

coefficent = regression.coef_
intercept = regression.intercept_
equation = intercept + coefficent * 50000000
print(equation)
score = regression.score(X, y)
print(score)

plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.3)
plt.plot(prediction, regression.predict(X), color='red', linewidth=4)
plt.title('Film Cost vs. Production Cost')
plt.xlabel("Production Cost")
plt.ylabel("Gross")
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()



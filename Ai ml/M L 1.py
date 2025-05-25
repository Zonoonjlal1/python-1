# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import mean_squared_error

# Load the dataset
dataset = pd.read_csv(r'E:\labtob\Ai ml\AI Files\AI Files\1 - Linear regression (simple , multi)\simple\student_scores.csv')
# jake a look at the  dataset

print(dataset.head())
print(dataset.tail())
print(dataset.shape)
print(dataset.info())
print(dataset.describe().sum())
print(dataset.describe())

#Displaying the data on a plot using matplotlib
dataset.plot(x='Hours', y='Scores', style='o', title='Hours vs Scores',xlabel='Hours Studied',
              ylabel='Percentage Score',color='blue',linewidth=2)
plt.show()

#Prepare the data
x = dataset.iloc[:,:-1].values  # Features (Hours)
print (x)
y = dataset.iloc[:,1].values    # Target variable (Scores)
print (y)
# Splitting the dataset into training and testing sets
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
#Train the aolgorithm
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# Making predictions on the test set
y_prod = regressor.predict(x_test)
#print("Predicted scores for the test set:", y_prod)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_prod})
print(df)
# Visualizing the training set results
df1 = df.head(25)  
df1.plot(kind = 'bar',figsize=(16,10))
plt.grid(which='major', linestyle='--', color='green')
plt.grid(which='minor', linestyle=':', color='black')
plt.show()
print('Mean Absolut Error is the average errors:', metrics.mean_absolute_error(y_test, y_prod))
print('Mean squared Error :', metrics.mean_squared_error(y_test, y_prod))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_prod)))
print(regressor.score(x,y))
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/module_5_auto.csv'
df = pd.read_csv(path)

df.to_csv('module_5_auto.csv')

df = df._get_numeric_data()
df.head()
from IPython.display import display
from IPython.html import widgets
from IPython.display import display
from ipywidgets import interact, interactive, fixed, interact_manual

def DistributionPlot(Red, Function, BlueFunction, RedName, BlueName, Title):
    width = 10
    height = 12
    plt.figure(figsize=(width, height))

    ax1 = sns.distplot(RedFunction, hist=False, color='r', label=RedName)
    ax2 = sns.distplot(BlueFunction, hist=False, color='b', label=BlueName)

    plt.title(Title)
    plt.xlabel('Price (in dollars)')
    plt.ylabel('Proportion of Cars')

    plt.show()
    plt.close()

def PollyPlot(xtrain, xtest, y_train, y_test, lr, poly_transform):
    width = 10
    height= 12
    plt.figure(figsize=(width, height))

    # training date
    # testing data
    # lr: linear regression object
    # poly_transform : polynomial transformation object

    xmax = max([xtrain.values.max(), xtest.values.max()])
    xmin = min([xtrain.values.min(), xtest.values.min()])
    x = np.arrange(xmin, xmax, 0.1)

    plt.plot(xtrain, y_train, 'ro', label='Training Data')
    plt.plot(xtest, ytest, 'go', label='Test Data')
    plt.plot(x, lr.predict(poly_transform.fit_transform(x.reshape(-1,1))), label='Predicted Function')
    plt.ylim([-10000, 60000])
    plt.ylabel('Price')
    plt.legend()

y_data = df['price']
x_data = df.drop('price',axis=1)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size =0.15, random_state=1)

print('Number of test samples:', x_test.shape[0])
print('Number of training samples:', x_train.shape[0])


x_train_1, x_test_1, y_train_1, y_test_1 = train_test_split(x_data, y_data, test_size=0.4, random_state=0)
print('Number of test samples:', x_test_1.shape[0])
print('Number of training samples:', x_train_1.shape[0])

from sklearn.linear_model import LinearRegression
lre = LinearRegression()
lre.fit(x_train[['horsepower']], y_train)
lre.score(x_test[['horsepower']], y_test)
lre.score(x_train[['horsepower']], y_train)

lre.fit(x_train_1[['horsepower']], y_train_1)
lre.score(x_test_1[['horsepower']], y_test_1) # R^2




from sklearn.model_selection import cross_val_score
Rcross = cross_val_score(lre, x_data[['horsepower']], y_data, cv= 4)
print(Rcross)
Rcross[1] # find the average R^2 for the second fold
print('The mean of the folds are', Rcross.mean(), 'and the standard deviation is', Rcross.std())

-1* cross_val_score(lre, x_data[['horsepower']],y_data, cv=4, scoring='neg_mean_squared_error')


from sklearn.model_selection import cross_val_predict
yhat = cross_val_predict(lre, x_data[['horsepower']], y_data, cv=4)
yhat[0:5]

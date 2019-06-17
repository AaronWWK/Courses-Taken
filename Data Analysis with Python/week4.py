import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)
df.head()
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm

X = df[['highway-mpg']]
Y = df[['price']]
lm.fit(X,Y)

Yhat = lm.predict(X)
Yhat[0:5]
lm.intercept_
lm.coef_



X =df[['engine-size']]
Y = df[['price']]
lm1 = lm.fit(df[['engine-size']],df[['price']])
lm1

lm1.intercept_
lm1.coef_

Yhat = lm1.predict(df[['engine-size']])
Yhat[0:10]

Yhat = -7963.34-166.86*X
Yhat[0:10]




Z = df[['horsepower','curb-weight','engine-size','highway-mpg']]
lm.fit(Z,df['price'])
lm.fit(Z,df[['price']])

lm.intercept_
lm.coef_
# Price = -15678.742628061467 + 52.65851272 x horsepower + 4.69878948 x curb-weight + 81.95906216 x engine-size + 33.58258185 x highway-mpg


Z2 = df[['normalized-losses','highway-mpg']]
lm.fit(Z2, df[['price']])
lm.intercept_
lm.coef_
# price = 38201.31 + 1.50*normalized-losses -820.45*highway-mpg

import seaborn as sns


width = 12
height = 10
plt.figure(figsize=(width,height))
sns.regplot(x='highway-mpg',y='price',data=df)
plt.ylim(0,)

plt.figure(figsize=(width,height))
sns.regplot(x='peak-rpm',y='price',data=df)
plt.ylim(0,)
# The same thing
plt.figure(figsize=(width,height))
sns.regplot(df['peak-rpm'],df['price'])
plt.ylim(0,)

df2 =df[['peak-rpm','highway-mpg','price']]
df2.head(20)
df2.corr()

df[['peak-rpm','highway-mpg','price']].corr()


width =12
height =10
plt.figure(figsize=(width,height))
sns.residplot(df['highway-mpg'],df['price'])
# sns.residplot(x='highway-mpg',y='price', data=df)
plt.show()

Yhat =lm.predict(Z)
plt.figure(figsize=(width,height))
ax1 = sns.distplot(df['price'], hist=False, color="r", label="Actual Value")
sns.distplot(Yhat, hist=False, color="b", label="Fitted Values" , ax=ax1)

sns.distplot(df['price'], hist = False, color='r', label='Actual Value')
sns.distplot(Yhat, hist=False, color='b', label='Fitted Values')   # This 2 lines of code have the same output as above, why that rather than this way

plt.title('Acutal va Fitted Value for Price')
plt.xlabel('Price (in dollars)')
plt.ylabel('Proportion of Cars')

plt.show()
plt.close()



def PlotPolly(model, independent_variable, dependent_variable, Name):
    x_new = np.linspace(15,55,100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variable, '.',x_new, y_new, '-')
    plt.title('Polynomial Fit With Matplotlib for Price ~ Length')
    ax= plt.gca()
    ax.set_facecolor((0.898,0.898,0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('Price of Cars')
    plt.ylim(0,)

    plt.show()
    plt.close()

x = df['highway-mpg']
y = df['price']

f = np.polyfit(x,y,3)
p = np.poly1d(f)
print(p)
PlotPolly(p, x, y, 'highway-mpg')
np.polyfit(x, y, 3)


f2 = np.polyfit(x, y, 11)
p2 = np.poly1d(f2)
print(p2)

PlotPolly(p2, x, y, 'highway-mpg')


from sklearn.preprocessing import PolynomialFeatures
pr = PolynomialFeatures(degree =2)
pr

Z_pr = pr.fit_transform(Z)
Z.shape
Z_pr.shape

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


Input = [('scale',StandardScaler()), ('polynomial', PolynomialFeatures(include_bias=False)), ('model', LinearRegression())]
pipe = Pipeline(Input)
pipe.fit(Z,y)
ypipe = pipe.predict(Z)
ypipe[0:4]


Input2 =[('scale', StandardScaler()),('model', LinearRegression())]
pipe2 = Pipeline(Input2)
pipe2.fit(Z, y)
ypipe = pipe.predict(Z)
ypipe[0:10:2]
ypipe[0:10]






lm.fit(X, Y)
print('The R-square =', lm.score(X,Y))
Yhat = lm.predict(X)
print('The output of the first predicted value is:', Yhat[0:4])
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(df['price'], Yhat)
print('The mean square error of price and predicted value is:',mse)



lm.fit(Z,df['price'])
print('The R-square =', lm.score(Z, df['price']))

Y_predict_multifit = lm.predict(Z)
print('The output of the first predicted value is:', Y_predict_multifit[0:4])
mse2 = mean_squared_error(df['price'], Y_predict_multifit)
print('The mean square error of price and predicted value is:', mse2)



from sklearn.metrics import r2_score
r_squared = r2_score(y, p(x))
# X = df[['engine-size']]
# Y = df[['price']]
# x = df['engine-size']
# y = df['price']
print('The R-square value is:', r_squared)

mean_squared_error(df['price'],p(x))


new_input = np.arange(1,100,1).reshape(-1,1)
lm.fit(X,Y)
lm
yhat = lm.predict(new_input)
yhat[0:5]
plt.plot(new_input, yhat)
plt.show()

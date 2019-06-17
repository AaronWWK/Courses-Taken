
# ------WEEK 1 ----------------
# ------WEEK 1 ----------------
# ------WEEK 1 ----------------
import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

df = pd.read_csv(url,header = None)

# df.head(n) # to show the first n rows of the data frame
# df.tail(n) # to show the bottom n rows of the data frame

print('The first 5 rows in the dataframe:')
df.head(5)
df.tail(10)


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers
df.head(5)

# path = '/Users/wanweikang/Library/Mobile Documents/com~apple~CloudDocs/Python/Data Analysis with Python/auto.csv'
# df.to_csv(path)   #save the file to the scv file

df.to_csv('automobile.csv', index = False)

df.describe(include = 'all')  # show all the columns
df.info

#df.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
#Drop specified labels from rows or columns.
# df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)  inplace =  False do not change the data dataframe
# Remove missing values.
#axis = 0 drop the row,  axis = 1 drop the column

df.dropna(subset= ['price'],axis=0)

print(df.columns)

#df.dtypes  #returns a Series with the data type of each column.
print(df.dtypes)

df.describe()
# This shows the statistical summary of all numeric-typed (int, float) columns.
# For example, the attribute "symboling" has 205 counts, the mean value of this column is 0.83, the standard deviation is 1.25, the minimum value is -2, 25th percentile is 0, 50th percentile is 1, 75th percentile is 2, and the maximum value is 3.
# However, what if we would also like to check all the columns including those that are of type object.


df.describe(include = 'all')
# Now, it provides the statistical summary of all the columns, including object-typed attributes.
# We can now see how many unique values, which is the top value and the frequency of top value in the object-typed columns.
# Some values in the table above show as "NaN", this is because those numbers are not available regarding a particular column type

df[['length','compression-ratio']].describe()    # include = 'all' do not change the resule
# You can select the columns of a data frame by indicating the name of each column, for example, you can select the three columns as follows:
# dataframe[[' column 1 ',column 2', 'column 3']]
# Where "column" is the name of the column, you can apply the method ".describe()" to get the statistics of those columns as follows:
# dataframe[[' column 1 ',column 2', 'column 3'] ].describe()

df.info

# ------WEEK 2 ----------------
# ------WEEK 2 ----------------
# ------WEEK 2 ----------------
df.dropna(subset = ['symboling'],axis = 0)  #axis = 0 drop the row,  axis = 1 drop the column

df.head(5)q
df['symboling'] = df['symboling']+1
df.head(5)

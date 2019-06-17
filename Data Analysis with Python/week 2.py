
import pandas as pd
import matplotlib as plt
import numpy as np

filename = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv'

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(filename, names = headers)  # names , not name
df.head(5)     #  head and tail not read
df.replace('?', np.nan, inplace = True)
df.head(5)


#  .isnull()  .notnull()  The output is a boolean value indicating whether the value that is passed into the argument is in fact missing data.
missing_data =df.isnull()
missing_data.head(5)
missing_data2 = df.notnull()
missing_data2.head(5)

#    Series.tolist()       Return a ---list---- of the values.
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print('')

avg_norm_loss = df['normalized-losses'].astype('float').mean(axis = 0)  # axis = 0 means calculate the mean along the row, which is from the 1st row to the bottom
print("Average of normalized-losses:",avg_norm_loss)
df['normalized-losses'].replace(np.nan, avg_norm_loss, inplace = True)

avg_bore = df['bore'].astype('float').mean(axis = 0)
print('Average of bore:', avg_bore)
df['bore'].replace(np.nan, avg_bore, inplace = True)

avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
print('Average horsepower', avg_horsepower)
df['horsepower'].replace(np.nan, avg_horsepower, inplace = True)

avg_peakrpm = df['peak-rpm'].astype('float').mean(axis=0)
print('Average peak rpm', avg_peakrpm)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace = True)


df['num-of-doors'].value_counts()
most = df['num-of-doors'].value_counts().idxmax()
df['num-of-doors'].replace(np.nan, most, inplace = True)

df.dropna(subset=['price'], axis=0, inplace=True)
df.reset_index(drop = True, inplace=True)

df.head()


# --------------Correct data format-------------
# We are almost there!
# The last step in data cleaning is checking and making sure that all data is in the correct format (int, float, text or other).
#
# In Pandas, we use
# .dtype() to check the data type
# .astype() to change the data type

df.dtypes

df[['bore','stroke']] = df[['bore','stroke']].astype('float')    ##  ----why double [] not one []  ???  the inner [] represents a list
df[['normalized-losses']] = df[['normalized-losses']].astype('int')
df[['price']] = df[['price']].astype('float')
df[['peak-rpm']]= df[['peak-rpm']].astype('float')

df.dtypes
# --------------Data Standardization-------------
# Data is usually collected from different agencies with different formats. (Data Standardization is also a term for a particular type of data normalization, where we subtract the mean and divide by the standard deviation)
#
# What is Standardization?
#
# Standardization is the process of transforming data into a common format which allows the researcher to make the meaningful comparison.
#
# Example
#
# Transform mpg to L/100km:
#
# In our dataset, the fuel consumption columns "city-mpg" and "highway-mpg" are represented by mpg (miles per gallon) unit. Assume we are developing an application in a country that accept the fuel consumption with L/100km standard
#
# We will need to apply data transformation to transform mpg into L/100km?
#
# The formula for unit conversion is
#
# L/100km = 235 / mpg
#
# We can do many mathematical operations directly in Pandas.

df['city-L/100km'] = 235 / df['city-mpg']   #Convert mpg to L/100km by mathematical operation (235 divided by mpg)  add a new column called 'city-L/100km'
df.head()
df['highway-L/100km'] = 235/df['highway-mpg']
df.head()


# -------------Data Normalization------------
# Why normalization?
#
# Normalization is the process of transforming values of several variables into a similar range. Typical normalizations include scaling the variable so the variable average is 0, scaling the variable so the variance is 1, or scaling variable so the variable values range from 0 to 1
#
# Example
#
# To demonstrate normalization, let's say we want to scale the columns "length", "width" and "height"
#
# Target:would like to Normalize those variables so their value ranges from 0 to 1.
#
# Approach: replace original value by (original value)/(maximum value)
df['length'] = df['length'] / df['length'].max()
df['width'] = df['width'] / df['width'].max()
df['height'] = df['height'] / df['height'].max()
df.head()

# -------------Binning-----------------
# Why binning?
# Binning is a process of transforming continuous numerical variables into discrete categorical 'bins', for grouped analysis.
#
# Example:
#
# In our dataset, "horsepower" is a real valued variable ranging from 48 to 288, it has 57 unique values. What if we only care about the price difference between cars with high horsepower, medium horsepower, and little horsepower (3 types)? Can we rearrange them into three ‘bins' to simplify analysis?
#
# We will use the Pandas method 'cut' to segment the 'horsepower' column into 3 bins


df['horsepower'] = df['horsepower'].astype(int, copy=True)
# %matplotlib inline
import matplotlib as plt
from matplotlib import pyplot

plt.pyplot.hist(df['horsepower'])
# set x/y labels and plot title
plt.pyplot.xlabel('horsepower')
plt.pyplot.ylabel('count')
plt.pyplot.title('horsepower bins')

# We would like 3 bins of equal size bandwidth so we use ------ numpy's linspace(start_value, end_value, numbers_generated ------function.
# Since we want to include the minimum value of horsepower we want to set start_value=min(df["horsepower"]).
# Since we want to include the maximum value of horsepower we want to set end_value=max(df["horsepower"]).
# Since we are building >>> 3 bins of equal length, there should be 4 dividers  <<<<, so numbers_generated=4.
# We build a bin array, with a minimum value to a maximum value, with bandwidth calculated above.
# The bins will be values used to determine when one bin ends and another begins.

bins = np.linspace(min(df['horsepower']), max(df['horsepower']), 4)  #
bins

# We set group names:
group_names = ['Low', 'Medium', 'High']

# We apply the function "cut" the determine what each value of "df['horsepower']" belongs to.
df['horsepower-bined'] = pd.cut(df['horsepower'], bins, labels = group_names, include_lowest=True)
df[['horsepower','horsepower-bined']].head(20)  #only show 2 columns of the dataframe df[]  ['','']list of column names

df['horsepower-bined'].value_counts()


plt.pyplot.bar(group_names, df['horsepower-bined'].value_counts())
plt.pyplot.xlabel('horsepower')
plt.pyplot.ylabel('count')
plt.pyplot.title('horsepower bins')

#
# ---------------  Bins visualization   -----------------
# Normally, a histogram is used to visualize the distribution of bins we created above.
a =(0,1,2)
# draw historgram of attribute "horsepower" with bins = 3
plt.pyplot.hist(df['horsepower'], bins =3)

plt.pyplot.xlabel('horsepower')
plt.pyplot.ylabel('count')
plt.pyplot.title('horsepower bins')

#  ---------------  Indicator variable (or dummy variable)  ------------------
# What is an indicator variable?
# An indicator variable (or dummy variable) is a numerical variable used to label categories.
# They are called 'dummies' because the numbers themselves don't have inherent meaning.
# Why we use indicator variables?
# So we can use categorical variables for regression analysis in the later modules.
# Example
# We see the column "fuel-type" has two unique values, "gas" or "diesel". Regression doesn't understand words, only numbers.
# To use this attribute in regression analysis, we convert "fuel-type" into indicator variables.
# We will use the panda's method 'get_dummies' to assign numerical values to different categories of fuel type.

df.columns
dummny_variable_1 = pd.get_dummies(df['fuel-type'])
dummny_variable_1.head(5)

dummny_variable_1.rename(columns = {'diesel':'diesel1','gas':'gas1'}, inplace = True)
dummny_variable_1.head(5)

# We now have the value 0 to represent "gas" and 1 to represent "diesel" in the column "fuel-type". We will now insert this column back into our original dataset.

# merge data frame "df" and "dummy_variable_1"
df= pd.concat([df, dummny_variable_1], axis = 1)   # two data frame name in the list []
df.head(5)

# drop original column "fuel-type" from "df"
df.drop('fuel-type', axis =1, inplace = True)
df.head(5)


dummy_variable_2 = pd.get_dummies(df['aspiration'])
dummy_variable_2.head(5)
dummy_variable_2.rename(columns ={'std':'aspiration-std','turbo':'aspiration-turbo'},inplace = True)
dummy_variable_2.head()

#merge the new dataframe to the original datafram
df = pd.concat([df, dummy_variable_2], axis=1)

# drop original column "aspiration" from "df"
df.drop('aspiration', axis = 1, inplace=True)









df.to_csv('auto_week2.csv')

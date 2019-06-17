import pandas as pd
import numpy as np

path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df= pd.read_csv(path)
df.head()
import matplotlib.pyplot as plt
import seaborn as sns

# How to choose the right visualization method?
# When visualizing individual variables, it is important to ========>>>  first understand what type of variable you are dealing with.  <<<=========
# This will help us find the right visualization method for that variable.

print(df.dtypes)
#
# Question #1:
# What is the data type of the column "peak-rpm"?
# For example, we can calculate the correlation between variables of type 'int' or 'float64' using the method 'corr'
df.corr()

df[['bore','stroke','compression-ratio',"horsepower"]].corr()


# =====>>>  Continuous numerical variables:  <<<=====
# Continuous numerical variables are variables that may contain any value within some range. Continuous numerical variables can have the type "int64" or "float64".
# A great way to visualize these variables is by using scatterplots with fitted lines.
#
# In order to start understanding the (linear) relationship between an individual variable and the price.
# We can do this by using "regplot", which plots the scatterplot plus the fitted regression line for the data.

sns.regplot(x='engine-size', y='price', data = df)
plt.ylim(0,)   # the value of y start from 0 and then goes up

df[['engine-size','price']].corr()

sns.regplot(x='highway-mpg',y='price',data = df)
plt.ylim(0,)

df[['highway-mpg','price']].corr()

sns.regplot(x= 'peak-rpm',y = 'price', data = df)
plt.ylim(0,)

df[['peak-rpm','price']].corr()


# =====>>>  Categorical variables:  <<<=====
# These are variables that describe a 'characteristic' of a data unit, and are selected from a small group of categories.
# The categorical variables can have the type "object" or "int64". A good way to visualize categorical variables is by using boxplots.
# Let's look at the relationship between "body-style" and "price".

sns.boxplot(x='body-style',y='price', data= df)
# We see that the distributions of price between the different body-style categories have a significant overlap,
# and so body-style would not be a good predictor of price.

# Let's examine engine "engine-location" and "price":
sns.boxplot(x='engine-location',y='price' ,data =df)
# Here we see that the distribution of price between these two engine-location categories, front and rear,
# are distinct enough to take engine-location as a potential good predictor of price.
#
# Let's examine "drive-wheels" and "price".
sns.boxplot(x='drive-wheels',y='price', data=df)
# Here we see that the distribution of price between the different drive-wheels categories differs;
# as such drive-wheels could potentially be a predictor of price.



# ==========>>>>>> 3. Descriptive Statistical Analysis <<<<<<<===========
# Let's first take a look at the variables by utilizing a description method.
#
# The describe function automatically computes basic statistics for all continuous variables. Any NaN values are automatically skipped in these statistics.
#
# This will show:
#
# the count of that variable
# the mean
# the standard deviation (std)
# the minimum value
# the IQR (Interquartile Range: 25%, 50% and 75%)
# the maximum value
#
# We can apply the method "describe" as follows:

df.describe()
# The dufault setting of 'describe' skips variables of type object. We can apply the method 'describe' on the variable of type 'object' as follows:
df.describe(include=['object'])

# Value Counts
# Value-counts is a good way of understanding how many units of each characteristic/variable we have. We can apply the "value_counts" method on the column 'drive-wheels'.
# Don’t forget the method "value_counts" =====>>>>>  only works on Pandas series, not Pandas Dataframes  <<<<<=======.
# As a result, we only include one bracket =======>>>>  "df['drive-wheels']"--series <<<<<======= not two brackets "df[['drive-wheels']]--- dataframes".

df['drive-wheels'].value_counts()
# We can convert the series to a dataframe as follows:
df['drive-wheels'].value_counts().to_frame()

drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns= {'drive-wheels':'value_counts'},inplace=True)
drive_wheels_counts

drive_wheels_counts.index.name= 'drive-wheels'
drive_wheels_counts

engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns = {'engine-location':'value-counts'}, inplace = True)
engine_loc_counts.index.name = 'engine-location'
engine_loc_counts.head(20)


# ==========>>>>>> 4. Basics of Grouping <<<<<<=========
# The "groupby" method groups data by different categories. The data is grouped based on one or several variables and analysis is performed on the individual groups.
#
# For example, let's group by the variable "drive-wheels". We see that there are 3 different categories of drive wheels.
df['drive-wheels'].unique()

# If we want to know, on average, which type of drive wheel is most valuable, we can group "drive-wheels" and then average them.
#
# We can select the columns 'drive-wheels', 'body-style' and 'price', then assign it to the variable "df_group_one".

# Example 1
df_group_one = df[['drive-wheels','body-style','price']]  # dataframe use two brackets [[]]
df_group_one= df_group_one.groupby(['drive-wheels'], as_index=False).mean()
df_group_one
# Example 2
df_group_one_1 = df[['drive-wheels','length','price']]  # dataframe use two brackets [[]]
df_group_one_1= df_group_one_1.groupby(['drive-wheels'], as_index=False).mean()
df_group_one_1
# The difference between these two example is that :
# In example 1, data in body-style is object, can not be 'mean'ed,
# In example 2, data in length is float64, can be 'mean'ed

# the one on Youtube
df_group_one.groupby('drive-wheels').price.mean()
# You can also group with multiple variables. For example, let's group by both 'drive-wheels' and 'body-style'.
# This groups the dataframe by the unique combinations 'drive-wheels' and 'body-style'. We can store the results in the variable 'grouped_test1'.
df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'], as_index=False).mean()
grouped_test1

# This grouped data is much easier to visualize when it is made into a pivot table.
# A pivot table is like an Excel spreadsheet, with one variable along the column and another along the row.
# We can convert the dataframe to a pivot table using the method "pivot " to create a pivot table from the groups.
# In this case, we will leave the drive-wheel variable as the rows of the table, and pivot body-style to become the columns of the table:
grouped_pivot = grouped_test1.pivot(index = 'drive-wheels', columns ='body-style')
grouped_pivot

# Often, we won't have data for some of the pivot cells. We can fill these missing cells with the value 0,
# but any other value could potentially be used as well. It should be mentioned that missing data is quite a complex subject and is an entire course on its own.
grouped_pivot = grouped_pivot.fillna(0)  #Fill missing value with 0
grouped_pivot

# Use the "groupby" function to find the average "price" of each car based on "body-style" ?
df_gptest2 = df[['drive-wheels','body-style','price']]
df_gptest2 = df_gptest2.groupby(['body-style'],as_index=False).mean()
df_gptest2

df_group_one = df[['drive-wheels','body-style','price']]
df_group_one_2 =df_group_one.groupby(['body-style'],as_index=False).mean()
df_group_one_2

# Let's use a heat map to visualize the relationship between Body Style vs Price.
plt.pcolor(grouped_pivot, cmap='RdBu')
plt.colorbar()
plt.show()

# The heatmap plots the target variable (price) proportional to colour with respect to the variables 'drive-wheel' and 'body-style'
# in the vertical and horizontal axis respectively. This allows us to visualize how the price is related to 'drive-wheel' and 'body-style'.
fig, ax = plt.subplots()
im = ax.pcolor(grouped_pivot, cmap='RdBu')

#label names
row_labels = grouped_pivot.columns.levels[1]
col_labels = grouped_pivot.index

#move ticks and labels to the center
ax.set_xticks(np.arange(grouped_pivot.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(grouped_pivot.shape[0]) + 0.5, minor=False)

#insert col_labels
ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(col_labels, minor=False)

#rotate label if too along
plt.xticks(rotation=90)

fig.colorbar(im)
plt.show()

# Visualization is very important in data science, and Python visualization packages provide great freedom.
# We will go more in-depth in a separate Python Visualizations course.
#
# The main question we want to answer in this module, is "What are the main characteristics which have the most impact on the car price?".
#
# To get a better measure of the important characteristics, we look at the correlation of these variables
# with the car price, in other words: how is the car price dependent on this variable?

# =======>>>>>> 5. Correlation and Causation  <<<<<<<======

# Correlation: a measure of the extent of interdependence between variables.
# Causation: the relationship between cause and effect between two variables.
#
# It is important to know the difference between these two and that correlation does not imply causation.
# Determining correlation is much simpler the determining causation as causation may require independent experimentation.
#
# Pearson Correlation
# The Pearson Correlation measures the linear dependence between two variables X and Y.
# The resulting coefficient is a value between -1 and 1 inclusive, where:
#     1: Total positive linear correlation.
#     0: No linear correlation, the two variables most likely do not affect each other.
#     -1: Total negative linear correlation.
# Pearson Correlation is the default method of the function "corr".
# Like before we can calculate the Pearson Correlation of the of the 'int64' or 'float64' variables.

df.corr()

from scipy import stats
# Wheel-base vs Price
pearson_coef, p_value = stats.pearsonr(df['wheel-base'],df['price'])
print('The Pearson Correlation Cofficient is', pearson_coef,'with a P-value of p =', p_value)
# Since the p-value is  <  0.001, the correlation between wheel-base and price is statistically significant,
# although the linear relationship isn't extremely strong (~0.585)


# Horsepower vs Price
pearson_coef, p_value = stats.pearsonr(df['horsepower'],df['price'])
print('The Pearson Correlation Cofficient is', pearson_coef, 'with a P-value of P=' ,p_value)
# Since the p-value is < 0.001, the correlation between length and price is statistically significant,
# and the linear ralationship is moderately strong (~0.809), close to 1


# Length vs Price
pearson_coef, p_value = stats.pearsonr(df['length'],df['price'])
print('The Pearson Correlatin Cofficient is ', pearson_coef, 'with a P-value of p=', p_value)
# Since the p-value is  <  0.001, the correlation between length and price is statistically significant,
# and the linear relationship is moderately strong (~0.691)


# Width vs Price
pearson_coef, p_value = stats.pearsonr(df['width'],df['price'])
print('The Pearson Correlation Cofficient is', pearson_coef, 'with a P-value of p=', p_value)

# Since the p-value is < 0.001, the correlation between width and price is statistically significant,
# and the linear relationship is quite strong (~0.751).

# Curb-weight vs price
pearson_coef, p_value = stats.pearsonr(df['curb-weight'],df['price'])
print('The Pearson Correlation Cofficient is', pearson_coef, 'with a P-value of p=', p_value)
# Since the p-value is  <  0.001, the correlation between curb-weight and price is statistically significant,
# and the linear relationship is quite strong (~0.834).

# Engine vs Price
pearson_coef, p_value = stats.pearsonr(df['engine-size'],df['price'])
print('The Pearson Correlation Cofficient is ', pearson_coef, 'with a P-value of p=', p_value)
# Since the p-value is  <  0.001, the correlation between engine-size and price is statistically significant,
# and the linear relationship is very strong (~0.872).

# Bore vs Price
pearson_coef, p_value = stats.pearsonr(df['bore'],df['price'])
print('The Pearson Correlation COfficient is ', pearson_coef, 'with a p value of p=', p_value)
# Since the p-value is  <  0.001, the correlation between bore and price is statistically significant,
# but the linear relationship is only moderate (~0.521).

# City-mpg vs Price
pearson_coef, p_value = stats.pearsonr(df['city-mpg'],df['price'])
print('The pearson Correlaton Cofficient is ', pearson_coef, 'with a p-value of p=', p_value)
# Since the p-value is  <  0.001, the correlation between city-mpg and price is statistically significant,
# and the coefficient of ~ -0.687 shows that the relationship is negative and moderately strong.

# Highway-mpg vs Price
pearson_coef,p_value = stats.pearsonr(df['highway-mpg'],df['price'])
print('The pearson correlation cofficient is', pearson_coef, 'with a p-value of p=', p_value)
# Since the p-value is < 0.001, the correlation between highway-mpg and price is statistically significant,
# and the coefficient of ~ -0.705 shows that the relationship is negative and moderately strong.


# 6. ANOVA
# ANOVA: Analysis of Variance
# The Analysis of Variance (ANOVA) is a statistical method used to test whether there are significant
# differences between the means of two or more groups. ANOVA returns two parameters:
#
# F-test score: ANOVA assumes the means of all groups are the same, calculates how much the actual means deviate from the assumption,
# and reports it as the F-test score. A larger score means there is a larger difference between the means.
#
# P-value: P-value tells how statistically significant is our calculated score value.
#
# If our price variable is strongly correlated with the variable we are analyzing, expect ANOVA to return a sizeable F-test score and a small p-value.
#
# ========>>>>>>   Drive Wheels     <<<<<<<<========
# Since ANOVA analyzes the difference between different groups of the same variable, the groupby function will come in handy.
# Because the ANOVA algorithm averages the data automatically, we do not need to take the average before hand.
#
# Let's see if different types 'drive-wheels' impact 'price', we group the data.

grouped_test2 = df_gptest[['drive-wheels','price']].groupby(['drive-wheels'])
grouped_test2.head(2)
df_gptest
grouped_test2.get_group('4wd')['price']
grouped_test2.get_group('4wd')['price'].to_frame()
f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'],grouped_test2.get_group('rwd')['price'],grouped_test2.get_group('4wd')['price'])
print('ANOVA results : F=', f_val, ', P= ', p_val)
# This is a great result, with a large F test score showing a strong correlation and a P value of almost 0 implying almost certain statistical significance.
# But does this mean all three tested groups are all this highly correlated?

# Separately : fwd and rwd
f_val, p_val = stats.f_oneway (grouped_test2.get_group('fwd')['price'],grouped_test2.get_group('rwd')['price'])
print('ANOVA results : F=', f_val, ', P= ', p_val)

f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'],grouped_test2.get_group('rwd')['price'])
print('ANOVA results : F=', f_val, ', P= ', p_val)

f_val, p_val = stats.f_oneway(grouped_test2.get_group('4wd')['price'], grouped_test2.get_group('fwd')['price'])
print('ANOVA results : F=', f_val, ', P= ', p_val)

Python – Basics of Pandas using Iris Dataset



Python language is one of the most trending programming languages as it is
dynamic than others. Python is a simple high-level and an open-source language
used for general-purpose programming. It has many open-source libraries and
Pandas is one of them. Pandas is a powerful, fast, flexible open-source
library used for data analysis and manipulations of data frames/datasets.
Pandas can be used to read and write data in a dataset of different formats
like CSV(comma separated values), txt, xls(Microsoft Excel) etc.  
In this post, you will learn about various features of Pandas in Python and
how to use it to practice.

 **Prerequisites:** Basic knowledge about coding in Python.

 **Installation:**

So if you are new to practice Pandas, then firstly you should install Pandas
on your system.  
Go to Command Prompt and run it as administrator. Make sure you are connected
with an internet connection to download and install it on your system.

Then type “ **pip install pandas** “, then press Enter key.

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428230316/gfg171.jpg)

Download the Dataset **“Iris.csv”** from here

 **Iris dataset** is the Hello World for the Data Science, so if you have
started your career in Data Science and Machine Learning you will be
practicing basic ML algorithms on this famous dataset. Iris dataset contains
five columns such as Petal Length, Petal Width, Sepal Length, Sepal Width and
Species Type.  
Iris is a flowering plant, the researchers have measured various features of
the different iris flowers and recorded digitally.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428162631/gfg123.jpg)

 **Getting Started with Pandas:**

 **Code: Importing pandas to use in our code as pd.**

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd  
  
---  
  
 __

 __

 **Code: Reading the dataset “Iris.csv”.**

 __

 __  
 __

 __

 __  
 __  
 __

data= pd.read_csv("your downloaded dataset location ")  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428230143/gfg162.jpg)

 **Code: Displaying up the top rows of the dataset with their columns**  
The function head() will display the top rows of the dataset, the default
value of this function is 5, that is it will show top 5 rows when no argument
is given to it.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

data.head()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428213203/gfg212-1.jpg)

 **Displaying the number of rows randomly.**  
In sample() function, it will also display the rows according to arguments
given, but it will display the rows randomly.

 __

 __  
 __

 __

 __  
 __  
 __

data.sample(10)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428213323/gfg310.jpg)

 **Code: Displaying the number of columns and names of the columns.**  
The column() function prints all the columns of the dataset in a list form.

 __

 __  
 __

 __

 __  
 __  
 __

data.columns  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428213441/gfg44.jpg)

 **Code: Displaying the shape of the dataset.**  
The shape of the dataset means to print the total number of rows or entries
and the total number of columns or features of that particular dataset.

 __

 __  
 __

 __

 __  
 __  
 __

#The first one is the number of rows and

# the other one is the number of columns.

data.shape  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428213650/gfg54.jpg)

 **Code: Display the whole dataset**

 __

 __  
 __

 __

 __  
 __  
 __

print(data)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428213828/gfg64.jpg)

 **Code: Slicing the rows.**  
Slicing means if you want to print or work upon a particular group of lines
that is from 10th row to 20th row.

 __

 __  
 __

 __

 __  
 __  
 __

#data[start:end]

#start is inclusive whereas end is exclusive

print(data[10:21])

# it will print the rows from 10 to 20.

 

# you can also save it in a variable for further use in analysis

sliced_data=data[10:21]

print(sliced_data)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428214846/gfg83.jpg)

 **Code: Displaying only specific columns.**  
In any dataset, it is sometimes needed to work upon only specific features or
columns, so we can do this by the following code.

 __

 __  
 __

 __

 __  
 __  
 __

#here in the case of Iris dataset

#we will save it in a another variable named "specific_data"

 

specific_data=data[["Id","Species"]]

#data[["column_name1","column_name2","column_name3"]]

 

#now we will print the first 10 columns of the specific_data dataframe.

print(specific_data.head(10))  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428215929/gfg93.jpg)

 **Filtering:Displaying the specific rows using “iloc” and “loc” functions.  
**  
The “loc” functions use the index name of the row to display the particular
row of the dataset.  
The “iloc” functions use the index integer of the row, which gives complete
information about the row.  
 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

#here we will use iloc

 

data.iloc[5]

#it will display records only with species "Iris-setosa".

data.loc[data["Species"] == "Iris-setosa"]  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428220144/gfg103.jpg) iloc()[/caption]

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200502165155/gfg241.jpg)

loc()

 **Code: Counting the number of counts of unique values using
“value_counts()”.**  
The value_counts() function, counts the number of times a particular instance
or data has occurred.

 __

 __  
 __

 __

 __  
 __  
 __

#In this dataset we will work on the Species column, it will count number of
times a particular species has occurred.

data["Species"].value_counts()

#it will display in descending order.  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428220440/gfg1110.jpg)

 **Calculating sum, mean and mode of a particular column.**  
We can also calculate the sum, mean and mode of any integer columns as I have
done in the following code.

 __

 __  
 __

 __

 __  
 __  
 __

# data["column_name"].sum()

 

sum_data = data["SepalLengthCm"].sum()

mean_data = data["SepalLengthCm"].mean()

median_data = data["SepalLengthCm"].median()

 

print("Sum:",sum_data, "\nMean:", mean_data,
"\nMedian:",median_data)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428221053/gfg124.jpg)

 **Code: Extracting minimum and maximum from a column.**  
Identifying minimum and maximum integer, from a particular column or row can
also be done in a dataset.

 __

 __  
 __

 __

 __  
 __  
 __

min_data=data["SepalLengthCm"].min()

max_data=data["SepalLengthCm"].max()

 

print("Minimum:",min_data, "\nMaximum:", max_data)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428221600/gfg133.jpg)

 **Code: Adding a column to the dataset.**  
If want to add a new column in our dataset, as we are doing any calculations
or extracting some information from the dataset, and if you want to save it a
new column. This can be done by the following code by taking a case where we
have added all integer values of all columns.

 __

 __  
 __

 __

 __  
 __  
 __

# For example, if we want to add a column let say "total_values",

# that means if you want to add all the integer value of that particular

# row and get total answer in the new column "total_values".

# first we will extract the columns which have integer values.

cols = data.columns

 

# it will print the list of column names.

print(cols)

 

# we will take that columns which have integer values.

cols = cols[1:5]

 

# we will save it in the new dataframe variable

data1 = data[cols]

 

# now adding new column "total_values" to dataframe data.

data["total_values"]=data1[cols].sum(axis=1)

 

# here axis=1 means you are working in rows, 

# whereas axis=0 means you are working in columns.  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428221811/gfg143.jpg)

 **Code: Renaming the columns.**  
Renaming our column names can also be possible in python pandas libraries. We
have used the rename() function, where we have created a dictionary “newcols”
to update our new column names. The following code illustrates that.

 __

 __  
 __

 __

 __  
 __  
 __

newcols={

"Id":"id",

"SepalLengthCm":"sepallength"

"SepalWidthCm":"sepalwidth"}

 

data.rename(columns=newcols,inplace=True)

 

print(data.head())  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200428222816/gfg152.jpg)

 **Formatting and Styling:**  
Conditional formatting can be applied to your dataframe by using
Dataframe.style function. Styling is used to visualize your data, and most
convenient way of visualizing your dataset is in tabular form.  
Here we will highlight the minimum and maximum from each row and columns.

 __

 __  
 __

 __

 __  
 __  
 __

#this is an example of rendering a datagram,

which is not visualised by any styles. 

data.style  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200502161552/gfg181.jpg)

Now we will highlight the maximum and minimum column-wise, row-wise, and the
whole dataframe wise using Styler.apply function. The Styler.apply function
passes each column or row of the dataframe depending upon the keyword argument
axis. For column-wise use axis=0, row-wise use axis=1, and for the entire
table at once use axis=None.

 __

 __  
 __

 __

 __  
 __  
 __

# we will here print only the top 10 rows of the dataset,

# if you want to see the result of the whole dataset remove 

#.head(10) from the below code

 

data.head(10).style.highlight_max(color='lightgreen',
axis=0)

 

data.head(10).style.highlight_max(color='lightgreen',
axis=1)

 

data.head(10).style.highlight_max(color='lightgreen',
axis=None)  
  
---  
  
 __

 __

 **Output:**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200502162348/gfg191.jpg)

for axis=0

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200502162439/gfg202.jpg)

for axis=1

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200502162541/gfg212-1.jpg)

for axis=None

 **Code: Cleaning and detecting missing values**  
In this dataset, we will now try to find the missing values i.e NaN, which can
occur due to several reasons.

 __

 __  
 __

 __

 __  
 __  
 __

data.isnull()

#if there is data is missing, it will display True else False.  
  
---  
  
 __

 __

 **Output:**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200502163845/gfg221.jpg)

isnull()

 **Code: Summarizing the missing values.**  
We will display how many missing values are present in each column.

 __

 __  
 __

 __

 __  
 __  
 __

data.isnull.sum()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200502164053/gfg231.jpg)

 **Heatmap: Importing seaborn**  
The heatmap is a data visualisation technique which is used to analyse the
dataset as colors in two dimensions. Basically it shows correlation between
all numerical variables in the dataset. Heatmap is an attribute of the Seaborn
library.  
 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

import seaborn as sns

 

iris = sns.load_dataset("iris")

sns.heatmap(iris.corr(),camp = "YlGnBu", linecolor = 'white',
linewidths = 1)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200502212612/gfg251.jpg)  
 **Code: Annotate each cell with the numeric value using integer formatting**

 __

 __  
 __

 __

 __  
 __  
 __

sns.heatmap(iris.corr(),camp= "YlGnBu", linecolor = 'white',
linewidths = 1, annot = True )  
  
---  
  
 __

 __

 **Output:**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200502213106/gfg261.jpg)

heatmap with annot=True

  
 **Pandas Dataframe Correlation:**  
Pandas correlation is used to determine pairwise correlation of all the
columns of the dataset. In datafram.corr(), the missing values are excluded
and non-numeric columns are also ignored.  
 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

data.corr(method='pearson')  
  
---  
  
 __

 __

 **Output:**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200502213904/gfg271.jpg)

data.corr()

The output dataframe can be seen as for any cell, row variable correlation
with the column variable is the value of the cell. The correlation of a
variable with itself is 1. For that reason, all the diagonal values are 1.00.

 **Multivariate Analysis:**  
Pair plot is used to visualize the relationship between each type of column
variable. It is implemented only by one line code, which is as follows :  
 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

g= sns.pairplot(data,hue="Species")  
  
---  
  
 __

 __

 **Output:**  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200502220804/gfg281.jpg)

Pairplot of variable “Species”, to make it more understandable.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save


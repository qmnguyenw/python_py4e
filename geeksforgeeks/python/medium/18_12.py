Exploratory Data Analysis in Python | Set 1



 **Exploratory Data Analysis** is a technique to analyze data with visual
techniques and all statistical results. We will learn about how to apply these
techniques before applying any Machine Learning Models.

To get the link to csv file used, click here.

 **Loading Libraries:**

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

 

 

from scipy.stats import trim_mean  
  
---  
  
 __

 __

 **Loading Data:**

 __

 __  
 __

 __

 __  
 __  
 __

data= pd.read_csv("state.csv")

 

# Check the type of data

print ("Type : ", type(data), "\n\n")

 

# Printing Top 10 Records

print ("Head -- \n", data.head(10))

 

# Printing last 10 Records 

print ("\n\n Tail -- \n", data.tail(10))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    Type : class 'pandas.core.frame.DataFrame'
    
    
    **Head --**
              State  Population  Murder.Rate Abbreviation
    0      Alabama     4779736          5.7           AL
    1       Alaska      710231          5.6           AK
    2      Arizona     6392017          4.7           AZ
    3     Arkansas     2915918          5.6           AR
    4   California    37253956          4.4           CA
    5     Colorado     5029196          2.8           CO
    6  Connecticut     3574097          2.4           CT
    7     Delaware      897934          5.8           DE
    8      Florida    18801310          5.8           FL
    9      Georgia     9687653          5.7           GA
    
    
    **Tail --**
                 State  Population  Murder.Rate Abbreviation
    40   South Dakota      814180          2.3           SD
    41      Tennessee     6346105          5.7           TN
    42          Texas    25145561          4.4           TX
    43           Utah     2763885          2.3           UT
    44        Vermont      625741          1.6           VT
    45       Virginia     8001024          4.1           VA
    46     Washington     6724540          2.5           WA
    47  West Virginia     1852994          4.0           WV
    48      Wisconsin     5686986          2.9           WI
    49        Wyoming      563626          2.7           WY
    

**Code #1 :** Adding Column to the dataframe

 __

 __  
 __

 __

 __  
 __  
 __

# Adding a new column with derived data

 

data['PopulationInMillions'] = data['Population']/1000000

 

# Changed data

print (data.head(5))  
  
---  
  
 __

 __

 **Output :**

    
    
            State  Population  Murder.Rate Abbreviation  PopulationInMillions
    0     Alabama     4779736          5.7           AL              4.779736
    1      Alaska      710231          5.6           AK              0.710231
    2     Arizona     6392017          4.7           AZ              6.392017
    3    Arkansas     2915918          5.6           AR              2.915918
    4  California    37253956          4.4           CA             37.253956
    

**Code #2 :** Data Description

 __

 __  
 __

 __

 __  
 __  
 __

data.describe()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-content/uploads/describe-1.jpg)

 **Code #3 :** Data Info

 __

 __  
 __

 __

 __  
 __  
 __

data.info()  
  
---  
  
 __

 __

 **Output :**

    
    
    
    RangeIndex: 50 entries, 0 to 49
    Data columns (total 4 columns):
    State           50 non-null object
    Population      50 non-null int64
    Murder.Rate     50 non-null float64
    Abbreviation    50 non-null object
    dtypes: float64(1), int64(1), object(2)
    memory usage: 1.6+ KB
    

**Code #4 :** Renaming a column heading

 __

 __  
 __

 __

 __  
 __  
 __

# Rename column heading as it

# has '.' in it which will create

# problems when dealing functions 

 

data.rename(columns ={'Murder.Rate': 'MurderRate'}, inplace =
True)

 

# Lets check the column headings

list(data)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    ['State', 'Population', 'MurderRate', 'Abbreviation']
    

**Code #5 :** Calculating Mean

 __

 __  
 __

 __

 __  
 __  
 __

Population_mean= data.Population.mean()

print ("Population Mean : ", Population_mean)

 

MurderRate_mean = data.MurderRate.mean()

print ("\nMurderRate Mean : ", MurderRate_mean)  
  
---  
  
 __

 __

 **Output:**

    
    
    Population Mean :  6162876.3
    
    MurderRate Mean :  4.066
    

**Code #6 :** Trimmed mean

 __

 __  
 __

 __

 __  
 __  
 __

# Mean after discarding top and

# bottom 10 % values eliminating outliers

 

population_TM = trim_mean(data.Population, 0.1)

print ("Population trimmed mean: ", population_TM)

 

murder_TM = trim_mean(data.MurderRate, 0.1)

print ("\nMurderRate trimmed mean: ", murder_TM)  
  
---  
  
 __

 __

 **Output :**

    
    
    Population trimmed mean:  4783697.125
    
    MurderRate trimmed mean:  3.9450000000000003
    

**Code #7 :** Weighted Mean

 __

 __  
 __

 __

 __  
 __  
 __

# here murder rate is weighed as per

# the state population

 

murderRate_WM = np.average(data.MurderRate, weights =
data.Population)

print ("Weighted MurderRate Mean: ", murderRate_WM)  
  
---  
  
 __

 __

 **Output :**

    
    
    Weighted MurderRate Mean:  4.445833981123393
    

**Code #8 :** Median

 __

 __  
 __

 __

 __  
 __  
 __

Population_median= data.Population.median()

print ("Population median : ", Population_median)

 

MurderRate_median = data.MurderRate.median()

print ("\nMurderRate median : ", MurderRate_median)  
  
---  
  
 __

 __

 **Output :**

    
    
    Population median :  4436369.5
    
    MurderRate median :  4.0
    

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save


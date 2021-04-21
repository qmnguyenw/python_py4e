Ordinary Least Squares (OLS) using statsmodels



In this article, we will use Python’s **statsmodels** module to implement
**Ordinary Least Squares** ( **OLS** ) method of linear regression.

 **Introduction :**  
A linear regression model establishes the relation between a dependent
variable( **y** ) and at least one independent variable( **x** ) as :  
![\\hat{y}=b_1x+b_0](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-b9b26af2490b00d890be091ce23eb2a2_l3.png)  
In _OLS_ method, we have to choose the values of
![b_1](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
caf66ecd4c1afbf56d7c015aff25a46b_l3.png) and
![b_0](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-039528dcbf64af7068be4cacdfe8dd55_l3.png) such that, the
total sum of squares of the difference between the calculated and observed
values of y, is minimised.  
 **Formula for OLS:**

![S=\\sum\\limits_{i=1}^n \(y_i - \\hat{y_i}\)^2 = \\sum\\limits_{i=1}^n \(y_i
- b_1x_1 - b_0\)^2 = \\sum\\limits_{i=1}^n \(\\hat{\\epsilon_i}\)^2 =
min](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-91969e7103ae5b6d917dbd49cdcf0748_l3.png)

Where,  
![\\hat{y_i}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e32e4b496584af60f4616ca88a89278b_l3.png) = predicted
value for the ith observation  
![y_i](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
aa4072aa7d68e86ba6302fb6c7240c2d_l3.png) = actual value for the ith
observation  
![\\epsilon_i](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-1ee7c22bede07d01e1496da128e11783_l3.png) = error/residual
for the ith observation  
n = total number of observations

To get the values of ![b_0](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-039528dcbf64af7068be4cacdfe8dd55_l3.png) and
![b_1](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
caf66ecd4c1afbf56d7c015aff25a46b_l3.png) which minimise S, we can take a
partial derivative for each coefficient and equate it to zero.

  

  

 **Modules used :**

  *  **statsmodels :** provides classes and functions for the estimation of many different statistical models.
    
        pip install statsmodels

  *  **pandas :** library used for data manipulation and analysis.
    
        pip install pandas

  *  **NumPy :** core library for array computing.
    
        pip install numpy

  *  **Matplotlib :** a comprehensive library used for creating static and interactive graphs and visualisations.
    
        pip install matplotlib

 **Approach :**

  * First we define the variables **x** and **y**. In the example below, the variables are read from a _csv_ file using _pandas_. The file used in the example can be downloaded here.
  * Next, We need to add the constant ![b_0](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-039528dcbf64af7068be4cacdfe8dd55_l3.png) to the equation using the **add_constant()** method.
  * The **OLS()** function of the **statsmodels.api** module is used to perform OLS regression. It returns an OLS object. Then **fit()** method is called on this object for fitting the regression line to the data.
  * The **summary()** method is used to obtain a table which gives an extensive description about the regression results

>  **Syntax :** statsmodels.api.OLS(y, x)  
>  **Parameters :**
>
>   *  **y :** the variable which is dependent on x
>   *  **x :** the independent variable
>

 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

import statsmodels.api as sm

import pandas as pd

 

# reading data from the csv

data = pd.read_csv('train.csv')

 

# defining the variables

x = data['x'].tolist()

y = data['y'].tolist()

 

# adding the constant term

x = sm.add_constant(x)

 

# performing the regression

# and fitting the model

result = sm.OLS(y, x).fit()

 

# printing the summary table

print(result.summary())  
  
---  
  
 __

 __

 **Output :**

    
    
                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                      y   R-squared:                       0.989
    Model:                            OLS   Adj. R-squared:                  0.989
    Method:                 Least Squares   F-statistic:                 2.709e+04
    Date:                Fri, 26 Jun 2020   Prob (F-statistic):          1.33e-294
    Time:                        15:55:38   Log-Likelihood:                -757.98
    No. Observations:                 300   AIC:                             1520.
    Df Residuals:                     298   BIC:                             1527.
    Df Model:                           1                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const         -0.4618      0.360     -1.284      0.200      -1.169       0.246
    x1             1.0143      0.006    164.598      0.000       1.002       1.026
    ==============================================================================
    Omnibus:                        1.034   Durbin-Watson:                   2.006
    Prob(Omnibus):                  0.596   Jarque-Bera (JB):                0.825
    Skew:                           0.117   Prob(JB):                        0.662
    Kurtosis:                       3.104   Cond. No.                         120.
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    
    

Description of some of the terms in the table :

  *  **R-squared :** the coefficient of determination. It is the proportion of the variance in the dependent variable that is predictable/explained
  *  **Adj. R-squared :** Adjusted R-squared is the modified form of R-squared adjusted for the number of independent variables in the model. Value of adj. R-squared increases, when we include extra variables which actually improve the model.
  *  **F-statistic :** the ratio of mean squared error of the model to the mean squared error of residuals. It determines the overall significance of the model.
  *  **coef :** the coefficients of the independent variables and the constant term in the equation.
  *  **t :** the value of t-statistic. It is the ratio of the difference between the estimated and hypothesised value of a parameter, to the standard error

 **Predicting values:**  
From the results table, we note the coefficient of x and the constant term.
These values are substituted in the original equation and the regression line
is plotted using _matplotlib_.  
 **Code:**

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

 

# reading data from the csv

data = pd.read_csv('train.csv')

 

# plotting the original values

x = data['x'].tolist()

y = data['y'].tolist()

plt.scatter(x, y)

 

# finding the maximum and minimum

# values of x, to get the

# range of data

max_x = data['x'].max()

min_x = data['x'].min()

 

# range of values for plotting

# the regression line

x = np.arange(min_x, max_x, 1)

 

# the substituted equation

y = 1.0143 * x - 0.4618

 

# plotting the regression line

plt.plot(y, 'r')

plt.show()  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200626160821/Screenshot-2020-06-26-at-3.56.22-PM.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


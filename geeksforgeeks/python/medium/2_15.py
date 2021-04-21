Polynomial Regression using Turicreate



In this article, we will discuss the implementation of Polynomial Regression
using Turicreate. **Polynomial Regression:** Polynomial regression is a form
of regression analysis that models the relationship between a dependent say
**y** and an independent variable say **x** as a **nth** degree polynomial. It
is expressed as :

> y= b0+b1x1+ b2x12+ b2x13+…… bnx1n
>
> [where b0, b1, b2, …… bn are regression coefficients]

So let’s learn this concept through practicals.

 **Step 1:** Import the important libraries and generate a very small data set
using SArray and SFrame in turicreate that we are going to use to perform
Polynomial Regression.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing required python libraries

import turicreate

import matplotlib.pyplot as plt

import random

 

# Generating datapoints

X = [data for data in range(1, 21)]

Y = [random.randrange(100, 1000, 1) for data in
range(20)]

 

# Creating Sarrays from the generated data points

Xs = turicreate.SArray(X, dtype=float)

Ys = turicreate.SArray(Y, dtype=float)

 

print(f"""Xs : {Xs}

\n-------------------------------------------------------------------------------------------\n

Ys : {Ys}""")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210118190700/Screenshotfrom202101091245241-660x92.png)

 **Step 2:** Plotting the generated data

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# plotting the generated data

plt.scatter(Xs, Ys)

plt.show()  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210118190701/Screenshotfrom202101091245421.png)

 **Step 3:** Create an SFrame containing the input, its polynomial_degrees,
and the output in order to fit our regression model.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Creating an Sframe where all the inputs and the polynomial degree and
output

def createSframe(inputs, pol_degree):

 datapoints = turicreate.SFrame({'x1': inputs})

 for degree in range(2, pol_degree+1):

 datapoints[f'x{degree}'] =
datapoints[f'x{degree-1}']*datapoints['x1']

 return datapoints

 

 

# Creating a SFrame with polynomial degree 20

data_points = createSframe(Xs, 20)

data_points['y'] = Ys

 

# showing the first 10 entries in the SFrame

data_points.head()  
  
---  
  
 __

 __


Implementation of Locally Weighted Linear Regression



LOESS or LOWESS are non-parametric regression methods that combine multiple
regression models in a k-nearest-neighbor-based meta-model. LOESS combines
much of the simplicity of linear least squares regression with the flexibility
of nonlinear regression. It does this by fitting simple models to localized
subsets of the data to build up a function that describes the variation in the
data, point by point.

  * This algorithm is used for making predictions when there exists a non-linear relationship between the features.
  * Locally weighted linear regression is a supervised learning algorithm.
  * It a non-parametric algorithm.
  * doneThere exists No training phase. All the work is done during the testing phase/while making predictions.

Suppose we want to evaluate the hypothesis function h at a certan query
point x. For linear regression we would do the following:

![Fit $\\theta$ to minimize $\\sum_{i=1}^{m}\\left\(y^{\(i\)}-\\theta^{T}
x^{\(i\)}\\right\)^{2}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-fb425eac6521f691b34c962b44950d8d_l3.png)  
  
![Output $\\theta^{T} x$](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-300637b5124c5b09a36ce17479c8a5f0_l3.png)

For locally weighted linear regression we will instead do the following:  
![Fit $\\theta$ to minimize $\\sum_{i=1}^{m} w^{\(i\)}\\left\(^{\(i\)}
y-\\theta^{T} x^{\(i\)}\\right\)^{2}$](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-567282b2a5d429e7b2b3ed8cbd20b394_l3.png)  
  
![Output $\\theta^{T} x$](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-300637b5124c5b09a36ce17479c8a5f0_l3.png)  
  
where w(i) is a is a non-negative “weight” associated with training point
x(i). A higher “preference” is given to the points in the training set lying
in the vicinity of x than the points lying far away from x. so For x(i)
lying closer to the query point x, the value of w(i) is large, while for
x(i) lying far away from x the value of w(i) is small.  
w(i) can be chosen as –  
![$w^{\(i\)}=\\exp
\\left\(-\\frac{\\left\(x^{\(i\)}-x\\right\)^{T}\\left\(x^{\(i\)}-x\\right\)}{2
\\tau^{2}}\\right\)$](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-dac49496d69e3d320c5bc91aeff38a95_l3.png)

Directly using **closed Form solution** to find parameters-  
![$\\theta=\\left\(X^{\\top} W X\\right\)^{-1}\\left\(X^{\\top} W
Y\\right\)$](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-32d70fdc5ccb8bea9ecd8a542b06aa5d_l3.png)

  

  

 **Code: Importing Libraries :**

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

 

plt.style.use("seaborn")  
  
---  
  
 __

 __

 **Code: Loading Data :**

 __

 __  
 __

 __

 __  
 __  
 __

# Loading CSV files from local storage

dfx = pd.read_csv('weightedX_LOWES.csv')

dfy = pd.read_csv('weightedY_LOWES.csv')

# Getting data from DataFrame Object and storing in numpy n-dim arrays

X = dfx.values

Y = dfy.values  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200820060319/Screenshot-2020-08-20-at-10.32.57-AM.png)

 **Code: Function to calculate weight matrix :**

 __

 __  
 __

 __

 __  
 __  
 __

# function to calculate W weight diagnal Matric used in calculation of
predictions

def get_WeightMatrix_for_LOWES(query_point, Training_examples, Bandwidth):

 # M is the No of training examples

 M = Training_examples.shape[0]

 # Initialising W with identity matrix

 W = np.mat(np.eye(M))

 # calculating weights for query points

 for i in range(M):

 xi = Training_examples[i]

 denominator = (-2 * Bandwidth * Bandwidth)

 W[i, i] = np.exp(np.dot((xi-query_point),
(xi-query_point).T)/denominator)

 return W  
  
---  
  
 __

 __

 **Code: Making Predictions:**

 __

 __  
 __

 __

 __  
 __  
 __

# function to make predictions

def predict(training_examples, Y, query_x, Bandwidth):

 M = Training_examples.shape[0]

 all_ones = np.ones((M, 1))

 X_ = np.hstack((training_examples, all_ones))

 qx = np.mat([query_x, 1])

 W = get_WeightMatrix_for_LOWES(qx, X_, Bandwidth)

 # calculating parameter theta

 theta = np.linalg.pinv(X_.T*(W * X_))*(X_.T*(W *
Y))

 # calculating predictions

 pred = np.dot(qx, theta)

 return theta, pred  
  
---  
  
 __

 __

 **Code: Visualise Predictions :**


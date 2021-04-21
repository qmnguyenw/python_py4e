Python | Mean Squared Error



The **Mean Squared Error (MSE)** or **Mean Squared Deviation (MSD)** of an
estimator measures the average of error squares i.e. the average squared
difference between the estimated values and true value. It is a risk function,
corresponding to the expected value of the squared error loss. It is always
non – negative and values close to zero are better. The MSE is the second
moment of the error (about the origin) and thus incorporates both the variance
of the estimator and its bias.

 **Steps to find the MSE**

  1. Find the equation for the regression line.

(1)  ![   \\begin{equation*}   \\hat{Y}_i = \\hat{\\beta}_0 + \\hat{\\beta}_1
X_i + \\hat{\\epsilon}_i   \\end{equation*}
](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
ef48678c5cb7c706d0c5b8beeea8b8c3_l3.png)

  2. Insert X values in the equation found in step 1 in order to get the respective Y values i.e.

(2)  ![ \\begin{equation*} \\hat{Y}_i \\end{equation*}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7c512e91ed0686588eb1ffcef1cadb00_l3.png)

  3. Now subtract the new Y values (i.e. ![\\hat{Y}_i](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-d6fb1b6d20012809fdad1be52f21b7a5_l3.png)) from the original Y values. Thus, found values are the error terms. It is also known as the vertical distance of the given point from the regression line.

(3)  ![  \\begin{equation*}  Y_i - \\hat{Y}_i  \\end{equation*}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-28ad36c09ea07ddf258981e63865ed1d_l3.png)

  

  

  4. Square the errors found in step 3.

(4)  ![  \\begin{equation*}  {\(Y_i - \\hat{Y}_i\)}^2  \\end{equation*}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-14e259369a501e0294c6c900dc495dd1_l3.png)

  5. Sum up all the squares.

(5)  ![  \\begin{equation*}  \\sum_{i=1}^{N}\(Y_i - \\hat{Y}_i\)^2
\\end{equation*} ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-fa4cd4f32b9f48f1b1cd431a69bae976_l3.png)

  6. Divide the value found in step 5 by the total number of observations.

(6)  ![  \\begin{equation*}  MSE = \\frac{1}{N}\\sum_{i=1}^{N}\(Y_i -
\\hat{Y}_i\)^2  \\end{equation*} ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-50d568506216f6ab6402504298c570e2_l3.png)

**Example:**  
Consider the given data points: (1,1), (2,1), (3,2), (4,2), (5,4)  
You can use this online calculator to find the regression equation / line.

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190616084931/1376-300x300.png)

 **Regression line equation: Y = 0.7X – 0.1** X| Y|
![\\hat{Y}_i](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d6fb1b6d20012809fdad1be52f21b7a5_l3.png)| 1| 1| 0.6| 2|
1| 1.29| 3| 2| 1.99| 4| 2| 2.69| 5| 4| 3.4  
---|---|---  
  
Now, using formula found for **MSE** in step 6 above, we can get **MSE =
0.21606**

 **MSE using scikit – learn:**

 __

 __  
 __

 __

 __  
 __  
 __

from sklearn.metrics import mean_squared_error

 

# Given values

Y_true = [1,1,2,2,4] # Y_true = Y (original
values)

 

# calculated values

Y_pred = [0.6,1.29,1.99,2.69,3.4] # Y_pred = Y'

 

# Calculation of Mean Squared Error (MSE)

mean_squared_error(Y_true,Y_pred)  
  
---  
  
 __

 __

    
    
    **Output:** 0.21606

 **MSE using Numpy module:**

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

 

# Given values

Y_true = [1,1,2,2,4] # Y_true = Y (original
values)

 

# Calculated values

Y_pred = [0.6,1.29,1.99,2.69,3.4] # Y_pred = Y'

 

# Mean Squared Error

MSE = np.square(np.subtract(Y_true,Y_pred)).mean()  
  
---  
  
 __

 __

    
    
     **Output:** 0.21606

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


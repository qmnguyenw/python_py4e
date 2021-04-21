ML | Boston Housing Kaggle Challenge with Linear Regression



 **Boston Housing Data:** This dataset was taken from the StatLib library and
is maintained by Carnegie Mellon University. This dataset concerns the housing
prices in housing city of Boston. The dataset provided has 506 instances with
13 features.

The Description of dataset is taken from  
![](https://media.geeksforgeeks.org/wp-content/uploads/Untitled-
drawing-1-11.png)

Let’s make the Linear Regression Model, predicting housing prices

Inputing Libraries and dataset.

 __

 __  
 __

 __

 __  
 __  
 __

# Importing Libraries

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

 

# Importing Data

from sklearn.datasets import load_boston

boston = load_boston()  
  
---  
  
 __

 __

Shape of input Boston data and getting feature_names

  

  

 __

 __  
 __

 __

 __  
 __  
 __

boston.data.shape  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/boston1.png)

 __

 __  
 __

 __

 __  
 __  
 __

boston.feature_names  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/boston2.png)  

Converting data from nd-array to dataframe and adding feature names to the
data

 __

 __  
 __

 __

 __  
 __  
 __

data= pd.DataFrame(boston.data)

data.columns = boston.feature_names

 

data.head(10)  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/boston3.png)  
  
Adding ‘Price’ column to the dataset

 __

 __  
 __

 __

 __  
 __  
 __

# Adding 'Price' (target) column to the data

boston.target.shape  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/boston4.png)

 __

 __  
 __

 __

 __  
 __  
 __

data['Price'] = boston.target

data.head()  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/boston5.png)  

Description of Boston dataset

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

![](https://media.geeksforgeeks.org/wp-content/uploads/boston6.png)  
  
Info of Boston Dataset

  

  

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

![](https://media.geeksforgeeks.org/wp-content/uploads/boston7.png)  
  
Getting input and output data and further splitting data to training and
testing dataset.

 __

 __  
 __

 __

 __  
 __  
 __

# Input Data

x = boston.data

 

# Output Data

y = boston.target

 

 

# splitting data to training and testing dataset. 

from sklearn.cross_validation import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size
=0.2,

 random_state = 0)

 

print("xtrain shape : ", xtrain.shape)

print("xtest shape : ", xtest.shape)

print("ytrain shape : ", ytrain.shape)

print("ytest shape : ", ytest.shape)  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/boston9.png)  
  
Applying Linear Regression Model to the dataset and predicting the prices.

 __

 __  
 __

 __

 __  
 __  
 __

# Fitting Multi Linear regression model to training model

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(xtrain, ytrain)

 

# predicting the test set results

y_pred = regressor.predict(xtest)  
  
---  
  
 __

 __

Plotting Scatter graph to show the prediction results – ‘ytrue’ value vs
‘y_pred’ value

 __

 __  
 __

 __

 __  
 __  
 __

# Plotting Scatter graph to show the prediction

# results - 'ytrue' value vs 'y_pred' value

plt.scatter(ytest, y_pred, c = 'green')

plt.xlabel("Price: in $1000's")

plt.ylabel("Predicted value")

plt.title("True value vs predicted value : Linear Regression")

plt.show()  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/boston10.png)  
Results of Linear Regression i.e. Mean Squred Error.

 __

 __  
 __

 __

 __  
 __  
 __

# Results of Linear Regression.

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(ytest, y_pred)

print("Mean Square Error : ", mse)  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/boston11.png)  
![](https://media.geeksforgeeks.org/wp-content/uploads/2-70.jpg)

As per the result our model is only 66.55% accurate. So, the prepared model is
not very good for predicting the housing prices. One can improve the
prediction results using many other possible machine learning algorithms and
techniques.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save


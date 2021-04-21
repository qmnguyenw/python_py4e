Heart Disease Prediction using ANN



Deep Learning is a technology of which mimics a human brain in the sense that
it consists of multiple neurons with multiple layers like a human brain. The
network so formed consists of an input layer, an output layer, and one or more
hidden layers. The network tries to learn from the data that is fed into it
and then performs predictions accordingly. The most basic type of neural
network is the ANN (Artificial Neural Network). The ANN does not have any
special structure, it just comprises of multiple neural layers to be used for
prediction.  
Let’s build a model that predicts whether a person has heart disease or not by
using ANN.

 **About the data:**  
In the dataset, we have _13_ columns in which we are given different
attributes such as sex, age, cholesterol level, etc. and we are given a target
column which tells us whether that person has heart disease or not. We will
keep all the columns as independent variables other than the target column
because it will be our dependent variable. We will build an ANN which will
predict whether a person has heart disease or not given other attributes of
the person.

You can find the dataset here heart disease dataset

 **Code: Importing Libraries**

 __

 __  
 __

 __

 __  
 __  
 __

import tensorflow as tf

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import keras

from keras.models import Sequential

from keras.layers import Dense

from sklearn.metrics import confusion_matrix  
  
---  
  
 __

 __

 **Code: Importing Dataset**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

data= pd.read_csv('heart.csv')

data.head()  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200323095532/heart1.png)

 **Data Description:**

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

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200323101546/g214.png)

 **Code: Check for null values**

 __

 __  
 __

 __

 __  
 __  
 __

data.isnull().any()  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200318172844/ANN21.png)  
 **Assign Dependent and Independent variable**

 __

 __  
 __

 __

 __  
 __  
 __

X= data.iloc[:,:13].values

y = data["target"].values  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200323101701/g141.png)

 **Code : Split data into Train and Test dataset**

 __

 __  
 __

 __

 __  
 __  
 __

X_train,X_test,y_train, y_test= train_test_split(X,y,test_size = 0.3
, random_state = 0 )  
  
---  
  
 __

 __

 **Code: Scale the data.**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(X_train)

X_test = sc.transform(X_test)  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/20200323102352/g41.png)  
 **Code: Building the Model**

 __

 __  
 __

 __

 __  
 __  
 __

classifier= Sequential()

classifier.add(Dense(activation = "relu", input_dim = 13, 

 units = 8, kernel_initializer = "uniform"))

classifier.add(Dense(activation = "relu", units = 14, 

 kernel_initializer = "uniform"))

classifier.add(Dense(activation = "sigmoid", units = 1, 

 kernel_initializer = "uniform"))

classifier.compile(optimizer = 'adam' , loss =
'binary_crossentropy', 

 metrics = ['accuracy'] )  
  
---  
  
 __

 __

 **Code : Fitting the Model**

 __

 __  
 __

 __

 __  
 __  
 __

classifier.fit(X_train , y_train , batch_size= 8 ,epochs = 100 )  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-content/uploads/20200323102512/g61.png)  
 **Code : Performing prediction and rescaling**

 __

 __  
 __

 __

 __  
 __  
 __

y_pred= classifier.predict(X_test)

y_pred = (y_pred > 0.5)  
  
---  
  
 __

 __

 **Code: Confusion Matrix**

 __

 __  
 __

 __

 __  
 __  
 __

cm= confusion_matrix(y_test,y_pred)

cm  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200323102100/g310.png)

 **Code: Accuracy**

 __

 __  
 __

 __

 __  
 __  
 __

accuracy= (cm[0][0]+cm[1][1])/(cm[0][1]
+ cm[1][0] +cm[0][0] +cm[1][1])

print(accuracy*100)  
  
---  
  
 __

 __

![](https://media.geeksforgeeks.org/wp-
content/uploads/20200318173807/ANN31.png)  
We will get accuracy approximately around 85%.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save


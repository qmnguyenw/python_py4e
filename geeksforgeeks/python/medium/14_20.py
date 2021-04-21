Python | CAP – Cumulative Accuracy Profile analysis



CAP popularly called the ‘Cumulative Accuracy Profile’ is used in the
performance evaluation of the classification model. It helps us to understand
and conclude about the robustness of the classification model. In order to
visualize this, three distinct curves are plotted in our plot:

  1. A random plot
  2. A plot obtained by using a SVM classifier or a random forest classifier
  3. A perfect plot( an ideal line)

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190802081422/gee11.png)

We are working the DATA to understand the concept.

 **Code : Loading dataset.**

 __

 __  
 __

 __

 __  
 __  
 __

# importing libraries

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

import numpy as np

 

# loading dataset

data =
pd.read_csv('C:\\Users\\DELL\\Desktop\\Social_Network_Ads.csv')

 

print ("Data Head : \n\n", data.head())  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    Data Head : 
    
         User ID  Gender  Age  EstimatedSalary  Purchased
    0  15624510    Male   19            19000          0
    1  15810944    Male   35            20000          0
    2  15668575  Female   26            43000          0
    3  15603246  Female   27            57000          0
    4  15804002    Male   19            76000          0
    

**Code : Data Input Output.**

 __

 __  
 __

 __

 __  
 __  
 __

# Input and Output

x = data.iloc[:, 2:4]

y = data.iloc[:, 4]

 

print ("Input : \n", x.iloc[0:10, :])  
  
---  
  
 __

 __

 **Output :**

    
    
    Input : 
        Age  EstimatedSalary
    0   19            19000
    1   35            20000
    2   26            43000
    3   27            57000
    4   19            76000
    5   27            58000
    6   27            84000
    7   32           150000
    8   25            33000
    9   35            65000
    

**Code : Splitting dataset for training and testing.**

 __

 __  
 __

 __

 __  
 __  
 __

# splitting data

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(

 x, y, test_size = 0.3, random_state = 0)  
  
---  
  
 __

 __

 **Code : Random Forest Classifier**

 __

 __  
 __

 __

 __  
 __  
 __

# classifier

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators = 400)

 

# training

classifier.fit(x_train, y_train)

 

# predicting

pred = classifier.predict(x_test)  
  
---  
  
 __

 __

 **Code : Finding the classifier accuracy.**

 __

 __  
 __

 __

 __  
 __  
 __

# Model Performance

from sklearn.metrics import accuracy_score

print("Accuracy : ", accuracy_score(y_test, pred) * 100)  
  
---  
  
 __

 __

 **Output :**

    
    
    Accuracy :  91.66666666666666

###  **Random Model**

The random plot is made under the assumption that we have plotted the total
number of points ranging from 0 to the total number of data points in the
dataset. The y-axis has been kept as the total number of points for which the
dependent variable from our dataset has the outcome as 1. The random plot can
be understood like a linearly increasing relationship. An example is a model
that predicts whether a product is bought (positive outcome) by each
individual from a group of people (classifying parameter) based on factors
such as their gender, age, income etc. If group members would be contacted at
random, the cumulative number of products sold would rise linearly toward a
maximum value corresponding to the total number of buyers within the group.
This distribution is called the **“random” CAP**.  
 **  
Code : Random Model**

 __

 __  
 __

 __

 __  
 __  
 __

# code for the random plot

import matplotlib.pyplot as plt

import numpy as np

 

# length of the test data

total = len(y_test)

 

# Counting '1' labels in test data

one_count = np.sum(y_test)

 

# counting '0' lables in test data 

zero_count = total - one_count

 

plt.figure(figsize = (10, 6))

 

# x-axis ranges from 0 to total people contacted 

# y-axis ranges from 0 to the total positive outcomes.

 

plt.plot([0, total], [0, one_count], c = 'b', 

 linestyle = '--', label = 'Random Model')

plt.legend()  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190803103400/Untitled156.png)

  

  

###  **Random Forest Classifier Line**

 **Code :** Random forest classification algorithm is applied to the dataset
for the **random classifier line plot**.

 __

 __  
 __

 __

 __  
 __  
 __

lm= [y for _, y in sorted(zip(pred, y_test), reverse =
True)]

x = np.arange(0, total + 1)

y = np.append([0], np.cumsum(lm))

plt.plot(x, y, c = 'b', label = 'Random classifier', linewidth
= 2)  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190803110452/Untitled212.png)

 **Explanation:** pred is the prediction made by the random classifier. We
**zip** the prediction and test values and sort it in the reverse order so
that higher values come first and then the lower values. We extract only the
**y_test** values in an array and store it in **lm**. **np.cumsum()** creates
an array of values while cumulatively adding all previous values in the array
to the present value.The x-values will be ranging from 0 to the total + 1. We
add one to the total cause **arange()** does not include one to the array and
we want the x axis to range from 0 to the total.

###  **Perfect Model**

We then plot the perfect plot(or the ideal line). A perfect prediction
determines exactly which group members will buy the product, such that the
maximum number of products sold will be reached with a minimum number of
calls. This produces a steep line on the CAP curve that stays flat once the
maximum is reached (contacting all other group members will not lead to more
products sold), which is the **“perfect” CAP**.

 __

 __  
 __

 __

 __  
 __  
 __

plt.plot([0, one_count, total], [0, one_count, one_count],

 c = 'grey', linewidth = 2, label = 'Perfect Model')  
  
---  
  
 __

 __

 **Output :**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190803110305/Untitled310.png)


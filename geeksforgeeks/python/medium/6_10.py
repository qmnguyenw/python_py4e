ML – Decision Function



Decision function is a method present in classifier{ SVC, Logistic Regression
} class of sklearn machine learning framework. This method basically returns a
Numpy array, In which each element represents whether a predicted sample for
x_test by the classifier lies to the right or left side of the Hyperplane and
also how far from the HyperPlane.

It also tells us that how confidently each value predicted for x_test by the
classifier is Positive ( large-magnitude Positive value ) or Negative ( large-
magnitude Negative value).

 **Math behind the Decision Function method:**  
Let’s consider the SVM for linearly-separable binary class classification
problem:

 **Cost Function:**  
  
![ \\left.\\min _{\\theta} C \\sum_{i=1}^{m}\\left\[u^{\(0\)}
\\operatorname{cost}_{1}\\left\(\\theta^{T}
x^{\(\\theta\)}\\right\)+\\left\(1-y^{\(0\)}\\right\)
\\operatorname{cost}_{0}\\left\(\\theta^{T}
x^{\(0\)}\\right\)\\right\]+\\frac{1}{2} \\sum_{i=1}^{n}
\\theta\\right\\}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-ca9aec29b74e0010e835e33c2233fcc6_l3.png)

 **Hypothesis for this Linearly Separable Binary class classification:**  
  
![ h_{\\theta}\(x\)=\\theta^{T} x](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-1a106fca3be39a512b85b6fc40938269_l3.png)  
The **optimization Algorithm** minimizes the cost function to find the best
value of the model parameter for the hypothesis such that:  
  
![ \\begin{array}{ll} \\theta^{T} x^{\(i\)} \\geq 1 & \\text { if }
y^{\(i\)}=1 \\\\ \\theta^{T} x^{\(i\)} \\leq-1 & \\text { if } y^{\(i\)}=0
\\end{array}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-0ab06d9ff33ad122d40aa5a593cdb682_l3.png)

  

  

 **What Actually happens when we pass a data instance to Decision Function
method ?**  
This data sample is substituted in this hypothesis whose model parameters have
been found by minimizing the cost function and returns the value outputted by
this hypothesis which would be >1 if actual output is 1 or <-1 if the actual
output is 0. This returned value indeed represents on which side of the
hyperplane and also how far from it the given data sample lie.

 **Code: create our own data set and plot the input.**

 __

 __  
 __

 __

 __  
 __  
 __

# This code may not run on GFG IDE

# As required modules are not available.

 

# Create a simple data set

# Binary-Class Classification.

 

# Import Required Modules.

import matplotlib.pyplot as plt

import numpy as np

 

# Input Feature X.

x = np.array([[2, 1.5], [-2, -1], [-1,
-1], [2, 1],

 [1, 5], [0.5, 0.5], [-2, 0.5]])

 

# Input Feature Y.

y = np.array([0, 0, 1, 1, 1, 1, 0])

 

# Training set Featute x_train.

x_train = np.array([[2, 1.5], [-2, -1], [-1,
-1], [2, 1]])

 

# Training set Target Variable y_train.

y_train = np.array([0, 0, 1, 1])

 

# Test set Featute x_test.

x_test = np.array([[1, 5], [0.5, 0.5], [-2,
0.5]])

 

# Test set Target Variable y_test

y_test = np.array([1, 1, 0])

 

# Plot the obtained data

plt.scatter(x[:, 0], x[:, 1], c = y)

plt.xlabel('Feature 1 --->')

plt.ylabel('Feature 2 --->')

plt.title('Created Data')  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200807193237/download-300x227.png)

 **Code: train our model**

 __

 __  
 __

 __

 __  
 __  
 __

# This code may not run on GFG IDE

# As required modules are not available.

 

# Import SVM Class from sklearn.

from sklearn.svm import SVC

clf = SVC()

 

# Train the model on the training set.

clf.fit(x_train, y_train) 

 

# Predict on Test set

predict = clf.predict(x_test)

print('Predicted Values from Classifier:', predict)

print('Actual Output is:', y_test)

print('Accuracy of the model is:', clf.score(x_test, y_test))  
  
---  
  
 __

 __

 **Output:**

    
    
    Predicted Values from Classifier: [0 1 0]
    Actual Output is: [1 1 0]
    Accuracy of the model is: 0.6666666666666666
    

**Code: decision function method**

 __

 __  
 __

 __

 __  
 __  
 __

# This code may not run on GFG IDE

# As required modules are not available.

 

# Using Decision Function Method Present in svc class

Decision_Function = clf.decision_function(x_test)

print('Output of Decision Function is:', Decision_Function)

print('Prediction for x_test from classifier is:', predict)  
  
---  
  
 __

 __

 **Output:**

    
    
    Output of Decision Function is: [-0.04274893  0.29143233 -0.13001369]
    Prediction for x_test from classifier is: [0 1 0]
    

From the above output, we can conclude that the decision function output
represents whether a predicted sample for x_test by the classifier lies to the
right side or left side of hyperplane and also how far from it. It also tells
us how confidently each value predicted for x_test by the classifier is
Positive ( large-magnitude Positive value ) or Negative ( large-magnitude
Negative value)

 **Code: Decision Boundary**

 __

 __  
 __

 __

 __  
 __  
 __

# This code may not run on GFG IDE

# As required modules are not available.

 

# To Plot the Decision Boundary.

arr1 = np.arange(x[:, 0].min()-1, x[:,
0].max()+1, 0.01)

arr2 = np.arange(x[:, 1].min()-1, x[:,
1].max()+1, 0.01)

 

xx, yy = np.meshgrid(arr1, arr2)

input_array = np.array([xx.ravel(), yy.ravel()]).T

labels = clf.predict(input_array)

 

plt.figure(figsize =(10, 7))

plt.contourf(xx, yy, labels.reshape(xx.shape), alpha = 0.1)

plt.scatter(x_test[:, 0], x_test[:, 1], c = y_test.ravel(), alpha
= 1)

plt.xlabel('Feature 1')

plt.ylabel('Feature 2')

plt.title('Decision Boundary')  
  
---  
  
 __

 __

Let’s Visualize the above conclusion.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200807200608/download-300x217.png)  
The advantage of Decision Function output is to set DECISION THRESHOLD and
predict a new output for x_test, such that we get desired precision or recall
value If our project is precision-oriented or recall-oriented respectively.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save


ML | Cancer cell classification using Scikit-learn



Machine Learning is a sub-field of Artificial Intelligence that gives systems
the ability to learn themselves without being explicitly programmed to do so.
Machine Learning can be used in solving many real world problems.  
Let’s classify cancer cells based on their features, and identifying them if
they are ‘malignant’ or ‘benign’. We will be using scikit-learn for machine
learning problem. Scikit-learn is an open-source machine learning, data mining
and data analysis library for Python programming language.

 **The dataset:**  
Scikit-learn comes with a few small standard datasets that do not require
downloading any file from any external website. The dataset that we will be
using for our machine learning problem is the Breast cancer wisconsin
(diagnostic) dataset. The dataset includes several data about the breast
cancer tumors along with the classifications labels, viz., malignant or
benign. It can be loaded using the following function:

    
    
    load_breast_cancer([return_X_y])

The data set has 569 instances or data of 569 tumors and includes data on 30
attributes or features like the radius, texture, perimeter, area, etc. of a
tumor. We will be using these features to train our model.

 **Installing the necessary modules:**  
For this machine learning project, we will be needing the ‘Scikit-learn’
Python module. If you don’t have it installed in your machine, download and
install it by running the following command in the command prompt:

    
    
    pip install scikit-learn

 **Note:** You can use any IDE for this project, by it is highly recommended
Jupyter notebook for the project. This is because, since Python is an
interpreted language, so, one can take its full advantage by running a few
lines of code and see and understand what’s happening, step by step, instead
of writing the whole script and once and then running it.  
Install it by running the following command in the command prompt:

  

  

    
    
    pip install jupyter

#### Step by step implementation of classification using Scikit-learn:

 **Step #1:** Importing the necessary module and dataset.

We will be needing the ‘Scikit-learn’ module and the Breast cancer wisconsin
(diagnostic) dataset.

 __

 __  
 __

 __

 __  
 __  
 __

# importing the Python module

import sklearn

 

# importing the dataset

from sklearn.datasets import load_breast_cancer  
  
---  
  
 __

 __

  
**Step #2:** Loading the dataset to a variable.

 __

 __  
 __

 __

 __  
 __  
 __

# loading the dataset

data = load_breast_cancer()  
  
---  
  
 __

 __

The important attributes that we must consider from that dataset are ‘target-
names'(the meaning of the labels), ‘target'(the classification labels),
‘feature_names'(the meaning of the features) and ‘data'(the data to learn).

 **Step #3:** Organizing the data and looking at it.  
To get a better understanding of what the dataset contains and how we can use
the data to train our model, let us first organize the data and then see what
it contains by using the print() function.

 __

 __  
 __

 __

 __  
 __  
 __

# Organize our data

label_names = data['target_names']

labels = data['target']

feature_names = data['feature_names']

features = data['data']  
  
---  
  
 __

 __

Then, using the **print()** function, let us examine the data.

 __

 __  
 __

 __

 __  
 __  
 __

# looking at the data

print(label_names)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['malignant' 'benign']

So, we see that each dataset of a tumor is labelled as either ‘malignant’ or
‘benign’.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

print(labels)  
  
---  
  
 __

 __

 **Output:**

    
    
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     1 0 0 0 0 0 0 0 0 1 0 1 1 1 1 1 0 0 1 0 0 1 1 1 1 0 1 0 0 1 1 1 1 0 1 0 0
     1 0 1 0 0 1 1 1 0 0 1 0 0 0 1 1 1 0 1 1 0 0 1 1 1 0 0 1 1 1 1 0 1 1 0 1 1
     1 1 1 1 1 1 0 0 0 1 0 0 1 1 1 0 0 1 0 1 0 0 1 0 0 1 1 0 1 1 0 1 1 1 1 0 1
     1 1 1 1 1 1 1 1 0 1 1 1 1 0 0 1 0 1 1 0 0 1 1 0 0 1 1 1 1 0 1 1 0 0 0 1 0
     1 0 1 1 1 0 1 1 0 0 1 0 0 0 0 1 0 0 0 1 0 1 0 1 1 0 1 0 0 0 0 1 1 0 0 1 1
     1 0 1 1 1 1 1 0 0 1 1 0 1 1 0 0 1 0 1 1 1 1 0 1 1 1 1 1 0 1 0 0 0 0 0 0 0
     0 0 0 0 0 0 0 1 1 1 1 1 1 0 1 0 1 1 0 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1
     1 0 1 1 0 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 0 1 0 1 1 1 1 0 0 0 1 1
     1 1 0 1 0 1 0 1 1 1 0 1 1 1 1 1 1 1 0 0 0 1 1 1 1 1 1 1 1 1 1 1 0 0 1 0 0
     0 1 0 0 1 1 1 1 1 0 1 1 1 1 1 0 1 1 1 0 1 1 0 0 1 1 1 1 1 1 0 1 1 1 1 1 1
     1 0 1 1 1 1 1 0 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 0 1 1 1 1 1 0 1 1
     0 1 0 1 1 0 1 0 1 1 1 1 1 1 1 1 0 0 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 0 1
     1 1 1 1 1 1 0 1 0 1 1 0 1 1 1 1 1 0 0 1 0 1 0 1 1 1 1 1 0 1 1 0 1 0 1 0 0
     1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 0 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
     1 1 1 1 1 1 1 0 0 0 0 0 0 1]
    

From here, we see that, each label is linked to binary values of 0 and 1,
where 0 represents malignant tumors and 1 represents benign tumors.

 __

 __  
 __

 __

 __  
 __  
 __

print(feature_names)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['mean radius' 'mean texture' 'mean perimeter' 'mean area'
     'mean smoothness' 'mean compactness' 'mean concavity'
     'mean concave points' 'mean symmetry' 'mean fractal dimension'
     'radius error' 'texture error' 'perimeter error' 'area error'
     'smoothness error' 'compactness error' 'concavity error'
     'concave points error' 'symmetry error' 'fractal dimension error'
     'worst radius' 'worst texture' 'worst perimeter' 'worst area'
     'worst smoothness' 'worst compactness' 'worst concavity'
     'worst concave points' 'worst symmetry' 'worst fractal dimension']
    

Here, we see all the 30 features or attributes that each dataset of the tumor
has. We will be using the numerical values of these features in training our
model and make the correct prediction, whether or not a tumor is malignant or
benign, based on this features.

 __

 __  
 __

 __

 __  
 __  
 __

print(features)  
  
---  
  
 __

 __

 **Output:**

    
    
    [[1.799e+01 1.038e+01 1.228e+02 ... 2.654e-01 4.601e-01 1.189e-01]
     [2.057e+01 1.777e+01 1.329e+02 ... 1.860e-01 2.750e-01 8.902e-02]
     [1.969e+01 2.125e+01 1.300e+02 ... 2.430e-01 3.613e-01 8.758e-02]
     ...
     [1.660e+01 2.808e+01 1.083e+02 ... 1.418e-01 2.218e-01 7.820e-02]
     [2.060e+01 2.933e+01 1.401e+02 ... 2.650e-01 4.087e-01 1.240e-01]
     [7.760e+00 2.454e+01 4.792e+01 ... 0.000e+00 2.871e-01 7.039e-02]]
    

This is a huge dataset containing the numerical values of the 30 attributes of
all the 569 instances of tumor data.

So, from the above data, we can conclude that the first instance of tumor is
malignant and it has a mean radius of value 1.79900000e+01.  
  
**Step #4:** Organizing the data into Sets.

For testing the accuracy of our classifier, we must test the model on unseen
data. So, before building the model, we will split our data into two sets,
viz., training set and test set. We will be using the training set to train
and evaluate the model and then use the trained model to make predictions on
the unseen test set.  
The sklearn modlue has a built-in function called the **train_test_split()** ,
which automatically divides the data into these sets. We will be using this
function two split the data.

 __

 __  
 __

 __

 __  
 __  
 __

# importing the function

from sklearn.model_selection import train_test_split

 

# splitting the data

train, test, train_labels, test_labels = train_test_split(features,
labels,

 test_size = 0.33, random_state = 42)  
  
---  
  
 __

 __

Thetrain_test_split() function randomly splits the data using the parameter
**test_size**. What we have done here is that, we have split 33% of the
original data into test data (test). The remaining data (train) is the
training data. Also, we have respective labels for both the train variables
and test variables, i.e. train_labels and test_labels.

To learn more about how to use the train_test_split() function, you can
refer to the official documentation.  
  
**Step #5:** Building the Model.

There are many machine learning models to choose from. All of them have their
own advantages and disadvantages. For this model, we will be using the Naive
Bayes algorithm that usually performs well in binary classification tasks.
Firstly, import the GaussianNB module and initialize it using the
GaussianNB() function. Then train the model by fitting it to the data in the
dataset using the fit() method.

 __

 __  
 __

 __

 __  
 __  
 __

# importing the module of the machine learning model

from sklearn.naive_bayes import GaussianNB

 

# initializing the classifier

gnb = GaussianNB()

 

# training the classifier

model = gnb.fit(train, train_labels)  
  
---  
  
 __

 __

After the training is complete, we can use the trained model to make
predictions on our test set that we have prepared before. To do that, we will
use the built-inpredict() function which returns an array of prediction
values for data instance in the test set. We will then print our predictions
using the print() function.

 __

 __  
 __

 __

 __  
 __  
 __

# making the predictions

predictions = gnb.predict(test)

 

# printing the predictions

print(predictions)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1 0 0 1 1 0 0 0 1 1 1 0 1 0 1 0 1 1 1 0 1 1 0 1 1 1 1 1 1 0 1 1 1 1 1 1 0
     1 0 1 1 0 1 1 1 1 1 1 1 1 0 0 1 1 1 1 1 0 0 1 1 0 0 1 1 1 0 0 1 1 0 0 1 0
     1 1 1 1 1 1 0 1 1 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 1 0 0 1 0 0 1 1 1 0 1 1 0
     1 1 0 0 0 1 1 1 0 0 1 1 0 1 0 0 1 1 0 0 0 1 1 1 0 1 1 0 0 1 0 1 1 0 1 0 0
     1 1 1 1 1 1 1 0 0 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1 0 1 1 0 1 1 1 1 1 1 0 0
     0 1 1]
    

From the output above, we see that the predict() function returned an array
of 0s and 1s. These values represents the predicted values of the test set for
the tumor class (malignant or benign).  
  
**Step #6:** Evaluating the trained model’s accuracy.

As we have predicted values now, we can evaluate our model’s accuracy by
comparing it with the actual labels of the test set, i.e., comparing
predictions with test_labels. For this purpose, we will be using the built-in
**accuracy_score()** function in the sklearn module.

 __

 __  
 __

 __

 __  
 __  
 __

# importing the accuracy measuring function

from sklearn.metrics import accuracy_score

 

# evaluating the accuracy

print(accuracy_score(test_labels, predictions))  
  
---  
  
 __

 __

 **Output:**

    
    
    0.9414893617021277

So, we find out that this machine learning classifier based on the Naive Bayes
algorithm is 94.15% accurate in predicting whether a tumor is malignant or
benign.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save


Learning Model Building in Scikit-learn : A Python Machine Learning Library



Pre-requisite: Getting started with machine learning  
scikit-learn is an open source Python library that implements a range of
machine learning, pre-processing, cross-validation and visualization
algorithms using a unified interface.

 **Important features of scikit-learn:**

  * Simple and efficient tools for data mining and data analysis. It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means, etc.
  * Accessible to everybody and reusable in various contexts.
  * Built on the top of NumPy, SciPy, and matplotlib.
  * Open source, commercially usable – BSD license.

In this article, we are going to see how we can easily build a machine
learning model using scikit-learn.

 **Installation:**

Scikit-learn requires:

  

  

  * NumPy
  * SciPy as its dependencies.

Before installing scikit-learn, ensure that you have NumPy and SciPy
installed. Once you have a working installation of NumPy and SciPy, the
easiest way to install scikit-learn is using pip:

    
    
    pip install -U scikit-learn

Let us get started with the modeling process now.

 **Step 1: Load a dataset**

A dataset is nothing but a collection of data. A dataset generally has two
main components:

  *  **Features** : (also known as predictors, inputs, or attributes) they are simply the variables of our data. They can be more than one and hence represented by a **feature matrix** (‘X’ is a common notation to represent feature matrix). A list of all the feature names is termed as **feature names**.
  *  **Response** : (also known as the target, label, or output) This is the output variable depending on the feature variables. We generally have a single response column and it is represented by a **response vector** (‘y’ is a common notation to represent response vector). All the possible values taken by a response vector is termed as **target names**.

 **Loading exemplar dataset:** scikit-learn comes loaded with a few example
datasets like the iris and digits datasets for classification and the boston
house prices dataset for regression.  
Given below is an example of how one can load an exemplar dataset:

 __

 __  
 __

 __

 __  
 __  
 __

# load the iris dataset as an example

from sklearn.datasets import load_iris

iris = load_iris()

 

# store the feature matrix (X) and response vector (y)

X = iris.data

y = iris.target

 

# store the feature and target names

feature_names = iris.feature_names

target_names = iris.target_names

 

# printing features and target names of our dataset

print("Feature names:", feature_names)

print("Target names:", target_names)

 

# X and y are numpy arrays

print("\nType of X is:", type(X))

 

# printing first 5 input rows

print("\nFirst 5 rows of X:\n", X[:5])  
  
---  
  
 __

 __

Output:

    
    
    Feature names: ['sepal length (cm)','sepal width (cm)',
                    'petal length (cm)','petal width (cm)']
    Target names: ['setosa' 'versicolor' 'virginica']
    
    Type of X is: 
    
    First 5 rows of X:
     [[ 5.1  3.5  1.4  0.2]
     [ 4.9  3.   1.4  0.2]
     [ 4.7  3.2  1.3  0.2]
     [ 4.6  3.1  1.5  0.2]
     [ 5.   3.6  1.4  0.2]]

 **Loading external dataset:** Now, consider the case when we want to load an
external dataset. For this purpose, we can use **pandas library** for easily
loading and manipulating dataset.

To install pandas, use the following pip command:

  

  

    
    
    pip install pandas
    

In pandas, important data types are:

 **Series** : Series is a one-dimensional labeled array capable of holding any
data type.

 **DataFrame** : It is a 2-dimensional labeled data structure with columns of
potentially different types. You can think of it like a spreadsheet or SQL
table, or a dict of Series objects. It is generally the most commonly used
pandas object.

Note: The CSV file used in example below can be downloaded from here:
weather.csv

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

# reading csv file

data = pd.read_csv('weather.csv')

 

# shape of dataset

print("Shape:", data.shape)

 

# column names

print("\nFeatures:", data.columns)

 

# storing the feature matrix (X) and response vector (y)

X = data[data.columns[:-1]]

y = data[data.columns[-1]]

 

# printing first 5 rows of feature matrix

print("\nFeature matrix:\n", X.head())

 

# printing first 5 values of response vector

print("\nResponse vector:\n", y.head())  
  
---  
  
 __

 __

Output:

    
    
    Shape: (14, 5)
    
    Features: Index([u'Outlook', u'Temperature', u'Humidity', 
                    u'Windy', u'Play'], dtype='object')
    
    Feature matrix:
         Outlook Temperature Humidity  Windy
    0  overcast         hot     high  False
    1  overcast        cool   normal   True
    2  overcast        mild     high   True
    3  overcast         hot   normal  False
    4     rainy        mild     high  False
    
    Response vector:
    0    yes
    1    yes
    2    yes
    3    yes
    4    yes
    Name: Play, dtype: object

 **Step 2: Splitting the dataset**

One important aspect of all machine learning models is to determine their
accuracy. Now, in order to determine their accuracy, one can train the model
using the given dataset and then predict the response values for the same
dataset using that model and hence, find the accuracy of the model.  
But this method has several flaws in it, like:

  * Goal is to estimate likely performance of a model on an **out-of-sample** data.
  * Maximizing training accuracy rewards overly complex models that won’t necessarily generalize our model.
  * Unnecessarily complex models may over-fit the training data.

A better option is to split our data into two parts: first one for training
our machine learning model, and second one for testing our model.  
 **To summarize:**

  * Split the dataset into two pieces: a training set and a testing set.
  * Train the model on the training set.
  * Test the model on the testing set, and evaluate how well our model did.

 **Advantages of train/test split:**

  * Model can be trained and tested on different data than the one used for training.
  * Response values are known for the test dataset, hence predictions can be evaluated
  * Testing accuracy is a better estimate than training accuracy of out-of-sample performance.

Consider the example below:

 __

 __  
 __

 __

 __  
 __  
 __

# load the iris dataset as an example

from sklearn.datasets import load_iris

iris = load_iris()

 

# store the feature matrix (X) and response vector (y)

X = iris.data

y = iris.target

 

# splitting X and y into training and testing sets

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.4, random_state=1)

 

# printing the shapes of the new X objects

print(X_train.shape)

print(X_test.shape)

 

# printing the shapes of the new y objects

print(y_train.shape)

print(y_test.shape)  
  
---  
  
 __

 __

Output:

    
    
    (90L, 4L)
    (60L, 4L)
    (90L,)
    (60L,)

The **train_test_split** function takes several arguments which are explained
below:

  *  **X, y** : These are the feature matrix and response vector which need to be splitted.
  *  **test_size** : It is the ratio of test data to the given data. For example, setting test_size = 0.4 for 150 rows of X produces test data of 150 x 0.4 = 60 rows.
  *  **random_state** : If you use random_state = some_number, then you can guarantee that your split will be always the same. This is useful if you want reproducible results, for example in testing for consistency in the documentation (so that everybody can see the same numbers).

 **Step 3: Training the model**

Now, its time to train some prediction-model using our dataset. Scikit-learn
provides a wide range of machine learning algorithms which have a
unified/consistent interface for fitting, predicting accuracy, etc.

The example given below uses KNN (K nearest neighbors) classifier.

 **Note** : We will not go into the details of how the algorithm works as we
are interested in understanding its implementation only.

Now, consider the example below:

 __

 __  
 __

 __

 __  
 __  
 __

# load the iris dataset as an example

from sklearn.datasets import load_iris

iris = load_iris()

 

# store the feature matrix (X) and response vector (y)

X = iris.data

y = iris.target

 

# splitting X and y into training and testing sets

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.4, random_state=1)

 

# training the model on training set

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train, y_train)

 

# making predictions on the testing set

y_pred = knn.predict(X_test)

 

# comparing actual response values (y_test) with predicted response values
(y_pred)

from sklearn import metrics

print("kNN model accuracy:", metrics.accuracy_score(y_test, y_pred))

 

# making prediction for out of sample data

sample = [[3, 5, 4, 2], [2, 3, 5, 4]]

preds = knn.predict(sample)

pred_species = [iris.target_names[p] for p in preds]

print("Predictions:", pred_species)

 

# saving the model

from sklearn.externals import joblib

joblib.dump(knn, 'iris_knn.pkl')  
  
---  
  
 __

 __

Output:

    
    
    kNN model accuracy: 0.983333333333
    Predictions: ['versicolor', 'virginica']
    

Important points to note from the above code:

  * We create a knn classifier object using:
    
        knn = KNeighborsClassifier(n_neighbors=3)
    

  * The classifier is trained using X_train data. The process is termed as **fitting**. We pass the feature matrix and the corresponding response vector.
    
        knn.fit(X_train, y_train)
    

  * Now, we need to test our classifier on the X_test data. **knn.predict** method is used for this purpose. It returns the predicted response vector, **y_pred**.
    
        y_pred = knn.predict(X_test)
    

  * Now, we are interested in finding the accuracy of our model by comparing **y_test** and **y_pred**. This is done using metrics module’s method **accuracy_score** :
    
        print(metrics.accuracy_score(y_test, y_pred))
    

  * Consider the case when you want your model to make prediction on **out of sample** data. Then, the sample input can simply pe passed in the same way as we pass any feature matrix.
    
        sample = [[3, 5, 4, 2], [2, 3, 5, 4]]
    preds = knn.predict(sample)
    

  * If you are not interested in training your classifier again and again and use the pre-trained classifier, one can save their classifier using **joblib**. All you need to do is:
    
        joblib.dump(knn, 'iris_knn.pkl')
    

  * In case you want to load an already saved classifier, use the following method:
    
        knn = joblib.load('iris_knn.pkl')

As we approach the end of this article, here are some benefits of using
scikit-learn over some other machine learning libraries(like R libraries):

  *  **Consistent interface** to machine learning models
  * Provides many **tuning parameters** but with **sensible defaults**
  * Exceptional **documentation**
  * Rich set of functionality for **companion tasks**.
  *  **Active community** for development and support.

 **References:**

  * http://scikit-learn.org/stable/documentation.html
  * https://github.com/justmarkham/scikit-learn-videos

This article is contributed by Nikhil Kumar. If you like GeeksforGeeks and
would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

![Try out the all-new GeeksforGeeks
Premium!](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210304125233/GFG-Go-Premium.png)

My Personal Notes _arrow_drop_up_

Save


ML | Chi-square Test for feature selection



Feature selection is also known as attribute selection is a process of
_extracting the most relevant features_ from the dataset and then applying
machine learning algorithms for the better performance of the model. A large
number of irrelevant features increases the training time exponentially and
increase the risk of overfitting.

 **Chi-square Test for Feature Extraction:**  
 _Chi-square_ test is used for categorical features in a dataset. We calculate
Chi-square between each feature and the target and select the desired number
of features with best Chi-square scores. It determines if the association
between two categorical variables of the sample would reflect their real
association in the population.  
Chi- square score is given by :  
![](https://media.geeksforgeeks.org/wp-content/uploads/Capture-214.png)  
 **where –**

>  **Observed frequency** = No. of observations of class  
>  **Expected frequency** = No. of expected observations of class if there was
> no relationship between the feature and the target.

Python Implementation of Chi-Square feature selection:

 __

 __  
 __

 __

 __  
 __  
 __

# Load libraries

from sklearn.datasets import load_iris

from sklearn.feature_selection import SelectKBest

from sklearn.feature_selection import chi2

 

# Load iris data

iris_dataset = load_iris()

 

# Create features and target

X = iris_dataset.data

y = iris_dataset.target

 

# Convert to categorical data by converting data to integers

X = X.astype(int)

 

# Two features with highest chi-squared statistics are selected

chi2_features = SelectKBest(chi2, k = 2)

X_kbest_features = chi2_features.fit_transform(X, y)

 

# Reduced features

print('Original feature number:', X.shape[1])

print('Reduced feature number:', X_kbest.shape[1])  
  
---  
  
 __

 __

 **Output:**

    
    
    Original feature number: 4
    Reduced feature number : 2

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save


Stratified K Fold Cross Validation



In machine learning, When we want to train our ML model we split our entire
dataset into training_set and test_set using train_test_split() class
present in sklearn.Then we train our model on training_set and test our
model on test_set. The problems that we are going to face in this method are:

Whenever we change the random_state parameter present in train_test_split(),
We get different accuracy for different random_state and hence we can’t
exactly point out the accuracy for our model.  
The train_test_split() splits the dataset into training_test and
test_set by random sampling.But stratified sampling is performed.

 **What is random sampling and Stratified sampling ?**  
Suppose you want to take a survey and decided to call 1000 people from a
particular state, If you pick either 1000 male completely or 1000 female
completely or 900 female and 100 male (randomly) to ask their opinion on a
particular product.Then based on these 1000 opinion you can’t decide the
opinion of that entire state on your product.This is random sampling.

But in Stratified Sampling, Let the population for that state be 51.3% male
and 48.7% female, Then for choosing 1000 people from that state if you pick
531 male ( 51.3% of 1000 ) and 487 female ( 48.7% for 1000 ) i.e 531 male +
487 female (Total=1000 people) to ask their opinion. Then these groups of
people represent the entire state. This is called as Stratified Sampling.

 **Why random sampling is not prefered in machine learning ?**  
Let’s consider a binary-class classification problem. Let our dataset consists
of 100 samples out of which 80 are negative class { 0 } and 20 are positive
class { 1 }.

  

  

 **Random sampling:**  
If we do random sampling to split the dataset into training_set and test_set
in 8:2 ratio respectively.Then we might get all negative class {0} in
training_set i.e 80 samples in training_test and all 20 positive class {1} in
test_set.Now if we train our model on training_set and test our model on
test_set, Then obviously we will get a bad accuracy score.

 **Stratified Sampling:**  
In stratified sampling, The training_set consists of 64 negative class{0} (
80% 0f 80 ) and 16 positive class {1} ( 80% of 20 ) i.e. 64{0}+16{1}=80
samples in training_set which represents the original dataset in equal
proportion and similarly test_set consists of 16 negative class {0} ( 20% of
80 ) and 4 positive class{1} ( 20% of 20 ) i.e. 16{0}+4{1}=20 samples in
test_set which also represents the entire dataset in equal proportion.This
type of train-test-split results in good accuracy.

 **What is the solution for mentioned problems?**  
The solution for the first problem where we were able to get different
accuracy score for different random_state parameter value is to use K-Fold
Cross-Validation. But K-Fold Cross Validation also suffer from second problem
i.e. random sampling.

The solution for both first and second problem is to use Stratified K-Fold
Cross-Validation.

 **What is Stratified K-Fold Cross Validation?**  
Stratified k-fold cross-validation is same as just k-fold cross-validation,
But in Stratified k-fold cross-validation, it does stratified sampling instead
of random sampling.

 **Code: Python code implementation of Stratified K-Fold Cross Validation**

 __

 __  
 __

 __

 __  
 __  
 __

# This code may not be run on GFG IDE

# as required packages are not found. 

 

# STRATIFIES K-FOLD CROSS VALIDATION { 10-fold }

 

# Import Required Modules.

from statistics import mean, stdev

from sklearn import preprocessing

from sklearn.model_selection import StratifiedKFold

from sklearn import linear_model

from sklearn import datasets

 

# FEATCHING FEATURES AND TARGET VARIABLES IN ARRAY FORMAT.

cancer = datasets.load_breast_cancer()

# Input_x_Features.

x = cancer.data 

 

# Input_ y_Target_Variable.

y = cancer.target 

 

 

# Feature Scaling for input features.

scaler = preprocessing.MinMaxScaler()

x_scaled = scaler.fit_transform(x)

 

# Create classifier object.

lr = linear_model.LogisticRegression()

 

# Create StratifiedKFold object.

skf = StratifiedKFold(n_splits=10, shuffle=True,
random_state=1)

lst_accu_stratified = []

 

for train_index, test_index in skf.split(x, y):

 x_train_fold, x_test_fold = x_scaled[train_index],
x_scaled[test_index]

 y_train_fold, y_test_fold = y[train_index], y[test_index]

 lr.fit(x_train_fold, y_train_fold)

 lst_accu_stratified.append(lr.score(x_test_fold, y_test_fold))

 

# Print the output.

print('List of possible accuracy:', lst_accu_stratified)

print('\nMaximum Accuracy That can be obtained from this model is:',

 max(lst_accu_stratified)*100, '%')

print('\nMinimum Accuracy:',

 min(lst_accu_stratified)*100, '%')

print('\nOverall Accuracy:',

 mean(lst_accu_stratified)*100, '%')

print('\nStandard Deviation is:', stdev(lst_accu_stratified))  
  
---  
  
 __

 __

 **Output:**

    
    
    List of possible accuracy: [0.9298245614035088, 0.9649122807017544, 0.9824561403508771, 1.0, 0.9649122807017544, 0.9649122807017544, 0.9824561403508771, 0.9473684210526315, 0.9473684210526315, 0.9821428571428571]
    
    Maximum Accuracy That can be obtained from this model is: 100.0 %
    
    Minimum Accuracy That can be obtained from this model is: 92.98245614035088 %
    
    The overall Accuracy of this model is: 96.66353383458647 %
    
    The Standard Deviation is: 0.02097789213195869

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save


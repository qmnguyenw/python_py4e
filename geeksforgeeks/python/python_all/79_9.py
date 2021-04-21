Python – Random Sample Training and Test Data from dictionary



Sometimes, while working with Machine Learning Algorithm, we can have problem
in which we need to differentiate the training and testing data randomly. This
is very common problem and solution to it is desirable for Machine Learning
domains. This article discusses approach to solve this without using external
libraries.

 **Method : Usingkeys() + random.randint() \+ computations**  
This problem can be solved by using combination of above functions. In this,
we perform the task of extraction of random keys using randint(), from the
keys extracted using keys(). The logical computations are performed for
getting the separated test and training data.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Random Sample Training and Test Data

# Using keys() + randint() + computations

import random

 

# initializing dictionary

test_dict = {'gfg' : 4, 'is' : 12, 'best' : 6,
'for' : 7, 'geeks' : 10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing ratio

test = 40

training = 60

 

# Random Sample Training and Test Data

# Using keys() + randint() + computations

key_list = list(test_dict.keys())

 

test_key_count = int((len(key_list) / 100) * test)

test_keys = [random.choice(key_list) for ele in
range(test_key_count)]

train_keys = [ele for ele in key_list if ele not in
test_keys]

 

testing_dict = dict((key, test_dict[key]) for key in test_keys


 if key in test_dict) 

training_dict = dict((key, test_dict[key]) for key in
train_keys 

 if key in test_dict) 

 

# printing result 

print("The testing dictionary is : " + str(testing_dict)) 

print("The training dictionary is : " + str(training_dict))   
  
---  
  
__

__

**Output :**

> The original dictionary is : {‘is’: 12, ‘gfg’: 4, ‘best’: 6, ‘for’: 7,
> ‘geeks’: 10}  
> The testing dictionary is : {‘is’: 12, ‘for’: 7}  
> The training dictionary is : {‘gfg’: 4, ‘best’: 6, ‘geeks’: 10}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save


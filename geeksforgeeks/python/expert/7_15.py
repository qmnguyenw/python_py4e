Python | Classify Handwritten Digits with Tensorflow



Classifying handwritten digits is the basic problem of the machine learning
and can be solved in many ways here we will implement them by using TensorFlow

 **Using a Linear Classifier Algorithm with tf.contrib.learn**

linear classifier achieves the classification of handwritten digits by making
a choice based on the value of a linear combination of the features also known
as feature values and is typically presented to the machine in a vector called
a feature vector.

 **Modules required :**

NumPy:

  

  

    
    
    $ pip install numpy 

Matplotlib:

    
    
    $ pip install matplotlib 

Tensorflow:

    
    
    $ pip install tensorflow 

## **Steps to follow**

 **Step 1 :** Importing all dependence

 __

 __  
 __

 __

 __  
 __  
 __

import numpy as np

import matplotlib.pyplot as plt

import tensorflow as tf

 

learn = tf.contrib.learn

 

tf.logging.set_verbosity(tf.logging.ERROR)  
  
---  
  
 __

 __


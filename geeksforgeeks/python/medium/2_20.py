Placement prediction using Logistic Regression



 **Prerequisites:**Understanding Logistic Regression, Logistic Regression
using Python

In this article, we are going to discuss how to predict the placement status
of a student based on various student attributes using Logistic regression
algorithm.

Placements hold great importance for students and educational institutions. It
helps a student to build a strong foundation for the professional career ahead
as well as a good placement record gives a competitive edge to a
college/university in the education market.

This study focuses on a system that predicts if a student would be placed or
not based on the student’s qualifications, historical data, and experience.
This predictor uses a machine-learning algorithm to give the result.

The algorithm used is logistic regression. Logistic regression is basically a
supervised classification algorithm. In a classification problem, the target
variable(or output), y, can take only discrete values for given set of
features(or inputs), X. Talking about the dataset, it contains the secondary
school percentage, higher secondary school percentage, degree percentage,
degree, and work experience of students. After predicting the result its
efficiency is also calculated based on the dataset. The dataset used here is
in _.csv_ format.

  

  

###  **Below is the step-by-step Approach:**

 **Step 1:** Import the required modules.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# import modules

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt  
  
---  
  
 __

 __

 **Step 2:** Now to read the dataset that we are going to use for the analysis
and then checking the dataset.

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# reading the file

dataset = pd.read_csv('Placement_Data_Full_Class.csv')

dataset  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210101104223/2-660x246.png)

 **Step 3:** Now we will drop the columns that are not needed.

## Python

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# dropping the serial no and salary col

dataset = dataset.drop('sl_no', axis=1)

dataset = dataset.drop('salary', axis=1)  
  
---  
  
 __

 __


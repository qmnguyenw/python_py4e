Tumor Detection using classification – Machine Learning and Python



In this article, we will be making a project through Python language which
will be using some Machine Learning Algorithms too. It will be an exciting one
as after this project you will understand the concepts of using AI & ML with a
scripting language. The following libraries/packages will be used in this
project:

  *  **numpy** **:** It’s a Python library that is employed for scientific computing. It contains among other things – a strong array object, mathematical and statistical tools for integrating with other language’s code i.e. C/C++ and Fortran code.
  *  **pandas** **:** It’s a Python package providing fast, flexible, and expressive data structures designed to form working with “relational” or “labeled” data both easy and intuitive.
  *  **matplotlib** **:** Matplotlib may be a plotting library for the Python programing language which produces 2D plots to render visualization and helps in exploring the info sets. matplotlib.pyplot could be a collection of command style functions that make matplotlib work like MATLAB.
  *  **searborn** **:**. Seaborn is an open-source Python library built on top of matplotlib. It’s used for data visualization and exploratory data analysis. Seaborn works easily with dataframes and also the Pandas library.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Checking for any warning

import warnings

warnings.filterwarnings('ignore')  
  
---  
  
 __

 __

After this step we will install some **dependencies** : Dependencies are all
the software components required by your project in order for it to work as
intended and avoid runtime errors. We will be needing the **numpy, pandas,
matplotlib & seaborn libraries / dependencies. **As we will need a CSV file to
do the operations, for this project we will be using a CSV file that contains
data for **Tumor** (brain disease). So in this project at last we will be able
to predict whether a subject (candidate) has a potent chance of suffering from
a Tumor or not?

 **Step 1: Pre-processing the Data:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Importing dependencies

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

 

# Including & Reading the CSV file:

df =
pd.read_csv("https://raw.githubusercontent.com/ingledarshan/AIML-B2/main/data.csv")  
  
---  
  
 __

 __


How to read csv file with Pandas without header?



 **Prerequisites:** Pandas

A header of the CSV file is an array of values assigned to each of the
columns. It acts as a row header for the data. This article discusses how we
can read a csv file without header using pandas. To do this header attribute
should be set to None while reading the file.

 **Syntax:**

> read_csv(“file name”, header=None)

### Approach

  * Import module
  * Read file
  * Set header to None
  * Display data 

Let us first see how data is displayed with headers, to make difference
crystal clear.

  

  

 **Data file used:**

  * file.csv
  * sample.csv

 **Example1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing python package

import pandas as pd

 

# read the contents of csv file

dataset = pd.read_csv("file.csv")

 

# display the modified result

display(dataset)  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210225022922/Screenshot456.png)

Now let us see the implementation without headers.

 **Example 2:**

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# importing python package

import pandas as pd

 

# read the contents of csv file

dataset = pd.read_csv("file.csv", header=None)

 

# display the modified result

display(dataset)  
  
---  
  
 __

 __


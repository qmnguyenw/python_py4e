Python | Pandas Series.cov() to find Covariance



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric Python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **Series.cov()** is used to find covariance of two series. In the
following example, covariance is found using both Pandas method and manually
ways and the answers are then compared.

To learn more about Covariance, click here.  
  

>  **Syntax:** Series.cov(other, min_periods=None)
>
>  **Parameters:**  
>  **other:** Other series to be used in finding covariance  
>  **min_periods:** Minimum number of observations to be taken to have a valid
> result
>
>  
>
>
>  
>
>
>  **Return type:** Float value, Returns covariance of caller series and
> passed series

 **Example :**

In this example, two lists are made and converted to series using Pandas
.Series() method. The average if both series is found and a function is
created to find Covarience manually. Pandas .cov() is also applied and
results from both ways are stored in variables and printed to compare the
outputs.  
  

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

# list 1

a = [2, 3, 2.7, 3.2, 4.1]

 

# list 2

b = [10, 14, 12, 15, 20]

 

# storing average of a

av_a = sum(a)/len(a)

 

# storing average of b

av_b = sum(b)/len(b)

 

# making series from list a

a = pd.Series(a)

 

# making series from list b

b = pd.Series(b)

 

# covariance through pandas method

covar = a.cov(b)

 

 

# finding covariance manually

def covarfn(a, b, av_a, av_b):

 cov = 0

 

 for i in range(0, len(a)):

 cov += (a[i] - av_a) * (b[i] - av_b)

 return (cov / (len(a)-1))

 

# calling function

cov = covarfn(a, b, av_a, av_b)

 

# printing results

print("Results from Pandas method: ", covar)

print("Results from manual function method: ", cov)  
  
---  
  
 __

 __

 **Output:**  
As it can be seen in output, the output from both ways is same. Hence this
method is useful when finding co variance for large series.

    
    
    Results from Pandas method:  2.8499999999999996
    Results from manual function method:  2.8499999999999996
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


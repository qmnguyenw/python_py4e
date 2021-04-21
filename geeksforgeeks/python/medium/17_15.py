Absolute and Relative frequency in Pandas



 **Frequency** is the number of occurrences of an outcome in the given sample.
It can be termed in two different ways.

 **1\. Absolute Frequency:**  
It is the number of observations in a particular category. It has always an
integer value or we can say it has discrete values.

 **Example:**

> Following data are given about pass or fail of students in an exam held of
> Mathematics in a class.  
> P, P, F, P, F, P, P, F, F, P, P, P
>
> where, P = Passed and F = Failed.
>
>  
>
>
>  
>
>
>  **Solution:**  
>  From the given data we can say that,  
> There are 8 students who passed the exam  
> There are 4 students who failed the exam

 **Implementation in Python:**  
Let’s the result of 12 persons declared in two categories Pass(P) and Fail(F)
is categorized as 1 and 0 respectively.

    
    
    P, P, F, P, F, P, P, F, F, P, P, P
    1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1
    

__

__  
__

__

__  
__  
__

import pandas as pd

 

data = [1, 1, 0, 1, 0, 1, 1, 0, 0,
1, 1, 1]

 

# Create Data Frame using pandas library

# .value_counts() counts the number of 

# occurrences of particular observation

 

df = pd.Series(data).value_counts()

print(df)  
  
---  
  
 __

 __

 **Output:**

    
    
    1    8
    0    4
    dtype: int64
    

**2\. Relative Frequency:**  
It is the fraction of observations of a particular category in given data set.
It has floating values and also represented in percentage. Let us consider the
given example of passed and failed students in the Mathematics exam. Then,

> relative frequency of passed students = 8 / ( 8 + 4 ) = 0.666 = 66.6 %  
> relative frequency of failed students = 4 / ( 8 + 4 ) = 0.333 = 33.3 %

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

data = [1, 1, 0, 1, 0, 1, 1, 0, 0,
1, 1, 1]

 

# Create Data Frame using pandas library

# .value_counts() counts the number of 

# occurrences of particular observation

 

df = pd.Series(data).value_counts() 

print(df / len(data))  
  
---  
  
 __

 __

 **Output:**

    
    
    1    0.666667
    0    0.333333
    dtype: float64
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


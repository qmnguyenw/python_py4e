Python | Pandas Series.abs()



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Pandas **Series.abs()** method is used to get the absolute numeric value of
each element in Series/DataFrame.

>  **Syntax:** Series.abs()
>
>  **Parameters:** No parameters
>
>  **Returns:** Return the Series or DataFrame containing the absolute value
> of each element.
>
>  
>
>
>  
>

 **Code #1:**

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd 

 

# creating lists

lst = [2, -10.87, -3.14, 0.12]

lst2 = [-10.87 + 4j]

 

ser = pd.Series(lst)

ser1 = pd.Series(lst2)

 

# printing values explaining abs()

print(ser1.abs(), '\n\n', ser.abs())  
  
---  
  
 __

 __

 **Output:**

    
    
    0    11.582612
    dtype: float64 
    
     0     2.00
    1    10.87
    2     3.14
    3     0.12
    dtype: float64

  
**Code #2:** Explaning use of abs() on specific row

 __

 __  
 __

 __

 __  
 __  
 __

# importing pandas module

import pandas as pd 

 

df = pd.DataFrame({'Name': ['John', 'Hari', 'Peter',
'Loani'],

 'Age': [31, 29, 57, 40],

 'val': [98, 48, -80, -14]})

 

 

df['ope'] = (df.val - 87).abs()

 

df  
  
---  
  
 __

 __

 **Output:**

    
    
    Name    Age    val    ope
    0    John    31    98    11
    1    Hari    29    48    39
    2    Peter    57    -80    167
    3    Loani    40    -14    101

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Determine Period Index and Column for DataFrame in Pandas



In Pandas to determine Period Index and Column for Data Frame, we will use the
pandas.period_range() method. It is one of the general functions in Pandas
which is used to return a fixed frequency PeriodIndex, with day (calendar) as
the default frequency.

>  _ **Syntax:** pandas.to_numeric(arg, errors=’raise’, downcast=None)_
>
>  _ **Parameters:**_  
>  _ **start :** Left bound for generating periods_  
>  _ **end :** Right bound for generating periods_  
>  _ **periods :** Number of periods to generate_  
>  _ **freq :** Frequency alias_  
>  _ **name :** Name of the resulting PeriodIndex_
>
>  _ **Returns:** PeriodIndex_

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

 

 

course = ["DBMS", "DSA", "OOPS",

 "System Design", "CN", ]

 

# pass the period and staring index

webinar_date = pd.period_range('2020-08-15', periods=5)

 

# Determine Period Index and Column

# for DataFrame

df = pd.DataFrame(course, index=webinar_date,
columns=['Course'])

 

df  
  
---  
  
 __

 __

 **Output** :

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201016134341/pandas1.png)

  

  

 **Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

day = ["Sun", "Mon", "Tue",

 "Wed", "Thurs", "Fri", "Sat"]

 

# pass the period and staring index

daycode = pd.period_range('2020-08-15', periods=7)

 

# Determine Period Index and Column for DataFrame

df = pd.DataFrame(day, index=daycode, columns=['day'])

 

df  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201016134441/pandas2.png)

 **Example 3:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

Team = ["Ind", "Pak", "Aus"]

 

# pass the period and staring index

match_date = pd.period_range('2020-08-01', periods=3)

 

# Determine Period Index and Column for DataFrame

df = pd.DataFrame(Team, index=match_date, columns=['Team'])

 

df  
  
---  
  
 __

 __

 **Output** :

![](https://media.geeksforgeeks.org/wp-
content/uploads/20201016134545/pandas3.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


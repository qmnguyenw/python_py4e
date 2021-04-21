Python – Convert day number to date in particular year



Given day number, convert to date it refers to.

>  **Input** : day_num = “339”, year = “2020”  
> **Output** : 12-04-2020  
> **Explanation** : 339th Day of 2020 is 4th December.
>
>  **Input** : day_num = “4”, year = “2020”  
> **Output** : 01-04-2020  
> **Explanation** : 4th Day of 2020 is 4th January.

**Method #1 : Using datetime.strptime()**

In this, we get the year string and day number string, and pass to strptime(),
converts to the corresponding required date.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert day number to date in particular year

# Using datetime.strptime()

from datetime import datetime

 

# initializing day number

day_num = "339"

 

# print day number

print("The day number : " + str(day_num))

 

# adjusting day num

day_num.rjust(3 + len(day_num), '0')

 

# Initialize year

year = "2020"

 

# converting to date

res = datetime.strptime(year + "-" + day_num,
"%Y-%j").strftime("%m-%d-%Y")

 

# printing result

print("Resolved date : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The day number : 339
    Resolved date : 12-04-2020
    

**Method #2 : Using timedelta()**

In this, we initialize the date by 1st of January and then add number of days
using timedelta(), resultant gives the date required.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert day number to date in particular year

# Using datetime.strptime()

from datetime import datetime, date, timedelta

 

# initializing day number

day_num = "339"

 

# print day number

print("The day number : " + str(day_num))

 

# adjusting day num

day_num.rjust(3 + len(day_num), '0')

 

# Initialize year

year = "2020"

 

# Initializing start date

strt_date = date(int(year), 1, 1)

 

# converting to date

res_date = strt_date + timedelta(days=int(day_num) - 1)

res = res_date.strftime("%m-%d-%Y")

 

# printing result

print("Resolved date : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The day number : 339
    Resolved date : 12-04-2020
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


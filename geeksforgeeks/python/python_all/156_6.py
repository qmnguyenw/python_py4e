Python | Sort given list of dictionaries by date



Given a list of dictionary, the task is to sort the dictionary by date. Let’s
see a few methods to solve the task.

 **Method #1: Using naive approach**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sort a list of dictionary

# where value date is in string

 

# Initialising list of dictionary

ini_list = [{'name':'akash', 'd.o.b':'1997-03-02'},

 {'name':'manjeet', 'd.o.b':'1997-01-04'}, 

 {'name':'nikhil', 'd.o.b':'1997-09-13'}]

 

# printing initial list

print ("initial list : ", str(ini_list))

 

# code to sort list on date

ini_list.sort(key = lambda x:x['d.o.b'])

 

# printing final list

print ("result", str(ini_list))  
  
---  
  
 __

 __

 **Output:**

> initial list : [{‘name’: ‘akash’, ‘d.o.b’: ‘1997-03-02’}, {‘name’:
> ‘manjeet’, ‘d.o.b’: ‘1997-01-04’}, {‘name’: ‘nikhil’, ‘d.o.b’:
> ‘1997-09-13’}]
>
> result [{‘name’: ‘manjeet’, ‘d.o.b’: ‘1997-01-04’}, {‘name’: ‘akash’,
> ‘d.o.b’: ‘1997-03-02’}, {‘name’: ‘nikhil’, ‘d.o.b’: ‘1997-09-13’}]
>
>  
>
>
>  
>

 **Method #2: Usingdatetime.strptime and lambda**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sort a list of dictionary

# where value date is in a string

 

from datetime import datetime

 

# Initialising list of dictionary

ini_list = [{'name':'akshat', 'd.o.b':'1997-09-01'},

 {'name':'vashu', 'd.o.b':'1997-08-19'},

 {'name':'manjeet', 'd.o.b':'1997-01-04'},

 {'name':'nikhil', 'd.o.b':'1997-09-13'}]

 

# printing initial list

print ("initial list : ", str(ini_list))

 

# code to sort list on date

ini_list.sort(key = lambda x: datetime.strptime(x['d.o.b'],
'%Y-%m-%d'))

 

# printing final list

print ("result", str(ini_list))  
  
---  
  
 __

 __

 **Output:**

> initial list : [{‘d.o.b’: ‘1997-09-01’, ‘name’: ‘akshat’}, {‘d.o.b’:
> ‘1997-08-19’, ‘name’: ‘vashu’}, {‘d.o.b’: ‘1997-01-04’, ‘name’: ‘manjeet’},
> {‘d.o.b’: ‘1997-09-13’, ‘name’: ‘nikhil’}]
>
> result [{‘d.o.b’: ‘1997-01-04’, ‘name’: ‘manjeet’}, {‘d.o.b’: ‘1997-08-19’,
> ‘name’: ‘vashu’}, {‘d.o.b’: ‘1997-09-01’, ‘name’: ‘akshat’}, {‘d.o.b’:
> ‘1997-09-13’, ‘name’: ‘nikhil’}]

  
**Method #3: Usingoperator.itemgetter**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# sort a list of dictionary

# where value date is in string

 

import operator

 

# Initialising list of dictionary

ini_list = [{'name':'akash', 'd.o.b':'1997-03-02'},

 {'name':'manjeet', 'd.o.b':'1997-01-04'},

 {'name':'nikhil', 'd.o.b':'1997-09-13'}]

 

# printing initial list

print ("initial list : ", str(ini_list))

 

# code to sort list on date

ini_list.sort(key = operator.itemgetter('d.o.b'))

 

# printing final list

print ("result", str(ini_list))  
  
---  
  
 __

 __

 **Output:**

> initial list : [{‘d.o.b’: ‘1997-03-02’, ‘name’: ‘akash’}, {‘d.o.b’:
> ‘1997-01-04’, ‘name’: ‘manjeet’}, {‘d.o.b’: ‘1997-09-13’, ‘name’: ‘nikhil’}]
>
> result [{‘d.o.b’: ‘1997-01-04’, ‘name’: ‘manjeet’}, {‘d.o.b’: ‘1997-03-02’,
> ‘name’: ‘akash’}, {‘d.o.b’: ‘1997-09-13’, ‘name’: ‘nikhil’}]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


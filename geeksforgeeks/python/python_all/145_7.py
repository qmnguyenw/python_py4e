Python | Sort nested dictionary by key



Sorting has quite vivid applications and sometimes, we might come up with the
problem in which we need to sort the nested dictionary by the nested key. This
type of application is popular in web development as JSON format is quite
popular. Let’s discuss certain ways in which this can be performed.

 **Method #1 : UsingOrderedDict() + sorted()**

This task can be performed using OrderedDict function which converts the
dictionary to specific order as mentioned in its arguments manipulated by
sorted function in it to sort by the value of key passed.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sort nested dictionary by key

# using OrderedDict() + sorted()

from collections import OrderedDict

from operator import getitem

 

# initializing dictionary

test_dict = {'Nikhil' : { 'roll' : 24, 'marks' :
17},

 'Akshat' : {'roll' : 54, 'marks' : 12}, 

 'Akash' : { 'roll' : 12, 'marks' : 15}}

 

# printing original dict

print("The original dictionary : " + str(test_dict))

 

# using OrderedDict() + sorted()

# Sort nested dictionary by key

res = OrderedDict(sorted(test_dict.items(),

 key = lambda x: getitem(x[1], 'marks')))

 

# print result

print("The sorted dictionary by marks is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘Nikhil’: {‘roll’: 24, ‘marks’: 17}, ‘Akash’:
> {‘roll’: 12, ‘marks’: 15}, ‘Akshat’: {‘roll’: 54, ‘marks’: 12}}  
> The sorted dictionary by marks is : OrderedDict([(‘Akshat’, {‘roll’: 54,
> ‘marks’: 12}), (‘Akash’, {‘roll’: 12, ‘marks’: 15}), (‘Nikhil’, {‘roll’: 24,
> ‘marks’: 17})])
>
>  
>
>
>  
>

**Method #2 : Usingsorted()**

We can achieve the above result better if we just use the sorted function as
it returns the result in a more usable format, dict and performs exactly the
desired task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sort nested dictionary by key

# using sorted()

 

# initializing dictionary

test_dict = {'Nikhil' : { 'roll' : 24, 'marks' :
17},

 'Akshat' : {'roll' : 54, 'marks' : 12}, 

 'Akash' : { 'roll' : 12, 'marks' : 15}}

 

# printing original dict

print("The original dictionary : " + str(test_dict))

 

# using sorted()

# Sort nested dictionary by key

res = sorted(test_dict.items(), key = lambda x:
x[1]['marks'])

 

# print result

print("The sorted dictionary by marks is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original dictionary : {‘Nikhil’: {‘marks’: 17, ‘roll’: 24}, ‘Akshat’:
> {‘marks’: 12, ‘roll’: 54}, ‘Akash’: {‘marks’: 15, ‘roll’: 12}}  
> The sorted dictionary by marks is : [(‘Akshat’, {‘marks’: 12, ‘roll’: 54}),
> (‘Akash’, {‘marks’: 15, ‘roll’: 12}), (‘Nikhil’, {‘marks’: 17, ‘roll’: 24})]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python | Combine the values of two dictionaries having same key



Dictionary is a collection which is unordered, changeable and indexed. In
Python, dictionaries are written with curly brackets, and they have keys and
values. It is widely used in day to day programming, web development, and
machine learning. Combining dictionaries is very common task in operations of
dictionary.

Let’s see how to combine the values of two dictionaries having same key.  
  
 **Method #1: UsingCounter**  
Counter is a special subclass of dictionary which performs acts same as
dictionary in most cases.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate combining

# two dictionaries having same key

 

from collections import Counter

 

# initialising dictionaries

ini_dictionary1 = Counter({'nikhil': 1, 'akash' : 5,

 'manjeet' : 10, 'akshat' : 15})

ini_dictionary2 = Counter({'akash' : 7, 'akshat' : 5,

 'm' : 15})

 

# printing initial dictionaries

print ("initial 1st dictionary", str(ini_dictionary1))

print ("initial 2nd dictionary", str(ini_dictionary2))

 

# combining dictionaries

# using Counter

final_dictionary = ini_dictionary1 + ini_dictionary2

 

# printing final result

print ("final dictionary", str(final_dictionary))  
  
---  
  
 __

 __

 **Output:**

> initial 1st dictionary Counter({‘akshat’: 15, ‘manjeet’: 10, ‘akash’: 5,
> ‘nikhil’: 1})  
> initial 2nd dictionary Counter({‘m’: 15, ‘akash’: 7, ‘akshat’: 5})  
> final dictionary Counter({‘akshat’: 20, ‘m’: 15, ‘akash’: 12, ‘manjeet’: 10,
> ‘nikhil’: 1})

  
**Method #2: Usingdict() and items**  
This method is for Python version 2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate combining

# two dictionaries having same key

 

 

# initialising dictionaries

ini_dictionary1 = {'nikhil': 1, 'akash' : 5,

 'manjeet' : 10, 'akshat' : 15}

ini_dictionary2 = {'akash' : 7, 'akshat' : 5,

 'm' : 15}

 

# printing initial dictionaries

print ("initial 1st dictionary", str(ini_dictionary1))

print ("initial 2nd dictionary", str(ini_dictionary2))

 

# combining dictionaries

# using dict() and items()

final_dictionary = dict(ini_dictionary1.items() +
ini_dictionary2.items() +

 [(k, ini_dictionary1[k] + ini_dictionary2[k])

 for k in set(ini_dictionary2)

 & set(ini_dictionary1)])

 

# printing final result

print ("final dictionary", str(final_dictionary))  
  
---  
  
 __

 __

 **Output:**

> (‘initial 1st dictionary’, “{‘manjeet’: 10, ‘nikhil’: 1, ‘akshat’: 15,
> ‘akash’: 5}”)  
> (‘initial 2nd dictionary’, “{‘m’: 15, ‘akshat’: 5, ‘akash’: 7}”)  
> (‘final dictionary’, “{‘nikhil’: 1, ‘m’: 15, ‘manjeet’: 10, ‘akshat’: 20,
> ‘akash’: 12}”)

  
**Method #3: Using dict comprehension and set**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate combining

# two dictionaries having same key

 

# initialising dictionaries

ini_dictionary1 = {'nikhil': 1, 'akash' : 5, 

 'manjeet' : 10, 'akshat' : 15}

ini_dictionary2 = {'akash' : 7, 'akshat' : 5, 

 'm' : 15}

 

# printing initial dictionaries

print ("initial 1st dictionary", str(ini_dictionary1))

print ("initial 2nd dictionary", str(ini_dictionary2))

 

# combining dictionaries

# using dict comprehension and set

final_dictionary = {x: ini_dictionary1.get(x, 0) +
ini_dictionary2.get(x, 0)

 for x in set(ini_dictionary1).union(ini_dictionary2)}

 

# printing final result

print ("final dictionary", str(final_dictionary))  
  
---  
  
 __

 __

 **Output:**

> initial 1st dictionary {‘nikhil’: 1, ‘akshat’: 15, ‘akash’: 5, ‘manjeet’:
> 10}  
> initial 2nd dictionary {‘akshat’: 5, ‘akash’: 7, ‘m’: 15}  
> final dictionary {‘nikhil’: 1, ‘akshat’: 20, ‘akash’: 12, ‘m’: 15,
> ‘manjeet’: 10}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python – Remove Units from Value List



Sometimes, while working with Python value lists, we can have a problem in
which we need to perform removal of units that come along with values. This
problem can have direct application in day-day programming and data
preprocessing. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [“54 cm”, “23 cm”, “12cm”, “19 cm”], unit = “cm”  
>  **Output** : [’54’, ’23’, ’12’, ’19’]
>
>  **Input** : test_list = [“54 cm”], unit = “cm”  
>  **Output** : [’54’]

 **Method #1 : Usingregex() \+ list comprehension**  
The combination of these functions can be used to solve this problem. In this,
we approach by extracting just the numbers using regex, and remove rest of
string units.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Units from Value List

# Using list comprehesion + regex()

import re

 

# initializing list

test_list = ["54 kg", "23 kg", "12kg", "19 kg"] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing unit 

unit = "kg"

 

# Remove Units from Value List

# Using list comprehesion + regex()

res = re.findall('\d+', ' '.join(test_list))

 

# printing result 

print("List after unit removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : ['54 kg', '23 kg', '12kg', '19  kg']
    List after unit removal : ['54', '23', '12', '19']
    


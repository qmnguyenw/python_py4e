Python – Extract Kth index elements from Dictionary Value list



Given a dictionary with list as values, extract all the Kth index elements.

>  **Input** : {“Gfg” : [4, 7, 5], “Best” : [8, 6, 7], “is” : [9, 3, 8]}, K =
> 2  
>  **Output** : [5, 7, 8]  
>  **Explanation** : The 2nd index elements are 5, 7 and 8 respectively in
> different keys.
>
>  **Input** : {“Gfg” : [4, 7, 5], “Best” : [8, 6, 7], “is” : [9, 3, 8]}, K =
> 0  
>  **Output** : [4, 8, 9]  
>  **Explanation** : The 0th index elements are 4, 8 and 9 respectively in
> different keys.

 **Method #1 : Using list comprehension + values()**

The combination of above functionalities can be used to solve this problem. In
this, the values are extracted using values() and list comprehension is used
to construct new list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Kth index elements from Dictionary Value list

# Using list comprehension + values()

 

# initializing dictionary

test_dict = {"Gfg" : [4, 7, 5], "Best" : [8,
6, 7], "is" : [9, 3, 8]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 1

 

# one liner, values() getting all value according to keys

res = [sub[K] for sub in test_dict.values()]

 

# printing result 

print("The extracted values : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [4, 7, 5], 'Best': [8, 6, 7], 'is': [9, 3, 8]}
    The extracted values : [7, 6, 3]
    

**Method #2 : Using map() + itemgetter()**

The combination of above functionalities can be used to solve this problem. In
this, we use map() to extend logic of getting values of particular key, and
itemgetter is used for extracting particular index.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Kth index elements from Dictionary Value list

# Using map() + itemgetter()

from operator import itemgetter

 

# initializing dictionary

test_dict = {"Gfg" : [4, 7, 5], "Best" : [8,
6, 7], "is" : [9, 3, 8]}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 1

 

# map and itemgetter() extracting result 

# list() used to convert result from map() to list format

res = list(map(itemgetter(K), test_dict.values()))

 

# printing result 

print("The extracted values : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': [4, 7, 5], 'Best': [8, 6, 7], 'is': [9, 3, 8]}
    The extracted values : [7, 6, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


Python – Find frequency of given Datatype in tuple



Sometimes, while working with Python records, we can have a problem in which
we need to extract count of any data type occurred in tuple. This can have
application in various domains such as day-day programming and web
development. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_tuple = (5, ‘Gfg’, 2, 8.8, 1.2, ‘is’), data_type = int  
>  **Output** : 2
>
>  **Input** : test_tuple = (5, ‘Gfg’, 2, 8.8, 1.2, ‘is’), data_type = str  
>  **Output** : 2

 **Method #1 : Using loop +isinstance()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of checking for data type using isinstance() and run a
counter to increment on match.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Data type frequency in tuple

# Using loop + isinstance()

 

# initializing tuples

test_tuple = (5, 'Gfg', 2, 8.8, 1.2, 'is')

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# initializing data type

data_type = float

 

# Data type frequency in tuple

# Using loop + isinstance()

count = 0

for ele in test_tuple:

 if isinstance(ele, float):

 count = count + 1

 

# printing result 

print("The data type frequency : " + str(count))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple : (5, 'Gfg', 2, 8.8, 1.2, 'is')
    The data type frequency : 2
    


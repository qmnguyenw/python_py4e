Python – Remove particular data type Elements from Tuple



Sometimes, while working with Python tuples, we can have a problem in which we
need to remove particular data type elements from tuple. This kind of problem
can occur in domains which require data preprocessing. Let’s discuss certain
ways in which this task can be performed.

>  **Input** : test_tuple = (4, 5, ‘Gfg’, 7.7, ‘Best’), data_type = str  
>  **Output** : [4, 5, 7.7]
>
>  **Input** : test_tuple = (4, 5, ‘Gfg’, 7.7, ‘Best’), data_type = float  
>  **Output** : [4, 5, ‘Gfg’, ‘Best’]

 **Method #1 : Using loop +isinstance()**  
The combination of above functionalities can be used to solve this problem. In
this, we need to iterate for each element and discard the element if it
matches the data type, using isinstance().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove particular data type Elements from Tuple

# Using loop + isinstance() 

 

# initializing tuple

test_tuple = (4, 5, 'Gfg', 7.7, 'Best')

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# initializing data type

data_type = int

 

# Remove particular data type Elements from Tuple

# Using loop + isinstance()

res = []

for ele in test_tuple:

 if not isinstance(ele, data_type):

 res.append(ele)

 

# printing result 

print("The filtered tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple : (4, 5, 'Gfg', 7.7, 'Best')
    The filtered tuple : ['Gfg', 7.7, 'Best']
    


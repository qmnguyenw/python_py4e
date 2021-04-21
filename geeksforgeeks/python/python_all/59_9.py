Python – Retain Numbers in String



Sometimes, while working with Python Strings, we can have a problem in which
we need to perform the removal of all the characters other than integers. This
kind of problem can have application in many data domains such as Machine
Learning and web development. Let’s discuss certain ways in which this task
can be performed.

>  **Input** : test_str = ‘G4g is No. 1’  
>  **Output** : 41
>
>  **Input** : test_str = ‘Gfg is No. 1’  
>  **Output** : 1

 **Method #1 : Using list comprehension +join() + isdigit()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of extracting integers using isdigit(), list comprehension
is used for iteration and join() is used to perform join of numbers filtered.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Retain Numbers in String

# Using list comprehension + join() + isdigit()

 

# initializing string

test_str = 'G4g is No. 1 for Geeks 7'

 

# printing original string

print("The original string is : " + str(test_str))

 

# Retain Numbers in String

# Using list comprehension + join() + isdigit()

res = "".join([ele for ele in test_str if ele.isdigit()])

 

# printing result 

print("String after integer retention : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original string is : G4g is No. 1 for Geeks 7
    String after integer retention : 417
    


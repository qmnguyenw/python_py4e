Python – Add Custom Column to Tuple list



Sometimes, while working with Python records, we can have a problem in which
we need to add custom column to tuples list. This kind of problem can have
application in data domains such as web development. Lets discuss certain ways
in which this task can be performed.

>  **Input** :  
> test_list = [(3, ), (7, ), (2, )]  
> cus_eles = [7, 8, 2]  
>  **Output** : [(3, 7), (7, 8), (2, 2)]
>
>  **Input** :  
> test_list = [(3, 9, 6, 10)]  
> cus_eles = [7]  
>  **Output** : [(3, 9, 6, 10, 7)]

 **Method #1 : Using list comprehension +zip()**  
The combination of above functionalities can be used to solve this problem. In
this, we perform the pairing of custom elements and tuples with the help of
zip().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add Custom Column to Tuple list

# Using list comprehension + zip()

 

# initializing list

test_list = [(3, 4), (78, 76), (2, 3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing add list

cus_eles = [17, 23, 12]

 

# Add Custom Column to Tuple list

# Using list comprehension + zip()

res = [sub + (val, ) for sub, val in zip(test_list,
cus_eles)]

 

# printing result 

print("The tuples after adding elements : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(3, 4), (78, 76), (2, 3)]
    The tuples after adding elements : [(3, 4, 17), (78, 76, 23), (2, 3, 12)]
    


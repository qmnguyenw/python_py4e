Python – Convert String Truth values to Boolean



Given a String List, convert the String Truth values to Boolean values.

>  **Input** : test_list = [“True”, “False”, “True”, “False”]  
>  **Output** : [True, False, True, False]  
>  **Explanation** : String booleans converted to actual Boolean.
>
>  **Input** : test_list = [“True”]  
>  **Output** : [True]  
>  **Explanation** : String boolean converted to actual Boolean.

 **Method #1 : Using list comprehension**

In this, we check for just the True value, rest values are automatically
converted to False boolean.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String Truth values to Boolean

# Using list comprehension

 

# initializing lists

test_list = ["True", "False", "True", "True",
"False"]

 

# printing string

print("The original list : " + str(test_list))

 

# using list comprehension to check "True" string

res = [ele == "True" for ele in test_list]

 

# printing results 

print("The converted Boolean values : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['True', 'False', 'True', 'True', 'False']
    The converted Boolean values : [True, False, True, True, False]
    

**Method #2 : Using map() + lambda**

In this, we apply same approach, just the different way to solve the problem.
The map() is used to extend logic of values computed by lambda function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String Truth values to Boolean

# Using map() + lambda

 

# initializing lists

test_list = ["True", "False", "True", "True",
"False"]

 

# printing string

print("The original list : " + str(test_list))

 

# using map() to extend and lambda to check "True" string

res = list(map(lambda ele: ele == "True", test_list))

 

# printing results 

print("The converted Boolean values : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['True', 'False', 'True', 'True', 'False']
    The converted Boolean values : [True, False, True, True, False]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


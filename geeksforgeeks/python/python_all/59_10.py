Python – Convert Float String List to Float Values



Sometimes, while working with Python Data, we can have a problem in which we
need to perform conversion of Float Strings to float values. This kind of
problem is quite common in all domains and find application quite often. Let’s
discuss certain ways in which this task can be performed.

>  **Input** : test_list = [‘8.6’, ‘4.6’]  
>  **Output** : [8.6, 4.6]
>
>  **Input** : test_list = [‘4.5’]  
>  **Output** : [4.5]

 **Method #1 : Using list comprehension +float()**  
The combination of above functions can be used to solve this problem. In this,
we perform task of conversion using float() and list comprehension is used to
perform iteration.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Float String List to Float Values

# Using float() + list comprehension

 

# initializing list

test_list = ['87.6', '454.6', '9.34', '23', '12.3']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Convert Float String List to Float Values

# Using float() + list comprehension

res = [float(ele) for ele in test_list]

 

# printing result 

print("List after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list : ['87.6', '454.6', '9.34', '23', '12.3']
    List after conversion : [87.6, 454.6, 9.34, 23.0, 12.3]
    


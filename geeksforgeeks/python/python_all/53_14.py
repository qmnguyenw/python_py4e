Python – Cost computation using Frequency and Price dictionary



Given price and frequency dictionary, compute total cost of products, i.e by
summing the product of price and frequency of each item.

>  **Input** : test_dict = {“Apple” : 2, “Mango” : 2, “Grapes” : 2}, {“Apple”
> : 2, “Mango” : 2, “Grapes” : 2}  
>  **Output** : 12  
>  **Explanation** : (2*2) + (2*2) + (2*2) = 12.
>
>  **Input** : test_dict = {“Apple” : 3, “Mango” : 2, “Grapes” : 3}, {“Apple”
> : 2, “Mango” : 2, “Grapes” : 2}  
>  **Output** : 16  
>  **Explanation** : The summation of product leads to 16 as above.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we iterate
through all the keys and multiply the frequency of each element by its cost
and keep performing intermediate summation.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cost computation using Frequency and Price dictionary

# Using loop

 

# initializing dictionary

test_dict = {"Apple" : 5, "Mango" : 8, "Grapes" :
10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing Frequency dict 

cost_dict = {"Apple" : 3, "Mango" : 4, "Grapes" :
6}

 

res = 0

for key in test_dict:

 

 # computing summation of product

 res = res + (test_dict[key] * cost_dict[key])

 

# printing result 

print("The extracted summation : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Apple': 5, 'Mango': 8, 'Grapes': 10}
    The extracted summation : 107
    

**Method #2 : Using sum() + list comprehension**

The combination of these functionalities provide a shorthand to solve this
problem. In this, we perform summation using sum() and list comprehension is
used to compile result and iterate.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Cost computation using Frequency and Price dictionary

# Using sum() + list comprehension

 

# initializing dictionary

test_dict = {"Apple" : 5, "Mango" : 8, "Grapes" :
10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing Frequency dict 

cost_dict = {"Apple" : 3, "Mango" : 4, "Grapes" :
6}

 

# using list comprehension and sum() to provide one-liner

res = sum([cost_dict[key] * test_dict[key] for key in
test_dict])

 

# printing result 

print("The extracted summation : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Apple': 5, 'Mango': 8, 'Grapes': 10}
    The extracted summation : 107
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


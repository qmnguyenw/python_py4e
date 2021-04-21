Python – List of dictionaries all values Summation



Given a list of dictionaries, extract all the values summation.

>  **Input** : test_list = [{“Apple” : 2, “Mango” : 2, “Grapes” : 2}, {“Apple”
> : 2, “Mango” : 2, “Grapes” : 2}]  
>  **Output** : 12  
>  **Explanation** : 2 + 2 +…(6-times) = 12, sum of all values.
>
>  **Input** : test_list = [{“Apple” : 3, “Mango” : 2, “Grapes” : 2}, {“Apple”
> : 2, “Mango” : 3, “Grapes” : 3}]  
>  **Output** : 15  
>  **Explanation** : Summation of all values leads to 15.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we iterate for
all the dictionaries from list and then perform sum of all the keys of each
dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List of dictionaries all values Summation

# Using loop

 

# initializing lists

test_list = [{"Gfg" : 6, "is" : 9, "best" : 10},


 {"Gfg" : 8, "is" : 11, "best" : 19},

 {"Gfg" : 2, "is" : 16, "best" : 10},

 {"Gfg" : 12, "is" : 1, "best" : 8},

 {"Gfg" : 22, "is" : 6, "best" : 8}]

 

# printing original list

print("The original list : " + str(test_list))

 

res = 0

# loop for dictionaries

for sub in test_list:

 for key in sub:

 

 # summation of each key 

 res += sub[key]

 

# printing result 

print("The computed sum : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 6, 'is': 9, 'best': 10}, {'Gfg': 8, 'is': 11, 'best': 19}, {'Gfg': 2, 'is': 16, 'best': 10}, {'Gfg': 12, 'is': 1, 'best': 8}, {'Gfg': 22, 'is': 6, 'best': 8}]
    The computed sum : 148
    

**Method #2 : Using sum() + values() + list comprehension**

The combination of above functions can be used as one-liner alternative to
solve this problem. In this, summation is performed using sum(), and values( )
is used to extract values of all dictionaries in list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List of dictionaries all values Summation

# Using sum() + values() + list comprehension

 

# initializing lists

test_list = [{"Gfg" : 6, "is" : 9, "best" : 10},


 {"Gfg" : 8, "is" : 11, "best" : 19},

 {"Gfg" : 2, "is" : 16, "best" : 10},

 {"Gfg" : 12, "is" : 1, "best" : 8},

 {"Gfg" : 22, "is" : 6, "best" : 8}]

 

# printing original list

print("The original list : " + str(test_list))

 

res = sum([sum(list(sub.values())) for sub in
test_list])

 

# printing result 

print("The computed sum : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [{'Gfg': 6, 'is': 9, 'best': 10}, {'Gfg': 8, 'is': 11, 'best': 19}, {'Gfg': 2, 'is': 16, 'best': 10}, {'Gfg': 12, 'is': 1, 'best': 8}, {'Gfg': 22, 'is': 6, 'best': 8}]
    The computed sum : 148
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


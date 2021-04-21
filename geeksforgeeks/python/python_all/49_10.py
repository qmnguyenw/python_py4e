Python – Dictionary Keys whose Values summation equals K



Given a dictionary and a value K, extract keys whose summation of values
equals K.

>  **Input** : {“Gfg” : 3, “is” : 5, “Best” : 9, “for” : 8, “Geeks” : 10}, K =
> 17  
>  **Output** : [‘Best’, ‘for’]  
>  **Explanation** : 9 + 8 = 17, hence those keys are extracted.
>
>  **Input** : {“Gfg” : 3, “is” : 5, “Best” : 9, “for” : 8, “Geeks” : 10}, K =
> 19  
>  **Output** : [‘Best’, ‘Geeks’]  
>  **Explanation** : 9 + 10 = 19, hence those keys are extracted.

 **Method #1 : Using loop**

This is one of the ways in which this task can be performed. In this, we
iterate for all the keys, and next keys in inner list, and keep on checking
values summation. If its equal to K. The keys are stored.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Keys whose Values summation equals K 

# Using loop

 

# initializing dictionary

test_dict = {"Gfg" : 3, "is" : 5, "Best" : 9,
"for" : 8, "Geeks" : 10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 14

 

# extracting keys and values

keys = list(test_dict.keys())

values = list(test_dict.values())

 

res = None

for i in range(len(keys)):

 for j in range(i + 1, len(keys)):

 

 # checking if values equals K

 if values[i] + values[j] == K:

 res = [keys[i], keys[j]]

 

# printing result 

print("Keys whose sum equals K : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 3, 'is': 5, 'Best': 9, 'for': 8, 'Geeks': 10}
    Keys whose sum equals K : ['is', 'Best']
    

**Method #2 : Using list comprehension**

This is yet another way in which this task can be performed. In this, we
perform task similar to above method but in shorthand manner using list
comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Dictionary Keys whose Values summation equals K 

# Using list comprehension 

 

# initializing dictionary

test_dict = {"Gfg" : 3, "is" : 5, "Best" : 9,
"for" : 8, "Geeks" : 10}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing K 

K = 14

 

# extracting keys and values

keys = list(test_dict.keys())

values = list(test_dict.values())

 

# checking for keys in one liner

res = [[keys[i], keys[j]] for i in range(len(keys)) for
j in range(i + 1, len(keys)) if values[i] + values[j]
== K]

 

# printing result 

print("Keys whose sum equals K : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 3, 'is': 5, 'Best': 9, 'for': 8, 'Geeks': 10}
    Keys whose sum equals K : [['is', 'Best']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


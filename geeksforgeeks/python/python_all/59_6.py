Python – Selective Key Values Summation



Sometimes, while working with Python dictionaries, we can have a problem in
which we desire to get summation of certain keys’ values in dictionary. This
kind of application can have usecase in many domains such as day-day
programming. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_dict = {‘Gfg’ : 4, ‘is’ : 2, ‘best’ : 7}, key_list =
> [‘Gfg’, ‘best’]  
>  **Output** : 11
>
>  **Input** : test_dict = {‘Gfg’ : 4, ‘best’ : 7}, key_list = [‘Gfg’]  
>  **Output** : 4

 **Method #1 : Using loop**  
This is one of the ways in which this task can be performed. In this, we
iterate for target list keys and sum the corresponding values from dictionary.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Selective Key Values Summation

# Using loop

 

# initializing dictionary

test_dict = {'Gfg' : 4, 'is' : 2, 'best' : 7,
'for' : 9, 'geeks' : 10} 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing keys_list

key_list = ['Gfg', 'best', 'geeks']

 

# Selective Key Values Summation

# Using loop

res = 0

for key in key_list:

 res += test_dict[key] 

 

# printing result 

print("The keys summation : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original dictionary is : {'Gfg': 4, 'is': 2, 'best': 7, 'for': 9, 'geeks': 10}
    The keys summation : 21
    


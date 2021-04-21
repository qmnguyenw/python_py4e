Python – Common keys in list and dictionary



Given a dictionary and list, extract all the keys and list which are common.

>  **Input** : test_dict = {“Gfg”: 3, “is” : 5, “best” : 9, “for” : 0, “geeks”
> : 3}, test_list = [“Gfg”, “best”, “CS”]  
>  **Output** : [‘Gfg’, ‘best’]  
>  **Explanation** : Gfg and best are present in both dictionary and List.
>
>  **Input** : test_dict = {“Gfg”: 3, “is” : 5, “best” : 9, “for” : 0, “geeks”
> : 3}, test_list = [“Gfg”, “good”, “CS”]  
>  **Output** : [‘Gfg’]  
>  **Explanation** : Gfg is present in both dictionary and List.

 **Method #1 : Using list comprehension**

This is one of the ways in which this task can be performed. In this, we
iterate for all the dictionary and list values, if find a match, they are
added to result.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Common keys in list and dictionary

# Using list comprehension

 

# initializing dictionary

test_dict = {"Gfg": 3, "is" : 5, "best" : 9,
"for" : 0, "geeks" : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing test_list 

test_list = ["Gfg", "best", "geeks"]

 

# using in operator to check for match 

res = [ele for ele in test_dict if ele in test_list]

 

# printing result 

print("The required result : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 3, 'is': 5, 'best': 9, 'for': 0, 'geeks': 3}
    The required result : ['Gfg', 'best', 'geeks']
    

**Method #2 : Using set() + intersection()**

This is yet another way in which this task can be performed. In this, we
convert both the containers, list and dictionary keys to set() and then
intersect to find required match.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Common keys in list and dictionary

# Using set() + intersection()

 

# initializing dictionary

test_dict = {"Gfg": 3, "is" : 5, "best" : 9,
"for" : 0, "geeks" : 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# initializing test_list 

test_list = ["Gfg", "best", "geeks"]

 

# intersection() used to get Common elements 

res = set(test_list).intersection(set(test_dict))

 

# printing result 

print("The required result : " + str(list(res)))   
  
---  
  
__

__

**Output**

    
    
    The original dictionary is : {'Gfg': 3, 'is': 5, 'best': 9, 'for': 0, 'geeks': 3}
    The required result : ['best', 'geeks', 'Gfg']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


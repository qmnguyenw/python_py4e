Python – Values frequency across Dictionaries lists



Given two list of dictionaries, compute frequency corresponding to each value
in dictionary 1 to second.

>  **Input** : test_list1 = [{“Gfg” : 6}, {“best” : 10}], test_list2 = [{“a” :
> 6}, {“b” : 10}, {“d” : 6}}]  
>  **Output** : {‘Gfg’: 2, ‘best’: 1}  
>  **Explanation** : 6 has 2 occurrence in 2nd list, 10 has 1.
>
>  **Input** : test_list1 = [{“Gfg” : 6}], test_list2 = [{“a” : 6}, {“b” : 6},
> {“d” : 6}}]  
>  **Output** : {‘Gfg’: 3}  
>  **Explanation** : 6 has 3 occurrence in 2nd list.

 **Method : Using dictionary comprehension + count() + list comprehension**

The combination of above functionalities can be used to solve this problem. In
this, we perform this task using 2 steps, in first we extract all values from
second list, and then perform mapping with frequency with first dictionary
using list comprehension and count().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Values frequency across Dictionaries lists

# Using list comprehension + dictionary comprehension + count()

 

# initializing lists

test_list1 = [{"Gfg" : 6}, {"is" : 9}, {"best" :
10}]

test_list2 = [{"a" : 6}, {"b" : 10}, {"c" : 9},
{"d" : 6}, {"e" : 9}, {"f" : 9}]

 

# printing original list

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# extracting values from target dictionary

temp = [val for sub in test_list2 for key, val in
sub.items()]

 

# frequency mapping from 1st dictionary keys 

res = {key : temp.count(val) for sub in test_list1 for key,
val in sub.items()}

 

# printing result 

print("The frequency dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [{'Gfg': 6}, {'is': 9}, {'best': 10}]
    The original list 2 : [{'a': 6}, {'b': 10}, {'c': 9}, {'d': 6}, {'e': 9}, {'f': 9}]
    The frequency dictionary : {'Gfg': 2, 'is': 3, 'best': 1}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


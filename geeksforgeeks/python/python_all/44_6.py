Python – Substring presence in Strings List



Given list of substrings and list of string, check for each substring, if they
are present in any of strings in List.

>  **Input** : test_list1 = [“Gfg”, “is”, “best”], test_list2 = [“I love Gfg”,
> “Its Best for Geeks”, “Gfg means CS”]  
>  **Output** : [True, False, False]  
>  **Explanation** : Only Gfg is present as substring in any of list String in
> 2nd list.
>
>  **Input** : test_list1 = [“Gfg”, “is”, “best”], test_list2 = [“I love Gfg”,
> “It is Best for Geeks”, “Gfg means CS”]  
>  **Output** : [True, True, False]  
>  **Explanation** : Only Gfg and is are present as substring in any of list
> String in 2nd list.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we for, each
element in list check if it’s substring of any of other list’s element.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substring presence in Strings List

# Using loop

 

# initializing lists

test_list1 = ["Gfg", "is", "Best"]

test_list2 = ["I love Gfg", "Its Best for Geeks", "Gfg means
CS"]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using loop to iterate

res = []

for ele in test_list1 :

 temp = False

 

 # inner loop to check for

 # presence of element in any list

 for sub in test_list2 :

 if ele in sub:

 temp = True

 break

 res.append(temp)

 

# printing result 

print("The match list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : ['Gfg', 'is', 'Best']
    The original list 2 : ['I love Gfg', 'Its Best for Geeks', 'Gfg means CS']
    The match list : [True, False, True]
    

**Method #2 : Using list comprehension + any()**

The combination of above functions can be used to solve this problem. In this,
we check for any sublist using any() and list comprehension is used to perform
iteration.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Substring presence in Strings List

# Using list comprehension + any()

 

# initializing lists

test_list1 = ["Gfg", "is", "Best"]

test_list2 = ["I love Gfg", "Its Best for Geeks", "Gfg means
CS"]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# any() reduces a nesting

# checks for element presence in all Substrings

res = [True if any(i in j for j in test_list2)
else False for i in test_list1]

 

# printing result 

print("The match list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : ['Gfg', 'is', 'Best']
    The original list 2 : ['I love Gfg', 'Its Best for Geeks', 'Gfg means CS']
    The match list : [True, False, True]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


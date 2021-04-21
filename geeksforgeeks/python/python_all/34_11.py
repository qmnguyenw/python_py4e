Python – Replace vowels by next vowel



Given a String replace each vowel with next vowel in series.

>  **Input** : test_str = ‘geekforgeeks’  
>  **Output** : giikfurgiiks  
>  **Explanation** : After e, next vowel is i, all e replaced by i.
>
>  **Input** : test_str = ‘geekforgeeks is best’  
>  **Output** : giikfurgiiks os bist  
>  **Explanation** : After e, next vowel is i, all e replaced by i.

 **Method #1 : Using zip() + list comprehension**

This is one of the ways in which this task can be performed. In this we
perform the task of forming replace dictionary using zip() and then list
comprehension is used to perform the task of replacement with next vowel.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace vowels by next vowel

# Using list comprehension + zip()

 

# initializing string

test_str = 'geekforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# constructing dictionary using zip()

vow = 'a e i o u'.split()

temp = dict(zip(vow, vow[1:] + [vow[0]]))

 

# list comprehension to perform replacement

res = "".join([temp.get(ele, ele) for ele in test_str])

 

# printing result 

print("The replaced string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeks
    The replaced string : giikfurgiiks
    

**Method #2 : Using dictionary comprehension + list comprehension**

This is yet another way in which this task can be performed. In this we
perform the task of mapping using dictionary comprehension and list
comprehension is used to perform task of replacement.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace vowels by next vowel

# Using list comprehension + dictionary comprehension

 

# initializing string

test_str = 'geekforgeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# constructing dictionary using dictionary comprehension

vow = "aeiou"

temp = {vow[idx] : vow[(idx + 1) % len(vow)] for idx
in range(len(vow))}

 

# using get() to map elements to dictionary and join to convert

res = "".join([temp.get(ele, ele) for ele in test_str])

 

# printing result 

print("The replaced string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geekforgeeks
    The replaced string : giikfurgiiks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


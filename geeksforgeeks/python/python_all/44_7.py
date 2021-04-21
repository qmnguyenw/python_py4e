Python – Fill list characters in String



Given String and list, construct a string with only list values filled.

>  **Input** : test_str = “geeksforgeeks”, fill_list = [‘g’, ‘s’, ‘f’, k]  
>  **Output** : g__ksf__g__ks  
>  **Explanation** : All occurrences are filled in their position of g, s, f
> and k.
>
>  **Input** : test_str = “geeksforgeeks”, fill_list = [‘g’, ‘s’]  
>  **Output** : g___s___g___s  
>  **Explanation** : All occurrences are filled in their position of g and s.

 **Method #1 : Using loop**

This is brute force approach to this problem. In this, we iterate for all the
elements in string, if it’s in list we fill it, else fill with “space” value.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Fill list characters in String 

# Using loop

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing fill list 

fill_list = ['g', 's', 'f']

 

# loop to iterate through string 

res = ""

for chr in test_str:

 

 # checking for presence

 if chr in fill_list:

 temp = chr

 else:

 temp = "_"

 res += temp

 

# printing result 

print("The string after filling values : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    The string after filling values : g___sf__g___s
    

**Method #2 : Using join() + list comprehension**

The combination of above functions can be used to solve this problem. In this,
we formulate logic using list comprehension and join() is used to perform join
of required values using conditions.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Fill list characters in String 

# Using join() + list comprehension

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing fill list 

fill_list = ['g', 's', 'f']

 

# join() used to concatenate result 

# using conditionals in list comprehension

res = "".join([chr if chr in fill_list else "_" 

 for chr in list(test_str)])

 

# printing result 

print("The string after filling values : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : geeksforgeeks
    The string after filling values : g___sf__g___s
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


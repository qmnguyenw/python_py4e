Python program to convert a list of strings with a delimiter to a list of
tuple



Given a List containing strings with a particular delimiter. The task is to
remove the delimiter and convert the string to the list of tuple.

 **Examples:**

>  **Input** : test_list = [“1-2”, “3-4-8-9”], K = “-”  
> **Output** : [(1, 2), (3, 4, 8, 9)]  
> **Explanation** : After splitting, 1-2 => (1, 2).  
>
>
> **Input** : test_list = [“1*2”, “3*4*8*9”], K = “*”  
> **Output** : [(1, 2), (3, 4, 8, 9)]  
> **Explanation** : After splitting, 1*2 => (1, 2).

**Method #1 : Using list comprehension + split()**

  

  

In this, first, each string is split using split() with K as an argument, then
this is extended to all the Strings using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert K delim Strings to Integer Tuple List

# Using list comprehension + split()

 

# initializing list

test_list = ["1-2", "3-4-8-9", "4-10-4"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = "-"

 

# conversion using split and list comprehension

# int() is used for conversion

res = [tuple(int(ele) for ele in sub.split(K)) for
sub in test_list]

 

# printing result

print("The converted tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['1-2', '3-4-8-9', '4-10-4']
    The converted tuple list : [(1, 2), (3, 4, 8, 9), (4, 10, 4)]
    

**Method #2 : Using map() + split() + list comprehension**

In this, the task of extension of integral extension logic is done using map()
and then list comprehension is used to perform the task of construction of the
list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert K delim Strings to Integer Tuple List

# Using map() + split() + list comprehension

 

# initializing list

test_list = ["1-2", "3-4-8-9", "4-10-4"]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = "-"

 

# extension logic using map()

# int() is used for conversion

res = [tuple(map(int, sub.split(K))) for sub in
test_list]

 

# printing result

print("The converted tuple list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['1-2', '3-4-8-9', '4-10-4']
    The converted tuple list : [(1, 2), (3, 4, 8, 9), (4, 10, 4)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save


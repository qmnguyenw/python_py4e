Python – Incremental Slice concatenation in String list



Given a String list, perform the task of the concatenation of strings by
increasing the size at each string.

 **Examples:**

>  **Input** : test_list = [‘gfg’, ‘for’, ‘all’, ‘geeks’],  
> **Output** : gfoallgeek  
> **Explanation** : g, fo, all, geek -> concatenated from each string [
> increasing order ].  
>
>
> **Input** : test_list = [‘gfg’, ‘for’, ‘geeks’],  
> **Output** : gfogee  
> **Explanation** : g, fo, gee -> concatenated from each string [ increasing
> order ].

**Method #1 : Using loop +** **slicing** ****

  

  

In this, using loop, each string is iterated and concatenated by slicing
increasing the counter at each pass.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Incremental Slice concatenation in String list

# Using loop + slicing

 

# initializing list

test_list = ['gfg', 'for', 'all', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

res = ''

for idx in range(len(test_list)):

 

 # Incremental slicing

 res += test_list[idx][:idx + 1]

 

# printing result 

print("Incremental sliced concatenated string : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'for', 'all', 'geeks']
    Incremental sliced concatenated string : gfoallgeek
    
    

**Method #2 : Using join() + list comprehension**

In this, task of concatenation is done using join(), task of iteration is done
using list comprehension to provide shorthand.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Incremental Slice concatenation in String list

# Using join() + list comprehension

 

# initializing list

test_list = ['gfg', 'for', 'all', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# join performs concatenation

res = ''.join([test_list[idx][:idx + 1] for idx in
range(len(test_list))])

 

# printing result 

print("Incremental sliced concatenated string : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'for', 'all', 'geeks']
    Incremental sliced concatenated string : gfoallgeek
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

